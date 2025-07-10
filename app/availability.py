def check_availability(reservations, new_reservation):
    for r in reservations:
        if r['room'] == new_reservation['room'] and r['time'] == new_reservation['time']:
            return False
    return True
