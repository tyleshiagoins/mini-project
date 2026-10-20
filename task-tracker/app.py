from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Task Tracker</h1><p>Keep track of your daily tasks.</p>"

if __name__ == "__main__":
    app.run()
