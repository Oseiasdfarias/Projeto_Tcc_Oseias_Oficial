/* ************************  |  ****************************
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
const int pinPWM = 25;    // pino para sinal PWM.
const int freq_pwm = 500; // Frequência do sinal PWM.
const int canal_pwm = 0;  // Canal para o sinal PWM (0-15).
const int resolucao = 8;  // Resolução do sinal PWM.
int ciclo_trabalho = 0;   // Ciclo de trabalho.

float sinal_ref = 0.0,      // Setpoint.
    sinal_entrada_ma = 0.0, // Sinal de entrada em malha aberta
    erro = 0.0,             // Sinal de Erro do sistema em Malha Fechada.
    theta_saida = 0.0,      // Ângulo theta.
    sinal_controle = 0.0;

/* Parâmetros do sinal de referência */
float ampl = 0.2,
      freq_ref = 0.2,
      offset = 30.0;
int selecionar_onda = 0;

/* Tempo de amostragem e Período. */
float t = 0.0,
      Ts = 0.02; // ms

/* definir sistema em malha fechada ou malha aberta */
bool conf_sistema = false;
bool executar = false;

/* Iniciando uma instáncia do gerador de sinais e do controlador PID. */
SinaisRefs gerar_ref;        // Gerador de sinais
Conversor conv;              // Converte escalas
PID mypid(0.02, 0.025, 0.4); // Controlador PID

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
  if (executar)
  {
    /* Sinal de saída - Sinal de tensão no potenciômetro. */
    valorAD_POT = analogRead(pinAD_POT);

    /* Sinal de saída - Sinal de tensão no potenciômetro convertido para ângulo Graus. */
    theta_saida = conv.converte_escala(valorAD_POT, 0.0, 4095., 0.0, 270.0, 528.0);

    if (conf_sistema)
    {
      /* ###### Define o sistema em malha fechada ###### */
      /* Sinal de referência */
      if (selecionar_onda == 0)
        sinal_ref = gerar_ref.referencia_onda_quadrada(freq_ref, ampl, offset, Ts);
      else if (selecionar_onda == 1)
        sinal_ref = gerar_ref.referencia_seno(freq_ref, ampl, offset, t);
      else if (selecionar_onda == 2)
        sinal_ref = gerar_ref.referencia_onda_dente_serra(freq_ref, ampl, offset, Ts);

      /* Sinal de erro calculado, caso seja menor que zero, desliga o Motor. */
      erro = sinal_ref - theta_saida;

      /* Sinal de Controle calculado.*/
      sinal_controle = mypid.atualiza_pid(erro, theta_saida, Ts);
      /* Converte o nível de tensão de controle para nível PWM */
      ciclo_trabalho = conv.converte_tensao_ciclo(sinal_controle);
    }
    else
    {
      /* ###### Define o sistema em malha aberta ###### */
      sinal_entrada_ma = gerar_ref.referencia_onda_quadrada(0.2, 0.5, 1.0, Ts);
      sinal_ref = 0.0;
      sinal_controle = 0.0;
      erro = 0.0;
      ciclo_trabalho = conv.converte_tensao_ciclo(sinal_entrada_ma);
    }

    // Escrevendo sinal PWM na GPIO
    ledcWrite(canal_pwm, ciclo_trabalho);

    enviar_dados_serial(&sinal_ref, &theta_saida, &erro, &sinal_controle, &sinal_entrada_ma, &t);
    delay(1000 * Ts);

    if (Serial.available() > 0)
    {
      ler_dados_serial(&ampl, &freq_ref, &offset, &selecionar_onda, &conf_sistema, &executar);
    }
    t += Ts;
  }
  else
  {
    if (Serial.available() > 0)
    {
      ler_dados_serial(&ampl, &freq_ref, &offset, &selecionar_onda, &conf_sistema, &executar);
    }
  }
}
