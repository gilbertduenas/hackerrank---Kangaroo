# Less lines of code, but longer run time because it loops to 5000
def kangaroo(x1, v1, x2, v2):
    for i in range(5000):
        x1 += v1
        x2 += v2

        if x1 == x2:
            return 'YES'

    return 'NO'
