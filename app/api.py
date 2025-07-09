from flask import Flask, request, render_template, redirect, url_for, flash
from app.availability import check_availability

app = Flask(__name__)
app.secret_key = "supersecret"
reservations = []

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    try:
        room = request.form.get('room')
        time = request.form.get('time')

        if not room or not time:
            flash("Missing data")
            return redirect(url_for('home'))

        if not check_availability(room, time, reservations):
            flash("Room already reserved")
            return redirect(url_for('home'))

        reservations.append({'room': room, 'time': time})
        flash("Reserved successfully")
        return redirect(url_for('home'))

    except Exception as e:
        print("🔥 Error en reserva:", e)
        flash("Internal Server Error")
        return redirect(url_for('home'))
