from flask import Flask, request, redirect, render_template
import users
import sessions
import articles

app =  Flask("News Recommender")

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/login")
def login():
    if len(request.args.keys()) == 2:
        sessionid = users.try_login(request.args["username"], request.args["password"])
        if not(sessionid is None):
            print("Logged in!")
            return redirect("/session/"+sessionid)
    return app.send_static_file('login.html')

@app.route("/signup")
def signin():
    if len(request.args) == 3:
        sessionid = users.try_signup(
            request.args["name"],
            request.args["username"], 
            request.args["password"]
        )
        if not (sessionid is None):
            return redirect("/session/"+sessionid)
    return app.send_static_file('signin.html')

@app.route("/session/<sessionid>")
def user(sessionid):
    session=sessions.getsession(sessionid)
    if session is None:
        return "Invalid Session. Please login again"
    user=users.getuser(session[2])
    if user is None:
        return "Invalid User. Please signup"
    article_list = articles.recommend(user)
    sessions.add_event(sessionid, "LIST", user.un)
    return render_template(
        "user.html", 
        user=user,
        session=session,
        article_1=article_list[::2],
        article_2=article_list[1::2],
    )

@app.route("/deletesession/<sessionid>")
def delses(sessionid):
    sessions.add_event(sessionid, "STOPATTEMPT", sessionid)
    sess = sessions.getsession(sessionid)
    if sess is None:
        return "Invalid Session. Please login"
    user = users.getuser(sess[2])
    if user is None:
        return "Invalid User. Please login"
    user.update_preferences(sessionid)
    sessions.stop_session(sessionid)
    return redirect("/")

@app.route("/article/<sessionid>/<article_title>")
def show_article(sessionid, article_title):
    sess = sessions.getsession(sessionid)
    if sess is None:
        return "Invalid Session, login again"
    sessions.add_event(sessionid, "READ", article_title)
    return render_template("article.html", article=articles.get_article(article_title), session=sess)
