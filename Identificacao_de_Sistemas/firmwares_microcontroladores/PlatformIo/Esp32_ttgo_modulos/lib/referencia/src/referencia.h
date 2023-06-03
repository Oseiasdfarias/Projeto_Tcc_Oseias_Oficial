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

/* Gráfico de uma Onda senoidal */
float referencia_seno(float freq, float ampl,
                      float offset, float t);

/* Gráfico de uma Onda Quadrada */
float referencia_onda_quadrada(float freq, float ampl,
                               float offset, float Ts);

/* Gráfico de uma Onda Dente de Serra */
float referencia_onda_dente_serra(float freq, float ampl,
                                 float offset, float Ts);

#endif // REFERENCIA_H_INCLUDED
