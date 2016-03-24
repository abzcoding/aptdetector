"""docstring"""
from bs4 import BeautifulSoup


with open("tests/test_cuckoo.html") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
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
