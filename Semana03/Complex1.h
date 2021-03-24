#include <iostream>
#include <cmath>
using namespace std;

class ComplexR;

ComplexR SomaR (ComplexR ComplexR1, ComplexR ComplexR2);

ComplexR SubR (ComplexR ComplexR1, ComplexR ComplexR2);

ComplexR MultR (ComplexR ComplexR1, ComplexR ComplexR2);

ComplexR DivR ( ComplexR ComplexR1, ComplexR ComplexR2);

//Classe complexa que aceita valores em coordenada retangular, possui métodos para conversão em polar
class ComplexR {
    public:
        float Real;
        float Imag;

        //Métodos para conversão
        float Arg() { 
            float r;
            r = sqrt((Real * Real) + (Imag * Imag));
            return r;
        }

        float Theta(){ 
            float t;
            t = atan(Imag / Real);
            //Como atan retorna valores entre pi/2 e -pi/2 é preciso um condicional para verificar o valor correto de theta
            if (Real < 0) {
                t = t + M_PI;
            };
            return t;
        }


};

//Funções para realização de operações
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

    //A divisão é realizada em coordenadas polares porque é mais fácil
    ComplexR DivR ( ComplexR ComplexR1, ComplexR ComplexR2) {
        ComplexR R;
        float ar, th;
        ar = ComplexR1.Arg() * ComplexR2.Arg();
        th = ComplexR1.Theta() - ComplexR2.Theta();
        R.Real = ar * cos(th);
        R.Imag = ar * sin(th);
        return R;
        
    };
    