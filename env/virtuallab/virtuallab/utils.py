# Utility function to check for integer
def RepresentsNumber(s):
    try:
        float(s)
        s = float(s)
        if s < 0:
            return False
        return True
    except ValueError:
        return False


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def RepresentsNegativeNumber(s):
    try:
        float(s)
        s = float(s)
        if s > 0:
            return False
        return True
    except ValueError:
        return False
