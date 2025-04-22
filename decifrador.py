cifra = list(input())
vogais = list('aeiou')

i = 0
while i < len(cifra):
    print(cifra[i], end='')
    if cifra[i] not in vogais:
        i+=2
    i+=1

