from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait

import numpy as np
import pandas as pd
from IPython.display import display
# import lxml #if you want to do read_html with pandas

import time

class Scraper:

  def __init__(self):
    self.driver = None
    self.start_driver()
  
  
  def start_driver(self):
    chrome_options = Options()
    
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # adding headless (i.e not loading gui)
    chrome_options.add_argument("headless")
    
    
    self.driver = webdriver.Chrome(options=chrome_options)
  
    # while True:
    #   self.fetch_neo_data(self.driver)
    #   time.sleep(120)
  
  def quit_driver(self):
    self.driver.quit()
  
  def fetch_neo_data(self, driver = None):

    # if param `driver` is None (i.e nothing passed as driver) then use global driver
    if driver == None:
      driver = self.driver
    
    driver.get("https://www.neo.inc/en/services/raising-assets/canadian-depositary-receipts")
    
    #Implict wait 10sec
    driver.implicitly_wait(10)
    #Explicit wait 10sec
    # wait = WebDriverWait(driver,10)
    
    ### Depreciated ###
    # tables = driver.find_elements_by_xpath('//*[@id="cdr"]/div[2]/div[4]/div[2]/table/tbody')
    
    # Extract data from neo exchange 
    # table_columns = driver.find_element("xpath", '//*[@id="cdr"]/div[2]/div[4]/div[2]/table/thead')
    table = driver.find_elements("xpath", '//*[@id="cdr"]/div[2]/div[4]/div[2]/table/tbody/tr')
  
    # print(table_columns.text)
  
    data_table_rows = []
    
    print("DATA: \n")
    ### Example row data: 
    ### PFE PFIZER CDR (CAD HEDGED) 23.06 22.75 -1.34 49 6,293
    for row in table:
      data_table_rows.append(self.parse_neo_row(row.text))
      
    # print(data_table_rows) #DEBUG
    # df = pd.read_html(driver.page_source)[0] # WONT WORK UNLESS IF YOU IMPORT LXML
  
    columns = ["SYMBOL", "NAME", "PREVIOUS CLOSE", "LAST PRICE", "CHANGE %", "TRADES", "VOLUME"]
    df = pd.DataFrame(data=data_table_rows, columns=columns)
  
    display(df)
    return df.to_markdown()
  
  
  ### Example row data: 
  ### PFE PFIZER CDR (CAD HEDGED) 23.06 22.75 -1.34 49 6,293
  def parse_neo_row(self, row):
    row = row.split()
  
    symb = row[0]
    name = ' '.join(row[1: -5])
    prev_close = row[-5]
    last_price = row[-4]
    change_perc = row[-3]
    trades = row[-2]
    vol = row[-1]
  
    return [symb, name, prev_close, last_price, change_perc, trades, vol]
  
  # start_driver()
