# scrapers/bestbuy.py
import requests
from bs4 import BeautifulSoup

class MercadoLibreScraper:
    def __init__(self):
    
        self.name = "Mercado Libre"
        self.url = "https://listado.mercadolibre.com.ar/"



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
                title = title_tag.text.strip()
                link = link_tag["href"]
                rating = rating_tag.text.strip()
                print(f"Encontrado producto: {title}, {link}, {rating}")  # Imprime los detalles del producto encontrado
                products.append({"title": title, "link": link, "rating": rating})
            else:
                print("Etiqueta no encontrada")  # Imprime si alguna etiqueta no se encuentra

        if not products:
            print("No se encontraron productos.")  # Imprime si no se encontraron productos
        #return products

        return {"products": products, "search_url": search_url}