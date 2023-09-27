from flask import Flask,render_template,redirect,url_for,request
from db import getTaskList,addTask,updateTask,deleteTask
app = Flask(__name__)
# tasklist=[["walk dog",True],["play cricket",True]]

@app.route("/")
def home():
    tasklist = getTaskList()
    return render_template("tasklist.html",TaskList=tasklist)

@app.route("/add",methods=['POST'])
def add():
    taskname = request.form['Task Name']
    isDone  = request.form['isDone']
    addTask(taskname,isDone)
    return redirect(url_for('home'))

@app.route("/update",methods=['POST'])
def update():
    taskname = request.form['updatedTask']
    isDone=request.form['updatedDate']
    id = request.form['id']
    button=request.form['SaveOrDelete']
    if button == 'save':
       updateTask(taskname,id,isDone)
    elif button == 'delete':
       deleteTask(id)

    return redirect(url_for('home'))
app.run()
