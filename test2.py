import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import numpy as np
import datetime

def Scrape():
    driver = webdriver.Chrome()
    driver.get(
        "https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e")

                # wait for 10 seconds for the page to load because javascript
    time.sleep(10)


    html = driver.page_source # convert the HTML content of the page

    # close the browser
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")     # parse the HTML using Beautiful Soup

    # extract the text
    text = soup.get_text()

    percent_full = float(text.split("% Full")[0][-3:]) # so the entire text is in the text variable,
    # this finds the first instance of % full, and grabs the data I could have done this
    # more specifically with the scraper but the data was behind a span tag that was giving me so much trouble
    print(percent_full/100)
    return (percent_full/100)

def record_data_every_60():

    # opens the scraped_data.csv and starts recording the data every minute nad records the time
    with open('scraped_data2.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["Timestamp", "Data"])

        data = Scrape()  # gets the data from the scrape function
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # records system time, th# is part was weird
        writer.writerow([current_time, data])  # when I enventually graph this, time is the x value
        # and the data is the y value
            # I might have to extend this and idk how im going to run this
            # throughout the weeks? maybe theres somewhere online I could run this?
record_data_every_60()
