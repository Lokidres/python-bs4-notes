from bs4 import BeautifulSoup as bs

with open("index.html",encoding="UTF-8") as file:
    html = file.read()

obj = bs(html,"html.parser")

sonuc = obj.find(id="item1") # item1 id li elementi getir
print(sonuc.find_all("li")[2])
print("======================")
sonuc = obj.find_all(class_="item")[1].find_all("li")[2] # class dan sonra _ önemli!!
print(sonuc)
print("================================")
sonuc = obj.select("#item1") #burda ise sadece bir tane item1 olmasına rağmen o 1 içeriği de list olarak getirdi.
print(sonuc) 
print("================================")
sonuc = obj.select(".item") # burda id değil class seçtik
sonuc = obj.select_one(".item") # .select find_all gibi çalışır, select_one ise find gibi<
print(sonuc) 
print("===================================")
sonuc = obj.div.attrs["id"] #ilk divin id si (item1)
sonuc = obj.div.attrs["class"] # ilk divin classı (list olarak gelir)

sonuc = obj.find_all("ul")[1].get_text() # .string gibi aslında, bütün ul lerden ikincisinin içeriğini getiriyor.
print(sonuc)

sonuc = obj.find_all("ul")[1].get_text(strip=True, separator="-") # boşlukları atar ve hepsinin arasına - koyar
print(sonuc)
print("===================================")

for a in obj.find_all("a"):
    print(a.get("href")) # bütün a elementleri içinde href özelliğinin içeriğini text olarak çekme
   # print(a["href"]) # aynı işlev