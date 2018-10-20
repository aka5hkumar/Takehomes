#!/usr/bin/env python3
class FizzBuzz:
    def __init__(self, num):
        self.num = num
        try:
            if  (int(num) < 0):
                print('input is not a positive number')
            else:
                self.fizzBuzzMethod(int(num))
        except ValueError:
            print('Input is not a number')
        except NameError:
            print('Input must be an integer')

    def fizzBuzzMethod(self, num):
        fizzArr = range(1, num+1)
        for i, j in enumerate(fizzArr):
            for digit in str(j):
                if digit == '3':
                    fizzArr[i] = 'lucky'
        # print(fizzArr)
        for i, j in enumerate(fizzArr):
            if (isinstance(j, str)):
                pass
            else:
                if j % 3 == 0:
                    fizzArr[i] = 'fizz'
                if j % 5 == 0:
                    fizzArr[i] = 'buzz'
                if j % 15 == 0:
                    fizzArr[i] = 'fizzbuzz'
        self.makePretty(fizzArr)
    def makePretty(self, arrayIn):
        print( ' '.join(map(str,arrayIn)))

if __name__ == "__main__":
    fizIn = raw_input("Input Fizzbuzz number: ")
    FizzBuzz(fizIn)