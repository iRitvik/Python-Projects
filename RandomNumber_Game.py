import sys
import random
def checkValue(num):
    if num > random_value:
        print("Too High")
        again()
    elif num < random_value:
        print("Too Low")
        again()
    else:
        print("you got it")
        return 0

def again():
    number = int(input("Enter : "))
    return checkValue(number)
while True:
    try:
        random_value = random.randint(int(sys.argv[1]),int(sys.argv[2]))
        first = int(sys.argv[3])
    except ValueError:
        print(f"Guess the number between {sys.argv[1]} - {sys.argv[2]}: ")
        again()
        break
    else:
        checkValue(first)
        break

