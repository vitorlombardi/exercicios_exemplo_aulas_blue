from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


user = 'ywmswqox'
password = 'i5oXVwybHjfgsk03Docu8Ul6krB0pZSX'
host = 'tuffi.db.elephantsql.com'
database = 'ywmswqox'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def read_single(registro_id):
        # select * from anuncios where id=1
        return anuncios.query.get(registro_id)

class anuncios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_vendedor = db.Column(db.String(255), nullable=False)
    nome_produto = db.Column(db.String(255), nullable=False)
    valor_produto = db.Column(db.Integer, nullable=False)
    descricao_produto = db.Column(db.String, nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome_vendedor, nome_produto, valor_produto, descricao_produto, imagem_url):
        self.nome_vendedor = nome_vendedor
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.descricao_produto = descricao_produto
        self.imagem_url = imagem_url

    @staticmethod
    def read_all():
        # select * from anuncios order by id desc
        return anuncios.query.order_by(anuncios.id.asc()).all()

    @staticmethod
    def read_single(registro_id):
        # select * from anuncios where id=1
        return anuncios.query.get(registro_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, new_data):
        self.nome_vendedor = new_data.nome_vendedor
        self.nome_produto = new_data.nome_produto
        self.valor_produto = new_data.valor_produto
        self.descricao_produto = new_data.descricao_produto
        self.imagem_url = new_data.imagem_url
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/read')
def read_all():
    registros = anuncios.read_all()
    return render_template('read_all.html', registros=registros)


@app.route('/read/<registro_id>')  # Posso colocar qualquer nome entre <>
def read_single(registro_id):
    registro = anuncios.read_single(registro_id)
    print(registro)

    return render_template('read_single.html', registro=registro)

@app.route('/create', methods=('GET', 'POST'))
def create():
    id_atribuido = None
    if request.method == 'POST':
        form = request.form
        registro = anuncios(form['nome_vendedor'], form['nome_produto'], form['valor_produto'], form['descricao_produto'], form['imagem_url'])
        registro.save()
        id_atribuido = registro.id

    return render_template('create.html', id_atribuido=id_atribuido)

@app.route('/update/<registro_id>', methods=('GET', 'POST'))
def update(registro_id):
    sucesso = None
    registro = anuncios.read_single(registro_id)

    if request.method == 'POST':
        form = request.form
        new_data = anuncios(form['nome_vendedor'], form['nome_produto'],form['valor_produto'], form['descricao_produto'], form['imagem_url'])
        registro.update(new_data)
        sucesso = True
    return render_template('update.html', registro=registro, sucesso=sucesso)

@app.route('/dados/<registro_id>', methods=('GET', 'POST'))
def dados(registro_id):
    usuario = Usuario.read_single(registro_id)
    comprado_s = None
    id = None
    nome= None
    email = None
    endereco = None
    registro = anuncios.read_single(registro_id)
    novo = None
    
    if request.method == 'POST':
        form = request.form
        novo = Usuario(form['nome'],form['email'], form['endereco'])
        novo.save()
        comprado_s = True
        nome = novo.nome
        email= novo.email
        endereco = novo.endereco
        id = novo.id
     
    return render_template('dados.html', usuario = usuario, registro=registro, id = id, comprado_s = comprado_s, nome = nome, email = email, endereco = endereco)


@app.route('/dados/<registro_id>/confirmar')
def confirmar(registro_id):
    comprado = None
    registro = anuncios.read_single(registro_id)

    if registro:
        registro.delete()
        comprado = True
        
            
    return render_template('dados.html', registro_id=registro_id, registro=registro, comprado=comprado)





if __name__ == "__main__":
    app.run(debug=True)
