const card_pokemons = document.querySelectorAll('.card_pokemon');
const pokemon_selecionado = document.querySelector('#pokemon_selecionado');

//logica para selecionar o pokemon quando o usuario clicar em card(imagem)

for (const card_pokemon of card_pokemons) {

    card_pokemon.addEventListener("click", function () {

        const nome_pokemon = this.getAttribute("data-nome");

        if (!this.classList.contains('selecionado')) {
            this.classList.add('selecionado');

            pokemon_selecionado.innerHTML = `o último pokemon selecionado foi o <b>${nome_pokemon}</b>!`;

        } else {

            this.classList.remove('selecionado');

            const pokemon_selecionados = document.querySelectorAll('.selecionado');

            if (pokemon_selecionados.length >= 1) {

                pokemon_selecionado.innerHTML = `você desmarcou o pokemon <b>${nome_pokemon}</b>. Restantes :<b>${pokemon_selecionados.length}</b>`;

            } else {
                pokemon_selecionado.innerHTML = 'selecione um pokemon';
            }
        }
    });
}