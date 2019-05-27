def fibonacci_num(snum):
    if snum in (0, 1):
        return 1
    else:
        return fibonacci_num(snum - 1) + fibonacci_num(snum - 2)
