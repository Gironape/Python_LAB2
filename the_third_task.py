import datetime
import csv

def Week_csv(w_file, week_start, week_end):
    start = datetime.datetime.strftime(week_start, '%Y%m%d')
    end = datetime.datetime.strftime(week_end, '%Y%m%d')
    N = open((start + '_' + end) + ".csv", "w", encoding='utf-8')
    reader = csv.DictReader(w_file)
    w_file.seek(0)
    for row in reader:
        if (row['Дата'] >= week_end.strftime('%Y-%m-%d')):
            if (row['Дата'] <= week_start.strftime('%Y-%m-%d')):
                N.write(row['Дата'] + '\t')
                N.write(row['Курс Доллара'] + '\n')