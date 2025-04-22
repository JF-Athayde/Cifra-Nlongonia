function firstMin(lista) {
    let min = Math.min(...lista);
    return lista.indexOf(min);
}

function distancias(c, lista02) {
    return lista02.map(b => Math.abs(c - b));
}

function proximaVogal(letra, alfabeto, vogais) {
    let iLetra = alfabeto.indexOf(letra);
    let iVogais = vogais.map(v => alfabeto.indexOf(v));
    let dists = distancias(iLetra, iVogais);
    return vogais[firstMin(dists)];
}

function crifrar(palavra, alfabeto, vogais) {
    let cifra = [];
    for (let letra of palavra) {
        cifra.push(letra);
        if (!vogais.includes(letra) && letra !== ' ') {
            cifra.push(proximaVogal(letra, alfabeto, vogais));
            let cont = 1;
            while (true) {
                let proxIndex = (alfabeto.indexOf(letra) + cont) % alfabeto.length;
                let proximaConsoante = alfabeto[proxIndex];
                if (!vogais.includes(proximaConsoante)) {
                    cifra.push(proximaConsoante);
                    break;
                }
                cont++;
            }
        }
    }
    return cifra.join('');
}

document.getElementById("cifraForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const palavra = document.getElementById("palavra").value.trim().toLowerCase();
    const alfabeto = document.getElementById("alfabeto").value.trim().toLowerCase().split('');
    const vogais = document.getElementById("vogais").value.trim().toLowerCase().split('');

    const resultado = crifrar(palavra, alfabeto, vogais);
    document.getElementById("resultado").innerHTML = `<strong>Resultado:</strong> ${resultado}`;
});
