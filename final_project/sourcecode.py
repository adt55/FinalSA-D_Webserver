from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__,template_folder='templates')
Bootstrap(app)

@app.route("/home")
def home():
    return render_template("home.htm")

@app.route('/result')
def result():
    return render_template("result.htm")

@app.route('/addrec/',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        item_id = request.form['item_id']
        nm = request.form['nm']
        phone_type = request.form['phone_type']
        case_color = request.form['case_color']
        price = request.form['price']

        with sql.connect("cases_db.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO cases (item_id,name,type,color,price) VALUES('{0}','{1}','{2}','{3}', '{4}')".format(item_id, nm, phone_type, case_color, price))
            con.commit()

        return render_template("result.htm")
        con.close()

@app.route('/list/')
def list():
    con = sql.connect("cases_db.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from cases")

    rows = cur.fetchall()
    return render_template("list.htm", rows = rows)

@app.route('/add/')
def add():
    return render_template("add.htm")

if __name__ == "__main__":
    app.run(debug=True)