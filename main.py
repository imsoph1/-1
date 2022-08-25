from views import *

def main():
    while True:
        print('Actions: \n\tCREATE - 1\n\tLISTING - 2\n\tRETREIVE - 3\n\tUPDATE - 4\n\tDELETE - 5')
        choice = input('enter actions: 1, 2, 3, 4, 5: ')
        if choice == '1':
            print(creat())
        elif choice == '2':
            print(listing())
        elif choice == '3':
            print(retrieve())
        elif choice == '4':
            print(update())
        elif choice == '5':
            print(delete())
        else:
            print('invalid choice! ')
        ask = input('do you wanna continue?: (yes/no): ')
        if ask == 'no':
            break
        else:
            print('let\'s continue! ')
main()


