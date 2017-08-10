from bs4 import BeautifulSoup
import datetime
import decimal
import sys

if(len(sys.argv) > 1):
	for i in range(1,len(sys.argv)):
		html_doc = open(sys.argv[i], "r")
		soup = BeautifulSoup(html_doc, 'html.parser')

		item_list = []
		price_list = []
		price_per_unit = []
		quantity_list = []

		tcNbr = soup.find("input",{"name":"tcNbr"})['value']
		formatted_tcNbr = ' '.join(tcNbr[i:i+4] for i in range(0,len(tcNbr),4))

		visit_date = soup.find("input",{"name":"visitDate"})['value']
		formatted_date = datetime.datetime.strptime(visit_date,'%B %d, %Y').strftime('%Y%m%d')

		for item in soup.find_all("div", class_="half radio_btn"):
			desc = item.find("div", class_="desc")
			desc = desc.get_text()
			item_list.append(desc)

		for item in soup.find_all("div", class_="half radio_btn"):
			quantity = item.find("div", class_="qty")
			quantity = quantity.get_text()
			quantity = decimal.Decimal(quantity[5:])
			quantity_list.append(quantity)

		for item in soup.find_all("div", class_="half radio_btn"):
			price = item.find("div", class_="price")
			price = price.get_text()
			price = decimal.Decimal(price[1:5])
			price_list.append(price)

		itr = 0
		for quantity in quantity_list:
			price_per_unit.append(price_list[itr] / quantity)
			itr = itr + 1

		itr = 0
		for item in item_list:
			print(formatted_date + ',' + formatted_tcNbr + ',' + item_list[itr] + ',' + str(price_per_unit[itr]))
			itr = itr + 1
	

else:
	print("No arguments found")


	
