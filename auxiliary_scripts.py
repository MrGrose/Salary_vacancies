from statistics import mean

from terminaltables import AsciiTable


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_from and not salary_to:
        return salary_from * 1.2
    elif not salary_from and salary_to:
        return salary_to * 0.8
    else:
        return None


def predict_rub_salary_sj(vacancy):
    currency = vacancy.get("currency")
    if currency != "rub":
        return None
    return predict_salary(vacancy.get("payment_from"), vacancy.get("payment_to"))


def predict_rub_salary_hh(vacancy):
    salary = vacancy.get("salary")
    if not salary:
        return None
    currency = salary.get("currency")
    if currency != "RUR":
        return None
    return predict_salary(salary.get("from"), salary.get("to"))


def get_vacancies_statistic(vacancies, predict_rub_salary_func):
    vacancies_statistic = {}
    for language, data in vacancies.items():
        vacancies_count = data.get("count")
        vacancies_items = data.get("items")
        salaries = []
        for vacancy in vacancies_items:
            salary = predict_rub_salary_func(vacancy)
            if salary:
                salaries.append(salary)
        average_salary = int(mean(salaries)) if salaries else 0

        vacancies_statistic[language] = {
            "vacancies_found": vacancies_count,
            "vacancies_processed": len(salaries),
            "average_salary": average_salary,
        }
    return vacancies_statistic


def draw_table(vacancies_statistic, title):
    raw_table = [
        [
            "Язык программирования",
            "Вакансий найдено",
            "Вакансий обработано",
            "Средняя зарплата",
        ]
    ]
    for language in vacancies_statistic:
        raw_table.append(
            [
                language,
                vacancies_statistic[language]["vacancies_found"],
                vacancies_statistic[language]["vacancies_processed"],
                vacancies_statistic[language]["average_salary"],
            ]
        )
    table_instance = AsciiTable(raw_table, title)
    return table_instance.table