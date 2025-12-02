// Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica.

#include <stdio.h>

int main()
{
    int a;
    int b;
    float media_aritmetica;

    printf("Inserisci il valore di a: ");
    scanf("%d", &a);

    printf("Inserisci il valore di b: ");
    scanf("%d", &b);

    media_aritmetica = (a + b) / 2.0;

    printf("La media è : %f", media_aritmetica);

    return 0;
}