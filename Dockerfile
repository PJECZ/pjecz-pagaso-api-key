FROM python:3.10

WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 6001

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:6001", "-k", "uvicorn.workers.UvicornWorker", "pegaso.app:app" ]