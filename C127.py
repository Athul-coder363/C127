from email import header
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/Incre/C127/chromedriver") #the path where you have saved chromedriver

browser.get(START_URL)#open our website in the chrome
time.sleep(10)
def scrape():
    #headers include the column names described in the web page
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    #planet_data is collect all the details of the planet
    planet_data = []
    for i in  range (0,202):
        soup = BeautifulSoup(browser.page_source, "html.parser")#this will helps to get the page source
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}): #iterating to find all the iul tags with class exponent
            li_tags = ul_tag.find_all("li")#iterate to find all the li tags, where it conatin data
            temp_list = []
          #to group first li and the rest of the li tags , then treat it seperately
            for index, li_tag in enumerate(li_tags):#enumerate is a fn that return the index along with the element.
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])#first finding the anchor tag and copying the inner HTML
                else:
                    try: #since, if there is any column is missing value it will throw error
                        temp_list.append(li_tag.contents[0])#directly copy the inner html of the li tag
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    print(planet_data[0])
    with open("newOne.csv","w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data)
scrape()