def count_digits(num):
    digits = 0
    while num >= 1:
        num //= 10
        digits += 1
    return digits

def count_trillions(num):
    trill = 0
    while num >= 1:
        num //= 1000000000000
        trill += 1
    return trill

mt = 2**19937 - 1
nt = mt // 5000000000
nt = nt // 60 // 60
nt = nt // 24 // 365
nt = nt // 10000
print(count_trillions(nt))