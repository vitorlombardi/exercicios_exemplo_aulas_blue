const elemento_por_ID= document.getElementById('elemento_1');
elemento_por_ID.innerHTML = 'eu represento o elemento com ID "elemento_1"';

const elementos_por_Classe= document.getElementsByClassName('classe_exemplo');
for (const elemento of elementos_por_Classe){
    elemento.innerHTML = 'eu sou um elemento com a classe "elementos_exemplo'
}