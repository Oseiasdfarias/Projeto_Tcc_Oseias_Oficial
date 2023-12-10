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

#include "Arduino.h"

class Controladores
{
public:
    // long lastProcess = 0;
    float
        u0 = 0.0,
        u1 = 0.0,
        u2 = 0.0,
        e1 = 0.0,
        e2 = 0.0,
        theta = 0.0;
    float controlador_1(float erro);
};

float Controladores::controlador_1(float erro)
{
    // double deltaTime = 0.02;
    // lastProcess = millis();
    this->u0 = 1.724 * this->u1 - 0.7241 * this->u2 + 19.09 * erro - 35.66 * this->e1 + 16.68 * this->e2;

    this->u2 = this->u1;
    this->u1 = this->u0;
    this->e2 = this->e1;
    this->e1 = erro;

    if (this->u0 > 1)
        this->u0 = 1;
    if (this->u0 < -1)
        this->u0 = -1;

    return this->u0;
}
