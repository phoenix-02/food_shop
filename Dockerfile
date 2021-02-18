FROM python:3.8

EXPOSE 8000
WORKDIR mysite
COPY . /mysite/
ADD . .
RUN 'dir'
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
