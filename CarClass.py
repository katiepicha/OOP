class Car:

    def __init__ (self,model,make):
        self.__year_model = model
        self.__make = make
        self.__speed = 0

    def accelerate(self,speed):
        self.__speed += 5

    def brake(self,speed):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed



    