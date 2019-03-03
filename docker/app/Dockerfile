FROM python:3.6.3

RUN mkdir /code
ADD requirements.txt /code/
ADD Pipfile /code/
# ADD Pipfile.lock /code/
WORKDIR /code
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv --python /usr/local/bin/python
RUN pipenv lock --pre
RUN pipenv install && \
    apt-get update && \
    apt-get install -y mysql-client

CMD pipenv run python3 /code/manage.py runserver 0.0.0.0:80
