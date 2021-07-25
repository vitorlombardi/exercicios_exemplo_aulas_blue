const calculadora = require('./calculadora'); //ECMA 5

console.log(calculadora.soma(6,6));
console.log(calculadora.sub(6,6));
console.log(calculadora.mult(6,6));
console.log(calculadora.div(6,6));

console.log(calculadora.nome);

calculadora.nome = 'calculadora versão batata-doce 2.0';

console.log(calculadora.nome);
