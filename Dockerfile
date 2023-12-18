FROM python:3.9
LABEL authors="onelots"


ENV LANG fr_FR.UTF-8
WORKDIR /app
COPY . /app
LABEL authors="onelots"

CMD [ "python", "main.py" ]