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
#include "referencia.h"

const int pinAD_POT = 2; // Valor do potenciômetro.
int valorAD_POT = 0;      // Valor de tensão (potenciômetro) lido pela conversor ADC.

// Define a direção de rotação do motor.
const int pinSentido1 = 32;
const int pinSentido2 = 33;

// Configurações do Sinal PWM
const int pinPWM = 25;    // pino para sinal PWM.
const int freq_pwm = 500; // Frequência do sinal PWM.
const int canal_pwm = 0;  // Canal para o sinal PWM (0-15).
const int resolucao = 8;  // Resolução do sinal PWM.
int ciclo_trabalho = 0.0; // Ciclo de trabalho.

float sinal_ref = 0.0;    // Setpoint.
float erro = 0.0;         // Sinal de Erro do sistema em Malha Fechada.
float theta_saida = 0.0;  // Ângulo theta.
/* Variável para salvar o sinal de controle, obtido pelo conversor AD. */
float sinal_controle = 0.0;
float Kp = 0.2;           // Ganho do controlador Proporcional.

/* Parâmetros do sinal de referência */
float ampl = 0.0, freq_ref = 0.5, offset = 30.0;

/* Tempo de amostragem e Período.  */
float t = 0, Ts = 0.02; // ms

void setup()
{
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

void loop()
{
  /* Sinal de referência */
  // ref_controle = referencia_seno(freq_ref, ampl, offset, t);
  // ref_controle = referencia_onda_quadrada(freq_ref, ampl, offset, Ts);
  sinal_ref = referencia_onda_dente_serra(freq_ref, ampl, offset, Ts);

  /* Sinal de tensão no potenciômetro. */
  valorAD_POT = analogRead(pinAD_POT);
  /* Sinal de tensão no potenciômetro. */
  theta_saida = map(valorAD_POT, 528., 3235., 0., 180.);

  // Sinal de erro calculado, caso seja menor que zero, desliga o Motor.
  erro = sinal_ref - theta_saida;

  if (erro < 0)
  {
    digitalWrite(pinSentido1, LOW);
    digitalWrite(pinSentido2, LOW);
  }
  else
  {
    digitalWrite(pinSentido1, HIGH);
    digitalWrite(pinSentido2, LOW);
  }

  // Sinal de Controle calculado.
  sinal_controle = Kp*erro;  

  if (0.0 <= sinal_controle <= 3.3)
    ciclo_trabalho = (sinal_controle*255.0)/3.3;
  else if (sinal_controle > 3.3)
    ciclo_trabalho = 255;

  ledcWrite(canal_pwm, ciclo_trabalho);

  enviar_dados_serial(&valorAD_POT, &sinal_ref,
                      &theta_saida, &erro, &sinal_controle, &ampl);
  delay(1000 * Ts);
  if (Serial.available() > 0)
  {
    ler_dados_serial(&ampl, &freq_ref, &offset);
  }
  t += Ts;
}