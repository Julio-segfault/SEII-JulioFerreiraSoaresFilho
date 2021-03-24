
#include <iostream>
#include <cmath>
#include <Complex1.h> 
//A biblioteca está inclusa por meio de "-I", "${workspaceFolder"} no arquivo do visual studio que chama o compilador
using namespace std;

//Parte do código antes da criação da bibliotec estática
/*
class ComplexR {
    public:
        float Real;
        float Imag;

        float Arg() { 
            float r;
            r = sqrt((Real * Real) + (Imag * Imag));
            return r;
        }

        float Theta(){ 
            float t;
            t = atan(Imag / Real);
            return t;
        }


};

    ComplexR SomaR (ComplexR ComplexR1, ComplexR ComplexR2) {
        ComplexR R;
        R.Real = ComplexR1.Real + ComplexR2.Real;
        R.Imag = ComplexR1.Imag + ComplexR2.Imag;
        return R;
    };
    ComplexR SubR (ComplexR ComplexR1, ComplexR ComplexR2) {
        ComplexR R;
        R.Real = ComplexR1.Real - ComplexR2.Real;
        R.Imag = ComplexR1.Imag - ComplexR2.Imag;
        return R;
    };
    ComplexR MultR (ComplexR ComplexR1, ComplexR ComplexR2) {
        ComplexR R;
        R.Real = (ComplexR1.Real * ComplexR2.Real) - (ComplexR1.Imag * ComplexR2.Imag);
        R.Imag = (ComplexR1.Imag * ComplexR2.Real) + (ComplexR1.Real * ComplexR2.Imag);
        return R;
    };
    ComplexR DivR ( ComplexR ComplexR1, ComplexR ComplexR2) {
        ComplexR R;
        float ar, th;
        ar = ComplexR1.Arg() * ComplexR2.Arg();
        th = ComplexR1.Theta() - ComplexR2.Theta();
        R.Real = ar * cos(th);
        R.Imag = ar * sin(th);
        return R;
        
    };
    
*/

//Programa que pega dois números complexos e realizas as operações básicas
int main () {
    float r1, r2, i1,i2;
    ComplexR N1, N2, M;

    cout << "\nType the real value of the first number: ";
    cin >> r1;
    cout << "\nType the imaginary value of the first number: ";
    cin >> i1;
    cout << "\nType the real value of the second number: ";
    cin >> r2 ;
    cout << "\nType the imaginary value of the second number: ";
    cin >> i2 ;

    N1.Real = r1;
    N1.Imag = i1;
    N2.Real = r2;
    N2.Imag = i2;

    cout << "\nNumber 1 is: " << N1.Real << " + " << N1.Imag << "i";
    cout << "\nNumber 1 in polar coordinates: " << N1.Arg() << " ; " << N1.Theta();

    cout << "\nNumber 2 is: " << N2.Real << " + " << N2.Imag << "i";
    cout << "\nNumber 2 in polar coordinates: " << N2.Arg() << " ; " << N2.Theta();
    cout<< "\n";


    M = SomaR(N1, N2);
    cout << "\nThe sum is: " << M.Real << " + " << M.Imag << "i";
    cout << "\nThe sum in polar coordinates is: " << M.Arg() << " ; " << M.Theta();
    cout<< "\n";


    M = SubR(N1, N2);
    cout << "\nThe subtraction is: " << M.Real << " + " << M.Imag << "i";
    cout << "\nThe sum in subtraction in polar coordinates is: " << M.Arg() << " ; " << M.Theta();
    cout<< "\n";


    M = MultR(N1, N2);
    cout << "\nThe multiplication is: " << M.Real << " + " << M.Imag << "i";
    cout << "\nThe multiplication in polar coordinates is: " << M.Arg() << " ; " << M.Theta();
    cout<< "\n";


    M = DivR(N1, N2);
    cout << "\nThe division is: " << M.Real << " + " << M.Imag << "i";
    cout << "\nThe division in polar coordinates is: " << M.Arg() << " ; " << M.Theta();

    cout<< "\n";

return 0;

};