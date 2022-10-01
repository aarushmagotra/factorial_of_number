def main():
    a = int(input('Enter the number you want to find the factorial of: '))
    fact = 1
    for i in range(1, a+1):
        fact *= i
    print(fact)
    print()
    fchoice()

def fchoice():
    choice =  input('Would you like to find the factorial of another number (y/n): ')
    print()
    if choice == 'y':
        main()
    elif choice == 'n':
        print('Bye!!')
        quit()
    else:
        print('Invalid Input!!!')
        print()
        print('Try again')
        print()
        fchoice()

if __name__ == '__main__':
    main()
