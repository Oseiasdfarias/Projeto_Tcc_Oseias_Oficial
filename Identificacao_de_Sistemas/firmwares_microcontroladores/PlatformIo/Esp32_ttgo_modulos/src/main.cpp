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
#include "controlador_pid.h"
#include "conversor.h"

const int pinAD_POT = 2; // Valor do potenciômetro.
int valorAD_POT = 0;     // Valor de tensão (potenciômetro) lido pela conversor ADC.

// Define a direção de rotação do motor.
const int pinSentido1 = 32;
const int pinSentido2 = 33;

// Configurações do Sinal PWM
const int pinPWM    = 25;    // pino para sinal PWM.
const int freq_pwm  = 500; // Frequência do sinal PWM.
const int canal_pwm = 0;  // Canal para o sinal PWM (0-15).
const int resolucao = 8;  // Resolução do sinal PWM.
int ciclo_trabalho  = 0; // Ciclo de trabalho.

float sinal_ref = 0.0,   // Setpoint.
      erro = 0.0,        // Sinal de Erro do sistema em Malha Fechada.
      theta_saida = 0.0, // Ângulo theta.
      sinal_controle = 0.0;

/* Parâmetros do sinal de referência */
float ampl = 0.0, freq_ref = 0.5, offset = 30.0;

/* Tempo de amostragem e Período. */
float t = 0.0, Ts = 0.02; // ms

/* Iniciando uma instáncia do gerador de sinais e do controlador PID. */
SinaisRefs gerar_ref;
PID mypid(0.02, 0.025, 0.4);
Conversor conv(0.0, 4095., 0.0, 270.0, 528.0);

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
  // sinal_ref = sref.referencia_seno(freq_ref, ampl, offset, t);
  // sinal_ref = sref.referencia_onda_quadrada(freq_ref, ampl, offset, Ts);
  sinal_ref = gerar_ref.referencia_onda_dente_serra(freq_ref, ampl, offset, Ts);

  /* Sinal de tensão no potenciômetro. */
  valorAD_POT = analogRead(pinAD_POT);
  /* Sinal de tensão no potenciômetro. */
  theta_saida = conv.converte_escala(valorAD_POT);
  //theta_saida = map(valorAD_POT, 528., 3235., 0., 180.);

  // Sinal de erro calculado, caso seja menor que zero, desliga o Motor.
  erro = sinal_ref - theta_saida;

  // Sinal de Controle calculado.
  sinal_controle = mypid.atualiza_pid(erro, theta_saida, Ts);

  if (0.0 <= sinal_controle <= 3.3)
    ciclo_trabalho = (sinal_controle * 255.0) / 3.3;
  else if (sinal_controle > 3.3)
    ciclo_trabalho = 255;

  ledcWrite(canal_pwm, ciclo_trabalho);

  enviar_dados_serial(&valorAD_POT, &sinal_ref,
                      &theta_saida, &erro, &sinal_controle, &ampl, &t);
  delay(1000 * Ts);
  if (Serial.available() > 0)
  {
    ler_dados_serial(&ampl, &freq_ref, &offset);
  }
  t += Ts;
}
