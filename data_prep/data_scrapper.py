import pandas as pd
from IPython.display import display
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import seaborn as sns
import matplotlib


def adjust_unit(value):
    if "%" in value:
        value = value.replace("%", "")
    elif "t" in value:
        value = value.replace("t", "")
    elif "kg" in value:
        value = value.replace("kg", "")
    elif "$" in value:
        value = value.replace("$", "").replace(",", "")
    elif "$" in value:
        value = value.replace("$", "").replace(",", "")
    elif "kcal" in value:
        value = value.replace("kcal", "").replace(",", "")
    return value.strip()

def adjust_number(value):
    if "" in value:
        return value.replace(",","")


def scrape_column_names(driver,url, col):
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, "table")
    headers = table.find_elements(By.TAG_NAME, "th")
    column_names = [header.text.strip() for header in headers]

def scrape_table_data(url,adjust_value_method,columns):
    driver = webdriver.Chrome(r"C:\Users\user\Desktop\driver\chromedriver.exe")
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    headers = table.find_elements(By.TAG_NAME, "th")

    column_names =[headers[id].text.strip().split('\n')[0] for id in columns]

    if any(col <= 0 or col >= len(rows) for col in columns):
        raise ValueError("Illegal column number")

    data = {}
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells:
            country = cells[0].text.strip()
            values = [adjust_value_method(cells[col].text.strip()) for col in columns]
            data[country] = values

    driver.quit()
    return pd.DataFrame.from_dict(data, orient='index', columns=column_names)


def get_data_csv_specific_columns(csv_path, columns,encoding):
    return pd.read_csv(csv_path,usecols=columns,encoding=encoding).set_index(columns[0])


def get_data_csv(csv_path,encoding):
    return pd.read_csv(csv_path,encoding=encoding)


#if __name__=="__main__":
    # url = "https://data.worldbank.org/indicator/AG.LND.FRST.ZS?end=2020&name_desc=false&start=1990&view=chart"
    #table_data = scrape_table_data(url,lambda x: x ,1)

    # Display the table data
    #print(table_data)