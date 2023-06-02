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

#include "Arduino.h"
#include "referencia.h"
#include <math.h>


/* Gráfico de uma Onda senoidal */
float referencia_seno(float freq, float ampl, float offset, float t)
{
    float sinal;
    sinal = (ampl*sin(2 * M_PI * freq * t)) + offset;
    return sinal;
}
