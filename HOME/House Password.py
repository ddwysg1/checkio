#link: https://py.checkio.org/en/mission/house-password/
def checkio(data: str):
    import string
    def have_10(data):
        if len(data) >= 10:
            return True
        else:
            return False
    def have_digit(data):
        for dig in string.digits:
            if dig in data:
                return True
                break
        else:
            return False
    def have_lower(data):
        for lower in string.ascii_lowercase:
            if lower in data:
                return True
                break
        else:
            return False
    def have_upper(data):
        for upper in string.ascii_uppercase:
            if upper in data:
                return True
                break
        else:
            return False

    if have_digit(data) and have_lower(data) and have_upper(data) and have_10(data):
        return True
    else:
        return False
