from flask import Flask,render_template,request
import requests
base_url = "https://api.github.com/users/"
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        githubname=request.form.get("githubname")
        response_user=requests.get(base_url+githubname)
        response_repos=requests.get(base_url +githubname + "/repos")
        repos=response_repos.json()

        user_info=response_user.json()
        if "message" in user_info:
            return render_template("index.html",error="Ein solcher Benutzer wurde leider nicht gefunden")
        else:
            return render_template("index.html",profile= user_info,repos=repos)




    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
