import requests
from bs4 import BeautifulSoup

response = requests.get('https://imgflip.com/memetemplates?page=1')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    danh_sach_A = soup.find_all("a", class_="mt-caption")  # Đổi findall thành find_all
    for tag_a in danh_sach_A:
        full_href = tag_a['href']  # Lấy thuộc tính href của thẻ a
        print(full_href)  # In ra link đầy đủ
