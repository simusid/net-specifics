from flask import Flask
from flask import request, flash, session
from flask import render_template, url_for
import os
from glob import glob
import random
import shutil
from NetSpecifics import NSImage 

app = Flask(__name__)
app.secret_key = 'many rando bytes'

fnames = tuple(glob("app/data/unlabeled/*jpg"))   # immutable master copy

@app.route("/")
def do_index():
    global fnames
     
    fnames = random.sample(fnames,36) # todo
    for i in range(36):  # TODO fix this 
        shutil.copyfile(fnames[i], "app/static/array/{}.jpg".format(i))
    if("classes" not in session):
        #flash("there are no classes defined")
        classes = ''
    else:
        classes = session['classes']
    return render_template("index.html", classes=classes)

@app.route("/replaceimage/<index>")
@app.route("/replaceimage/<index>/<isnew>")
def do_replace_image(index, isnew=None):
    global fnames  
    fname= random.choice(fnames)
    shutil.copyfile(fname, "app/static/array/{}.jpg".format(index))
    #flash("Image added to class TBD")

    if("classes" not in session):
        #flash("there are no classes defined")
        classes = ''
    else:
        classes = session['classes']
    if(isnew!=None):
        flash("whoa we're adding a new class!")
    return render_template("index.html", classes = classes)

 


