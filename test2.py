import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import numpy as np

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
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Data"])

        while True:  # get recked Prof dinero, you said this was a stupid loop and youre right, but using time its practical
            data = Scrape()  # gets the data from the scrape function
            print(data)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())  # records system time, this part was weird
            writer.writerow([current_time, data])  # when I enventually graph this, time is the x value
            # and the data is the y value
            time.sleep(60)  # loop every 60 seconds,
            # I might have to extend this and idk how im going to run this
            # throughout the weeks? maybe theres somewhere online I could run this?
record_data_every_60()
def graph_data_with_data8():
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_csv(r'C:\Users\James Bond\PycharmProjects\Web Scraper for RSF\Lib\site-packages\scraped_data.csv')
    # Read the csv file into a pandas DataFrame

    # Get the columns to use for x and y axis of the scatterplot
    x_column = df.columns[0]
    y_column = df.columns[1]

    # Plot the scatterplot
    plt.scatter(df[x_column], df[y_column])

    # Label the x and y axis
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    # Show the plot
    plt.show()

#record_data_every_60()