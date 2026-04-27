from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model_kucing.pkl')
le = joblib.load('label_encoder.pkl')

# 🔹 Route utama (biar tidak Not Found)
@app.route('/')
def home():
    return "API Diagnosa Kucing Aktif 🐱"

# 🔹 Endpoint prediksi
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        input_data = [[
            data['nafsu_makan'],
            data['muntah'],
            data['lesu'],
            data['demam'],
            data['diare'],
            data['batuk'],
            data['bersin'],
            data['berat_badan_turun'],
            data['mata_berair']
        ]]

        pred = model.predict(input_data)
        hasil = le.inverse_transform(pred)

        return jsonify({'penyakit': hasil[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
