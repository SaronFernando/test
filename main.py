from flask import Flask,render_template, request, redirect

app=Flask(__name__)
@app.route("/")
def index ():
    return render_template('login.html')

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        print(request.form["user"])
        print(request.form["pass"])
    return redirect("/")
    
@app.route("/create", methods=["GET","POST"])
def create_account():
        return render_template('new_account.html')
        

if __name__=="__main__"  :
    app.run(debug=True)
