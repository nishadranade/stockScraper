from urllib.request import urlopen as url
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import csv
import time

#final results
finresults = [ ['Ticker Symbol',
 'Price',
 'Percent Change',
 'Net Change',
 'Previous Close',
 'Open',
 'Bid',
 'Ask',
 "Day's Range",
 '52 Week Range',
 'Volume',
 'Avg. Volume'  ] ]

#read the list produced by the earlier script as a CSV file into Python
corporations = []

reader = []
with open('s&pIndustries.csv') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        corporations.append(row[0])


#loop through all S&P 500 Company ticker symbols

index = 1
while index < 506:

    #create the url for that specific stock
    namestr = str(corporations[index])
    my_url = 'https://finance.yahoo.com/quote/' + namestr + '?p=' + namestr

    uClient = url(my_url, timeout= 500)
    page_html = uClient.read()
    uClient.close()

    page_soup = bs(page_html, "html.parser")

    #Find live stock price
    container2 = page_soup.findAll("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})

    str2 = container2[0].text

    i = 0                               #variable for length of price face value (digits)
    for c in str2:
        if c == "+" or c == "-" :
            break
        i += 1


    j = 0                           #variable for length of net change face value
    for c in str2:
        if c == " ":
            break
        j += 1

    #find percent change in stock price
    k1 = 0
    k2 = 0

    for c in str2:
        if c == "(":
            break;
        k1 += 1;

    for c in str2:
        if c == ")":
            break;
        k2 += 1;

    price = str2[:i]
    netChange = str2[i:j]
    percentChange = str2[k1+1: k2]

    entry1 = np.asarray([['Price', price], ['Percent Change', percentChange], ['Net Change', netChange]])

    #code to get all the other key stats from the webpage

    container1 = page_soup.findAll("table",{"class":"W(100%)"})
    str1 = str(container1[0])
    table = pd.read_html(str1)

    table = np.asarray(table[0])
    table = np.concatenate((entry1, table), axis = 0)

    values = []
    for i in table:
        values.append(i[1])
    values = np.asarray(values)

    newValues = [namestr]
    for c in values:
        newValues.append(c)

    finresults.append(newValues)

    time.sleep(0.5)
    print(index)

    index += 1

with open("finalScrape5.csv", "w", newline="") as f:
    cw = csv.writer(f)
    cw.writerows(r + [""] for r in finresults)
