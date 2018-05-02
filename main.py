from bs4 import BeautifulSoup
import urllib.request, lxml


url ="https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&sc=13110&sc=13112&cb=6.0&ct=8.5&mb=0&mt=9999999&md=02&et=9999999&cn=5&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50"

result = urllib.request.urlopen(url)

soup = BeautifulSoup(result, "lxml")
summary = soup.find("div", {'id':'js-bukkenList'})



body = soup.find("body")
pages = body.find_all("div", {'class':'pagination pagination_set-nav'})
pages_text = str(pages)
pages_split = pages_text.split('</a></li>')
pages_split0 = pages_split

#pages_split1 = pages_split0[-2:]
#pages_split2 = pages_split1.replace('>', '')
#pages_split3 = int(pages_split2)
print(pages_split)
print("nagasa", len(pages_split))



#print(pages_split2)

# urls = []

# urls.append(url)
