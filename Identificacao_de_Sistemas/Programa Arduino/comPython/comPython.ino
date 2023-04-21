// Bancada de Controle de velocidade: Motor-Gerador
// UFPA - Campus Tucuruí
// Monitoria de Sistemas de Controle para Engenharia - PGRAD - MONITORIA 03/2020
// Coodenador: Cleison Daniel Silva
// Bolsista: Felipe Silveira Piano
// Data: 26/09/2020

#define pinoAD     A0
#define pinoPWM    9
#define pinoSent1  7
#define pinoSent2  8

int valorAD = 0;
int valorPWM = 0;

void setup() {
  pinMode(pinoSent1, OUTPUT);
  pinMode(pinoSent2, OUTPUT);
  pinMode(pinoPWM, OUTPUT);
  Serial.begin(38400);
  Serial.setTimeout(5);
}

void loop()  {
  if (Serial.available() > 0) {
    valorPWM = Serial.parseInt();
    digitalWrite(pinoSent1, HIGH);
    digitalWrite(pinoSent2, LOW);
    analogWrite(pinoPWM, valorPWM);
    valorAD = analogRead(pinoAD);
    Serial.println(valorAD*5./1023.);
  }
}
