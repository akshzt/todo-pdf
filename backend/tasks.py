import psycopg2
from celery import Celery
import os
from PDFUtil import PDF


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")
conn = psycopg2.connect(
    database="postgres", user="postgres", password="mysecretpassword",
    host="127.0.0.1", port="5432"
)

conn.autocommit = True
cursor = conn.cursor()


def create_pdf(todos):
    pdf = PDF()
    pdf.add_page()
    # print(len(todos))
    for i in range(0, len(todos)):
        pdf.cell(0, 10, f"ID: {todos[i][0]}  TASK: {todos[i][1]}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("static/data_pdf.pdf")


@celery.task(name='create_pdf_task')
def create_pdf_task():

    cursor.execute('SELECT * FROM todos')
    result = cursor.fetchall()
    conn.commit()

    create_pdf(result)

    return True
