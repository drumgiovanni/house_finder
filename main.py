import scraper, excelgen


# this is just a sample url
url1 ="https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&sc=13110&sc=13112&cb=6.0&ct=8.5&mb=0&mt=9999999&md=02&et=9999999&cn=5&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50"
	

list1 = scraper.house_finder("https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13109&sc=13110&sc=13112&cb=6.0&ct=8.5&mb=0&mt=9999999&md=02&et=9999999&cn=5&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50")
list2 = scraper.house_finder("https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=14&sc=14133&cb=0.0&ct=8.5&et=9999999&md=02&cn=5&mb=0&mt=9999999&tc=0400501&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=")
excelgen.make_excel(list1, "東京都内")
excelgen.make_excel(list2, "川崎市")






