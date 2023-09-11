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
#include "ler_escrever_serial.h"
#include "conversor.h"


Conversor conv1;             // Converte escalas

void enviar_dados_serial(float *sinal_ref, float *theta_saida, float *erro,
                         float *sinal_controle, float *ampl, float *t)
{
    /* Sinal de Referência. */
    Serial.print(*sinal_ref + 17.5, 3);
    Serial.print(",");

    /* Sinal de tensão no potenciômetro. */
    Serial.print(*theta_saida, 3);
    Serial.print(",");

    /* Sinal de Erro. */
    //Serial.print(conv1.rad2grau(*erro), 3);
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

void ler_dados_serial(float *ampl, float *freq_ref, float *offset,
                      int *selecionar_onda, bool *conf_sistema, bool *executar)
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
    else if (rlen == 7000.0) // switch_event_den_serra
    {
        *selecionar_onda = 2;
    }
    else if (rlen == 8000.0) // referencia_seno
    {
        *selecionar_onda = 1;
    }
    else if (rlen == 9000.0) // referencia_onda_quadrada
    {
        *selecionar_onda = 0;
    }
    else if (rlen == 10000.0) // referencia_onda_quadrada
    {
        *conf_sistema = true;
    }
    else if (rlen == 11000.0) // referencia_onda_quadrada
    {
        *conf_sistema = false;
    }
    else if (rlen == 12000.0) // referencia_onda_quadrada
    {
        *executar = true;
    }
}
