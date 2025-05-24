import random

def ran():
    return int((random.random()) * (100 + 1))

number = None
count = 1

def restart():
    ask = str(input("enter 'y' for playing and 'enter' for no :"))
    if ask == 'y':
        main()


def main():
    global number
    number = ran()
    print(number)
    while True:
        user_input = int(input('Guess the number between 1 to 100 :'))
        global count

        if user_input < 1 or user_input > 100:
            print(" please enter the valid number")
        
        if user_input < number:
            print("low")
        else:
            print('high')

        if user_input == number:
            print(f"================\nResult\n=============== \nCorrect Answer is : {number}\nTotal Attempt : {count} \n===============")
            count = 1
            restart() 
            break 

        count += 1
main()