from bs4 import BeautifulSoup
import requests

#website that we are scraping, requesting that page

URL = input("Enter the URL of the Wikipedia Page: ")
page = requests.get(URL)
#parse the html from the page content, find all elements with these classes
soup = BeautifulSoup(page.content, "html.parser")
h2_list = soup.find_all("h2")
h3_list = soup.find_all("h3")
temp_list = []
for h2 in h2_list:
    if h2 is not None:
        h2 = h2.text
        temp_list.append(h2)

h2_list = temp_list
temp_list = []

for h3 in h3_list:
    if h3 is not None:
        h3 = h3.text
        temp_list.append(h3)
h3_list = temp_list

print("Header 2s:")
print(h2_list)
print("Header 3s:")

print(h3_list)

        
