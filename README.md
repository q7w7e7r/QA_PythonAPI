# QA_PythonAPI
requests, pytest, Allure, Docker

Git
  git clone https://github.com/q7w7e7r/QA_PythonAPI.git

Pytest
  Run all tests
    python -m pytest 

Allure
  python -m pytest --alluredir=test_results/ tests/
  allure serve test_results

Docker
  Create image
  docker build -t pytest_runner .
  Run conteiner
  docker run --rm --mount type=bind,src=C:\Users\q7w7e\PycharmProjects\QA_PythonAPI,target=/tests_project/ pytest_runner

Docker-compose
  docker-compose up --build
