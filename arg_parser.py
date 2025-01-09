import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="""
        Скрипт высчитывает среднюю зарлату по вакансиям разработчиков 
        в г.Москва на сервисе HeadHunter и SuperJob в разрезе языков программирования. 
        """
    )
    parser.add_argument(
        "-l",
        default=[
            "Python", 
            "Java", 
            "Javascript", 
            "C++", 
            "C#", 
            "Ruby", 
            "PHP", 
            "Swift", 
            "Go", 
            "Kotlin",
        ],
        nargs="+",
        help="список языков программирования для поиска вакансий",
    )
    return parser
