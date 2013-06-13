//
//  main.c
//  CBCSubCipher
//
//  Created by Christian Kiær on 13/06/13.
//  Copyright (c) 2013 Christian Kiær. All rights reserved.
//

#include <stdio.h>
#include <time.h>

int initVector;
int key[] = { 13, 4, 3, 12, 1, 0, 8, 10, 14, 6, 9,
    15, 11, 2, 5, 7 };
int plaintext[] = { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3 };
int cipher[16];
int bitSize = 16;
clock_t begin, end;
double timeSpent;

void encrypt(int *plainText, int initVector){
    
    cipher[0] = key[initVector ^ plainText[0]];
    
    for (int i = 1; i < bitSize; i++) {
        cipher[i] = key[cipher[i - 1] ^ plainText[i]];
    }
}

int main(int argc, const char * argv[])
{   
    begin = clock();
    for (int i = 0; i < bitSize; i++) {
        initVector = i;
        
        encrypt(plaintext, initVector);
        printf("InitVector: %d Cipher: ", initVector);
        for (int j = 0; j < bitSize; j++) {
            printf("%d ", cipher[j]);
        }
        printf("\n");
    }
    end = clock();
    printf("Elapsed: %f seconds\n", (double)(end - begin) / CLOCKS_PER_SEC);

}