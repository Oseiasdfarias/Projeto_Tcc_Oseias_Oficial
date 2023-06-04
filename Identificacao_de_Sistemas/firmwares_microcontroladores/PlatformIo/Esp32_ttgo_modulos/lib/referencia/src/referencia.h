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

/* Potótipos de Funções */
#ifndef REFERENCIA_H_INCLUDED
#define REFERENCIA_H_INCLUDED

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

#endif // REFERENCIA_H_INCLUDED
