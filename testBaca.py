w, h = 4, 100
list_of_gedung = [[0 for x in range(w)] for y in range(h)]

def load_gedung(filename):
    x = 0
    with open(filename) as file:
        for line in file:
            titik = [int(n) for n in line.strip().split(',')]
            list_of_gedung[x//4][x%4] = titik
            x = x + 1
    print(x//4)

load_gedung('itb_coordinate.txt')
            