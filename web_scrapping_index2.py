from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
tag['value'] = "new value"
tag['selected'] = "false"
tag['color'] = "red"
print(tag.attrs)
print(tag)