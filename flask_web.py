from flask import Flask,request

app=Flask(__name__)
app.secret_key="1234"


get_counter=0
post_counter=0



@app.route("/request-counter" , methods=["POST","GET"])
def req_counter():
    global post_counter
    global get_counter

    if request.method=="POST":
        post_counter+=1

    if request.method=="GET":
        get_counter+=1


@app.route("/statistics")
def statistics():
    pass

