from flask import Flask, render_template, request
from main import run_criador_artigo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    artigo = None
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        artigo = run_criador_artigo(pergunta)
    return render_template("home.html", artigo=artigo)

if __name__ == "__main__":
    app.run(debug=True)
