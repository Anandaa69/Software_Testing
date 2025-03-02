def fizzbuzz(number):
    x = number
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    return "..."
    
if __name__ == "__main__":
    while True:
        print(fizzbuzz(int(input("= "))))
        ans = input("again? (y/n) = ")
        if ans == 'y':
            continue
        if ans == 'n':
            break
        else:
            print('Wrong ans')
            break