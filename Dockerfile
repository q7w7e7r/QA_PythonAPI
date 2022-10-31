FROM python:3.8
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV END=dev
CMD python -m pytest -s --alluredir=test_results/ /tests_project/tests/