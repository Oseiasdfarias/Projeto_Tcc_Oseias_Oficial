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
#include "ler_escrever_serial.h"

void enviar_dados_serial(int *valorAD_POT, float *sinal_ref, float *theta_saida,
                         float *erro, float *sinal_controle, float *ampl, float *t)
{
    /* Sinal de Referência. */
    Serial.print(*sinal_ref, 3);
    Serial.print(",");

    /* Sinal de tensão no potenciômetro. */
    Serial.print(*theta_saida, 3);
    Serial.print(",");

    /* Sinal de Erro. */
    Serial.print(*erro, 3);
    Serial.print(",");

    /* Sinal de tensão aplicado ao motor cc. */
    Serial.print(*sinal_controle, 3);
    Serial.print(",");

    /* Estruturas reservas de envio de dados. */
    Serial.print(*ampl, 3);
    Serial.print(",");
    Serial.print(*ampl, 3);
    Serial.print(",");
    Serial.println(*t, 3);
}

void ler_dados_serial(float *ampl, float *freq_ref, float *offset)
{
    /* Leitura dos dados da porta serial. */
    float rlen = Serial.parseFloat();

    /* Dados do Amplitude. */
    if (1000.0 < rlen && rlen < 2001.0)
    {
        *ampl = (((rlen * 30.0) / 1000.0) - 30.0);
        /* Dados do Frequência. */
    }
    else if (2001.0 < rlen && rlen < 3001.0)
    {
        *freq_ref = (((rlen * 5.0) / 1000.0) - 10.0);
        /* Dados do offset. */
    }
    else if (3001.0 < rlen && rlen < 4001.0)
    {
        *offset = (((rlen * 120.0) / 1000.0) - 360.0);
    }
}