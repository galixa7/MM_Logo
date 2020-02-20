def has_validate_input(n):
    if n > 10000:
        print("Enter a number lower than 10 000!")
        return False
    if n < 2:
        print("Enter a number higher than 2!")
        return False
    if (n % 2) == 0:
        print("Enter an odd number!")
        return False
    return True
