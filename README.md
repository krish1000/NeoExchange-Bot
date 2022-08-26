# NeoExchange-Bot
Discord bot that scrapes Neoexchange for Canadian Depositary Receipts (CDRs) and notifies if any CDRs are created along with showing closing, price, change, trades and volume

Bot is hosted on replit.com

#### Scraping
Initially scrapy was used to scrape the website but it was found to not work well with dynamic-loaded content so instead Selenium was used with an implicit wait delay to load the html to scrape

#### Other packages used:
pandas: to create a dataframe to store scraped info and to display <br />
discord: to authenticate bot and be able to run onto discord servers <br />
numpy: ~ <br />
replit: ~ <br />
