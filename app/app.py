from flask import Flask
from flask import request, flash, session, redirect 
from flask import render_template, url_for
import os
from glob import glob
import random
import shutil
from NetSpecifics import NSImage, makeNewClass

app = Flask(__name__)
app.secret_key = 'abcdefg'   

fnames = tuple(glob("app/data/unlabeled/*jpg"))   # immutable master copy

@app.route("/")
def do_index():
    global fnames
     
    fnames = random.sample(fnames,36) # todo
    for i in range(36):  # TODO fix this 
        shutil.copyfile(fnames[i], "app/static/array/{}.jpg".format(i))
    if("classes" not in session):
        classes = []
    else:
        classes = session['classes']

    session['classes'] = list([ makeNewClass(12), makeNewClass(20)])

    print(session['classes'])
    return render_template("index.html", classes=classes)

@app.route("/replaceimage/<index>")
@app.route("/replaceimage/<index>/<isnew>")
def do_replace_image(index, isnew=None):
    global fnames  
    fname= random.choice(fnames)
    shutil.copyfile(fname, "app/static/array/{}.jpg".format(index))
 
    if("classes" not in session):
        classes = []
    else:
        classes = session['classes']

    if(session['status']=="newlabel"):
        print('adding a new class')
        thisclass = makeNewClass(index) # example [1,"example1.jpg", 22]

        print("session classes is {}".format(session['classes']))
        session['status'] = None
    return redirect(url_for("index.html", classes = classes))
 

@app.route('/setstatus/<status>')
def do_set_status(status):
    print("setting status to {}".format(status))
    session['status']=status
    return "success"


 


