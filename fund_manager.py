#scrapes fund values from Morningstar

import requests
from bs4 import BeautifulSoup

class main_funcs:

	def add_new_fund(link):
        if link == "":
            return
        page = requests.get(link)
        source_page = BeautifulSoup(page.content, 'html.parser')
		#get fund title
        fund_title = (source_page.select(".snapshotTitleTable h1"))
        fund_title = fund_title[0].get_text()
		#get overview table elements
        overview_table = (source_page.select(".overviewKeyStatsTable"))
        overview_table = overview_table[0].find_all("td")
		#get fund isin
        fund_isin = overview_table[15].get_text()
		#get fund nav
        fund_nav_temp = overview_table[3].get_text()
		#remove letters, consider splitting string in future for currency and value
        fund_nav = ""
        for c in fund_nav_temp:
            if (ord(c) == 46 or (ord(c) >= 48 and ord(c) <= 57)):
            fund_nav += c
		#get daily change
        fund_daily_change = overview_table[6].get_text()

        values = [fund_isin, fund_title, fund_nav, fund_daily_change]
        return(values)



