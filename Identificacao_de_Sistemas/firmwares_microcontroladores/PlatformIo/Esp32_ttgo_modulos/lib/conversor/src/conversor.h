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
#ifndef CONVERSOR_H_INCLUDED
#define CONVERSOR_H_INCLUDED

class Conversor
{
public:
      float converte_escala(float x_converter, float x_min, float x_max,
                            float y_min, float y_max, float offset);
      float converte_tensao_ciclo(float sinal_controle);
      float grau2rad(float angulo);
      float rad2grau(float angulo);
};
#endif // CONVERSOR_H_INCLUDED
