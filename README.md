# Сравниваем вакансии программистов
Этот проект предназначен для сбора и анализа вакансий с сайтов HeadHunter и SuperJob. Он позволяет получать статистику по средним зарплатам для различных языков программирования в Москве. Список поиска:
- Python, Java, Javascript, C++, C#, Ruby, PHP, Swift, Go, Kotlin

### Функциональность
- Сбор вакансий: Проект собирает вакансии с HeadHunter и SuperJob для заданных языков программирования.
- Расчет средних зарплат: Проект рассчитывает средние зарплаты для каждой вакансии и выводит статистику по языкам программирования.
- Вывод результатов: Результаты представлены в виде таблицы, где указано количество найденных и обработанных вакансий, а также средняя зарплата.

### Требования
- Проект написан на Python 3.12.3.
- API ключ:
    - API ключ для SuperJob получить можно по [инструкции](https://api.superjob.ru/).
### Установка
1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
2. Создайте файл .env в корне проекта и добавьте в него API ключ для SuperJob:
    ```bash
    SUPERJOB_API_KEY=ваш_ключ_сюда
    ```
### Использование
1. Основной исполняемый скрипт `main.py`, принимает обязательный аргумент:
    - рекомендуется запускать так, ищет по языкам из списка:
    ```bash
    python main.py
    ```
    - "-l", если вам нужен какой то один или несколько языков, то через запятую можно перечислить:
    ```bash
    python main.py -l Python, Java
    ```
2. Вывод будет представлен в виде таблицы для каждой платформы (HeadHunter и SuperJob), пример ниже.

    -![пример](https://private-user-images.githubusercontent.com/147311692/401578176-637f5e1c-ee5c-4c80-b611-e69da651b9d6.JPG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY0MzM0MzcsIm5iZiI6MTczNjQzMzEzNywicGF0aCI6Ii8xNDczMTE2OTIvNDAxNTc4MTc2LTYzN2Y1ZTFjLWVlNWMtNGM4MC1iNjExLWU2OWRhNjUxYjlkNi5KUEc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEwOVQxNDMyMTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZDhhM2I5M2EwMmMwNGFhZmFiNDI0YjlkY2ZjZDYwYjc1NDBiMGZkYWE1Njc0ZGQxMDVmZmM1ZDE5Njc4YTMzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.q7fsBoRIoJFxp-FlbqjJ4XA0jTRIwJvn8f7ZfXryQ_o)
    

### Структура проекта
- main.py: Основной скрипт, который запускает сбор и анализ вакансий.
- vacancies: Сбор вакансий с HeadHunter и SuperJob соответственно.
- auxiliary_scripts.py: Модуль с вспомогательными функциями для расчета зарплат и вывода таблиц.
