#Crifra da Nlongônia
def first_min(lista):
    return lista.index(min(lista))

def distancias(c, lista02):
    return [abs(a-b) for a, b in zip([c for _ in range(len(lista02))], lista02)]
        
def proxima_vogal(letra, alphabeto, vogais):
    i_letra = alphabeto.index(letra)
    i_vogais = [alphabeto.index(d) for d in vogais]

    distancias_ = distancias(i_letra, i_vogais)
    return vogais[first_min(distancias_)]

def crifrar(palavra, alphabeto, vogais):
    cifra = []
    for letra in palavra:
        cifra.append(letra)
        if letra not in vogais and letra != ' ':
            cifra.append(proxima_vogal(letra, alphabeto, vogais))
            cont = 1
            while True:
                proxima_consoante = alphabeto[alphabeto.index(letra)+cont]
                if proxima_consoante not in vogais:
                    cifra.append(proxima_consoante)
                    break
                cont += 1
    return ''.join(cifra)

palavra = list(input('Palavra para cifrar: '))
alphabeto = list(input('Seu Alphabeto: '))
vogais = list(input('Vogais d seu alphabeto: '))

print(crifrar(palavra, alphabeto, vogais))