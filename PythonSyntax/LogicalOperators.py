# temp = 40
# is_rating = False

# if temp > 35 or temp < 0 or is_rating:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")
    
temp = 0
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 0 < temp < 28 and is_sunny:
    print("It is warn ouside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("it is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 0 < temp < 28 and not is_sunny:
    print("It is warn ouside")
    print("It is CLOUDY")