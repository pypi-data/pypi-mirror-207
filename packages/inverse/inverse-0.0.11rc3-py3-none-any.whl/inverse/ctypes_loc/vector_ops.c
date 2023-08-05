#include <stdio.h>
#include <stdlib.h>
#include "./inverse/ctypes_loc/vector_ops.h"


// gcc -fPIC -shared -o vector_ops.so vector_ops.c
// gcc -fPIC -shared -o vector_opsSHARED.so vector_ops.c
// gcc -fPIC -shared -o inverse/ctypes_loc/vector_ops.so  inverse/ctypes_loc/vector_ops.c
// gcc -Wall -o inverse/ctypes_loc/vector_opsMAC  inverse/ctypes_loc/vector_ops.c
// gcc -fPIC -shared -o inverse/ctypes_loc/vector_opsSHARED.so inverse/ctypes_loc/vector_ops.c
// gcc -I -fPIC -shared -o inverse/ctypes_loc/vector_opsSHARED.so inverse/ctypes_loc/vector_ops.c


float *multiplyVector(float *vec, int size, float num) {
    float *result = (float *) malloc(size * sizeof(float));
    //  float currentResult;
    for (int i = 0; i < size; i++) {
        result[i] = vec[i] * num;
        // currentResult = vec[i];
        // printf("item number %d...%d \n", i, currentResult);
    }
    // printf("test1");
    return result;
}

double *multiplyVector_double(double *vec, int size, double num) {
    double *result = (double *) malloc(size * sizeof(double));
    //  float currentResult;
    for (int i = 0; i < size; i++) {
        result[i] = vec[i] * num;
        // currentResult = vec[i];
        // printf("item number %d...%d \n", i, currentResult);
    }
    // printf("test1");
    return result;
}


double *operate_inside_double_opt(int i , double *row_J, double *row_i, int size) {


    double *result = (double *) malloc(size * sizeof(double));
    double factor;



    if (row_i[i] == 0) {
        factor = 0;
    } else {
        factor = row_J[i] / row_i[i];
    }

    double * v2 = multiplyVector_double(row_i, size, factor);


    for (int i = 0; i < size; i++) {

        result[i] = row_J[i] - v2[i];
    }
    return result;
}

double *operate_inside_double(double number_j, double number_i, double *row_J, double *row_i, int size) {


    double *result = (double *) malloc(size * sizeof(double));
    double factor;



    if (number_i == 0) {
        factor = 0;
    } else {
        factor = number_j / number_i;
    }

    double * v2 = multiplyVector_double(row_i, size, factor);


    for (int i = 0; i < size; i++) {

        result[i] = row_J[i] - v2[i];
    }
    return result;
}

void free_memory_float(float *ptr) {

    free(ptr);
}


void free_memory_double(double *ptr) {

    free(ptr);
}

#include <stdio.h>

int main(void) {
//    double liste1[] = {10, 20};
//    double liste2[] = {10, 20};


//    double * result = operate_inside_double(10, 20, liste1, liste2, 2);
//    printf("%f %f ", result[0], result[1]) ;
    return 0;
}