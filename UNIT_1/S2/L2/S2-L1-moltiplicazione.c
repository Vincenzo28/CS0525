// Si scriva un programma che esegua l'operazione di moltiplicazione tra due numeri inseriti dall'utente.

#include <stdio.h>

int main()
{
    int a;
    int b;
    int moltiplicazione;

    printf("Inserisci il valore di a: ");
    scanf("%d", &a);

    printf("Inserisci il valore di b: ");
    scanf("%d", &b);

    moltiplicazione = a * b;

    printf("Il risultato della moltiplicazione è : %d", moltiplicazione);

    return 0;
}