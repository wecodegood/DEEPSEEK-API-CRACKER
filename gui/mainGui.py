from flask import Flask

app = Flask()


@app.route("/")
def GoToRoot():
    return "test"


if __name__ == "__main__":
    app.run()