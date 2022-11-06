import datetime


def N_csv(w_file, start_date, end_date):
    start = datetime.datetime.strftime(start_date, '%Y%m%d')
    end = datetime.datetime.strftime(end_date, '%Y%m%d')
    N = open((start + '_' + end)+".csv", "w", encoding='utf-8')
    for row in w_file:
        a1 = row.split()
        N.write(a1[0] + "\n")
