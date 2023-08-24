import requests
import json

from bs4 import BeautifulSoup
from pprint import pprint


class ParsingPage:

    @staticmethod
    def parse():
        url = 'http://sch38.minsk.edu.by/ru/main.aspx?guid=2571'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        schedule_table = soup.find_all('table')

        schedule_dict = dict()

        class_number = '6'

        for table in schedule_table:
            day = ''
            previous_day = ''

            for i, row in enumerate(table.find_all('tr')):
                if class_number.isdigit():
                    columns = row.find_all('td')
                    if i == 1:
                        class_number = columns[2].get_text(strip=True)[0]
                        if class_number.isdigit():
                            schedule_dict[class_number] = []
                        continue
                    elif i in [0, 2]:
                        continue
                    else:
                        lesson_number = columns[0].get_text(strip=True)
                        if lesson_number.isdigit():
                            subject = columns[1].get_text(strip=True)
                            room = columns[2].get_text(strip=True)
                            schedule_dict[class_number].append({
                                'day': day,
                                'lesson_number': lesson_number,
                                'subject': subject,
                                'room': room
                            })
                        else:
                            day = columns[0].get_text(strip=True)

                            lesson_number = columns[1].get_text(strip=True)
                            subject = columns[2].get_text(strip=True)
                            room = columns[3].get_text(strip=True)
                            schedule_dict[class_number].append({
                                'day': day,
                                'lesson_number': lesson_number,
                                'subject': subject,
                                'room': room
                            })

                else:
                    for i, row in enumerate(table.find_all('tr')):
                        columns = row.find_all('td')
                        upk = 'УПК'
                        if i == 0:
                            tenth_class = columns[2].get_text(strip=True)
                            eleventh_class = columns[3].get_text(strip=True)
                            schedule_dict[tenth_class] = []
                            schedule_dict[eleventh_class] = []
                            continue

                        elif i == 1:
                            continue

                        elif columns[2].get_text(strip=True) == 'УПК' or \
                                len(columns) == 3:
                            lesson_number = columns[0].get_text(strip=True)
                            if lesson_number.isdigit():
                                subject = upk
                                room = None
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = columns[1].get_text(strip=True)
                                room = columns[2].get_text(strip=True)
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                            else:
                                day = columns[0].get_text(strip=True)
                                lesson_number = columns[1].get_text(strip=True)
                                subject = upk
                                room = None
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = columns[3].get_text(strip=True)
                                room = columns[4].get_text(strip=True)
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })

                        elif columns[-1].get_text(strip=True) == 'УПК' or \
                                len(columns) == 3:
                            lesson_number = columns[0].get_text(strip=True)
                            if lesson_number.isdigit():
                                subject = columns[1].get_text(strip=True)
                                room = columns[2].get_text(strip=True)
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = upk
                                room = None
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })

                            else:
                                day = columns[0].get_text(strip=True)
                                lesson_number = columns[1].get_text(strip=True)
                                subject = columns[2].get_text(strip=True)
                                room = columns[3].get_text(strip=True)
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = upk
                                room = None
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })

                        else:
                            lesson_number = columns[0].get_text(strip=True)
                            if lesson_number.isdigit():
                                subject = columns[1].get_text(strip=True)
                                room = columns[2].get_text(strip=True)
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = columns[3].get_text(strip=True)
                                room = columns[4].get_text(strip=True)
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })

                            else:
                                day = columns[0].get_text(strip=True)
                                lesson_number = columns[1].get_text(strip=True)
                                subject = columns[2].get_text(strip=True)
                                room = columns[3].get_text(strip=True)
                                schedule_dict[tenth_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })
                                subject = columns[4].get_text(strip=True)
                                room = columns[5].get_text(strip=True)
                                schedule_dict[eleventh_class].append({
                                    'day': day,
                                    'lesson_number': lesson_number,
                                    'subject': subject,
                                    'room': room
                                })

        return schedule_dict

schedule_data = ParsingPage.parse()

output_filename = 'schedule_data.json'

with open(output_filename, 'w', encoding='utf-8') as output_file:
    json.dump(schedule_data, output_file, ensure_ascii=False, indent=4)
