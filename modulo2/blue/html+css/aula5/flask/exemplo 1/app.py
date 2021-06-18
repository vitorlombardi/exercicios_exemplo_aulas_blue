from flask import Flask,render_template,request
#from flask.wrappers import Request
app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
    if request.method== 'POST':
        usuario_nome = request.form['usuario_nome']
        usuario_sobrenome = request.form['usuario_sobrenome']
        apenas_uma_opcao = request.form['apenas_uma_opcao']
        varias_opcoes = request.form['varias_opcoes']
        print(f'nome do usuario: {usuario_nome}')
        print(f'sobrenome do usuario: {usuario_sobrenome}')
        print(f'apenas uma opção: {apenas_uma_opcao}')
        print(f'varias opções: {varias_opcoes}')

    return render_template('index001.html')





if __name__ == "__main__":
    app.run(debug=True)
