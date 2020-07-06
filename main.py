from flask import Flask, render_template
from FirebaseLogic import firebase_crud

app = Flask(__name__)

firebase_crud.update_firebase()
data = firebase_crud.retrieve_data()


@app.route("/")
def home():
    """Render homepage with updated firebase values"""
    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
