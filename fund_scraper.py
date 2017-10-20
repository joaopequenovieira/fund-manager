#scrapes fund values from Morningstar

import requests
from bs4 import BeautifulSoup

link = "http://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id=F00000MLUQ"

def get_fund_info(link):
	page = requests.get(link)
	source_page = BeautifulSoup(page.content, 'html.parser')
	#get fund title
	fund_title = (source_page.select(".snapshotTitleTable h1"))
	print(fund_title[0].get_text())
	#get overview table elements
	overview_table = (source_page.select(".overviewKeyStatsTable"))
	overview_table = overview_table[0].find_all("td")
	#get fund isin
	fund_isin = overview_table[15].get_text()
	print(fund_isin)
	#get fund nav
	fund_nav = overview_table[3].get_text()
	print(fund_nav)
	#get daily change
	fund_daily_change = overview_table[6].get_text()
	print(fund_daily_change)

get_fund_info(link)
