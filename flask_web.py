from flask import Flask,request
from flask_dojo import psql_db
from flask_dojo import Counter
import os


app=Flask(__name__)
app.secret_key="1234"
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flask_dojo.db')))

get_counter=0
post_counter=0

psql_db.connect()
psql_db.create_tables([Counter], safe=True)

def init_table():
    Counter.create(0,0)

@app.route("/request-counter" , methods=["POST","GET"])
def req_counter():
    global post_counter
    global get_counter

    if request.method=="POST":
        post_counter+=1
        update=Counter.update(post_request=post_counter).where(Counter.id==1)
        update.execute()

    if request.method=="GET":
        get_counter+=1
        update=Counter.update(get_request=get_counter).where(Counter.id==1)
        update.execute()

@app.route("/statistics")
def statistics():
    pass


if __name__=="__main__":
    app.run()

