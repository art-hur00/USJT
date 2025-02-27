let resp1 = prompt("Quer brincar de pauzinho? ;)");
let Player1 = prompt("Qual o seu nome?")
let qntdePalitosPlayer1 = 3
let qntdeJogada = 0
let qntdeChutePlayer1 = 0


//let Player2 = alert("Ola, me chamo Goku e hoje se ta na minha mão")
let qntdePalitosGoku = 3
let qntdeJogadaGoku = 0
let qntdeEscolhidosGoku = 0

function calculaPalpiteGoku(){
    let qtdeSorteado = parseInt(Math.random() * 10 % (1+qntdePalitosPlayer1));
    let palpite = qntdeEscolhidosGoku + qtdeSorteado
    return palpite
}

let test = calculaPalpiteGoku()
console.log(calculaPalpiteGoku())

while(qntdePalitosGoku != 0 && qntdePalitosPlayer1 != 0){
    qntdeJogada = prompt("Quantos palitos voce deseja separar?")
    qntdeJogada= parseInt;

    qntdeEscolhidosGoku = parseInt(Math.random() * 10 % +qntdePalitosGoku )+1;

    qntdeChutePlayer1 = prompt("Qual o seu palpite?")
    qntdeJogadaGoku =  calculaPalpiteGoku()

    let soma = palpite + qntdeJogada
    if(qntdeJogada == soma){
        alert("parabens" + Player1)
        qntdePalitosPlayer1--
    }else{
        if(palpite == soma){
            alert("Goku venceu")
             qntdePalitosGoku--

        }else{
            alert("Ninguém Acertou!!!!!")
        }

    }
    let text= Player1+ " com " + qntdePalitosPlayer1+" palitos\n" + "Achou que era" + qntdeChutePlayer1
     text= text +"Goku" + " com " + qntdePalitosGoku+" palitos\n" + "Achou que era" + qntdeEscolhidosGoku

    alert(text)
}

    
