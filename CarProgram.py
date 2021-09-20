import CarClass as c

def main():

    car = c.Car(2017,'Accord')

    for x in range(0,5):
        car.accelerate()
        print('Current speed:', car.get_speed())

    for y in range(0,5):
        car.brake()
        print('Current speed:', car.get_speed())
        

main()


