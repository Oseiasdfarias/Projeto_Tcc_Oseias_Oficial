\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{configuracoes/ufpa-fem-abntex2}[2019/01/07 v1.0]

% Repassa os parâmetros ao abntex2
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{abntex2}}

\PassOptionsToClass{%
% Opções da classe memoir
    12pt,                     % Tamanho da fonte
    a4paper,                  % Tamanho do papel.
    %sumario=tradicional,     % Seleciona o sumário tradicional
% Opções do pacote babel
    brazil,                   % Idioma do documento
}{abntex2}

\ProcessOptions\relax
\LoadClass{abntex2}
\RequirePackage[brazilian, hyperpageref]{backref}  % Produzir índice nas ref.
\hypersetup{linkcolor=black}
\RequirePackage{makeidx}      % Produzir índice remissivo de palavras
\RequirePackage{chngcntr}


% --------------------------------------------------------
% Configurações gerais
% --------------------------------------------------------

% Retira o espaço extra desnecessário nas frases
\frenchspacing
% Configurações do pacote backref usado sem a opção hyperpageref de backref
\renewcommand{\backrefpagesname}{Citado na(s) p\'agina(s):~}
% Texto padrão antes do número das páginas
\renewcommand{\backref}{}

% Define as listas de item compactas (sem espaçamento entre os itens)
%\setlist{noitemsep, topsep=0pt, parsep=0pt, partopsep=0pt}

% Define os textos da citação
\renewcommand*{\backrefalt}[4]
{%
    \ifcase #1
        Nenhuma cita\c{c}\~ao no texto.
    \or
        Citado na p\'agina #2.
    \else
        Citado #1 vezes nas p\'aginas #2.
    \fi
}
\usepackage{chngcntr}
\counterwithin{figure}{chapter}
\counterwithin{table}{chapter}
\counterwithin{equation}{chapter}
%\counterwithin{algorithm}{chapter}
% Define a numeração das equações de forma sequencial
%\counterwithout{equation}{chapter}

% ------------------------------------------------------
% PACOTES
%-------------------------------------------------------
\usepackage{subcaption}
\usepackage{caption}
\usepackage{varwidth}
\usepackage{rotating}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage[utf8]{inputenc}     % Codificação do documento
\usepackage[T1]{fontenc}        % Seleção de código de fonte
\usepackage{booktabs}           % Réguas horizontais em tabelas
\usepackage{color, colortbl}    % Controle das cores
\usepackage{float}    % Necess p/ tabelas/fig em amb multi-colunas
\usepackage{graphicx}           % Inclusão de gráficos e figuras
\usepackage{icomma}             % Uso de vírg em expre matemáticas
\usepackage{indentfirst}        % Indenta o 1parágrafo de cada seção
\usepackage{microtype}          % Melhor a justific do documento
\usepackage{multirow, array}    % Per tab com múltip linhas e col
\usepackage{subeqnarray}        % Permite subnumeração de equações
\usepackage{lastpage}           % P/ encontrar última página do doc
\usepackage{verbatim}           % Perm aprestar tex tal como escrito no documento, ainda que sejam comandos Latex
\usepackage{amsfonts, amssymb, amsmath}% Fontes e símbolos matemáticos
\usepackage[algoruled, portuguese]{algorithm2e}% Permite escrever algoritmos em português
%\usepackage[scaled]{helvet} % Usa a fonte Helvetica
\usepackage{lmodern}              % Usa a fonte Times
\usepackage[bottom]{footmisc}   % Mantém as notas de rodapé sempre na mesma posição
\usepackage{latexsym}           % Símbolos matemáticos
\usepackage{lscape}             % Permite páginas em modo "paisagem"

%\usepackage{picinpar}          % Dispor imagens em parágrafos
\usepackage{scalefnt}          % Permite redimensionar tamanho da fonte
\usepackage{subfig}            % Posicionamento de figuras
\usepackage{upgreek}           % Fonte letras gregas
%\usepackage{amsmath}
\usepackage{breqn}
\usepackage{setspace}
\usepackage{lineno}
\linenumbers
%Redefine a fonte para uma fonte similar a Arial (fonte Helvetica)
%\renewcommand*\familydefault{\sfdefault}

\usepackage{epigraph} %Epigrafe
\usepackage{adjustbox} %Ajusta a tabela as bordas
%\usepackage{showframe} %Mostra as bordas do documento


\usepackage{trivfloat}
\trivfloat{quadro}


\usepackage{setspace}
% ------------------------------------------------------------
% Comandos de dados
% -------------------------------------------------------------


% Comandos de dados - Departamento
\providecommand{\imprimirdepartamento}{}
\newcommand{\departamento}[1]{\renewcommand{\imprimirdepartamento}{#1}}
\providecommand{\imprimirdepartamentof}{}
\newcommand{\departamentof}[1]{\renewcommand{\imprimirdepartamentof}{#1}}

% Comandos de dados - Programa
\providecommand{\imprimirprograma}{}
\newcommand{\programa}[1]{\renewcommand{\imprimirprograma}{#1}}

% Comandos de dados - Subtítulo do trabalho
\providecommand{\imprimirsubtitulo}{}
\newcommand{\subtitulo}[1]{\renewcommand{\imprimirsubtitulo}{#1}}

% Comandos de dados - Instituição do orientador
\providecommand{\imprimirinstOrientador}{}
\newcommand{\instOrientador}[1]{\renewcommand{\imprimirinstOrientador}{#1}}

% Comandos de dados - Instituição do coorientador
\providecommand{\imprimirinstCoorientador}{}
\newcommand{\instCoorientador}[1]{\renewcommand{\imprimirinstCoorientador}{#1}}

% Comandos de dados -  Tipo de trabalho acadêmico (trabalho de conclusão de curso, tese, dissertação ou projeto de qualificação)
\providecommand{\imprimirprojeto}{}
\newcommand{\projeto}[1]{\renewcommand{\imprimirprojeto}{#1}}

% Comandos de dados - Título Acadêmico a ser alcançado (Bacharel)
\providecommand{\imprimirtituloAcademico}{}
\newcommand{\tituloAcademico}[1]{\renewcommand{\imprimirtituloAcademico}{#1}}

% Comandos de dados - Título em Inglês
\providecommand{\imprimirautorcitacao}{}
\newcommand{\autorcitacao}[1]{\renewcommand{\imprimirautorcitacao}{#1}}

% Comandos de dados - Nome autor para citação
\providecommand{\imprimirtitleabstract}{}
\newcommand{\titleabstract}[1]{\renewcommand{\imprimirtitleabstract}{#1}}

% Comandos de dados - Área de concentração com Rótulo
\newcommand{\imprimirareaconcentracaoRotulo}{\'Area de concentra\c{c}\~ao: }
\providecommand{\imprimirareaconcentracao}{}
\newcommand{\areaconcentracao}[1]{\renewcommand{\imprimirareaconcentracao}{#1}}

% Comandos de dados - linha de pesquisa
\newcommand{\imprimirlinhapesquisaRotulo}{Linha de pesquisa: }
\providecommand{\imprimirlinhapesquisa}{}
\newcommand{\linhapesquisa}[1]{\renewcommand{\imprimirlinhapesquisa}{#1}}

% Comandos de dados - Texto da folha de aprovação
%\providecommand{\imprimirtextopadraofolhadeaprovacao}{} 
%\newcommand{\textopadraofolhadeaprovacao}[1]{\renewcommand{\imprimirtextopadraofolhadeaprovacao}{#1}}
\providecommand{\imprimirdataaprovacao}{}
\newcommand{\dataaprovacao}[1]{\renewcommand{\imprimirdataaprovacao}{#1}}

%\providecommand{\imprimirconceito}{}
%\newcommand{\conceito}[1]{\renewcommand{\imprimirconceito}{#1}}

\providecommand{\imprimirnomePrimeiromembro}{}
\newcommand{\nomePrimeiromembro}[1]{\renewcommand{\imprimirnomePrimeiromembro}{#1}}
\providecommand{\imprimirinstPrimeiromembro}{}
\newcommand{\instPrimeiromembro}[1]{\renewcommand{\imprimirinstPrimeiromembro}{#1}}

\providecommand{\imprimirnomeSegundomembro}{}
\newcommand{\nomeSegundomembro}[1]{\renewcommand{\imprimirnomeSegundomembro}{#1}}
\providecommand{\imprimirinstSegundomembro}{}
\newcommand{\instSegundomembro}[1]{\renewcommand{\imprimirinstSegundomembro}{#1}}

\providecommand{\imprimirnomeTerceiromembro}{}
\newcommand{\nomeTerceiromembro}[1]{\renewcommand{\imprimirnomeTerceiromembro}{#1}}
\providecommand{\imprimirinstTerceiromembro}{}
\newcommand{\instTerceiromembro}[1]{\renewcommand{\imprimirinstTerceiromembro}{#1}}

% Comandos de dados - Logomarca da instituição
\providecommand{\imprimirlogoinstituicao}{}
\newcommand{\logoinstituicao}[2]{\renewcommand{\imprimirlogoinstituicao}{\includegraphics[width={#1}]{#2}}}


% =======================================
% Estilo de elementos
% =======================================

% Elementos pré-textuais
\renewcommand{\pretextual}
{%
    \pagenumbering{arabic}
    \aliaspagestyle{chapter}{empty}
    \pagestyle{empty}
    \aliaspagestyle{cleared}{empty}
    \aliaspagestyle{part}{empty}
}

% Configura layout para elementos textuais
\renewcommand{\textual}
{%
    %\pagenumbering{arabic} % A numeração das páginas é em algarismos arábicos, inciando em 1
    \pagestyle{simple}
    \pagestyle{abntheadings}
    \aliaspagestyle{chapter}{abntchapfirst}
    \nouppercaseheads
    \bookmarksetup{startatroot}
}

% Configura layout para elementos pós-textuais
\renewcommand{\postextual}
{%
    \chapterstyle{abnt}
    \phantompart
}


% -------------------------------------------------------
% Objetos flutuantes
% -------------------------------------------------------

% Comando que trata a fonte nos objetos flutuantes
\renewcommand{\fonte}[1]
{%
   \begin{onehalfspacing}\par\end{onehalfspacing}
    \centering\footnotesize{Fonte: #1}
}


% Comando que trata as notas nos objetos flutuantes
\renewcommand{\nota}[1]
{%
    \begin{SingleSpacing}\par\end{SingleSpacing}
    \begin{tabular}{l p{.85\textwidth}}%
        Nota: & #1
    \end{tabular}
}

% ----------------------------------------------------------
% Parágrafos
%------------------------------------------------------------

% Tamanho da indentação do parágrafo
\setlength{\parindent}{1.3cm}

% Espaçamento entre um parágrafo e outro
\setlength{\parskip}{1.5pt}

% ==========================
% Fontes
% ==========================

% Redefinição de fontes
\renewcommand{\ABNTEXchapterfont}{\normalfont}
\renewcommand{\ABNTEXchapterfontsize}{\normalsize\bfseries}

\renewcommand{\ABNTEXpartfont}{\normalfont}
\renewcommand{\ABNTEXpartfontsize}{\ABNTEXchapterfontsize}

\renewcommand{\ABNTEXsectionfont}{\normalfont}
\renewcommand{\ABNTEXsectionfontsize}{\normalsize\bfseries}

\renewcommand{\ABNTEXsubsectionfont}{\normalfont}
\renewcommand{\ABNTEXsubsectionfontsize}{\normalsize}

\renewcommand{\ABNTEXsubsubsectionfont}{\normalfont}
\renewcommand{\ABNTEXsubsubsectionfontsize}{\normalsize}

\renewcommand{\ABNTEXsubsubsubsectionfont}{\normalfont}
\renewcommand{\ABNTEXsubsubsubsectionfontsize}{\normalsize}

% =================
% Sumário
% =================

% Travessão no sumário para apêndices e anexos
%\renewcommand{\cftchapteraftersnum}{\hfill\textendash\hfill}

% Insere espaço entre os itens do sumário de diferentes capítulos
%\setlength{\cftbeforechapterskip}{1.0em \@plus\p@}

% ================================================
% Listas
% ===============================================

% Define os títulos das listas
\addto\captionsbrazil{%
% Ajusta nomes padrões do babel
    \renewcommand{\listadesiglasname}{LISTA DE SIGLAS}
    \renewcommand{\listadesimbolosname}{LISTA DE S\'{I}MBOLOS}
    \renewcommand{\listfigurename}{LISTA DE ILUSTRAÇÕES}
    \renewcommand{\listtablename}{LISTA DE TABELAS}
    \renewcommand{\indexname}{\'{I}NDICE REMISSIVO}
	\renewcommand{\bibname}{REFER\^{E}NCIAS}
% Ajusta nomes usados com a macro \autoref
    \renewcommand{\pageautorefname}{p\'agina}
    \renewcommand{\sectionautorefname}{Se\c{c}\~ao}
    \renewcommand{\subsectionautorefname}{Subse\c{c}\~ao}
    \renewcommand{\subsubsectionautorefname}{Subsubse\c{c}\~ao}
    \renewcommand{\paragraphautorefname}{Subse\c{c}\~ao}
}

% Cria a lista de quadros
%\newcommand{\listofquadrosname}{Lista de Quadros}
%\newcommand{\quadroname}{Quadro}
%%\newfloat[chapter]{quadro}{loq}{\quadroname}
%\newlistof{listofquadros}{loq}{\listofquadrosname}
%\newlistentry{quadro}{loq}{0}
%\counterwithout{quadro}{chapter}
%\renewcommand{\cftquadroname}{\quadroname\space}
%\renewcommand*{\cftquadroaftersnum}{\hfill--\hfill}


%====================================================
% REFERÊNCIAS
%====================================================

\usepackage[
alf,
abnt-emphasize=bf,
bibjustif,
recuo=0cm,
abnt-url-package=url,       % Utiliza o pacote url
abnt-refinfo=yes,           % Utiliza o estilo bibliográfico abnt-refinfo
abnt-etal-cite=3,
abnt-etal-list=0,
abnt-thesis-year=final
]{abntex2cite}     % Config as citações bib conforme a norma ABNT

%=============================================
%Configurações do pdf
%=============================================

%\include{configuracoes/pacotes}
\makeatletter
\hypersetup{%
	portuguese,
	colorlinks=true,   % true: "links" coloridos; false: "links" em caixas de texto
	linkcolor=black,    % Define cor dos "links" internos
	citecolor=black,    % Define cor dos "links" para as referências bibliográficas
	filecolor=black,    % Define cor dos "links" para arquivos
	urlcolor=black,     % Define a cor dos "hiperlinks"
	breaklinks=true,
	pdftitle={\@title},
	pdfauthor={\@author},
	pdfkeywords={abnt, latex, abntex, abntex2}
}
\makeatother

% REDEFINIÇÃO DE LABELS---------------------------------------
\renewcommand{\algorithmautorefname}{Algoritmo}
\def\equationautorefname~#1\null{Equa\c c\~ao~(#1)\null}

% CRIA ÍNDICE REMISSIVO----------------------------------------
\makeindex

% HIFENIZAÇÃO DE PALAVRAS QUE NÃO ESTÃO NO DICIONÁRIO----------
\hyphenation{%
	qua-dros-cha-ve
	Kat-sa-gge-los
}