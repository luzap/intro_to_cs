import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    date = datetime.datetime.now()
    return "Current date: {}/{}/{} {}:{}:{}".format(date.year, date.month, date.day, date.hour, date.minute, date.second)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
