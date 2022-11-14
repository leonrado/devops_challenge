from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config["MYSQL_USER"] = os.getenv('MYSQL_USER')
app.config["MYSQL_HOST"] = os.getenv('MYSQL_HOST')
app.config["MYSQL_PASSWORD"] = os.getenv('MYSQL_PASSWORD')
app.config["MYSQL_DB"] = os.getenv('MYSQL_DB')
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

#CREATE TABLE my_table(msg varchar(255));
#INSERT INTO my_table(msg) VALUES('Hello World!');

mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT msg FROM my_table""")
    data = cur.fetchall()
    return str(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
