import requests
from bs4 import BeautifulSoup

url = 'http://sch38.minsk.edu.by/ru/main.aspx?guid=2571'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

schedule_table = soup.find_all('table')

shedule_dict = dict()
day_lessons = []
day_lessons_11 = []
day_lessons_10 = []

days = []
lessons = []
class_number = '6'
index = 0
for table in schedule_table:
    day = ''
    previous_day = ''

    for i, row in enumerate(table.find_all('tr')):
        if class_number.isdigit():
            columns = row.find_all('td')
            if i == 1:
                class_number = columns[2].get_text(strip=True)[0]
                # shedule_dict['class_number'] = class_number
                continue
            elif i in [0, 2]:
                continue
            else:

                lesson_number = columns[0].get_text(strip=True)
                if lesson_number.isdigit():
                    subject = columns[1].get_text(strip=True)
                    room = columns[2].get_text(strip=True)
                    # shedule_dict[class_number][day] = {'lesson_number': lesson_number, 'subject': subject, 'room': room}
                    day_lessons.append({'class_number': class_number, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                else:
                    day = columns[0].get_text(strip=True)
                    lesson_number = columns[1].get_text(strip=True)
                    subject = columns[2].get_text(strip=True)
                    room = columns[3].get_text(strip=True)
                    # shedule_dict[class_number]['day'] = int(day)
                    # shedule_dict[class_number][day] = {'lesson_number': lesson_number, 'subject': subject, 'room': room}
                    day_lessons.append({'class_number': class_number, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})

        else:
            for i, row in enumerate(table.find_all('tr')):
                columns = row.find_all('td')
                upk = 'УПК'
                if i == 0:
                    tenth_class = columns[2].get_text(strip=True)
                    eleventh_class = columns[3].get_text(strip=True)
                    # print(tenth_class, eleventh_class)
                    continue

                elif i == 1:
                    continue



                elif columns[2].get_text(strip=True) == 'УПК' or \
                        len(columns) == 3:
                    lesson_number = columns[0].get_text(strip=True)
                    if lesson_number.isdigit():
                        subject = upk
                        room = None
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = columns[1].get_text(strip=True)
                        room = columns[2].get_text(strip=True)
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                    else:
                        day = columns[0].get_text(strip=True)
                        lesson_number = columns[1].get_text(strip=True)
                        subject = upk
                        room = None
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = columns[3].get_text(strip=True)
                        room = columns[4].get_text(strip=True)
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})

                elif columns[-1].get_text(strip=True) == 'УПК' or \
                        len(columns) == 3:
                    lesson_number = columns[0].get_text(strip=True)
                    if lesson_number.isdigit():
                        subject = columns[1].get_text(strip=True)
                        room = columns[2].get_text(strip=True)
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = upk
                        room = None
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                    else:
                        day = columns[0].get_text(strip=True)
                        lesson_number = columns[1].get_text(strip=True)
                        subject = columns[2].get_text(strip=True)
                        room = columns[3].get_text(strip=True)
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = upk
                        room = None
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})


                else:
                    lesson_number = columns[0].get_text(strip=True)
                    if lesson_number.isdigit():
                        subject = columns[1].get_text(strip=True)
                        room = columns[2].get_text(strip=True)
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = columns[3].get_text(strip=True)
                        room = columns[4].get_text(strip=True)
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                    else:
                        day = columns[0].get_text(strip=True)
                        lesson_number = columns[1].get_text(strip=True)
                        subject = columns[2].get_text(strip=True)
                        room = columns[3].get_text(strip=True)
                        day_lessons_10.append({'class_number': tenth_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})
                        subject = columns[4].get_text(strip=True)
                        room = columns[5].get_text(strip=True)
                        day_lessons_11.append({'class_number': eleventh_class, 'day': day, 'lesson_number': lesson_number, 'subject': subject, 'room': room})

print(day_lessons)
print("================================================")
print(day_lessons_10)
print("================================================")
print(day_lessons_10)
print("================================================")

