#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    number = 10
    while number > 0:
        if number == 1:
            print (number)
            print ("Happy New Year!")
        else:
            print (number)
        number -= 1
    pass

def square_integers(int_list):
    # code goes here!
    new_list = [number * number for number in int_list]
    return new_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 15 == 0:
            print ("FizzBuzz")
        elif i % 5 == 0:
            print ("Buzz")
        elif i % 3 == 0:
            print ("Fizz")
        else:
            print (i)
    pass

fizzbuzz()