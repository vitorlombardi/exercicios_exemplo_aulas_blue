from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    pokemons = [
        {
            'numero': '001',
            'nome': 'Bulbasaur'
        },
        {
            'numero': '002',
            'nome': 'Ivysaur'
        },
        {
            'numero': '003',
            'nome': 'Venusaur'
        },
        {
            'numero': '004',
            'nome': 'Charmander'
        },
        {
            'numero': '005',
            'nome': 'Charmeleon'
        },
        {
            'numero': '006',
            'nome': 'Charizard'
        },
        {
            'numero': '007',
            'nome': 'Squirtle'
        },
        {
            'numero': '008',
            'nome': 'Wartotle'
        },
        {
            'numero': '009',
            'nome': 'Blastoise'
        }
    ]
    caminho_base_imagem = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'

    return render_template(
        'index_010.html',
        pokemons = pokemons,
        caminho_base_imagem=caminho_base_imagem
    )
        
if __name__=='__main__':
    app.run(debug=True)
