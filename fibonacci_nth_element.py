## nth number in fibonacci series


def get_Fibonacci_num(index):
    if index <= 1:
        return 1
    else:
        return get_Fibonacci_num(index-1) + get_Fibonacci_num(index - 2)

n = input('Which number of Fibonacci series you want to know: ')
n = int(n)

if n == 0:
    print("Incorrect input")
else:
    print(get_Fibonacci_num(n-1))