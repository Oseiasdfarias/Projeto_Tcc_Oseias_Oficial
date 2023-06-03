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
//#include "controlador_pid.h"

class PID
{
      public:
            // long lastProcess = 0;
            float
            lastTheta,
            theta = 0.0;

            float Kp, Ki, Kd;
            float P = 0.0, I = 0.0, D = 0.0;
            PID(float _Kp, float _Ki, float _Kd);
            float atualiza_pid(float erro, float theta, float Ts);
};

PID::PID(float _Kp, float _Ki, float _Kd)
{
      this->Kp = _Kp;
      this->Ki = _Ki;
      this->Kd = _Kd;
}

float PID::atualiza_pid(float erro, float theta, float Ts)
{
      // double deltaTime = 0.02;
      // lastProcess = millis();
      this->P = erro * this->Kp;
      this->I += (erro * this->Ki) * Ts;
      this->D = this->Kd * erro* (this->lastTheta - theta) * Ts;
      this->lastTheta = theta;

      return (this->P + this->I + this->D);
}
