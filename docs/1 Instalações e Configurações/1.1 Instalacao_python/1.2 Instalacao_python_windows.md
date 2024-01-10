---
title: Tutorial - Instalando o Python 3.10 no Windows
author: Oséias Farias

---

<style>
        .tab {
            display: inline-block;
            margin-left: 40px;
        }
        .tab1 {
            display: inline-block;
            margin-left: 80px;
        }
</style>


<br>


Neste tutorial, vamos orientar você pelo processo de instalação do Python 3.10 no sistema operacional Windows. O Python é uma linguagem de programação poderosa e versátil, e a instalação no Windows é um processo relativamente simples.

#### Passo 1: Baixe o instalador do Python

Acesse o site oficial do Python em [python.org](https://www.python.org/), vá até a seção "Downloads" e clique em "View the full list of Python downloads". Escolha a versão mais recente do Python 3.10 para Windows e baixe o instalador executável (`.exe`).

#### Passo 2: Execute o instalador

Após o download, execute o arquivo `.exe` que você baixou. Na primeira tela do instalador, certifique-se de marcar a opção "Add Python 3.x to PATH" e clique em "Install Now". Isso adicionará o Python ao seu PATH, facilitando o uso do Python a partir do prompt de comando.

#### Passo 3: Aguarde a instalação

O instalador começará a instalar o Python em seu sistema. Aguarde o término do processo.

#### Passo 4: Verifique a instalação

Após a conclusão da instalação, abra o prompt de comando e digite:

```bash
python --version
```

Você deverá ver a versão do Python 3.10.

#### Passo 5: Instale o pip (gerenciador de pacotes do Python)

O pip é uma ferramenta essencial para instalar pacotes Python. Certifique-se de que o pip está instalado executando o seguinte comando no prompt de comando:

```bash
python -m ensurepip --default-pip
```

#### Conclusão

Agora você tem o Python 3.10 instalado no seu sistema Windows. Você pode começar a criar e executar seus scripts Python. Lembre-se de que o Python 3.10 inclui o pip, então você pode usar o pip para instalar pacotes adicionais conforme necessário para seus projetos.

