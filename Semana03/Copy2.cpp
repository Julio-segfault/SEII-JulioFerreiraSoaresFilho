

#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char* argv[]) {

    if (argc != 3) {
        cout << "Wrong numbers of arguments!";
        return -1;
    }

    //Abre o arquivo de origem, abre/cria o arquivo de destino em binário
    ifstream orig(argv[1], ios::binary);
    ofstream cop(argv[2], ios::binary);

    //Determina o tamanho do arquivo
    orig.seekg(0, ios::end);
    ifstream::pos_type sz = orig.tellg();
    orig.seekg(0);

    //Criação do buffer
    char* strg = new char[sz];

    //Leitura para o buffer e escrita no destino
    orig.read(strg, sz);
    cop.write(strg, sz);

    //Destrói os objetos, fecha os arquivos
    delete[] strg;
    orig.close();
    cop.close();

    return 0;
}