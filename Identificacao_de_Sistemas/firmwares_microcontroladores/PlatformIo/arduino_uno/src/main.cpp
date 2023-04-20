/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "Arduino.h"

int pinoAD = A0;
int pinoPWM = 10;

int valorAD = 0;
int valor_pwm = 130;

int pinoSentido1 = 8;
int pinoSentido2 = 9;
int LED = 13;

void setup() {
  pinMode(pinoSentido1, OUTPUT);
  pinMode(pinoSentido2, OUTPUT);
  pinMode(LED, OUTPUT);
  pinMode(pinoPWM, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(5);
}

void loop() {
  if (!Serial.available() > 0) {
    // valor_pwm = Serial.parseFloat();
    digitalWrite(pinoSentido1, LOW);   // controle do sentido de rotação do motor
    digitalWrite(pinoSentido2, HIGH);  // controle do sentido de rotação do motor
    digitalWrite(LED, HIGH);
    analogWrite(pinoPWM, valor_pwm);

    valorAD = analogRead(pinoAD);          // recebe o pino analogico A3
    Serial.println(valorAD * 5. / 1023.);  // escreve o valor da porta analogica na porta serial e converte
    delay(20);
  }  // Fim do IF

}  // Fim do loop
