def find_primes():
    prime_list = []
    for num in range(0, 100 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    continue
            else:
                prime_list.append(num)
    return prime_list