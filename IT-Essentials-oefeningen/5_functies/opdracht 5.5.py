def is_even(getal):
    if getal % 2 == 0:
        return True
    else:
        return False


def is_oneven(getal):
    return not is_even(getal)
    #if is_even(getal) == True:
    #   return False
    #else:
    #    return True


print(is_oneven(2988))
