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


int pinoAD_POT = A3;        // Valor do potenciômetro
int pinoAD_CONTROL = A1;    // Sinal de Controle
int pinoPWM = 10;           // pino para sinal PWM
float ref = 0.0;            // Setpoint

// Variáveis usadas no código
int valorAD_POT = 0;
float tensao_pot = 0.0;

float theta = 0.0;           // Ângulo theta
float tensao_control = 0.0;  // Sinal de controle em tensão
// Variável para salvar o sinal de controle, obtido pelo conversor AD.
int valorAD_CONTROL = 0;
int valor_pwm = 140;         // Sinal PWM

// Define a direção de rotação do motor
int pinoSentido1 = 8;
int pinoSentido2 = 9;
int LED = 13;                // Led do motor 

void setup() {
  pinMode(pinoSentido1, OUTPUT);
  pinMode(pinoSentido2, OUTPUT);
  pinMode(LED, OUTPUT);
  pinMode(pinoPWM, OUTPUT);
  Serial.begin(115200);
  Serial.setTimeout(5);
}

void loop() {
  if (!Serial.available()) {
    // valor_pwm = Serial.parseFloat();
    digitalWrite(pinoSentido1, LOW);
    digitalWrite(pinoSentido2, HIGH);
    digitalWrite(LED, HIGH);
    analogWrite(pinoPWM, valor_pwm);

    // Sinal de tensão no potenciômetro.
    valorAD_POT = analogRead(pinoAD_POT);
    Serial.print(valorAD_POT);
    Serial.print("  |  ");
    theta = map(valorAD_POT, 360., 480., 0., 180.);
    Serial.print(theta);
    Serial.print("° | ");

    // Sinal de tensão aplicado ao motor cc.
    valorAD_CONTROL = analogRead(pinoAD_CONTROL);
    tensao_control = valorAD_CONTROL * 5. / 1023.;
    Serial.print("Sianl Controle: ");
    Serial.print(tensao_control);
    Serial.println("(V)");

    delay(20);
  }
}
