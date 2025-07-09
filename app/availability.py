def check_availability(room, time):
    for r in reservations:
        if r['room'] == room and r['time'] == time:
            return False
    return True
