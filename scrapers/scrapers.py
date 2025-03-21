#scrapers/scrapers.py
import requests
from bs4 import BeautifulSoup



class Scraper:
    def __init__(self, name, url):
        self.name = name
        self.url = url

# Amazon
    def search(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.amazon.com" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}
#Ebay
    def search1(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.ebay.com/" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}
    
#Aliexpress
    def search2(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.aliexpress.com/" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}
    
#WalMart
    def search3(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.walmart.com/" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}
            

#Mercado Libre
    def search4(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.mercadolibre.com.ar/" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}

 
#Alibaba
    def search5(self, query):
        search_url = self.url + query
        print(f"Buscando en URL: {search_url}")  # Imprime la URL de búsqueda
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        for product in soup.find_all("div", {"class": "s-result-item"}):
            title_tag = product.find("h2", {"class": "a-size-medium"})
            link_tag = product.find("a", {"class": "a-link-normal"})
            rating_tag = product.find("span", {"class": "a-icon-alt"})
            
            if title_tag and link_tag and rating_tag:
                title = title_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                link = "https://www.alibaba.com/" + link_tag["href"]
                rating = rating_tag.text.strip()  # Asegúrate de extraer el texto correctamente
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        return {"products": products, "search_url": search_url}
    
     
    
scrapers_list = [
    Scraper("Amazon", "https://www.amazon.com/s?k="),
    # Puedes descomentar los siguientes scrapers y completar sus implementaciones según sea necesario
    Scraper("Ebay", "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw="),
    Scraper("Aliexpress", "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20230216133359&SearchText="),
    Scraper("Walmart", "https://www.walmart.com/search?query="),
    Scraper("Mercado Libre", "https://listado.mercadolibre.com.ar/"),
    Scraper("Alibaba", "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&keywords="),
    #Scraper("Best Buy", "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&type=page&st=&sc=Global&cp=1&qs=&_requestid=1096936"),
]




class AmazonScraper(Scraper):
    def __init__(self):
        super().__init__("Amazon", "https://www.amazon.com/s?k=")


class EbayScraper(Scraper):
    def __init__(self):
        super().__init__("Ebay", "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=")
        

class AliexpressScraper(Scraper):
    def __init__(self):
        super().__init__("Aliexpress", "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20230216133359&SearchText=")
        

class WalmartScraper(Scraper):
    def __init__(self):
        super().__init__("Walmart", "https://www.walmart.com/search?query=")
        


class MercadoLibreScraper(Scraper):
    def __init__(self):
        super().__init__("https://listado.mercadolibre.com.ar/")
        
        

class AlibabaScraper(Scraper):
    def __init__(self):
        super().__init__("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&keywords=")