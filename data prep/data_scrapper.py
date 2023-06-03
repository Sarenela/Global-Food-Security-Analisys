import pandas as pd
from IPython.display import display
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import seaborn as sns



def adjust_currency(value):
    if "%" in value:
        value = value.replace("%", "")
    elif "$" in value:
        value = value.replace("$", "").replace(",", "")
    return value

def adjust_number(value):
    if "" in value:
        return value.replace(",","")



def scrape_table_data(url,adjust_value_method,column):
    driver = webdriver.Chrome(r"C:\Users\user\Desktop\driver\chromedriver.exe")
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    if column <=0 or column>=len(rows):
        raise ValueError("illegal column number")

    data = {}
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            country = cells[0].text.strip()
            value = cells[column].text.strip()
            value = adjust_value_method(value)

            data[country] = float(value) if value else None

    driver.quit()
    return data


def get_data_csv_specific_columns(csv_path, columns):
    return pd.read_csv(csv_path,usecols=columns)


def get_data_csv(csv_path):
    return pd.read_csv(csv_path)



url = "https://data.worldbank.org/indicator/AG.LND.FRST.ZS?end=2020&name_desc=false&start=1990&view=chart"
table_data = scrape_table_data(url,lambda x: x ,1)

# Display the table data
print(table_data)