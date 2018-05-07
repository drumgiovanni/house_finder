import scraper, excelgen


# this is just a sample url
print("")
print("        house_finder")
print("")
print("-------------------------------")
print(""" SUUMOに掲載されている物件と目的地までの距離を
エクセルに出力することができます。""")
print("-------------------------------")
print("")

list1 = input("▶︎SUUMOで条件を指定し検索したページのurlを入力してください：　")
sheetname = input("▶地域名を入力：　")


data = list1.scraper.house_finder
excelgen.make_excel(data, sheetname)

