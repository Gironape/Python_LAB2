import csv

def new_csv(w_file):
    ' Принимает dataset и разбивает на Х и Y'
    with open("X.csv", "w", encoding='utf-8') as w_file_x:
        with open("Y.csv", "w", encoding='utf-8') as w_file_y:
            file_writer_X = csv.writer(w_file_x, delimiter=",", lineterminator="\r")
            file_writer_Y = csv.writer(w_file_y, delimiter=",", lineterminator='')
            w_file.seek(0)
            for row in w_file:
                a = row.split(',')
                file_writer_Y.writerow([a[1]])
                file_writer_X.writerow([a[0]])



