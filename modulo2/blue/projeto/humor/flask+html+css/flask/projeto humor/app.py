from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    nome_do_personagem = 'Zelda'
    idade='17'
    humor = True
    imagem1 = 'https://th.bing.com/th/id/R00130a0d1483091f6f4915eb0b3187f8?rik=pD%2fa772aoxOuNw&riu=http%3a%2f%2f31.media.tumblr.com%2f74c37a1745efbc6245a2bead85507174%2ftumblr_mvbjabiJjc1r84nrbo2_400.gif&ehk=jqcfjoMaek260AipO8mwemLaL2%2b8f%2f9veAN4aBzqcWI%3d&risl=&pid=ImgRaw'
    imagem2 = 'https://th.bing.com/th/id/Rd834a993f556dd6cfafd7cd51fe668a7?rik=vaprkNV%2byUnVLg&riu=http%3a%2f%2fmedia.tumblr.com%2ftumblr_lxi7p21TCq1qbbwtc.gif&ehk=9EsyuQMvHJgraoToi%2bgTrfs5DWI9TVvgwTqN15FgMcE%3d&risl=&pid=ImgRaw'
    return render_template(
        'index01.html',
        nome_do_personagem=nome_do_personagem,
        humor=humor,
        imagem1=imagem1,
        imagem2=imagem2,
        idade=idade
    )


@app.route('/humor',methods=['GET','POST'])
def humor():
    nome_do_personagem = 'Zelda'
    idade = '17'
    humor = False
    imagem1 = 'https://th.bing.com/th/id/R00130a0d1483091f6f4915eb0b3187f8?rik=pD%2fa772aoxOuNw&riu=http%3a%2f%2f31.media.tumblr.com%2f74c37a1745efbc6245a2bead85507174%2ftumblr_mvbjabiJjc1r84nrbo2_400.gif&ehk=jqcfjoMaek260AipO8mwemLaL2%2b8f%2f9veAN4aBzqcWI%3d&risl=&pid=ImgRaw'
    imagem2 = 'https://th.bing.com/th/id/Rd834a993f556dd6cfafd7cd51fe668a7?rik=vaprkNV%2byUnVLg&riu=http%3a%2f%2fmedia.tumblr.com%2ftumblr_lxi7p21TCq1qbbwtc.gif&ehk=9EsyuQMvHJgraoToi%2bgTrfs5DWI9TVvgwTqN15FgMcE%3d&risl=&pid=ImgRaw'
    return render_template(
        'index01.html',
        nome_do_personagem=nome_do_personagem,
        humor=humor,
        imagem1=imagem1,
        imagem2=imagem2,
        idade=idade
    )






if __name__ == "__main__":
    app.run(debug=True)
