from flask import Flask ,render_template,request,redirect
app=Flask(__name__)
todo=[]
@app.route("/")
def home():
    return render_template("index.html",todo=todo)
@app.route("/upload",methods=["post"])
def upload():
    task=request.form.get("task")
    priority=request.form.get("priority")
    due_date=request.form.get("due_date")
    assign=request.form.get("assign")
    data={"task":task,"priority":priority,"due_date":due_date,"assign":assign}

    todo.append(data)
    return redirect("/")
@app.route("/edit/<int:index>")
def edit_task(index):
    return render_template("todo.html",todo=todo,edit_task=todo[index],edit_idx=index)

@app.route("/update/<int:index>", methods=["POST"])
def update_task(index):
    task = request.form.get("task")
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")
    assign = request.form.get("assign")
    todo[index] = {"task": task,"priority": priority,"due_date": due_date,"assign": assign}
    return redirect("/")
@app.route("/detail/<int:idx>")
def detail(idx):
    return render_template( "detail.html", task=todo[idx] )
    return redirect("/")
@app.route("/delete/<int:idx>")
def delete(idx):
    todo.pop(idx)
    return redirect("/")
app.run(debug=True)