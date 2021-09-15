'''
Object Oriented Programming (OOP)
- objects have both attributes and methods
    - attributes describe
    - methods perform operations and functions on attributes
- Data hiding: object's data attributes are hidden from code outside the object to protect from accidental corruption
    - some methods would not make sense/work for other attributes
    - public vs. private (accessible by user vs. by creator) methods
    - * hide an attribute by putting two underscores '__' before the attribute name, so that no one can hack and manipulate your code
- Class: code that specifies the data attributes and methods of a particular type of object
    (similar to a blueprint of a house or a cookie cutter)
- Instance: an object created from a class
    (similar to a specific house built according to a blueprint)
    - there can be many instances of one class
- Class definition: set of statements that define a class's methods and data attributes
    - format: begin with class  class_name:
    (class names often start with uppercase letter)
    - begin class with an __int__ function (short for initialize) in order to create attributes
        - "self" ensures that you only perform methods on that specific instance
        - this function shows you the number of attributes within the class
- the __str__ method displays the object's state


'''