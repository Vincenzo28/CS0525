# Esercizio di Programmazione in Python: Genera un Nome per la Tua Band Obiettivo 
# Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente: 
# la città di origine e il nome del proprio animale domestico.

# Richiesta di Input: Il programma deve chiedere all'utente di inserire: 
# ○ Il nome della città di origine. 
# ○ Il nome del proprio animale domestico. 
# Generazione del Nome della Band: Una volta ricevuti gli input, 
# il programma deve combinare il nome della città e il nome dell'animale in un'unica stringa che rappresenta il nome della band. 
# Output: Il programma deve stampare a video il nome generato per la band.

city = input("Inserisci la tua città d'origine: ")
pet = input("Inserisci il nome del tuo animale domestico: ")

print(f"Il nome della tua band è: {city} {pet}")