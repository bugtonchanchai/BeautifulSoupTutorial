from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())