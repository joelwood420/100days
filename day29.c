// Take input of a positive int n and return the sum of all number 0 - n 
#include <stdio.h>

int main(void){
    int n, sum = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for (int i = 0; i <= n; i++) {
        sum += i;
    }

    printf("%d\n", sum);
    return 0;
}