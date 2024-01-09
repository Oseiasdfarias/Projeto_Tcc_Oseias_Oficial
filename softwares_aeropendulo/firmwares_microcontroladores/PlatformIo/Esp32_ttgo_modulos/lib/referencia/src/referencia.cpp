/* ****************************************************
 *
 * Universidade Federal do Pará
 * Campus Universitário de Tucuruí
 * Faculdade de Engenharia Elétrica
 * Trabalho de Conclusão de Curso - Aeropêndulo
 * Título : Firmware Potótipo Aeropêndulo
 *
 * Professor Orientador: Raphael Teixeira
 * Autor  : Oséias Farias
 *
 * Arquivo: main.cpp - Data: 2023
 *
 ****************************************************** */

#include <math.h>
#include "Arduino.h"

class SinaisRefs
{
public:
    float TEMP = 0.0;
    float SOMA = 0.0;
    float referencia_seno(float freq, float ampl,
                          float offset, float t);
    float referencia_onda_quadrada(float freq, float ampl, float Ts);
    float referencia_onda_dente_serra(float freq, float ampl,
                                      float offset, float Ts);
};

/* Gráfico de uma Onda senoidal */
float SinaisRefs::referencia_seno(
    float freq, float ampl, float offset, float t)
{
    float sinal;
    sinal = (ampl * sin(2 * M_PI * freq * t)) + offset;
    return sinal;
};

/* Gráfico de uma Onda Quadrada */
float SinaisRefs::referencia_onda_quadrada(
    float freq, float ampl, float Ts)
{
    float Tsf = 1.0 / freq;
    static float sinal;
    if (this->TEMP <= (Tsf / 2.0))
        sinal = ampl;
    else
        sinal = 0.0;
    if (this->TEMP >= Tsf)
        this->TEMP = 0.0;
    this->TEMP += Ts;
    return sinal;
};

/* Gráfico de uma Onda Dente de Serra */
float SinaisRefs::referencia_onda_dente_serra(
    float freq, float ampl, float offset, float Ts)
{
    float Tsf = 1.0 / freq;
    float somar = 1.0 / (Tsf / Ts);
    static float sinal;
    if (this->TEMP <= Tsf)
        sinal = ampl * this->SOMA + offset;
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

class OndaPrbs
{
public:
    float TEMP = 0.0;
    float SOMA = 0.0;
    float freq, ampl, offset, Ts, Tsf, Tsf_init, sinal;

    float onda_prbs();
    OndaPrbs(float freq_, float ampl_,
             float offset_, float Ts_)
    {
        freq = freq_;
        ampl = ampl_;
        offset = offset_;
        Ts = Ts_;
        Tsf = (float)1.0 / freq;
        Tsf_init = (float)1.0 / freq;
        sinal = (float)0.0;
    }

private:
    float sortear(float vTs[]);
};

/* Gráfico de uma Onda Quadrada */
float OndaPrbs::onda_prbs()
{
    float vTs[4] = {this->Tsf_init, this->Tsf_init / (float)1.5,
                    this->Tsf_init / (float)2.0, this->Tsf_init / (float)2.5}; //,
                    // this->Tsf_init / 2.5, this->Tsf_init / 3.0};

    if (this->TEMP <= (this->Tsf / (float)2.0))
        this->sinal = this->ampl + this->offset;
    else
        this->sinal = this->offset;

    if (this->TEMP >= this->Tsf)
    {
        this->TEMP = (float)0.0;
        this->Tsf = this->sortear(vTs);
        Serial.println(this->Tsf);
    }

    this->TEMP += Ts;
    return this->sinal;
};

float OndaPrbs::sortear(float vTs[])
{
    int flag = random(5);
    float valor = vTs[flag];
    return valor;
}