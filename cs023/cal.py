import datetime
from calendar import monthrange
import flask
import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    date = datetime.datetime.now()
    _, last_day = monthrange(date.year, date.month)
    cal = [0] * 35
    pos = 0
    for day in range(1, last_day + 1):
        if pos == 0:
            pos = datetime.datetime(date.year, date.month, day).weekday()
        cal[pos] = day
        pos += 1

    for day in range(1, len(cal) + 1):
        if cal[-day] == 0:
            del cal[-day]
        else:
            break

    nd_cal = [cal[i: i + 7] for i in range(0, len(cal), 7)]
    html_cal = """<table>\n"""
    header_string = "<th>{}</th>\n"
    entry_string = "<td {}>{}</td>\n"

    html_cal += "<tr>\n"
    for day in days:
        html_cal += header_string.format(day)
    html_cal += "</tr>\n"

    for row in nd_cal:
        html_cal += "<tr>\n"
        for col in row:
            html_cal += entry_string.format(
                'style="background-color: yellow"' if int(
                    col) == date.day else "",
                col if col != 0 else " ")
        html_cal += "</tr>\n"
    html_cal += "</table>"
    return html_cal


if __name__ == '__main__':
    app.run()
