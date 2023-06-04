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
// #include "conversor.h"

class Conversor
{
    public:
        float x_min, x_max,
              y_min, y_max, offset;

        Conversor(float _x_min, float _x_max,
                      float _y_min, float _y_max, float _offset);
        float converte_escala(float x_converter);
};

Conversor::Conversor(float _x_min, float _x_max,
                      float _y_min, float _y_max, float _offset)
{
    this -> x_min = _x_min;
    this -> x_max = _x_max;
    this -> y_min = _y_min;
    this -> y_max = _y_max;
    this -> offset = _offset;
}

float Conversor::converte_escala(float x_converter)
{
    float m, F, x_conv, offset_conv;

    if (abs(x_converter) > this -> x_max)
        m = abs(x_converter) / this -> x_max;
    else
        m = 1.0;
    F = ( this -> y_min - this -> y_max) / ( this -> x_min - this -> x_max);
    if (x_converter < this -> x_min)
    {
        if (x_converter < -this -> x_max)
            x_converter = -this -> x_max;
        x_conv = m * (((x_converter - this -> x_min) * F) - this -> y_min);
    }
    else
    {
        if (x_converter > this -> x_max)
            x_converter = this -> x_max;
        x_conv = m * (((x_converter - this -> x_min) * F) + this -> y_min);
    }
    offset_conv = (( this -> offset - this -> x_min)*F ) + this -> y_min;
    x_conv = x_conv - offset_conv;
    return x_conv;
}