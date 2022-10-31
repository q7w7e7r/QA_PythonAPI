import os
from datetime import datetime
from requests import Response


class Logger:
    file_name = "logs/log_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        cwd = os.getcwd()
        files = os.listdir(cwd)
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        testname = os.environ.get("PYTEST_CURRENT_TEST")  # Какой тест запущен и как называется

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"Time: {str(datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += "\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"Response code:{response.status_code}\n"
        data_to_add += f"Response text:{response.text}\n"
        data_to_add += f"Response headers:{response.headers}\n"
        data_to_add += f"Response cookies:{response.cookies}\n"
        data_to_add += "\n-----\n"

        cls._write_log_to_file(data_to_add)
