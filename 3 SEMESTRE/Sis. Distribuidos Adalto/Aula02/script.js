pessoa = {
nome: "Maria"  ,
idade : 25 ,
formacoes: ["Tecnico","Graduacao","Mestrado"]  ,
anoDeFormacao: [2006,2013,2017]  ,
    conjuge: {
        nome: "Joao",
        idade: 26,
    },
    temfilhos: true,
    filhos: [
        {
            nome: "Julia",
            idade: 16
        },
        {
            nome: "Pedro",
            idade: 3
        }

    ],
    getAno : function(){
        return 2025 - this.idade
    }    
}
function imprimir(){
   var divDados = document.getElementById("divDados");

    divDados.innerHTML = "Nome:" + pessoa.nome + "<br>Idade:" + pessoa.idade;
    divDados.innerHTML += "<br>Formacoes: "
    pessoa.formacoes.forEach( element => {
            divDados.innerHTML += curso + " - " 
    })
            divDados.innerHTML += "<br>Conjuge: " + pessoa.conjuge.nome + "Idade: " + pessoa.conjuge.idade;
            if(pessoa.temfilhos){
                divDados.innerHTML += "<br>Tem filhos?: Sim "
            
                pessoa.filhos.forEach( filho => {
                    divDados.innerHTML += "<br>Nome: " + filho.nome + "Idade: " + filho.idade;
                })
            }else{
                divDados.innerHTML += "<br>Tem filhos?: Nao "
            }    
            divDados.innerHTML += "<br>Ano de Nascimento: " + pessoa.getAno();
}   