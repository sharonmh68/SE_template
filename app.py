from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

def catalogue():
    con = sqlite3.connect("database/data.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM catalogue').fetchall()
    con.close()
    return data
    

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    data = catalogue;
    return render_template('index', catalogue_data = data)

if __name__ == '__main__':
    app.run(debug=True)

