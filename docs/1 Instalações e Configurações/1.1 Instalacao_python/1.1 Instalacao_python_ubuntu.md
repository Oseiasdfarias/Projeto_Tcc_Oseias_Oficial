---
title: Tutorial - Instalando o Python 3.10 no Ubuntu
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


Neste tutorial, vamos guiar você através do processo de instalação do Python 3.10 no sistema operacional Ubuntu. O Python é uma linguagem de programação poderosa e versátil, e ter a versão mais recente pode proporcionar acesso a recursos e melhorias mais recentes. 

#### Passo 1: Atualize o sistema

Antes de começar a instalação, é sempre recomendável garantir que seu sistema esteja atualizado. Abra o terminal e execute os seguintes comandos:

```bash
sudo apt update
sudo apt upgrade
```

Digite a senha de administrador quando solicitado e aguarde o término do processo.

#### Passo 2: Instale as dependências

O Python requer algumas dependências que precisam ser instaladas. Execute o seguinte comando:

```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

#### Passo 3: Baixe e compile o Python 3.10

Agora, você está pronto para baixar e compilar o Python 3.10. Utilizaremos o `wget` para baixar o arquivo de origem e o `tar` para descompactar. Em seguida, compilaremos e instalaremos o Python. Execute os seguintes comandos:

```bash
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
tar -xf Python-3.10.0.tgz
cd Python-3.10.0
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

O processo de compilação pode levar algum tempo. Se ocorrerem erros durante a execução do `make`, certifique-se de que todas as dependências foram instaladas corretamente no Passo 2.

#### Passo 4: Verifique a instalação

Após a conclusão da instalação, verifique se o Python 3.10 foi instalado corretamente. Execute:

```bash
python3.10 --version
```

Você deverá ver a versão do Python 3.10.

#### Conclusão

Agora, você tem o Python 3.10 instalado no seu sistema Ubuntu. Lembre-se de que a instalação manual pode ter suas vantagens, mas também significa que você é responsável por manter as atualizações do Python. Se preferir, pode optar por instalar o Python 3.10 usando ferramentas como `pyenv` ou `deadsnakes`. Certifique-se de escolher o método que melhor atenda às suas necessidades.


<br/>