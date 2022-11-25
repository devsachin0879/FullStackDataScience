
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


def BookScrape():
    try:
        ## range is 1 to 51 as we have 50 pages in the website
        for i in range(1,51):
            url = "http://books.toscrape.com/catalogue/page-" + str(i)+".html"
            
            ## hit url
            uClient = uReq(url)
            
            ## read data from url
            mainPage = uClient.read()
            uClient.close()
            
            ## beautify data we got from page
            mainPage_html = bs(mainPage,"html.parser")
            
            ## each product is present as list so find li tag from the page
            bigbox = mainPage_html.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            
            ## creating a csv file to store data
            filename = "BookstoScrape.csv"
            
            ## list to store data
            data_list = []
            
            try:
                ##loop through each product to get url for next page
                ##to get the information required
                for prod_num in range(len(bigbox)):
                    book_link = "http://books.toscrape.com/catalogue/" + bigbox[prod_num].a['href']
                    
                    ### product response
                    bookRes = requests.get(book_link)
                    
                    ###encoding
                    bookRes.encoding = 'utf-8'
                    book_html = bs(bookRes.text,"html.parser")
                    
                    ##get info 
                    title = book_html.find_all('h1')[0].text
                    price = book_html.find_all("p",{"class":"price_color"})[0].text
                    category = book_html.find_all("a")[3].text
                    
                    mydict = {"Title":title, "Price in Pounds":price[1:], "Category":category}
                    data_list.append(mydict)
                    
                ### create dataframe from list of dictionaries
                df = pd.DataFrame(data_list)
                
                ## writing condtion to avoid re-writting of title
                ## append data to csv file
                if i == 1:
                    df.to_csv(filename, mode='a', index=False, header=True)
                else:
                    df.to_csv(filename, mode='a', index=False, header=False)
                    
            except Exception as e:
                print("An error has occured in 2nd for loop",e)
            
    except Exception as e:
        print("An error has occured",d)
        
BookScrape()

