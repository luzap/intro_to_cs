import pymysql
from flask import Flask

app = Flask(__name__)

connection = pymysql.connect(host="10.224.45.113", user="cs101",
                             db='movies')

cursor = connection.cursor()


def make_table(cols, cursor):
    entry_string = "<td>{}</td>"
    html_table = "<table>"
    for item in cols:
        html_table += "<th>{}</th>".format(item)

    for row in cursor:
        html_table += "<tr>"
        for item in row:
            html_table += entry_string.format(item)
        html_table += "</tr>"
    html_table += "</table>"

    return html_table


@app.route("/actors")
def movies():
    cursor.execute("select * from actor")
    html_table = make_table(["ID", "Name"], cursor)

    return html_table


@app.route("/casting")
def casting():
    cursor.execute("select * from movie order by id")
    html_table = make_table(['Movie ID', "Title", "Yr", "Score", "Votes", "Director"], cursor)
    return html_table


@app.route("/listing")
def listing():
    cursor.execute("select actor.name, movie.title, movie.yr from actor join casting on actor.id=casting.actorid join movie on casting.movieid=movie.id where actor.id=188")
    html_table = make_table(['Actor',  'Movie', 'Year'], cursor)
    return html_table

if __name__ == '__main__':
    app.run(debug=True)
