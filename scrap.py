from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=deb7d190-effc-4567-9149-926009a23bdc&as-backfill=on"
page = requests.get(url)
print(page)




soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all("div" , class_ = "_1AtVbE col-12-12")
#print(lists)



f  = open("mobile.csv" , "w" , encoding = "utf-8")
theWriter = writer(f)
header = ['Title' , 'Price']
theWriter.writerow(header)
for listy in lists:
    title = listy.find('div' , class_ = "_4rR01T")
    if title == None:
        continue
    else:
         title = listy.find('div' , class_ = "_4rR01T").text
         price = listy.find('div' , class_ = "_30jeq3 _1_WHN1").text
         info = [title , price]
         print(info)
         theWriter.writerow(info)
