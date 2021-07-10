from flask import Flask,render_template
from flask.templating import render_template
app= Flask(__name__)


@app.route('/')
def home():

    samurai='Samurai'
    feiticeiro='Feiticeiro'
    slime='Slime'

    jorginho='Jorginho'
    thoia='Thoia'
    sophia='Shopia'

    img_samurai = '../static/gif/samurai-unscreen.gif'
    img_feiticeiro = '../static/gif/mago-unscreen.gif'
    img_slime = '../static/gif/slime.gif'

    img_jorginho = '../static/gif/espada1-unscreen.gif'
    img_thoia = '../static/gif/magia-unscreen.gif'
    img_sophia = '../static/gif/arco-unscreen.gif'


    return render_template(
        'index.html',
         samurai= samurai,
        feiticeiro=feiticeiro,
        slime=slime,

        jorginho=jorginho,
        thoia=thoia,
        sophia=sophia,

        img_samurai=img_samurai,
        img_feiticeiro=img_feiticeiro,
        img_slime=img_slime,

        img_jorginho=img_jorginho,
        img_thoia=img_thoia,
        img_sophia=img_sophia,

    )





if __name__ == "__main__":
    app.run(debug=True)
