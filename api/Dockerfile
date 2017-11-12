FROM python:3

ADD . /

ENV FLASK_APP app/main.py
RUN pip install -r ./requirements.txt

CMD [ "flask", "run" ]
EXPOSE 5000