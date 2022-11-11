import csv
import datetime

def Year_csv(w_file, start_date, end_date):
    'Принимает на вход данные за год и создает csv файл с этими данными'
    start = datetime.datetime.strftime(start_date, '%Y%m%d')
    end = datetime.datetime.strftime(end_date, '%Y%m%d')
    N = open((start + '_' + end)+".csv", "w", encoding='utf-8')

    reader = csv.DictReader(w_file)
    w_file.seek(0)
    for row in reader:
        if (row['Дата'] >= end_date.strftime('%Y-%m-%d')):
            if (row['Дата'] <= start_date.strftime('%Y-%m-%d')):
                N.write(row['Дата'] + '\t')
                N.write(row['Курс Доллара'] + '\n')

