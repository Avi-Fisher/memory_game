import random


def creat_table_card(size):
    matrix = []
    count = 1

    for i in range(size):
        row = []

        for j in range(size):
            if j % 2 == 0:
                row.append(str(count))
                row.append(str(count))
                count += 1

        matrix.append(row)

    return mixing(matrix)

def check_2(num):

        if num % 2 == 0:
            return True
        else:
            return False

def creat_table(size):
    matrix_card = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append("*")

        matrix_card.append(row)
    return matrix_card

def mixing(tabel):
    size = len(tabel) - 1

    for i in range(300):
        random1 = random.randint(0, size)
        random2 = random.randint(0, size)
        random3 = random.randint(0, size)
        random4 = random.randint(0, size)

        tabel[random1][random2],tabel[random3][random4] =  tabel[random3][random4],tabel[random1][random2]

    return tabel























