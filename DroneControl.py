

array = ['down', '3', 'cm', '4']
direction = array[0].lower()
value = int(array[1])
unit = array[2]


while True:
    if 'down' in direction:
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
                
    elif 'up' in direction:
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break

    elif 'back' in direction:
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break           
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break

    elif direction == 'forward':
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
                
    elif 'left' in direction:
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break

    elif 'right' in direction:
        if unit == 'm':
            if value <= 2:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
        elif unit == 'cm':
            if value <= 100:
                print("you have moved {} {} {}".format(direction, value, unit))
                break
    

            

