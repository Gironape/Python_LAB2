
def new_csv(w_file):
    ' Принимает dataset и разбивает на Х и Y'
    X = open("X.csv", "w", encoding='utf-8')
    Y = open("Y.csv", "w", encoding='utf-8')
    w_file.seek(0)
    for row in w_file:
        a = row.split(',')
        X.write(a[0] + "\n")
        Y.write(a[1])