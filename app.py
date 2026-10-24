from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
ITEMS = []


@app.route("/")
def index():
    return render_template("index.html", title="Create A Guessing Number From", items=ITEMS)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        ITEMS.append(text)
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
