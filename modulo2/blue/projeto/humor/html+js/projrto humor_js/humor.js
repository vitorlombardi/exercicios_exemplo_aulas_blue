const personagem = {

    nome: 'Zelda',
    idade: '17',

    humor: true,

    imagem_1: 'https://th.bing.com/th/id/R00130a0d1483091f6f4915eb0b3187f8?rik=pD%2fa772aoxOuNw&riu=http%3a%2f%2f31.media.tumblr.com%2f74c37a1745efbc6245a2bead85507174%2ftumblr_mvbjabiJjc1r84nrbo2_400.gif&ehk=jqcfjoMaek260AipO8mwemLaL2%2b8f%2f9veAN4aBzqcWI%3d&risl=&pid=ImgRaw',
    imagem_2: 'https://th.bing.com/th/id/Rd834a993f556dd6cfafd7cd51fe668a7?rik=vaprkNV%2byUnVLg&riu=http%3a%2f%2fmedia.tumblr.com%2ftumblr_lxi7p21TCq1qbbwtc.gif&ehk=9EsyuQMvHJgraoToi%2bgTrfs5DWI9TVvgwTqN15FgMcE%3d&risl=&pid=ImgRaw'

}

const personagem_nome = document.getElementById('nome');
const personagem_idade = document.getElementById('idade');

personagem_nome.innerHTML = personagem.nome;
personagem_idade.innerHTML = personagem.idade;


function atualizar_humor() {

    const personagem_imagem = document.getElementById('imagem');
    const personagem_humor = document.getElementById('humor');

    if (personagem.humor) {
        
        personagem_imagem.src = personagem.imagem_1;
        personagem_humor.innerText = personagem.nome + ' esta serio !';

    } else {

        personagem_imagem.src = personagem.imagem_2;
        personagem_humor.innerText = personagem.nome + ' esta puto !';

    }

}

atualizar_humor();

const botao_outro_versao = document.getElementById('outro_versao');
botao_outro_versao.addEventListener ('click', function () {
    personagem.humor = !personagem.humor;
    atualizar_humor();

});