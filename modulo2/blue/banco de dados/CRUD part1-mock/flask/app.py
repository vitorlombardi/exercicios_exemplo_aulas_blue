from flask import Flask,render_template
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# Read (select) - trabalhar com os dados mockados

registros= [

    {
        'id': 1,
        'nome': 'Os Vingadores',
        'imagem_url': 'http://guiadecompras.casasbahia.com.br/imagens/2012/09/os-vingadores-filme-1.jpg'
    },

    {
        'id': 2,
        'nome': 'Harry Potter e a Pedra Filosofal',
        'imagem_url': 'https://br.web.img3.acsta.net/medias/nmedia/18/95/59/60/20417256.jpg'
    },

    {
        'id': 3,
        'nome': 'Guardiões da Galáxia 2',
        'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/thumb/0/07/Guardians_of_the_galaxy_vol_two_poster.jpg/250px-Guardians_of_the_galaxy_vol_two_poster.jpg'
    },

    {
        'id': 4,
        'nome': 'Gente Grande 2',
        'imagem_url': 'https://br.web.img3.acsta.net/pictures/210/049/21004903_20130510170049514.jpg'
    },

    {
        'id': 5,
        'nome': 'As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa',
        'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/thumb/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg/250px-The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg'
    }
] 

@app.route('/read')
def read_all():
    return render_template('read_all.html',registros=registros)


@app.route('/read/<id_registro>')
def read_single(id_registro):
    return 'Em construção : Visualizar registro de Id'+ id_registro

if __name__ == '__main__':
    app.run(debug=True)
