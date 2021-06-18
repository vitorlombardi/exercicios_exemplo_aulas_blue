from flask import Flask, render_template
from flask.templating import render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    nome_do_jogador='jorginho'
    premio=False
    return render_template(
        'index.html',
        nome_do_jogador=nome_do_jogador,
        premio=premio
        )  




if __name__ == "__main__":
    app.run(debug=True)