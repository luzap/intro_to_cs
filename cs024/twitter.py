import pymysql
import flask
from flask import Flask

app = Flask(__name__)

connection = pymysql.connect(host="10.224.45.113", user="cs101",
                             db="twitter")

cursor = connection.cursor(pymysql.cursors.DictCursor)


@app.route("/", defaults={"user": None, "number": None}, methods=["GET", "POST"])
@app.route("/<user>:<number>", methods=["GET", "POST"])
def main(user, number):
    if flask.request.method == "GET":
        command = "SELECT * FROM tweet"
        if user is not None:
            command += ' WHERE user="{}"'.format(user)

        if number is not None:
            command += " LIMIT {}".format(number)

        cursor.execute(command)
        tweets = cursor.fetchall()

        cursor.execute("SELECT user FROM tweet")
        users = cursor.fetchall()

        return flask.render_template("main.html", tweets=tweets, users=users)
    if flask.request.method == "POST":
        if "new" in flask.request.form.keys():
            data = flask.request.form
            cursor.execute("insert into tweet (user, message) values ('{}', '{}')".format(
                data['user'], data['tweet']))
            return flask.redirect("/")
        elif "params" in flask.request.form.keys():
            data = flask.request.form
            user = data['user'] if data["user"] != "all" else None
            number = data['number'] if data['number'] != "" else 100000
            return flask.redirect("/{user}:{number}".format(user=user, number=number))


@app.route("/like/<int:id>")
def increment_likes(id):
    cursor.execute(
        "update tweet SET likes = likes + 1 where id = {}".format(id))
    return flask.redirect("/")

if __name__ == '__main__':
    app.run()
