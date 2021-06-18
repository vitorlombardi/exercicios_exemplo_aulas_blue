from flask import Flask,render_template,request


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def home():
    nome = None
    sobrenome = None
    escolha = None
    escolha_imagem = None

    if request.method =='POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        escolha = request.form['escolha']

        if escolha == 'elfo':
            escolha_imagem = 'https://i.pinimg.com/originals/52/b8/c3/52b8c320e93e722020f51d6e4920d6bc.gif'
        elif escolha == 'orc':
            escolha_imagem = 'https://thumbs.gfycat.com/ExemplarySeriousBeardedcollie-max-1mb.gif'
        elif escolha == 'hobbit':
            escolha_imagem = 'https://media.tenor.com/images/a758b5c5a136dde219fc5926b42c7b1b/tenor.gif'

    return render_template(
        'index0001.html',
        nome=nome,
        sobrenome=sobrenome,
        escolha=escolha,
        escolha_imagem=escolha_imagem
    )


if __name__=='__main__':
    app.run(debug=True)
