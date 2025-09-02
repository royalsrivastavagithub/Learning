from datetime import datetime
#program will return the day of the week
def get_weekday():
    today = datetime.today()
    weekday = today.weekday()
    match weekday:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"

if __name__ == "__main__":
    print(get_weekday())
