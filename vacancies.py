import time

import requests


def get_vacancies_hh(languages):
    vacancies = {}
    town_id = 1
    for language in languages:
        vacancies[language] = {"count": 0, "items": []}
        pages_number = 1
        page = 0
        while page < pages_number:
            params = {
                "area": town_id,
                "text": language,
                "search_field": "name",
                "page": page
            }
            try:
                page_response = requests.get(
                    "https://api.hh.ru/vacancies",
                    params=params,
                )
                page_response.raise_for_status()
                page_payload = page_response.json()
                pages_number = page_payload["pages"]
                page += 1
                vacancies[language]["count"] = page_payload["found"]
                vacancies[language]["items"].extend(page_payload["items"])
                time.sleep(0.5)
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при запросе: {e}")
                break
    return vacancies


def get_vacancy_superjob(languages, superjob_key):
    headers = {"X-Api-App-Id": superjob_key}
    vacancies = {}
    town_id = 4
    profession_id = 48
    number_vacancies_on_page = 20
    vacancies_number_limit = 500
    for language in languages:
        vacancies[language] = {"count": 0, "items": []}
        pages_number = 1
        page = 0
        while page < pages_number:
            params = {
                "town": town_id,
                "catalogues": profession_id,
                "keyword": language,
                "page": page,
                "count": number_vacancies_on_page
            }
            try:
                page_response = requests.get(
                    "https://api.superjob.ru/2.0/vacancies/",
                    headers=headers,
                    params=params,
                )
                page_response.raise_for_status()
                page_payload = page_response.json()
                vacancies[language]["count"] = page_payload["total"]
                if page_payload["total"] > vacancies_number_limit:
                    pages_number = vacancies_number_limit // number_vacancies_on_page
                elif page_payload["total"] < number_vacancies_on_page:
                    pages_number = 1
                else:
                    pages_number = page_payload["total"] // number_vacancies_on_page
                page += 1
                vacancies[language]["items"].extend(page_payload["objects"])
                time.sleep(0.5)
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при запросе: {e}")
                break
    return vacancies