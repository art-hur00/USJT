import express from 'express';
import bodyParser from 'body-parser'

const server = express();
server.use( bodyParser.json() );       // suporte para JSON-encoded bodies
server.use(bodyParser.urlencoded({     // suporte para URL-encoded bodies
  extended: true
}));

server.get('/', (req, res) => {
 res.send('🙋‍♂️ Oi gente');
});

server.listen(3001, () => {
 console.log('Server escutando na porta 3001');
});