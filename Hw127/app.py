import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

planetUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(planetUrl)
time.sleep(2)
planets = []

def scrape():
    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        save = []
        for trtag in soup.find_all("tr"):
            tdtags = trtag.find_all("td")
            row = [i.text.rstrip() for i in tdtags] 
            save.append(row)
        starNames = []
        mass = []
        radius = []
        distance = []
        for i in range(1,len(save)):
            starNames.append(save[i][1])
            mass.append(save[i][5])
            distance.append(save[i][3])
            radius.append(save[i][6])
    df2 = pd.DataFrame(list(zip(starNames,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
    print(df2) 
    df2.to_csv('bright_stars.csv')
scrape()

