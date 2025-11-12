from bs4 import BeautifulSoup as bs

with open("index.html",encoding="UTF-8") as file:
    html = file.read()

obj = bs(html,"html.parser")

# karşılaştığı ilk div: sonuc = obj.div

# sonuc = obj.find("div") yine karşılaştğı ilk div

sonuc = obj.find_all("div") # bütün divler
print(len(sonuc)) #3

sonuc = obj.find_all("div")[1] #ikinci div
sonuc = obj.find_all("div")[1].ul.li # ilk li
sonuc = obj.find_all("div")[1].ul.find_all("li") #bütün li elementleri liste halinde gelmiş olur
sonuc = obj.find_all("div")[1].ul.find_all("li")[1] # ikinci divi içinde ul içinde ikinci li
print(sonuc)
print("=================================================")
kacinci = 1
for div in obj.find_all("div"):
   
    print(div.h2,kacinci)
    kacinci +=1
print("=================================================")
for a in obj.find_all("a"):
    print(a)