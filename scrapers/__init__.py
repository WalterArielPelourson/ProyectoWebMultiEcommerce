from .amazon import AmazonScraper
from .ebay import EbayScraper
from .aliexpress import AliexpressScraper
from .walmart import WalmartScraper
#from .bestbuy import BestBuyScraper
from .mercadolibre import MercadoLibreScraper
from .alibaba import AlibabaScraper

scrapers_list = [
    AmazonScraper(),
    EbayScraper(),
    AliexpressScraper(),
    WalmartScraper(),
    #BestBuyScraper(),
    MercadoLibreScraper(),
    AlibabaScraper()
]
