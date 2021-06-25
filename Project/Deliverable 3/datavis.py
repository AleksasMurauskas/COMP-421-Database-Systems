import pandas as pd
import numpy as np
import psycopg2
import matplotlib.pyplot as plt
from datetime import timedelta
import calendar
from datetime import datetime


def main():
    # conn.close()
    passw = "Cinema2078"
    # print("please enter the password for cs421g78:")
    # pw= str(input())
    connection = psycopg2.connect(user="cs421g78",
                                  password=passw,
                                  host="comp421.cs.mcgill.ca",
                                  port="5432",
                                  database="cs421")
    profitsPerMonth(connection)

def profitsPerMonth(connection):
    print('Enter date to look from')
    date = input()

    query = """select price, date, quantity from product p, orders o where p.productid=o.productid and date>'""" + date + """' order by date"""
    # q_fin = q_input + "'" + in_date + "';"

    dat1 = pd.read_sql_query(query, connection)
    # conn.close()
    connection.close()
    print(dat1)
    plotarray1 = []
    for index, elem in dat1.iterrows():
        print(elem)
        plotarray1.append([str(elem['date']), int(elem['price']) * int(elem['quantity'])])
    print(plotarray1)
    curmonth = str(date[:-3])
    month = []
    profit = []
    profitc = 0
    for elem in plotarray1:
        print(str(elem[0][:-3]))
        print(str(curmonth))
        print(elem[0][-5:-2] == curmonth)

        if (elem[0][-5:-2] == curmonth):
            print(elem)
            profitc += elem[1]
            print(profitc)
        else:
            print('flag')
            curmonth = elem[0][-5:-2]
            profit.append(profitc)
            profitc = elem[1]
            month.append(elem[0][:-3])
    print(month)
    print(profit)
    plt.style.use('ggplot')
    plt.plot(month, profit)
    plt.title("Sales per month from " + date)
    plt.ylabel("Sales")
    plt.show()


if __name__ == "__main__":
    main()