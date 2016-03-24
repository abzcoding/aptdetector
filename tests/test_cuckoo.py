"""docstring"""
import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get("http://172.16.201.182:8000/analysis/17").
                     text, 'html.parser')
information = soup.find(id="information")
print("--------------informations--------------")
for ch in information.find(class_="panel-body"):
    if len(ch.string.strip()) > 0:
        print(ch.string.strip())
all_sig = soup.find(id="signatures")
print("----------------warnings----------------")
for ch in all_sig.find_all("div", class_="alert-warning"):
    print(ch.string.strip())
print("-----------------errors-----------------")
for ch in all_sig.find_all("div", class_="alert-danger"):
    print(ch.string.strip())
