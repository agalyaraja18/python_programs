def memoize_fibonacci():
    memo = {0: 0, 1: 1}
    def inner_fibonacci(n):
        if n in memo:
            return memo[n]
        memo[n] = inner_fibonacci(n - 1) + inner_fibonacci(n - 2)
        return memo[n]
    return inner_fibonacci
fib_memo_dict = memoize_fibonacci()
n_value = int(input("Enter the number for nth fibonacci number: "))
print(f"The {n_value}th Fibonacci number (using internal dictionary) is: {fib_memo_dict(n_value)}")
