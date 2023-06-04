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
#ifndef CONVERSOR_H_INCLUDED
#define CONVERSOR_H_INCLUDED

class Conversor
{
    public:
        float x_min, x_max,
              y_min, y_max, offset;

        Conversor(float _x_min, float _x_max,
                      float _y_min, float _y_max, float _offset);
        
        float converte_escala(float x_converter);

};
#endif // CONVERSOR_H_INCLUDED
