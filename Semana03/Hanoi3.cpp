
// Resolvido e verificado para 6 discos.

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

void Move (int k, int* inic, int* dest, int* buff);
void Resolve (int n, int ct, int* buffin, int* buffou, int* final, char A, char B, char C);
void Init (int n, int* buffin, int* buffou, int* final);
void Print (int n, int* buffin, int* buffou, int* final, char A, char B, char C);


//Função recursiva responsável por resolver a torre
//Resolve torre -1 pro buffer, move o disco pro destino, printa a torre a cada movimento, resolve o buffer pro destino
void Resolve (int n, int ct, int* buffin, int* buffou, int* final , char A, char B, char C) {

    if (n > 0) {
    Resolve ((n - 1), ct, buffin, final, buffou, A, C, B);

    Move (ct, buffin, final, buffou);

    //Condicionais para printar as torres nas posições certas
    if (A == 'A' && B == 'B') Print (ct, buffin, buffou, final, A, B, C);
    if (A == 'A' && B == 'C') Print (ct, buffin, final, buffou, A, C, B);
    if (A == 'B' && B == 'A') Print (ct, buffou, buffin, final, B, A, C);
    if (A == 'B' && B == 'C') Print (ct, final, buffin, buffou, C, A, B);
    if (A == 'C' && B == 'A') Print (ct, buffou, final, buffin, B, C, A);
    if (A == 'C' && B == 'B') Print (ct, final, buffou, buffin, C, A, B);


    Resolve ((n-1), ct, buffou, buffin, final, B, A, C);
    };
};

//Função de inicialização das torres
void Init (int n, int* buffin, int* buffou, int* final) {
    for (int i = 0; i <n; i++) {
        buffin[i] = n - i;
        buffou[i] = 0;
        final[i] = 0;
        //cout << "\t" << buffin[i] << "\t" << buffou[i] << "\t" << final[i] << "\n";
    }

};


//Função que faz o print das torres e sua identificação
void Print (int n, int* buffin, int* buffou, int* final, char A, char B, char C) {
    cout <<"\n";
    for (int i = 0; i < n; i++) {
        cout << "\t" << buffin[n -i -1] << "\t" << buffou[n- i -1] << "\t" << final[n - i -1] << "\n";
    }
        cout << "\t" << A << "\t" << B << "\t" << C << "\n";
        cout <<"\n**************************************\n";
};


//Função responsável por mover os discos, encontra o disco superior e o movimenta para posição livre na torre de destino
void Move (int k, int* inic, int* dest, int* buff) {
    int indi = (k-1), indd = (k-1), fli = 0, fld = 0;

    if (dest[0] == 0) {
        fld = 1; 
        indd = 0; }

    for (int i= (k - 1); i >= 0; i--) {
        if (fli == 0) {
            if (inic[i] != 0 || i == 0) {
                indi = i;
                fli = 1;
            };
        };
        if (fld == 0) {
            if (dest[i] != 0 || i == 0) {
                indd = i + 1;
                fld = 1;
            };
        };

    };

    if (inic[0] !=0 && indd < k) {
        dest[indd] = inic[indi];
        inic[indi] = 0;

    } else {
        if (inic [0] == 0) {
            cout << "\nNão há discos na origem!";
        };
        if (indd >= k) {
            cout << "\nDestino está lotado";
        };
    };

    
};



int main (int argc, char* argv[]) {
    

    if (argc != 2) {
        cout << "Wrong number of arguments!\n";
        return 1;
    }

    const int sz = stoi(argv[1]);

    //Alocação de memória
    int* buffin = new int[sz];
    int* buffou = new int[sz];
    int* final = new int[sz];

    Init(sz, buffin, buffou, final);
    Print(sz, buffin, buffou, final, 'A', 'B', 'C');

    Resolve (sz, sz, buffin, buffou, final, 'A', 'B', 'C');



    //Desaloca memória
    delete[] buffin;
    delete[] buffou;
    delete[] final;


    return 0;
}