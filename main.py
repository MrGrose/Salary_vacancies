import os

from arg_parser import create_parser
from auxiliary_scripts import (draw_table, get_vacancies_statistic,
                               predict_rub_salary_hh, predict_rub_salary_sj)
from dotenv import load_dotenv
from vacancies import get_vacancies_hh, get_vacancy_superjob


def main():
    load_dotenv()
    superjob_key = os.environ["SUPERJOB_API_KEY"]
    if "SUPERJOB_API_KEY" not in os.environ:
        return
    parser = create_parser()
    parsed_args = parser.parse_args()
    hh_vacancies = get_vacancies_hh(parsed_args.l)
    hh_statistic = get_vacancies_statistic(hh_vacancies, predict_rub_salary_hh)
    sj_vacancies = get_vacancy_superjob(parsed_args.l, superjob_key)
    sj_statistic = get_vacancies_statistic(sj_vacancies, predict_rub_salary_sj)
    print(draw_table(hh_statistic, "HeadHunter Moscow"))
    print()
    print(draw_table(sj_statistic, "SuperJob Moscow"))


if __name__ == '__main__':
    main()