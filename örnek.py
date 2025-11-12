import requests
from bs4 import BeautifulSoup as bs
import threading

def fetch_page(sayfa):
    url = f"https://www.hurriyet.com.tr/dunya/?p={sayfa}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Sayfa {sayfa} yüklenemedi. Kod: {response.status_code}")
        return
    obj = bs(response.text, "html.parser")
    haberler = obj.find_all("h2")
    print(f"\n--- {sayfa}. Sayfa Haberleri ---")
    for haber in haberler:
        baslik = haber.get_text(strip=True)
        if baslik:
            print(f"+ {baslik}")

def scrape():
    sayfa_sayisi = int(input("Kaç sayfa çekmek istiyorsunuz? "))
    threads = []
    for sayfa in range(1, sayfa_sayisi + 1):
        t = threading.Thread(target=fetch_page, args=(sayfa,)) # tek elemanlı tuple da , lazım
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    scrape()
