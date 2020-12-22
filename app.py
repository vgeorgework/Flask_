from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import os

app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = "mysql"
# app.config['MYSQL_DB'] = "TEST"
app.config['MYSQL_HOST'] = os.getenv('mysql')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "toor"


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
