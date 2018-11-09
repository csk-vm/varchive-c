# vforum.py


from flask import Flask,request,render_template,redirect,url_for
import pymysql
import os
import subprocess

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "mysqldb"
        user = "vforum"
        password = os.environ["DBPASS"]
        db = "vforum_db"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_comments(self):
        self.cur.execute("SELECT submit_date, name, comment FROM comments")
        result = self.cur.fetchall()

        return result

    def insert_comments(self, name, comment):
        self.name = name
        self.comment = comment
        self.cur.execute("INSERT into comments (submit_date, name, comment) values(now(), '"+self.name+"', '"+self.comment+"')")
        self.con.commit()
        self.con.close()


@app.route('/')
def index():
    def db_query():
        db = Database()
        cmts = db.list_comments()

        return cmts

    res = db_query()

    return render_template('index.html', result=res, content_type='application/json')

@app.route('/comment')
def comment():
    return render_template('comment.html',name=request.args.get('name'))

@app.route('/add_comment' ,methods = ['POST'])
def add_comment():
        db = Database()
        db.insert_comments(request.form['Name'], request.form['Comment'])

        return redirect(url_for('comment', name=request.form['Name']))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
