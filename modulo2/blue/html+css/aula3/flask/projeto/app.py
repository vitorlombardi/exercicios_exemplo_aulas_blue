from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    nome = 'Zelda'
    hp = ' 5000'

    exibir_imagen=True
    imagem = 'https://th.bing.com/th/id/R1913d04ea6a314311dc8ff7b85f6033b?rik=0V8u%2bAtGuaAmjw&riu=http%3a%2f%2f4.bp.blogspot.com%2f-gPtaxNh6BZE%2fU4c7pd0IfyI%2fAAAAAAAAIEM%2fGRjVRXh-Sfg%2fs1600%2fLink%2b5.gif&ehk=o1vVmqThRcvHH%2fPQu14yRh%2brOF%2fTy%2bCQ%2fnwgzopS%2b94%3d&risl=&pid=ImgRaw'

    return render_template(
        "index.html",
        nome=nome,
        hp=hp,
        exibir_imagen=exibir_imagen,
        imagem=imagem
        )





@app.route("/cleiton")
def cleiton():
    nome1 = 'Bom de guerra'
    hp1 = ' 10.000'

    exibir_imagen1=True
    imagem_cleiton = "https://4.bp.blogspot.com/-RSXxjFxQhls/WvG7MVrYQBI/AAAAAAAAChs/SILYwWJzwlE39dv_i1KI8qEm0g6mNdNsQCLcBGAs/s1600/Kratos%2Bgif%2B2.gif"

    return render_template(
        "index1.html",
        nome1=nome1,
        hp1=hp1,
        exibir_imagen1=exibir_imagen1,
        imagem_cleiton=imagem_cleiton
        )


if __name__ == "__main__":
    app.run(debug=True)
