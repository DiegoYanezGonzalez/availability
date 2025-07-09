from flask import Flask, request, jsonify, render_template # type: ignore
from availability import check_availability

app = Flask(__name__)
reservations = []

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    try:
        data = request.get_json(force=True) if request.is_json else request.form
        room = data.get('room')
        time = data.get('time')

        if not room or not time:
            return jsonify({"error": "Missing data"}), 422

        if not check_availability(room, time):
            return jsonify({"error": "Room already reserved"}), 409

        reservations.append({'room': room, 'time': time})
        return jsonify({"message": "Reserved successfully"}), 201

    except Exception as e:
        print("\U0001F525 Error en reserva:", e)
        return jsonify({"error": "Internal Server Error"}), 500