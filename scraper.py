def house_finder(url1):

	from bs4 import BeautifulSoup
	import urllib.request, lxml


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
	h_deposit = []
	h_keymoney = []
	h_brokerage = []
	h_area = []
	h_areacost = []

	totallist = [h_url, h_name, h_location, h_rent, h_admincost, h_readtotal, h_deposit, h_keymoney, h_brokerage, h_area, h_areacost]
	resultlist = []
	#for url in urls1:
	result = urllib.request.urlopen(urls1[0])
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
		location = houses[i].find_all("li",{'class':'cassetteitem_detail-col1'})
		location = str(location)
		location = location.replace('[<li class="cassetteitem_detail-col1">', '')
		location = location.replace('</li>]', '')
		
		# get the available room number
		rooms = houses[i].find_all('tbody')

		# add the info of title and location to the lists as many as the rooms
		for j in range(len(rooms)):
			h_name.append(title)
			h_location.append(location)

		# get the rent, admincost, area, and so on...
		tables = houses[i].find_all("table")
		rows = []
		room_props = []
		
		
		for i in range(len(tables)):
			rows.append(tables[i].find_all('tr'))

		data = []

		for row in rows:
			for tr in row:
				
				room_urls = tr.find_all('td',{'class':'ui-text--midium ui-text--bold'})
				room_urls = str(room_urls)
				room_urls = room_urls.split(' ')

				# avoiding the black list
				if len(room_urls) > 3:
					if room_urls[3] == "class=js-cassetLinkHref":
						room_urls = room_urls[4]
					else:
						room_urls = room_urls[3]
					room_urls = room_urls.replace('href="', '')
					room_urls = room_urls.replace('"', '')
					h_url.append(room_urls)

				room_props = tr.find_all('td')
				for td in room_props:
					text = td.find(text=True)
					data.append(text)
			
				if len(data) > 4:
					rent = float(data[3][0:-2]) * 10000
					h_rent.append(rent)
					brokerage = rent // 2 + 15000
					h_brokerage.append(brokerage)
					

					admincost = data[4][0:-1]
					if admincost == "":
						h_admincost.append('NA')
						readtotal = rent
						h_readtotal.append(rent)
					else:
						admincost = int(admincost)
						h_admincost.append(admincost)
						

						readtotal = rent + admincost
						h_readtotal.append(readtotal)

					mixed = data[5]
					mixed = mixed.split('/')
					
					for j in range(len(mixed)):
								if j == 0:
									if mixed[j] == "-":
										h_deposit.append('NA')
									else:
										deposit = float(mixed[j][0:-2]) * 10000
										h_deposit.append(deposit)
								
								elif j == 1:
									if mixed[j] == "-":
										h_keymoney.append('NA')
									else:
										keymoney = float(mixed[j][0:-2]) * 10000
										h_keymoney.append(keymoney)
							
					area = data[7]
					h_area.append(area)
					area1 = float(area[0:-1])
					areacost = area1 / rent
					h_areacost.append(areacost)

	# create the list of all info
	for i in range(len(totallist[0])):
		infolist = []
		for j in totallist:
			infolist.append(j[i])
			resultlist.append(infolist) 

	return resultlist
