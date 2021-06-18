from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "hello, jorginho !"

@app.route("/rota2")
def rota2():
    return "<h1> pagina da segunda rota</h1>"

@app.route("/blue")
def blue():
    return '<h3>jorginho e blumer</h3> '

if __name__ == "__main__":
    app.run(debug=True)
