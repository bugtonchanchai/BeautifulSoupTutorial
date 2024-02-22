from bs4 import BeautifulSoup
import requests

url = "https://www.advice.co.th/product/notebook/notebook-acer/notebook-acer-travelmate-tmp216-51-576q-t006-steel-gray-"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

# get price
prices = doc.find_all(text="ราคาหน้าร้าน")
parent = prices[0].parent.parent
price = parent.text.split(" ")[2]
print(price)