from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    temperature = data.get('temp')
    humidity = data.get('humidity')
    ldr_value = data.get('ldr_value')

    print(f"Received Data: Temperature: {temperature}, Humidity: {humidity}, LDR: {ldr_value}")

    # Di sini kamu bisa simpan data ke database atau lakukan operasi lain jika perlu.
    return jsonify({"status": "success", "message": "Data received successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
