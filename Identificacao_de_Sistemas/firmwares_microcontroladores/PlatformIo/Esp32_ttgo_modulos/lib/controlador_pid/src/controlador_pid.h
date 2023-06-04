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
// #pragma once
#ifndef CONTROLADOR_PID_H_INCLUDED
#define CONTROLADOR_PID_H_INCLUDED

class PID
{
      public:
            // long lastProcess = 0;
            float lastTheta, theta;
            float Kp, Ki, Kd;
            float P, I, D;

            PID(float _Kp, float _Ki, float _Kd);
            float atualiza_pid(float erro, float theta, float Ts);
      };

#endif // CONTROLADOR_PID_H_INCLUDED
