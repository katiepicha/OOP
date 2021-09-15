class Student:

    def __init__(self,StudentID,Name,DateofBirth,classification):
        self.__StudentID = StudentID
        self.__Name = Name
        self.__DateofBirth = DateofBirth
        self.__classification = classification

    def calc_age(self,DateofBirth):
        