
def creat_table(size):
    matrix = []
    count = 0

    for i in range(size):
        row = []

        for j in range(size):
            if j % 2 == 0:
                row.append(str(count))
                row.append(str(count))
                count += 1

        matrix.append(row)

    return matrix

def check_2(num):

        if num % 2 == 0:
            return True
        else:
            return False

def creat_table_card(size):
    matrix_card = []

    return matrix_card

def mixing(tabel):

    return tabel























