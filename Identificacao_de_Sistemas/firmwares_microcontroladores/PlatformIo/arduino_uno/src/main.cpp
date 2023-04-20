#include "Arduino.h"

int pinoAD = A0;
int pinoPWM = 10;

int valorAD = 0;
int valor_pwm = 120;

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
    digitalWrite(pinoSentido1, LOW);
    digitalWrite(pinoSentido2, HIGH);
    digitalWrite(LED, HIGH);
    analogWrite(pinoPWM, valor_pwm);

    valorAD = analogRead(pinoAD);
    Serial.println(valorAD * 5. / 1023.);
    delay(20);
  }

}
