def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    fibo_table = {}

    fibo_table[1] = 1
    fibo_table[2] = 1
    for i in range(3, num + 1):
        fibo_table[i] = fibo_table[i - 1] + fibo_table[i - 2]
    return fibo_table[num]

print(fibonacci(10))