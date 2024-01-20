for _ in range(10):
    n = input()

    for i in range(len(n)):
        if int(n[i]) % 2 != 0 and int(n[i]) % 3 == 0:
            print(n[i])