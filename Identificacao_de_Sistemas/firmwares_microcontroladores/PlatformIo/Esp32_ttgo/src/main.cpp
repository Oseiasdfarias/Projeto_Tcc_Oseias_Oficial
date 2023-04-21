/*
      * Universidade Federal do Pará
      * Campus Universitário de Tucuruí
      * Faculdade de Engenharia Elétrica
      * Trabalho de Conclusão de Curso
      *
      * Título : Potótipo Aeropêndulo
      * Professor Orientador: Raphael Teixeira
      * Autor  : Oséias Farias
      * 
      * Arquivo: main.cpp
      *
      * Data: 2023
*/

#include "Arduino.h"

const int pinoAD_POT = 2;         // Valor do potenciômetro
const int pinoAD_CONTROL = 13;    // Sinal de Controle

// Define a direção de rotação do motor
const int pinoSentido1 = 32;
const int pinoSentido2 = 33;

// Configurações do Sinal PWM
const int pinoPWM = 25;        // pino para sinal PWM
const int freq = 500;
const int pwmChannel = 0;
const int resolution = 8;
int dutyCycle = 120;
float ref = 0.0;               // Setpoint

// Variáveis usadas no código
int valorAD_POT = 0;
float tensao_pot = 0.0;

float theta = 0.0;             // Ângulo theta
float tensao_control = 0.0;    // Sinal de controle em tensão
// Variável para salvar o sinal de controle, obtido pelo conversor AD.
int valorAD_CONTROL = 0;

void setup() {
  pinMode(pinoSentido1, OUTPUT);
  pinMode(pinoSentido2, OUTPUT);
  pinMode(pinoPWM, OUTPUT);

  digitalWrite(pinoSentido1, HIGH);
  digitalWrite(pinoSentido2, LOW);

  ledcSetup(pwmChannel, freq, resolution);
  ledcAttachPin(pinoPWM, pwmChannel);

  Serial.begin(115200);
}

void loop() {
  if (!Serial.available()) {
    // valor_pwm = Serial.parseFloat();
    ledcWrite(pwmChannel, dutyCycle); 

    // Sinal de tensão no potenciômetro.
    valorAD_POT = analogRead(pinoAD_POT);
    Serial.print(valorAD_POT);
    Serial.print("  |  ");
    theta = map(valorAD_POT, 1085., 4095., 0., 180.);
    Serial.print(theta);
    Serial.print("° | ");

    // Sinal de tensão aplicado ao motor cc.
    valorAD_CONTROL = analogRead(pinoAD_CONTROL);
    tensao_control = valorAD_CONTROL * 3.3 / 4095.;
    Serial.print("Sianl Controle: ");
    Serial.print(tensao_control);
    Serial.println("(V)");

    delay(20);
  }
}
