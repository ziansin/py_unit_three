def area(a, b, c):
    side = (a + b + c) / 2
    a = (side * (side - a) * (side - b) * (side - c)) ** 0.5
    return a
def main():
    at = 10
    bt = 6
    ct = 8
    area_v = area(at, bt, ct)
    print(area_v)
main()

