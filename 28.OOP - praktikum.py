from math import radians, sin, cos, acos

# class Contact:
#     def __init__(self, name, phone, address, birthday):
#         self.name = name
#         self.phone = phone
#         self.address = address
#         self.birthday = birthday
#         print(f"Создаём новый контакт {name}")
#
#
#
#     def show_contact(self):
#         print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, "
#               f"день рождения: {self.birthday}")
#
#
# mike = Contact('Михаил Булгаков','2-03-27','Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
#                '15.05.1891')
# vlad = Contact('Владимир Маяковский','73-88','Россия, Москва, Лубянский проезд, д. 3, кв. 12','19.07.1893')
#
# # def print_contact():
# #     print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, "
# #           f"день рождения: {vlad.birthday}")
#
# mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# mike.phone = 'К-058-67'
# vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# vlad.phone = '2-35-71'
# mike.show_contact()
# vlad.show_contact()



# class Planet:
#     def __init__(self, name, radius, temp_celsius):
#         self.name = name
#         self.surface_area =  4 * math.pi * radius ** 2
#         self.average_temp_celcius = temp_celsius
#         self.average_temp_fahrenheit =  temp_celsius * 9/5 + 32
#
#     def show_info(self):
#         print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
#         print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")
#
# jupiter = Planet('Юпитер', 69911, -108)
#
# jupiter.show_info()



# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
# class Friend(User):
#     def show(self):
#         print(f'Имя: {self.name} || Телефон: {self.phone}')
# user = User("Виктор Гюго", "+33 1 42 72 10 16")
# # у класса friend нет конструктора, но он есть
# # у родительского класса User, поэтому код сработает]
# friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")
# user.show()
# friend.show()
#


# импортируем функции из библиотеки math для рассчёта расстояния

# class Point:
#     def __init__(self, latitude, longitude):
#         self.latitude = radians(latitude)
#         self.longitude = radians(longitude)
#
#     # считаем расстояние между двумя точками в км
#     def distance(self, other):
#         cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
#         self.longitude - other.longitude)
#         return 6371 * acos(cos_d)
#
# class City(Point):
#
#     def __init__(self, latitude, longitude, name, population):
#         super().__init__(latitude,longitude)
#         self.name = name
#         self.population = population
#
#     def show(self):
#         print(f"Город {self.name}, население {self.population} чел.")
#
# class Mountain(Point):
#
#     def __init__(self, latitude, longitude, name, height):
#         super().__init__(latitude,longitude)
#         self.name = name
#         self.height = height
#
#     def show(self):
#         print(f"Высота горы {self.name} - {self.height} м.")
#
# Msc = City(55.751244,37.618423,'Москва',144000000)
# Evrst = Mountain(27.986065, 86.922623,'Эверест',8849)
# Msc.show()
# Evrst.show()
# print(Msc.distance(Evrst))


class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')

class Student(Human):
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {question}')
        super().answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)

class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)

class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')