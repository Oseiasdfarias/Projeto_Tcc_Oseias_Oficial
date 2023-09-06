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

/* Potótipos de Funções */
#ifndef REFERENCIA_H_INCLUDED
#define REFERENCIA_H_INCLUDED


/* Sinais de Referências para aplicar ao sistema
    em malha fechda com controlador porjetado.
*/
class SinaisRefs
{
public:
    float TEMP;
    float SOMA;
    // SinaisRefs();
    float referencia_seno(float freq, float ampl,
                          float offset, float t);
    float referencia_onda_quadrada(float freq, float ampl,
                                   float offset, float Ts);
    float referencia_onda_dente_serra(float freq, float ampl,
                                      float offset, float Ts);
};


/* Sinal PRBS para identificação de sistema. */
class OndaPrbs
{
public:
    float TEMP = 0.0;
    float SOMA = 0.0;
    float freq, ampl, offset, Ts, Tsf, Tsf_init, sinal;
    float vTs[3];

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
        sinal = 0.0;
    }

private:
    float sortear(float vTs[]);
};

#endif // REFERENCIA_H_INCLUDED
