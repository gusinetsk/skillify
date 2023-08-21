import requests
from bs4 import BeautifulSoup

url = 'http://gymn6.minsk.edu.by/ru/main.aspx?guid=45071'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    schedule_entries = soup.find_all('div', class_='lesson')

    extracted_schedule = []
    for entry in schedule_entries:
        lesson_number = entry.find('div', class_='lesson-number').text.strip()
        lesson_name = entry.find('div', class_='lesson-name').text.strip()
        lesson_day = entry.find('div', class_='lesson-day').text.strip()

        extracted_schedule.append({
            "lesson_number": lesson_number,
            "lesson_name": lesson_name,
            "lesson_day": lesson_day
        })

    for entry in extracted_schedule:
        print(f"Урок {entry['lesson_number']} - {entry['lesson_name']} ({entry['lesson_day']})")
else:
    print('Ошибка при запросе к сайту')
