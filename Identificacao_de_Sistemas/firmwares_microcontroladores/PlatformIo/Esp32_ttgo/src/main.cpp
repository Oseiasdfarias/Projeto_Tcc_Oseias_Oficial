/*************************  | |  ****************************
      * Universidade Federal do Pará
      * Campus Universitário de Tucuruí
      * Faculdade de Engenharia Elétrica
      * Trabalho de Conclusão de Curso - Aeropêndulo

      * Título : Firmware Potótipo Aeropêndulo
      * Professor Orientador: Raphael Teixeira
      * Autor  : Oséias Farias

      * Arquivo: main.cpp    |   Data: 2023
           ***************   |   ***************/

#include "Arduino.h"

const int pinoAD_POT = 2;         // Valor do potenciômetro.
const int pinoAD_CONTROL = 13;    // Sinal de Controle.

// Define a direção de rotação do motor.
const int pinoSentido1 = 32;
const int pinoSentido2 = 33;

// Configurações do Sinal PWM
const int pinoPWM = 25;           // pino para sinal PWM.
const int freq_pwm = 500;         // Frequência do sinal PWM.
const int canal_pwm = 0;          // Canal para o sinal PWM (0-15).
const int resolucao = 8;          // Resolução do sinal PWM.
int ciclo_trabalho = 140;         // Ciclo de trabalho.
float ref1 = 90.0;                // Setpoint.
float erro = 7.0;                 // Erro do sistema.

// Variáveis usadas no código
int valorAD_POT = 0;              // Valor de tensão (potenciômetro) lido pela conversor ADC.
float tensao_pot = 0.0;           // Tensão no potenciômetro.

float theta = 0.0;                // Ângulo theta.
float tensao_control = 0.0;       // Sinal de controle em tensão.
/* Variável para salvar o sinal de controle, obtido pelo conversor AD. */
int valorAD_CONTROL = 0;

/* Parâmetros do sinal de referência */
float ampl = 0.4;
float freq_ref;
float offset;

/* Potótipos de Funções */
void enviar_dados_serial();
void ler_dados_serial();

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);
  while (!Serial)
    delay(10);

  /* Define os pinos como saída. */
  pinMode(pinoSentido1, OUTPUT);
  pinMode(pinoSentido2, OUTPUT);
  pinMode(pinoPWM, OUTPUT);

  /* Define o sentido de Giro do Motor */
  digitalWrite(pinoSentido1, HIGH);
  digitalWrite(pinoSentido2, LOW);

  /* Configura o sinal PWM usando para controle de velocidade do motor CC. */
  ledcSetup(canal_pwm, freq_pwm, resolucao);
  ledcAttachPin(pinoPWM, canal_pwm);
}

void loop() {

  enviar_dados_serial();
  delay(10);
  
  ler_dados_serial();
  delay(10);
}

void enviar_dados_serial(){
    // valor_pwm = Serial.parseFloat();
    ledcWrite(canal_pwm, ciclo_trabalho);

    /* Sinal de Referência. */
    Serial.print(ref1);
    Serial.print(",");

    /* Sinal de tensão no potenciômetro. */
    valorAD_POT = analogRead(pinoAD_POT);
    theta = map(valorAD_POT, 528., 3235., 0., 180.);
    Serial.print(theta);
    Serial.print(",");

    /* Sinal de Erro. */
    Serial.print(erro);
    Serial.print(",");

    /* Sinal de tensão aplicado ao motor cc. */
    valorAD_CONTROL = analogRead(pinoAD_CONTROL);
    tensao_control = valorAD_CONTROL * 3.3 / 4095.;
    Serial.print(tensao_control);
    Serial.print(",");

    /* Estruturas reservas de envio de dados. */
    Serial.print(freq_ref);
    Serial.print(",");
    Serial.println(ampl);
  }

void ler_dados_serial(){
    float rlen = Serial.parseFloat();

    /* Dados do Amplitude. */
    if (1000.0 < rlen && rlen < 2001.0){
      erro = (((rlen * 15.0) / 1000.0) - 15.0);

    /* Dados do Frequência. */
    } else if(2001.0 < rlen && rlen < 3001.0){
      freq_ref = (((rlen * 15.0) / 1000.0) - 30.0);

    /* Dados do offset. */
    }else if(3001.0 < rlen && rlen < 4001.0){
      offset = (((rlen * 15.0) / 1000.0) - 45.0);
    }
}
