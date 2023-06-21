from flask import Blueprint, render_template

about_app = Blueprint("about_app", __name__)

names_projects_list = [
    'Cервис по выбору мероприятий и покупки билетов во Владимире',
    'Сервис по распознаванию физических упражнений на видео',
    'Сервис оценки зарплаты в сфере Data Science',
    'Сервис по распознаванию автомобильных номеров',
]
urls_projects_list = [
    'https://t.me/koncert_calendar_bot',
    'http://109.201.65.62:5777/',
    'http://109.201.65.62:5666/',
    'http://109.201.65.62:5999/',
]

# НЕ ПОЛУЧАЕТСЯ ПРОЧИТАЛ ФАЙЛ ВО ВРЕМЯ ТКСТОВ:
# ERROR testing/test_homework_05/test_app.py - FileNotFoundError: [Errno 2] No such file or directory: 'text_paragraphs.txt'

# f_path = 'about_info_files/text_paragraphs.txt'
# f_path = 'text_paragraphs.txt'
# with open(f_path, mode='r') as f:
#     text_paragraphs = f.readlines()


# Поэтому пропишу хардкорно
text_paragraphs = [
    '''Я начинающий Python разработчик.''',

    '''    Два года работал инженером программистом.
        На втором году работы начал обучаться в УИИ на потоке PRO курса Data Science, где получил базовые знания в сфере аналитики и освоил язык программирования Python.
        В конце обучения успешно защитил дипломный проект на тему «Классификация физических упражнений по видео».''',

    '''    После защиты диплома начал активно заниматься аналитикой данных с применением алгоритмов машинного обучения (ML). Наиболее знакома область работы с изображениями и табличными данными.
    ''',
    '''    Год работал в АНО "Диалог Регионы" программистом разработчиком (Python) и аналитиком.
        Занимался разработкой и поддержкой БД (PostgreSQL), разработкой TG ботов, дашбордов, парсингом данных и обучение математических моделей на них.
    ''',
]


@about_app.get("/", endpoint="info")
def render_about_page():
    return render_template("my/about.html",
                           names_projects_list=names_projects_list,
                           urls_projects_list=urls_projects_list,
                           text_paragraphs=text_paragraphs,
                           zip=zip,
                           )
