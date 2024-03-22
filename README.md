<p align="center">
  <img height="60px" src="utils/logos_lg/logo_ufpa.png">
  <img height="60px" src="utils/favicon_aeropendulo_png.png">
</p>

<p align="center">
  <img height="20" src="./utils/logos_lg/UFPA-removebg-preview.png"> &
  <img height="20" src="./utils/logos_lg/Pendulab_lg-removebg-preview.png">
</p>

<p align="center">
    <a href="#protótipo">Protótipo</a>
  • <a href="#interface-gráfica">Interface gráfica</a> 
  • <a href="#firmware">Firmware</a>
  • <a href="#gêmeo-digital">Gêmeo Digital</a>
</p>

<h3  id="techs">Tecnologias</h3>

<p align=center> <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white""> <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black"> <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
  </ul>
  <br>
</p>

<h1 align=center>Trabalho de Conclusão de Curso [ Oséias Farias ]</h1>



<p align=center> <i><strong>Tema: Identificação de Sistemas, Simulador Gráfico e Prototipagem de um Aeropêndulo para estudos de Projetos de Controle</strong></i></p>

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

## Protótipo

Implementa um aeropêndulo real, pode ser usado para estudos e testes de controladores e identificação de sistemas etc.

<br>

<p align="center">
  <img height="60%" src="utils/img_aeropendulo.png">
</p>


## Interface gráfica

Usada para iteragir em tempo real com o protótipo, esse sistema plotado os gráficos da posição angular, erro, sinal de referência, sinal PRBS e sinal de controle em malha fechada.

<p align="center">
  <img height="60%" src="utils/demo_interface_dark1.png">
</p>

<p align="center">
  <img height="60%" src="utils/demo_interface_light.png">
</p>

## Firmware

Aplicação para o microcontrolador com finalidade de desenvolver as funcionalidades de comunicação com a interface gráfico do computador e implementar controlador para o sistema em malha fechada, além disso, o usuário pode incrementar outras funcionalidades.

<p align="center">
  <img height="60%" src="utils/arquitetura_firmware-1.png">
</p>



## Gêmeo Digital

Usa o sinal de saída (ângulo) para realizar a dinâmica do sinulador.
<br>

<p align="center">
  <img height="60%" src="utils/gemeo_digital.png">
</p>  
