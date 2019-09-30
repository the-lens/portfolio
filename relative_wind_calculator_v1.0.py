#This program is for calculate a relative wind angle to a plane.

version = '1.0 - after 2 weeks of learning Python'


while True:
    print('Enter Plane Heading')
    planeheading = input()
    if planeheading == 'exit':
        break
    else:
        ph = int(planeheading)

    print('Enter Wind Heading')
    windheading = input()

    if windheading == 'exit':
        break
    else:
        wh = int(windheading)

    temp = wh-ph

    if temp > 180:
        print('Corrdinates are', temp-360)
        print('Press enter to continue, or type "exit" to exit...')
        ext = input()

    if temp < -180:
        print('Corrdinates are', 360+temp)
        print('Press enter to continue, or type "exit" to exit...')
        ext = input()

    if 180 >= temp >= -180:
        print('Corrdinates are', temp)
        print('Press enter to continue, or type "exit" to exit...')
        ext = input()

    if ext == 'exit':
        break