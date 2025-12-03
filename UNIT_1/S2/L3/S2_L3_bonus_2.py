# Analisi delle parole
# Scrivi un programma che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.

# Ignora la punteggiatura e considera le parole in modo case-insensitive.

# Suggerimenti:

# usa il metodo str.lower() perconvertire il testo in minuscolo
# usa il modulo re per rimuovere la punteggiatura
# usa un dizionario per tenere traccia delle occorrenze delle parole
# Esempio di input:

# testo = "Ciao, ciao! Come stai? Stai bene?"
# Esempio di output:

# {'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}
import re

text = input("Inserisci il testo: ").lower()

text = re.sub(r'[^\w\s]', '', text)

words = text.split()

occurrences = {}

for word in words:
    if word in occurrences:
        occurrences[word] +=1
    else:
        occurrences[word] = 1
    
print(occurrences)
