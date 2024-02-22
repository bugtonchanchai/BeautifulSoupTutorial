from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
# print(doc.prettify())

tbody = doc.tbody
trs = tbody.contents

print(trs[0].next_sibling)


