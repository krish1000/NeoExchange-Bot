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
    self.counter = 0
  
  
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

    ########################################
    # data_table_rows = []
    
    # print("DATA: \n")
    # print(len(table))
    # for row in table:
    #   data_table_rows.append(self.parse_neo_row(row.text))
    ####################################
    data_table_rows = {}
    
    print("DATA: \n")
    print(len(table))
    for row in table:
      parsed = self.parse_neo_row_json(row.text)
      # print(parsed)
      # print("---")
      data_table_rows[parsed[0]] = parsed[1]

    ####################################
      
    # print(data_table_rows) #DEBUG
    # df = pd.read_html(driver.page_source)[0] # WONT WORK UNLESS IF YOU IMPORT LXML
  # ######################
  #   columns = ["SYMBOL", "NAME", "PREVIOUS CLOSE", "LAST PRICE", "CHANGE %", "TRADES", "VOLUME"]
  #   df = pd.DataFrame(data=data_table_rows, columns=columns)
  #   ######################
    # display(df)
    # return df.to_markdown()
    # return df.values

    self.counter += 1

    if self.counter >= 3:
      return {'AMZN': {'name': 'AMAZON.COM CDR (CAD HEDGED)', 'prev_close': '16.08', 'last_price': '15.79', 'change_perc': '-1.80', 'trades': '204', 'volume': '45,881'}, 'GOOG': {'name': 'ALPHABET INC. CDR (CAD HEDGED)', 'prev_close': '19.00', 'last_price': '18.72', 'change_perc': '-1.47', 'trades': '211', 'volume': '33,607'}, 'TSLA': {'name': 'TESLA, INC. CDR (CAD HEDGED)', 'prev_close': '27.15', 'last_price': '26.19', 'change_perc': '-3.54', 'trades': '401', 'volume': '104,825'}, 'AAPL': {'name': 'APPLE CDR (CAD HEDGED)', 'prev_close': '24.43', 'last_price': '23.96', 'change_perc': '-1.92', 'trades': '222', 'volume': '36,298'}, 'NFLX': {'name': 'NETFLIX CDR (CAD HEDGED)', 'prev_close': '9.12', 'last_price': '8.90', 'change_perc': '-2.41', 'trades': '84', 'volume': '33,678'}, 'DIS': {'name': 'WALT DISNEY CDR (CAD HEDGED)', 'prev_close': '13.73', 'last_price': '13.46', 'change_perc': '-1.97', 'trades': '62', 'volume': '10,791'}, 'MSFT': {'name': 'MICROSOFT CDR (CAD HEDGED)', 'prev_close': '20.09', 'last_price': '19.71', 'change_perc': '-1.89', 'trades': '178', 'volume': '28,791'}, 'PYPL': {'name': 'PAYPAL CDR (CAD HEDGED)', 'prev_close': '7.18', 'last_price': '7.07', 'change_perc': '-1.53', 'trades': '34', 'volume': '8,781'}, 'VISA': {'name': 'VISA CDR (CAD HEDGED)', 'prev_close': '19.83', 'last_price': '19.69', 'change_perc': '-0.71', 'trades': '19', 'volume': '1,355'}, 'AMD': {'name': 'ADVANCED MICRO DEVICES CDR (CAD HEDGED)', 'prev_close': '17.58', 'last_price': '16.98', 'change_perc': '-3.41', 'trades': '136', 'volume': '17,584'}, 'BRK': {'name': 'BERKSHIRE HATHAWAY CDR (CAD HEDGED)', 'prev_close': '22.42', 'last_price': '22.19', 'change_perc': '-1.03', 'trades': '93', 'volume': '8,094'}, 'COST': {'name': 'COSTCO CDR (CAD HEDGED)', 'prev_close': '25.43', 'last_price': '24.93', 'change_perc': '-1.97', 'trades': '98', 'volume': '9,399'}, 'CRM': {'name': 'SALESFORCE.COM CDR (CAD HEDGED)', 'prev_close': '13.21', 'last_price': '13.18', 'change_perc': '-0.23', 'trades': '41', 'volume': '6,110'}, 'IBM': {'name': 'IBM CDR (CAD HEDGED)', 'prev_close': '20.69', 'last_price': '20.69', 'change_perc': '0.00', 'trades': '6', 'volume': '22'}, 'JPM': {'name': 'JPMORGAN CDR (CAD HEDGED)', 'prev_close': '15.75', 'last_price': '15.75', 'change_perc': '0.00', 'trades': '19', 'volume': '3,933'}, 'MA': {'name': 'MASTERCARD CDR (CAD HEDGED)', 'prev_close': '21.52', 'last_price': '21.26', 'change_perc': '-1.21', 'trades': '12', 'volume': '1,142'}, 'MVRS': {'name': 'META CDR (CAD HEDGED)', 'prev_close': '9.20', 'last_price': '9.03', 'change_perc': '-1.85', 'trades': '131', 'volume': '22,554'}, 'PFE': {'name': 'PFIZER CDR (CAD HEDGED)', 'prev_close': '22.15', 'last_price': '22.03', 'change_perc': '-0.54', 'trades': '27', 'volume': '10,430'}, 'BOFA': {'name': 'BANK OF AMERICA CDR (CAD HEDGED)', 'prev_close': '18.44', 'last_price': '18.35', 'change_perc': '-0.49', 'trades': '12', 'volume': '469'}, 'GS': {'name': 'GOLDMAN SACHS CDR (CAD HEDGED)', 'prev_close': '17.25', 'last_price': '17.26', 'change_perc': '0.06', 'trades': '4', 'volume': '116'}, 'HD': {'name': 'HOME DEPOT CDR (CAD HEDGED)', 'prev_close': '19.87', 'last_price': '19.59', 'change_perc': '-1.41', 'trades': '39', 'volume': '3,766'}, 'NVDA': {'name': 'NVIDIA CDR (CAD HEDGED)', 'prev_close': '15.48', 'last_price': '14.86', 'change_perc': '-4.01', 'trades': '285', 'volume': '64,163'}, 'WMT': {'name': 'WALMART CDR (CAD HEDGED)', 'prev_close': '19.79', 'last_price': '19.72', 'change_perc': '-0.35', 'trades': '29', 'volume': '1,465'}, 'COLA': {'name': 'COCA-COLA CDR (CAD HEDGED)', 'prev_close': '23.46', 'last_price': '23.46', 'change_perc': '0.00', 'trades': '33', 'volume': '198'}, 'CSCO': {'name': 'CISCO CDR (CAD HEDGED)', 'prev_close': '23.57', 'last_price': '23.48', 'change_perc': '-0.38', 'trades': '6', 'volume': '285'}, 'MCDS': {'name': "MCDONALD'S CDR (CAD HEDGED)", 'prev_close': '23.20', 'last_price': '22.90', 'change_perc': '-1.29', 'trades': '14', 'volume': '325'}, 'NKE': {'name': 'NIKE CDR (CAD HEDGED)', 'prev_close': '20.87', 'last_price': '20.87', 'change_perc': '0.00', 'trades': '10', 'volume': '112'}, 'SBUX': {'name': 'STARBUCKS CDR (CAD HEDGED)', 'prev_close': '24.93', 'last_price': '24.50', 'change_perc': '-1.72', 'trades': '30', 'volume': '926'}, 'UNH': {'name': 'UNITEDHEALTH CDR (CAD HEDGED)', 'prev_close': '25.88', 'last_price': '25.60', 'change_perc': '-1.08', 'trades': '13', 'volume': '439'}, 'VZ': {'name': 'VERIZON CDR (CAD HEDGED)', 'prev_close': '19.57', 'last_price': '19.57', 'change_perc': '0.00', 'trades': '4', 'volume': '63'}, 'WOOOOO': {'name': 'VERIZON CDR (CAD HEDGED)', 'prev_close': '19.57', 'last_price': '19.57', 'change_perc': '0.00', 'trades': '4', 'volume': '63'}}
    
    
    return data_table_rows
  
  
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

  def parse_neo_row_json(self, row):
    row = row.split()
  
    symb = row[0]
    name = ' '.join(row[1: -5])
    prev_close = row[-5]
    last_price = row[-4]
    change_perc = row[-3]
    trades = row[-2]
    vol = row[-1]

    data = {
      "name": name,
      "prev_close": prev_close,
      "last_price": last_price,
      "change_perc": change_perc,
      "trades": trades,
      "volume": vol
    }
    return [symb, data]
  # start_driver()
