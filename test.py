
def sum(a, b):
    return a + b

dct = {
    'c': 1,
    'b': 2,
}


s = sum(**dct)
print(s)  # 3