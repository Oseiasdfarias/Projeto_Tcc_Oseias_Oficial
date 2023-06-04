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

/* Potótipos de Funções */
#ifndef LER_ESCREVER_SERIAL_H_INCLUDED
#define LER_ESCREVER_SERIAL_H_INCLUDED
void enviar_dados_serial(int *valorAD_POT, float *sinal_ref, float *theta_saida,
                         float *erro, float *sinal_controle, float *ampl, float *t);

void ler_dados_serial(float *erro, float *freq_ref, float *offset);

#endif // LER_ESCREVER_SERIAL_H_INCLUDED
