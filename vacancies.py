import time

import requests


def fetch_vacancies(url, headers=None, params=None, page=0, pages_number=1):
    vacancies = []
    while page < pages_number:
        params["page"] = page
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            payload = response.json()
            if "pages" in payload:
                pages_number = payload["pages"]
            elif "total" in payload:
                pages_number = payload["total"] // params["count"]
                if pages_number * params["count"] < payload["total"]:
                    pages_number += 1
            page += 1
            
            if "items" in payload:
                vacancies.extend(payload["items"])
            elif "objects" in payload:
                vacancies.extend(payload["objects"])
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            break
    return vacancies


def get_vacancies_hh(languages):
    url = "https://api.hh.ru/vacancies"
    town_id = 1
    period = 30
    params = {
        "area": town_id,
        "period": period,
        "search_field": "name",
    }
    vacancies = {}
    for language in languages:
        params["text"] = language
        vacancies[language] = fetch_vacancies(url, params=params)
    return vacancies


def get_vacancy_superjob(languages, superjob_key):
    url = "https://api.superjob.ru/2.0/vacancies/"
    headers = {"X-Api-App-Id": superjob_key}
    town_id = 4
    profession_id = 48
    number_vacancies_on_page = 20
    params = {
        "town": town_id,
        "catalogues": profession_id,
        "count": number_vacancies_on_page,
    }
    vacancies = {}
    for language in languages:
        params["keyword"] = language
        vacancies[language] = fetch_vacancies(url, headers=headers, params=params)
    return vacancies