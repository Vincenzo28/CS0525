# Calcolo della media mobile
# Scrivi una funzione che calcoli la media mobile di una lista di numeri.

# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

# Suggerimenti:

# usa slicing per ottenere gli ultimi n elementi
# usa la funzione sum() per calcolare la somma degli elementi e poi dividi per n.
# Esempio di input:

# numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# n = 3
# Esempio di output:

# [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [1,2,3,4,5,6,7,8,9,10]

n = int(input("Inserisci n: "))

result = []

for i in range(len(numbers)):

    if i < n - 1:
        # prendo gli elementi da 0 fino all'indice i
        elements = numbers[0:i+1]
        media = sum(elements) / len(elements)
    else:
        # prendo gli ultimi n elementi
        elements = numbers[i-n+1:i+1]
        media = sum(elements) / n

    result.append(media)

print(result)


