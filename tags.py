from bs4 import BeautifulSoup as bs
with open("index.html",encoding="UTF-8") as file:
    html = file.read()

obj = bs(html,"html.parser")

# print(obj.prettify()) # kodu girinti-çıkıntı gibi şeyleri düzenleyip okunaklı hale getirir

print(obj.title) # html title çekme
print(obj.title.string) # title etiketinin içeriği
print(obj.title.name) # hangi html etiketi içinde
#print(obj.body)
print(obj.body.h1) 
#rint(obj.h1) üstteki ile aynı şey
print(obj.body.div.name) # bu methodda bulduğu ilk div elementini alır, sonraki elementleri de almak için farklı methodlar var
print(obj.head.style.string)
# print(obj.head) 