def check_armstrong():
    for i in range(1, 1000):
        summ = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            summ += digit ** 3
            temp //= 10

        if i == summ:
            yield i


check_armstrong()
list(check_armstrong())

