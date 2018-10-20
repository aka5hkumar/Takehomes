#!/usr/bin/env python3
#Akash Kumar for Intersection 10/16/2018
class FizzBuzz:
    def __init__(self, num):
        self.num = num
        try:# Make sure the input is valid
            if  (int(num) < 0):
                print('input is not a positive number')
            else:
                self.fizzBuzzMethod(int(num))
        except ValueError:
            print('Input is not a number')
        except NameError:
            print('Input must be an integer')
    def fizzBuzzMethod(self, num):
        fizzArr = []
        for i in range(1, num+1):
            curr = '' # sets a temp string to add fizz and/or buzz to
            if i % 3 == 0: 
                curr += 'fizz'
            if i % 5 == 0:
                curr += 'buzz' #if 3 and 5, divisible by 15 so add fizz and buzz
            if curr == '': #All untouched values
                curr = str(i)
            fizzArr.append(curr)
        self.makePretty(fizzArr) #Makes output look like documentation
    def makePretty(self, arrayIn):
        print( ' '.join(map(str,arrayIn)))

if __name__ == "__main__": # take input if script is not called by another
    fizIn = input("Input Fizzbuzz number: ")
    FizzBuzz(fizIn)