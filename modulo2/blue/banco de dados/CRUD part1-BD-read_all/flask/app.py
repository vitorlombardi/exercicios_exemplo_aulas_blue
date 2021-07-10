from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

#danco de dados(tatabese)

user = 'ntnicjap'
password = 'tjZLNbwdCpuew3-kJwK5C8NQL0KIaeQF'
host = 'tuffi.db.elephantsql.com'
database = 'ntnicjap'

app.config['SQLALCHEMY_DATABASE_URI']= f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='123456'

db=SQLAlchemy(app)

#filmes db

class Filmes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(255),nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self,nome,imagem_url):
        self.nome = nome
        self.imagem_url=imagem_url



    @staticmethod
    def read_all():
        #select * from filmes order by id desc
        return Filmes.query.order_by(Filmes.id.desc()).all()


#rotas

@app.route('/')
def home():
    return render_template('index.html')

#read

@app.route('/read')
def read_all():
    registros=Filmes.read_all()
    return render_template('read_all.html',registros=registros)


@app.route('/read/<id_registro>')
def read_single(id_registro):
    return 'Em construção : Visualizar registro de Id'+ id_registro

if __name__ == '__main__':
    app.run(debug=True)
