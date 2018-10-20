#!/usr/bin/env python3
#Akash Kumar for Intersection 10/16/2018
class FizzBuzz:
    def __init__(self, num):
        self.num = num
        try: # Make sure the input is valid
            if  (int(num) < 0):
                print('input is not a positive number')
            else:
                self.fizzBuzzMethod(int(num))
        except ValueError:
            print('Input is not a number')
        except NameError:
            print('Input must be an integer')
    def fizzBuzzMethod(self, num):
        # Define the values to count
        counter = {
            'fizz': 0,
            'buzz': 0,
            'fizzbuzz': 0,
            'lucky': 0,
            'integer': int(num)
        }
        fizzArr = range(1, num+1) # run though the values for 3s ot replace with lucky
        for i, j in enumerate(fizzArr):
            for digit in str(j):
                if digit == '3':
                    fizzArr[i] = 'lucky'
        for i, j in enumerate(fizzArr): # run though the values for fizzbuzz
            if (isinstance(j, str)):
                counter['lucky'] += 1
                counter['integer'] -= 1
            else:
                if j % 3 == 0 and j % 5 ==0: # divisible by 15
                    fizzArr[i] = 'fizzbuzz'
                    counter['fizzbuzz'] += 1
                    counter['integer'] -= 1
                elif j % 3 == 0:
                    fizzArr[i] = 'fizz'
                    counter['fizz'] += 1
                    counter['integer'] -= 1
                elif j % 5 == 0:
                    fizzArr[i] = 'buzz'
                    counter['buzz'] += 1
                    counter['integer'] -= 1

                    
        self.makePretty(fizzArr, counter) #Makes the print statement look like documentation
    def makePretty(self, arrayIn, counterIn):
        print( ' '.join(map(str,arrayIn)))
        counterList = ['fizz', 'buzz', 'fizzbuzz', 'lucky', 'integer']
        counterStr=''
        for item in counterList: #prints counter in correct format
            counterStr=counterStr + item+': ' + str(counterIn[item]) + ' '
        print(counterStr.lstrip(' '))
if __name__ == "__main__": # take input if script is not called by another
    fizIn = raw_input("Input Fizzbuzz number: ")
    FizzBuzz(fizIn)