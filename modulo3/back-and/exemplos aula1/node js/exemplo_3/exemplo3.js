const http = require('http');

http.createServer(function(rec,res){

    res.end('<h1><b>Bem vindo ao meu site</b></h1> <a href>https://bluetechno.com.br/</a>');

}).listen(3000);

console.log('servidor ta on');
