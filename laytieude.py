import requests
from bs4 import BeautifulSoup
response = requests.get('https://imgflip.com/memetemplates?page=1')
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all("h3")
    images = soup.find_all("img", class_="shadow")
    for title, image in zip(titles, images):
        image_src = image['src'].replace("/4","",1)
        print(f"{title.get_text(strip=True)}: https:{image_src}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")