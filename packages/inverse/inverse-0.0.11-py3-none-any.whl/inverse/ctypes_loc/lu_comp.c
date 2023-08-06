#include <stdio.h>

#include <stdlib.h>

void LU_decomposition(double **A, int n) {

    int i, j, k;

    double **L = (double **)malloc(n * sizeof(double *));

    double **U = (double **)malloc(n * sizeof(double *));

    for (i = 0; i < n; i++) {

        L[i] = (double *)calloc(n, sizeof(double));

        U[i] = (double *)calloc(n, sizeof(double));

    }

    for (i = 0; i < n; i++) {

        for (j = i; j < n; j++) {

            double sum = 0.0;

            for (k = 0; k < i; k++) {

                sum += L[i][k] * U[k][j];

            }

            U[i][j] = A[i][j] - sum;

        }

        for (j = i; j < n; j++) {

            if (i == j) {

                L[i][i] = 1.0;

            } else {

                double sum = 0.0;

                for (k = 0; k < i; k++) {

                    sum += L[j][k] * U[k][i];

                }

                L[j][i] = (A[j][i] - sum) / U[i][i];

            }

        }

    }

    printf("L:\n");

    for (i = 0; i < n; i++) {

        for (j = 0; j < n; j++) {

            printf("%f ", L[i][j]);

        }

        printf("\n");

    }

    printf("U:\n");

    for (i = 0; i < n; i++) {

        for (j = 0; j < n; j++) {

            printf("%f ", U[i][j]);

        }

        printf("\n");

    }

}

int main() {

    double **A;

    int n = 3;

    int i, j;

    A = (double **)malloc(n * sizeof(double *));

    for (i = 0; i < n; i++) {

        A[i] = (double *)malloc(n * sizeof(double));

    }

    A[0][0] = 4.0; A[0][1] = 3.0; A[0][2] = 1.0;

    A[1][0] = 2.0; A[1][1] = 1.0; A[1][2] = 3.0;

    A[2][0] = 1.0; A[2][1] = 2.0; A[2][2] = 4.0;

    LU_decomposition(A, n);

    return 0;

}