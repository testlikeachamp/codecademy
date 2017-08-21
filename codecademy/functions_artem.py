def weather_report(temperature):
    if temperature < 0:
        return "freezing"
    elif 0 <= temperature < 10:
        return 'cold'
    else:
        return 'warm'
