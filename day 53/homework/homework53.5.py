def time_travel():
    current_age = int(input("Enter your current age: "))
    current_year = int(input("Enter the current year: "))
    time_travel_years = int(input("Enter how many years you want to travel: "))
    direction = input("Do you want to travel to the 'future' or 'past'? ").strip().lower()

    if direction == "future":
        new_year = current_year + time_travel_years
        new_age = current_age + time_travel_years
    elif direction == "past":
        new_year = current_year - time_travel_years
        new_age = current_age - time_travel_years
    else:
        return "Invalid direction"

    return f"After traveling, it will be the year {new_year} and you will be {new_age} years old."

print(time_travel())
