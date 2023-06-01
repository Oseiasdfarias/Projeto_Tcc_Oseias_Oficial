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

void enviar_dados_serial(int canal_pwm, int pinAD_POT, int *ciclo_trabalho, float *ref1,
                         float *theta, float *erro, float *freq_ref, float *ampl){
    // Variáveis usadas no código
    int static valorAD_POT = 0;        // Valor de tensão (potenciômetro) lido pela conversor ADC.
    float static tensao_pot = 0.0;     // Tensão no potenciômetro.
    float static tensao_control = 0.0; // Sinal de controle em tensão.

    ledcWrite(canal_pwm, *ciclo_trabalho);

    /* Sinal de Referência. */
    Serial.print(*ref1, 3);
    Serial.print(",");

    /* Sinal de tensão no potenciômetro. */
    valorAD_POT = analogRead(pinAD_POT);
    *theta = map(valorAD_POT, 528., 3235., 0., 180.);
    Serial.print(*theta, 3);
    Serial.print(",");

    /* Sinal de Erro. */
    Serial.print(*erro, 3);
    Serial.print(",");

    /* Sinal de tensão aplicado ao motor cc. */
    tensao_control = (*ciclo_trabalho * 3.3 / 255.0);
    Serial.print(tensao_control, 3);
    Serial.print(",");

    /* Estruturas reservas de envio de dados. */
    Serial.print(*freq_ref, 3);
    Serial.print(",");
    Serial.println(*ampl, 3);
}

void ler_dados_serial(float *erro, float *freq_ref, float *offset){
    /* Leitura dos dados da porta serial. */
    float rlen = Serial.parseFloat();
    
    /* Dados do Amplitude. */
    if (1000.0 < rlen && rlen < 2001.0){
        *erro = (((rlen * 15.0) / 1000.0) - 15.0);
        /* Dados do Frequência. */
    } else if (2001.0 < rlen && rlen < 3001.0){
        *freq_ref = (((rlen * 15.0) / 1000.0) - 30.0);
        /* Dados do offset. */
    } else if (3001.0 < rlen && rlen < 4001.0){
        *offset = (((rlen * 15.0) / 1000.0) - 45.0);
    }
}