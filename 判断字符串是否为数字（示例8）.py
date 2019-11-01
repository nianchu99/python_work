#用于判断字符串是否为数字
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        pass
    try :
        import unicodedata
        unicodedata.numeric(n)
        return True
    except (ValueError,TypeError):
        pass
    return False

print(is_number("100"))
print(is_number("四"))



