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

const int pinAD_POT = 2;            // Valor do potenciômetro.

// Define a direção de rotação do motor.
const int pinSentido1 = 32;
const int pinSentido2 = 33;

// Configurações do Sinal PWM
const int pinPWM = 25;              // pino para sinal PWM.
const int freq_pwm = 500;           // Frequência do sinal PWM.
const int canal_pwm = 0;            // Canal para o sinal PWM (0-15).
const int resolucao = 8;            // Resolução do sinal PWM.
int ciclo_trabalho = 140;           // Ciclo de trabalho.
float ref1 = 90.0;                  // Setpoint.
float erro = 7.0;                   // Erro do sistema.

float theta = 0.0;                  // Ângulo theta.
/* Variável para salvar o sinal de controle, obtido pelo conversor AD. */
int valorAD_CONTROL = 0;

/* Parâmetros do sinal de referência */
float ampl = 0.4;
float freq_ref;
float offset;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);

  while (!Serial)
    delay(10);

  /* Define os pinos como saída. */
  pinMode(pinSentido1, OUTPUT);
  pinMode(pinSentido2, OUTPUT);
  pinMode(pinPWM, OUTPUT);

  /* Define o sentido de Giro do Motor */
  digitalWrite(pinSentido1, HIGH);
  digitalWrite(pinSentido2, LOW);

  /* Configura o sinal PWM usando para controle de velocidade do motor CC. */
  ledcSetup(canal_pwm, freq_pwm, resolucao);
  ledcAttachPin(pinPWM, canal_pwm);
}

void loop() {
  enviar_dados_serial(canal_pwm, pinAD_POT, &ciclo_trabalho,
                      &ref1, &theta, &erro, &freq_ref, &ampl);
  delay(20);
  if (Serial.available() > 0){
    ler_dados_serial(&erro, &freq_ref, &offset);
  }
}