from bs4 import BeautifulSoup as bs

with open("index.html",encoding="UTF-8") as file:
    html = file.read()

obj = bs(html,"html.parser")

sonuc = obj.div.contents[3]
print(sonuc)
print("=====================")

for i in obj.div.children:
    print(i)
print("=====================")



for i in obj.div.descendants: # alt elemanların da alt elemanlarını alır
    print(i)
print("=====================")

sonuc = obj.h2.parent
sonuc = obj.div.ul.next_element.next_element
print(sonuc)
print("=====================")
sonuc = obj.div.next_sibling.next_sibling.next_element.next_element
sonuc = obj.div.find_next_sibling("div").find_next("li").string
print(sonuc)

print("=====================")
sonuc = obj.div.find_next_sibling("div").find_previous("li")
print(sonuc)



