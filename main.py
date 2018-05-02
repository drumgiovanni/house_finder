from bs4 import BeautifulSoup
import urllib.request, lxml

# this is just a sample url
url1 ="https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&sc=13110&sc=13112&cb=6.0&ct=8.5&mb=0&mt=9999999&md=02&et=9999999&cn=5&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50"

result = urllib.request.urlopen(url1)
soup = BeautifulSoup(result, "lxml")

# find out how many pages are there, and generate the urls 

body = soup.find("body")
pages = body.find_all("div", {'class':'pagination pagination_set-nav'})
pages = str(pages)
pages_split = pages.split('</a></li>')

urls1 = []
urls1.append(url1)

for i in range(len(pages_split) -1):

	pages_split1 = pages_split[i][-2:]
	pages_split2 = pages_split1.replace('>', '')
	pages_split3 = int(pages_split2)
	page_url = f"{url1}&pn={pages_split3}"

	urls1.append(page_url)
# prepare lists for data
h_url = []
h_name = []
h_location = []
h_rent = []
h_admincost = []
h_readtotal = []
h_keymoney = []
h_brokerage = []
h_totalinitialfee = []
h_area = []
h_areacost = []

for url in urls1:
	result = urllib.request.urlopen(urls1[0])
	print(urls1[0])
	soup = BeautifulSoup(result, "lxml")
	summary = soup.find("div",{'id':'js-bukkenList'})

	houses = summary.find_all("div",{'class':'cassetteitem'})


	for i in range(len(houses)):
		# get the name of the house
		title = houses[i].find_all("div",{'class':'cassetteitem_content-title'})
		title = str(title)
		title = title.replace('[<div class="cassetteitem_content-title">', '')
		title = title.replace('</div>]', '')
	

		# get the location of the house
		location = house[i].find_all("li",{'class':'cassetteitem_detail-col1'})
		locaion = str(location)
		location = location.replace('[<li class="cassetteitem_detail_col1">', '')
		location = location.replace('[</li>]', '')
		
		# get the available room number
		rooms = houses[i].find_all('tbody')

		# add the info of title and location to the lists as many as the rooms
		for j in range(len(rooms)):
			h_name.append(title)
			h_location.append(location)

		# get the rent, admincost, area, and so on...
		tables = houses[i].find_all("table")



print(h_name)



