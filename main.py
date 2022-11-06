import csv
from pprint import pprint
import requests
import datetime

def main():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    print("за сколько дней вы хотите увидеть курс доллара?:")
    count = 1
    max_count = int(input())

    with open("dataset.csv", mode="r+", encoding='utf-8') as w_file:
       X = open("X.csv", "w", encoding='utf-8')
       Y = open("Y.csv", "w", encoding='utf-8')
       file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
       file_writer.writerow(["Дата", "Курс Доллара"])

       while count <= max_count:
                date = data['Date']
                date = datetime.datetime.fromisoformat(date)
                print(date.strftime(('%Y-%m-%d')))
                pprint(data['Valute']['USD']['Value'])
                file_writer.writerow([date.strftime('%Y-%m-%d'), data['Valute']['USD']['Value']])
                data = requests.get('https:'+data['PreviousURL']).json()
                count += 1

       for row in w_file:
          a = row.split(',')
          X.write(a[0] + "\n")
          Y.write(a[1])

if __name__ == "__main__":
    main()