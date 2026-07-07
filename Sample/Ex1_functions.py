

def calculate_meeter(feets, inches):
    feet_into_meters = 0
    inches_into_meters = 0

    if feets > 0:
        feet_into_meters = feets * 0.3048

    if inches > 0:
        inches_into_meters = inches * 0.0254

    return feet_into_meters + inches_into_meters