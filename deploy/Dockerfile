FROM python:latest
RUN pip install --upgrade pip

WORKDIR /dash-flask-app

RUN useradd --create-home du
RUN chown du:du -R /dash-flask-app

USER du

COPY --chown=du:du requirements.txt /

ENV PATH="${PATH}:/home/du/.local/bin"

RUN pip install --user --upgrade -r /requirements.txt

COPY --chown=du:du app/ ./app

CMD ["gunicorn", "--bind", "0.0.0.0:8005", "--workers", "4", "app.app:server"]
