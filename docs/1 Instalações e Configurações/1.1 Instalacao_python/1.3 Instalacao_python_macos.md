---
title: Tutorial - Instalando o Python 3.10 no macOS
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


Neste tutorial, vamos guiar você pelo processo de instalação do Python 3.10 no sistema operacional macOS. O Python é uma linguagem de programação poderosa e versátil, e a instalação no macOS é relativamente simples.


#### Passo 1: Verifique a versão do macOS

Certifique-se de estar usando pelo menos o macOS 10.9 (Mavericks) ou posterior, pois as versões mais antigas podem ter complicações durante a instalação.

#### Passo 2: Instale o Homebrew (se ainda não estiver instalado)

O Homebrew é um gerenciador de pacotes que facilita a instalação de software no macOS. Abra o Terminal e execute o seguinte comando para instalar o Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Siga as instruções que aparecem no Terminal para concluir a instalação.

#### Passo 3: Instale o Python 3.10 com o Homebrew

Agora que o Homebrew está instalado, use-o para instalar o Python 3.10. No Terminal, execute os seguintes comandos:

```bash
brew update
brew install python@3.10
```

#### Passo 4: Adicione o Python ao PATH

Adicione o Python 3.10 ao seu PATH executando o seguinte comando:

```bash
echo 'export PATH="/usr/local/opt/python@3.10/bin:$PATH"' >> ~/.zshrc
```

Se você estiver usando o Bash, substitua `~/.zshrc` por `~/.bash_profile`.

#### Passo 5: Verifique a instalação

Feche e reabra o Terminal e digite o seguinte comando para verificar se o Python 3.10 foi instalado corretamente:

```bash
python3.10 --version
```

Você deverá ver a versão do Python 3.10.

#### Conclusão

Agora você tem o Python 3.10 instalado no seu sistema macOS. Pode começar a desenvolver e executar seus scripts Python. Lembre-se de que o Python 3.10 inclui o pip, então você pode usar o pip para instalar pacotes adicionais conforme necessário para seus projetos.


<br/>