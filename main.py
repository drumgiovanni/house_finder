from bs4 import BeautifulSoup
import urllib.request, lxml


url1 ="https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&sc=13110&sc=13112&cb=6.0&ct=8.5&mb=0&mt=9999999&md=02&et=9999999&cn=5&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50"

result = urllib.request.urlopen(url1)

soup = BeautifulSoup(result, "lxml")
summary = soup.find("div", {'id':'js-bukkenList'})


# find out how many pages are there, and generate the urls 

body = soup.find("body")
pages = body.find_all("div", {'class':'pagination pagination_set-nav'})
pages_text = str(pages)
pages_split = pages_text.split('</a></li>')

urls1 = []
urls1.append(url1)

for i in range(len(pages_split) -1):

	pages_split1 = pages_split[i][-2:]
	pages_split2 = pages_split1.replace('>', '')
	pages_split3 = int(pages_split2)
	page_url = f"{url1}&pn={pages_split3}"

	urls1.append(page_url)

print(urls1)

