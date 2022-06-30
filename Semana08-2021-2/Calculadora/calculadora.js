var valor;

function botao (num) {
    valor = document.calc.visor.value += num;
}

function reseta() {
    document.calc.visor.value = '';
}

function calcula() {
    document.calc.visor.value = eval(valor).toLocaleString('pt-br')
}