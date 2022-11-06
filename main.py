import csv
from pprint import pprint
import requests
import datetime
from first_task import new_csv
from second_task import N_csv

def main():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    print("за сколько дней вы хотите увидеть курс доллара?:")
    count = 1
    max_count = int(input())
    start_date = data['Date']
    start_date = datetime.datetime.fromisoformat(start_date)
    print('DATA =', start_date.year)

    with open("dataset.csv", mode="w+", encoding='utf-8') as w_file:
       file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
       file_writer.writerow(["Дата", "Курс Доллара"])

       while count <= max_count:
                date = data['Date']
                date = datetime.datetime.fromisoformat(date)
                print(date.strftime(('%Y-%m-%d')))
                pprint(data['Valute']['USD']['Value'])
                file_writer.writerow([date.strftime('%Y-%m-%d'), data['Valute']['USD']['Value']])
                if(start_date.year != date.year):
                    end_date = data['Date']
                    end_date = datetime.datetime.fromisoformat(end_date)
                    N_csv(w_file, start_date, end_date)
                    start_date = date
                data = requests.get('https:'+data['PreviousURL']).json()
                count += 1
       new_csv(w_file)




if __name__ == "__main__":
    main()