from bs4 import BeautifulSoup
import requests

url = "https://www.advice.co.th/product/notebook/notebook-acer/notebook-acer-travelmate-tmp216-51-576q-t006-steel-gray-"

result = requests.get(url)
print(result.text)