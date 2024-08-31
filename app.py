# requestを追加
from flask import Flask, request

app = Flask(__name__)


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """
        <form action="/login" method="post">
            Password:<input type="text"><br>
            <input type="submit">
        </form>
        """
    return "Logged in"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
