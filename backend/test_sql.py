import psycopg2
from PDFUtil import PDF


conn = psycopg2.connect(
    database="postgres", user="postgres", password="mysecretpassword",
    host="127.0.0.1", port="5432"
)

conn.autocommit = True
cursor = conn.cursor()
cursor.execute('SELECT * FROM todos')
result = cursor.fetchall()
print("Fetch results: ", result)
print(type(result))
print(result[0])
print(result[0][0])
conn.commit()

conn.close()


def create_pdf(todos):
    pdf = PDF()
    pdf.add_page()
    # print(len(todos))
    for i in range(0, len(todos)):
        pdf.cell(0, 10, f"ID: {todos[i][0]}  TASK: {todos[i][1]}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("static/data_pdf.pdf")


create_pdf(result)
