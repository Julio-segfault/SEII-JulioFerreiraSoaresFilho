
//To do: loop to reduce buffer size

#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char* argv[]) {

    ifstream orig(argv[1], ios::binary);
    ofstream cop(argv[2], ios::binary);

    orig.seekg(0, ios::end);
    ifstream::pos_type size = orig.tellg();
    orig.seekg(0);


    char* strg = new char[size];
    orig.read(strg, size);
    cop.write(strg, size);


    delete[] strg;
    orig.close();
    cop.close();

    return 0;
}