FROM python:3.10
WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir shared
COPY . .
ENTRYPOINT pytest -rP --continue-on-collection-errors tests/
