# stockScraper
A scraper that fetches real time data of the S&amp;P 500 listed stocks from Yahoo Finance 

This scraper was build from scratch in Python, using mainly BeautifulSoup4, Numpy, Pandas and urllib

First, I wrote code using the 'wikipedia' library in Python to get the list of S&P 500 companies into a CSV file.
The scraper then iterates through the list of stocks and looks up latest financial data from Yahoo Finance.

To go through the code, start with listIndustry.py, which uses the wikipedia library in Python to get the list of companies from the Wikipedia page for the S&P 500 companies. Note that once executed, you do not need to run this program every time you want the current stock information. The results of this script are stored in s&pIndustries.csv

After that, the script scraper.py is written using BeautifulSoup4, Numpy, Pandas and urllib.request libraries in Python. The results of the scraping are stored in finalScrape.csv. Actually scraping will take time, since a time delay is added after scraping every stock (to prevent issues with the website performance/security)
