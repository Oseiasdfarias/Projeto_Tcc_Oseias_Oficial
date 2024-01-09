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
#ifndef CONTROLADORES_H_INCLUDED
#define CONTROLADORES_H_INCLUDED

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

#endif // CONTROLADORES_H_INCLUDED
