from flask import Flask, request, jsonify
from app.availability import check_availability

app = Flask(__name__)
bookings = []

@app.route('/book', methods=['POST'])
def book_room():
    data = request.get_json()
    available = check_availability(bookings, data)

    if available:
        bookings.append(data)
        return jsonify({"message": "Booking successful"}), 201
    else:
        return jsonify({"message": "Room not available"}), 409
