const vida_personagem = {
    'samurai' : 17,
    'feiticeiro' : 22,
    'Slime' : 10,
};

const dano_golpe = {
    'Jorginho': 10,
    'thoia' : 16,
    'sophia': 7,
};

let personagem_selecionado
let golpe_selecionado

function iniciar() {

    const elementos = document.getElementsByClassName('selecionar');

    for (const elemento of elementos){
        elemento.addEventListener('click', marcar_elemento);
    }

    document.getElementById('calcular').addEventListener('click', calcular_dano);
    
}

function marcar_elemento (evento){

    const elemento_selecionado = evento.target.parentElement;

    if (!elemento_selecionado.classList.contains('selecionar')) {
        return;
    }

    const id_selecionado = elemento_selecionado.getAttribute('id');

    if (elemento_selecionado.classList.contains('personagem_img')) {

        personagem_selecionado = id_selecionado;
        limpa_elemento('personagem_img');
    }else{
        golpe_selecionado = id_selecionado;
        limpa_elemento('golpes_img');
    }

    elemento_selecionado.classList.add('clicado')

}

function calcular_dano(){

    if (!personagem_selecionado || !golpe_selecionado){

        alert('selecione um inimigo e um personagem para calcular o dano');
        return;
    }

    const dado = rolar_dado();
    const dano_personagem_golpe = dano_golpe[golpe_selecionado];
    const dano_total = dado+dano_personagem_golpe;
    const vida_personagem_monstro = vida_personagem[personagem_selecionado]


    let resultado = 'dano: '+ dano_total + '! o ';

    if (dano_total >= vida_personagem_monstro){

        resultado += personagem_selecionado + ' foi morto' ;
    }else{
        resultado +=  personagem_selecionado + ' não morreu... quem sabe no proximo ataque!'
    }

    document.getElementById('dano').innerHTML = resultado;

}

function limpa_elemento(tipo){
    const elementos = document.getElementsByClassName('selecionar');

    for (const elemento of elementos){
        if (elemento.classList.contains(tipo)){
            elemento.classList.remove('clicado');
        }
    }
}

function rolar_dado(){
    const min = Math.ceil(1);
    const max = Math.floor(10);

    return Math.floor(Math.random() * (max - min + 1)) + min;
}