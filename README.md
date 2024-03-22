<p align="center">
  <img height="60px" src="utils/logos_lg/logo_ufpa.png">
  <img height="60px" src="utils/favicon_aeropendulo_png.png">
</p>

<p align="center">
  <img height="20" src="./utils/logos_lg/UFPA-removebg-preview.png"> &
  <img height="20" src="./utils/logos_lg/Pendulab_lg-removebg-preview.png">
</p>

<p align="center">
    <a href="#roadmap">Roadmap</a>
  • <a href="#techs">Tecnologias</a> 
  • <a href="#challenge">Desafios</a>
</p>

<h1 align=center>Trabalho de Conclusão de Curso [ Oséias Farias ]</h1>



### Identificação de Sistemas, Simulador Gráfico e Prototipagem de um Aeropêndulo para estudos de Projetos de Controle

```
.
├── docs
├── materiais_complementares
├── mkdocs.yml
├── README.md
├── revisao_tcc
├── site
├── softwares_aeropendulo
└── utils
```

O projeto inclui 4 partes, sendo elas:

#### Potótipo

Implementa um aeropêndulo real, pode ser usado para estudos e testes de controladores e identificação de sistemas etc.

#### Interface gráfica

Usada para iteragir em tempo real com o protótipo, esse sistema plotado os gráficos da posição angular, erro, sinal de referência, sinal PRBS e sinal de controle em malha fechada.

#### Firmware

Implementa o controlador, envio e recebimento de dados inteface gráfica / microcontrolador, geração de sinal de referência, leitura do sensor potenciômetro.

#### Gêmeo Digital

Usa o sinal de saída (ângulo) para realizar a dinâmica do sinulador.

<br><br>

## Protótipo Aeropêndulo

<br>

<p align="center">
  <img height="60%" src="utils/img_aeropendulo.png">
</p>


<br><br>

## Interface Aeropêndulo

### Estrutura do Projeto da Interface Gráfica


<p align="center">
  <img height="60%" src="utils/demo_interface_dark1.png">
</p>

<p align="center">
  <img height="60%" src="utils/demo_interface_light.png">
</p>


## Firmware do Aeropêndulo

Aplicação para o microcontrolador com finalidade de desenvolver as funcionalidades de comunicação com a interface gráfico do computador e implementar controlador para o sistema em malha fechada, além disso, o usuário pode incrementar outras funcionalidades.

<p align="center">
  <img height="60%" src="utils/arquitetura_firmware-1.png">
</p>


## Simulador Aeropêndulo - (Gêmeo Digital)

<br>

<p align="center">
  <img height="60%" src="utils/gemeo_digital.png">
</p>  
