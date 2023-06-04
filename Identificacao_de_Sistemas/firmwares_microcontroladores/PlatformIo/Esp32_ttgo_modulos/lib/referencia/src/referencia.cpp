/* ************************  | |  ****************************
      * Universidade Federal do Pará
      * Campus Universitário de Tucuruí
      * Faculdade de Engenharia Elétrica
      * Trabalho de Conclusão de Curso - Aeropêndulo

      * Título : Firmware Potótipo Aeropêndulo
      * Professor Orientador: Raphael Teixeira
      * Autor  : Oséias Farias

      * Arquivo: main.cpp    |   Data: 2023
           ***************   |   ************** */

#include <math.h>
#include "Arduino.h"
// #include "referencia.h"

class SinaisRefs
{
    public:
        float TEMP = 0.0;
        float SOMA = 0.0;
        //SinaisRefs(){};
        float referencia_seno(float freq, float ampl,
                              float offset, float t);
        float referencia_onda_quadrada(float freq, float ampl,
                                       float offset, float Ts);
        float referencia_onda_dente_serra(float freq, float ampl,
                                 float offset, float Ts);
};

// SinaisRefs::SinaisRefs(){};

/* Gráfico de uma Onda senoidal */
float SinaisRefs::referencia_seno(
    float freq, float ampl, float offset, float t)
{
    float sinal;
    sinal = (ampl*sin(2 * M_PI * freq * t)) + offset;
    return sinal;
};

/* Gráfico de uma Onda Quadrada */
float SinaisRefs::referencia_onda_quadrada(
    float freq, float ampl, float offset, float Ts)
{
    float Tsf = 1.0/freq;
    static float sinal;
    if (this->TEMP <= (Tsf/2.0))
        sinal = ampl + offset;
    else
        sinal = offset;
    if (this->TEMP >= Tsf)
        this->TEMP = 0.0;
    this->TEMP += Ts;
    return sinal;
};

/* Gráfico de uma Onda Dente de Serra */
float SinaisRefs::referencia_onda_dente_serra(
    float freq, float ampl, float offset, float Ts)
{
    float Tsf = 1.0/freq;
    float somar = 1.0/(Tsf/Ts);
    static float sinal;
    if (this->TEMP <= Tsf)
    sinal = ampl*this->SOMA + offset;
    else
    {
        this->SOMA = 0.0;
        sinal = offset;
        this->TEMP = 0.0;
    }
    this->SOMA += somar;
    this->TEMP += Ts;
    return sinal;
}

