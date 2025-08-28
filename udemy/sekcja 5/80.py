def convertToSeconds(hours, minutes):
    seconds_hours = hours * 60 * 60
    seconds_minutes = minutes * 60
    seconds_seconds = seconds_hours + seconds_minutes
    return seconds_seconds


print(convertToSeconds(3, 25))


def convertToHours(minutes):
    hours = minutes // 60
    return hours


print(convertToHours(120))


def ileToGodzin(minuty):
    godziny = minuty // 60
    pozostale_minuty = minuty % 60
    wynik = f"{godziny}:{pozostale_minuty:02d}"
    return wynik

print(ileToGodzin(65))