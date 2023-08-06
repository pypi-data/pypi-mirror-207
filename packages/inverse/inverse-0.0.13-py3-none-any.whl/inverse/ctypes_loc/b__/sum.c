#include <stdio.h>

#include <stdlib.h>
// gcc -fPIC -shared -o sum.so sum.c


int sumArray(int * arr , int size ){
    int sum = 0 ;
    for (int i = 0 ; i<size ; i++ ){
    sum +=arr[ i ] ;
    }
    return sum ;
}


int* incArray(int * arr , int size ){
    int sum = 0 ;
    for (int i = 0 ; i<size ; i++ ){
     arr[ i ]++  ;
    }
    return arr  ;
}

void free_memory_int(int *arr ){
    printf("freeing the memory") ;
    free(arr) ;
}

