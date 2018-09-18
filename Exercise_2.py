
print("Exercise 2:\nThis program rounds the division to the next integer in the positive direction")
number_1 = float(input("Please enter the first number: "))
number_2 = float(input("Please enter the second number: "))

division = (number_1/number_2)
rounded_division = 0

if division-int(division) != 0:
    if division > 0:
        rounded_division = int(division + 1)


correct_round = round(division)

print("The float value of the division is: ", division, "\nThe rounded up division is: ", rounded_division)
print("The correctly rounded version is: ", correct_round)
