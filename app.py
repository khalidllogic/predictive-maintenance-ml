from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# 1. تحميل ملفات الذكاء الاصطناعي
# نتأكد من وجود المجلد والملفات لتجنب انهيار السيرفر
try:
    with open('model/final_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('model/columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    print("AI Model and Scaler loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}. Make sure the 'model' folder exists and contains the 3 files.")

# 2. المسار الرئيسي: عرض واجهة المستخدم
@app.route('/')
def home():
    return render_template('index.html')

# 3. مسار التنبؤ: استقبال البيانات من الواجهة وتحليلها
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # استقبال القراءات من الحقول في واجهة الويب
            # النوع: L=0, M=1, H=2 بناءً على الـ LabelEncoder
            type_val = float(request.form['type'])
            air_temp = float(request.form['air_temp'])
            process_temp = float(request.form['process_temp'])
            rotational_speed = float(request.form['rotational_speed'])
            torque = float(request.form['torque'])
            tool_wear = float(request.form['tool_wear'])
            
            # ترتيب البيانات في قاموس مؤقت
            input_data = {
                'Type': type_val,
                'Air temperature [K]': air_temp,
                'Process temperature [K]': process_temp,
                'Rotational speed [rpm]': rotational_speed,
                'Torque [Nm]': torque,
                'Tool wear [min]': tool_wear
            }
            
            # تحويل القاموس إلى DataFrame وترتيب الأعمدة تماماً كما تدربت عليها الخوارزمية
            df = pd.DataFrame([input_data])[columns]
            
            # توحيد مقاييس الأرقام (Scaling) بنفس المسطرة الرياضية للتدريب
            scaled_data = scaler.transform(df)
            
            # إصدار قرار التنبؤ
            prediction = model.predict(scaled_data)[0]
            
            if prediction == 1:
                result = "تحذير حرج: النظام يتنبأ بتعطل الآلة قريباً! يجب إجراء صيانة فورية."
                status = "danger"
            else:
                result = "النظام مستقر: الآلة تعمل ضمن النطاق الآمن."
                status = "success"
                
            return render_template('index.html', prediction_text=result, status=status)
            
        except Exception as e:
            return render_template('index.html', prediction_text=f"حدث خطأ في قراءة البيانات: {str(e)}", status="danger")

if __name__ == "__main__":
    app.run(debug=True)