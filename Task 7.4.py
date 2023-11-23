days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

day_to_number = {i + 1: day for i, day in enumerate(days_of_week)}
number_to_day = {day: i + 1 for i, day in enumerate(days_of_week)}

print(day_to_number)
print(number_to_day)
