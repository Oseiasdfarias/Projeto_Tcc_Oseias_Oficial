%%-----------------------------------------------------------------------------
%% The LaTeX Project Public License 
%%-----------------------------------------------------------------------------
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%   http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2005/12/01 or later.
%%
%% Further information about abnTeX2 are available on http://www.abntex.net.br/
%%------------------------------------------------------------------------------


% -----------------------------------------------------------------------------
% Universidade Federal do Pará - UFPA
% Faculdade de Engenharia Mecânica - FEM
% Customização da classe abnTeX2 (http://www.abntex.net.br/) para as normas da do 
%
%% Baseado em:
% Projeto: http://tcc.tsi.gp.utfpr.edu.br/paginas/modelos-latex-da-utfpr
% De:       Diego Marczal e 
% 	          Michael Vornes <https://github.com/mvornes>
%
%------------------------------------------------------------------------------
% Codificação: UTF-8
% LaTeX:  abnTeX2          
% -----------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{configuracoes/ufpa-ppgem-abntex2}[2019/01/07 v1.0]

% Repassa os parâmetros ao abntex2
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{abntex2}}

\PassOptionsToClass{%
% Opções da classe memoir
    12pt,                     % Tamanho da fonte
    a4paper,                  % Tamanho do papel.
    %sumario=tradicional,      % Seleciona o sumário tradicional
% Opções do pacote babel
    brazil,                   % Idioma do documento
}{abntex2}

\ProcessOptions\relax
\LoadClass{abntex2}

\RequirePackage[brazilian, hyperpageref]{backref}       % Produzir índice nas referências
\hypersetup{linkcolor=black}
\RequirePackage{makeidx}                                % Produzir índice remissivo de palavras
\RequirePackage{chngcntr}

% -----------------------------------------------------------------------------
% Configurações gerais
% -----------------------------------------------------------------------------

% Retira o espaço extra desnecessário nas frases
\frenchspacing

% Configurações do pacote backref usado sem a opção hyperpageref de backref
\renewcommand{\backrefpagesname}{Citado na(s) p\'agina(s):~}

% Texto padrão antes do número das páginas
\renewcommand{\backref}{}

% Define as listas de item compactas (sem espaçamento entre os itens)
\setlist{noitemsep, topsep=0pt, parsep=0pt, partopsep=0pt}

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

% -----------------------------------------------------------------------------
% Comandos de dados
% -----------------------------------------------------------------------------

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

% Comandos de dados - Título Acadêmico a ser alcançado (Bacharel, Tecnólogo)
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

\providecommand{\imprimirconceito}{}
\newcommand{\conceito}[1]{\renewcommand{\imprimirconceito}{#1}}

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

% -----------------------------------------------------------------------------
% Estilo de elementos
% -----------------------------------------------------------------------------

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
	%\pagestyle{abntheadings}
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

% -----------------------------------------------------------------------------
% Objetos flutuantes
% -----------------------------------------------------------------------------

% Comando que trata a fonte nos objetos flutuantes
\renewcommand{\fonte}[1]
{%
    \begin{SingleSpacing}\par\end{SingleSpacing}
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

% -----------------------------------------------------------------------------
% Parágrafos
% -----------------------------------------------------------------------------

% Tamanho da indentação do parágrafo
\setlength{\parindent}{1.5cm}

% Espaçamento entre um parágrafo e outro
%\setlength{\parskip}{0.0cm}

% -----------------------------------------------------------------------------
% Fontes
% -----------------------------------------------------------------------------

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

% -----------------------------------------------------------------------------
% Sumário
% -----------------------------------------------------------------------------

% Travessão no sumário para apêndices e anexos
%\renewcommand{\cftchapteraftersnum}{\hfill\textendash\hfill}

% Insere espaço entre os itens do sumário de diferentes capítulos
%\setlength{\cftbeforechapterskip}{1.0em \@plus\p@}

% -----------------------------------------------------------------------------
% Listas
% -----------------------------------------------------------------------------

% Define os títulos das listas
\addto\captionsbrazil{%
% Ajusta nomes padrões do babel
    \renewcommand{\listadesiglasname}{LISTA DE SIGLAS}
    \renewcommand{\listadesimbolosname}{LISTA DE S\'{I}MBOLOS}
    \renewcommand{\listfigurename}{LISTA DE FIGURAS}
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
\newcommand{\listofquadrosname}{Lista de Quadros}
\newcommand{\quadroname}{Quadro}
\newfloat[chapter]{quadro}{loq}{\quadroname}
\newlistof{listofquadros}{loq}{\listofquadrosname}
\newlistentry{quadro}{loq}{0}
\counterwithout{quadro}{chapter}
\renewcommand{\cftquadroname}{\quadroname\space}
\renewcommand*{\cftquadroaftersnum}{\hfill--\hfill}

% -----------------------------------------------------------------------------
% Capa
% -----------------------------------------------------------------------------
\makeatletter
\renewcommand{\imprimircapa}{
    \begin{capa}
        \begin{center}
		
		\begin{figure}[h]
			\center
				\imprimirlogoinstituicao
		\end{figure}

		\begin{SingleSpacing}
					
            		\large\MakeUppercase{\imprimirinstituicao} \\
	    		\abntex@ifnotempty{\imprimirdepartamento}
            		{
                		\MakeUppercase{\imprimirdepartamento} \\
            		}
				\abntex@ifnotempty{\imprimirdepartamentof}
            		{
                		\MakeUppercase{\imprimirdepartamentof} \\
            		}
           		\large\MakeUppercase{\imprimirprograma} \\
		\end{SingleSpacing}
        \end{center}
        \vspace{60pt}
	\begin{center}
		\large\MakeUppercase{\imprimirautor}\\
	\end{center}
	\vspace{60pt} %120
        \begin{center}
            \ABNTEXchapterfont\large\MakeUppercase{\imprimirtitulo}
            \abntex@ifnotempty{\imprimirsubtitulo}
	    {%
                {\ABNTEXchapterfont: }{\large{\imprimirsubtitulo}}
            }
        \end{center}
	\vspace{120pt}
%	\begin{center}
%		\large\MakeUppercase{\imprimirprojeto}
%	\end{center}
	\vfill
        \begin{center}
		\begin{SingleSpacing}
            		\large\MakeUppercase{\imprimirlocal}\\
            		\large\MakeUppercase{\imprimirdata}
		\end{SingleSpacing}
    	\end{center}

    \end{capa}

}
\makeatother

% -----------------------------------------------------------------------------
% Folha de rosto
% -----------------------------------------------------------------------------
\makeatletter
\renewcommand{\folhaderostocontent}
{%

    %\begin{figure}[h]
	%		\center
	%			\includegraphics[width=2.1cm]{ufpa}
	%	\end{figure}

%	\begin{center}
%	\begin{SingleSpacing}
%	\large\MakeUppercase{\imprimirinstituicao} \\
%	{
%		\MakeUppercase{\imprimirdepartamento} \\
%	}
%	\large\MakeUppercase{\imprimirprograma} \\
%\end{SingleSpacing}
%\vspace{60pt}
%\end{center}
\begin{center}
	\large\MakeUppercase{\imprimirautor}\\
\end{center}	
		
		
		
    \setcounter{page}{1}
    %\begin{center}
    %    \large\MakeUppercase{\imprimirautor}\\
    %\end{center}

    \vspace*{60pt}%{96pt}

    \begin{center}
        \ABNTEXchapterfont\large\MakeUppercase{\imprimirtitulo}
        \abntex@ifnotempty{\imprimirsubtitulo}
	{%
        	{\ABNTEXchapterfont: }{\large{\imprimirsubtitulo}}
        }
    \end{center}

    \vspace*{20pt}

    \abntex@ifnotempty{\imprimirpreambulo}
    {%
        \SingleSpacing
        \begin{tabular}{p{.25\textwidth}p{.13\textwidth}p{.44\textwidth}}
            & \multicolumn{2}{p{.6\textwidth}}{\small\hyphenpenalty=10000{\imprimirpreambulo}} \\ & & \\
            \abntex@ifnotempty{\imprimirareaconcentracao}
            {%
                & \multicolumn{2}{p{.6\textwidth}}{\small\hyphenpenalty=10000{\imprimirareaconcentracaoRotulo\imprimirareaconcentracao}} \\ & & \\
            }
            \abntex@ifnotempty{\imprimirlinhapesquisa}
            {%
                & \multicolumn{2}{p{.6\textwidth}}{\small\hyphenpenalty=10000{\imprimirlinhapesquisaRotulo\imprimirlinhapesquisa}} \\ & & \\
            }
            \abntex@ifnotempty{\imprimirorientador}
            {%
                & \small\imprimirorientadorRotulo & \imprimirorientador \\
                & & \small\imprimirinstOrientador \\ & & \\
            }
            \abntex@ifnotempty{\imprimircoorientador}
            {%
                & \small\imprimircoorientadorRotulo & \imprimircoorientador \\
                & & \small\imprimirinstCoorientador
            }
        \end{tabular}
    }

    \vspace*{\fill}

    \begin{center}
	\begin{SingleSpacing}
            \large\MakeUppercase{\imprimirlocal}\\
            \large\MakeUppercase{\imprimirdata}
	\end{SingleSpacing}
    \end{center}
}
\makeatother

% -----------------------------------------------------------------------------
%% Folha de aprovação
%% -----------------------------------------------------------------------------
%\makeatletter
%\newcommand{\imprimirfolhadeaprovacao}
%{%
%	\begin{center}
%		\large\MakeUppercase{\imprimirautor}\\
%	\end{center}	
%		
%	\vspace*{60pt}%{96pt}
%    \begin{folhadeaprovacao}
%        \vspace*{\fill}
%
%        \begin{tabular}{p{.45\textwidth}p{.45\textwidth}}
%            %& \imprimirtextopadraofolhadeaprovacao \\
%            & \insert{estrutura\pre-textuais\folhaaprova} \\
%        \end{tabular}
%
%        \vspace*{\fill}
%    \end{folhadeaprovacao}
%}
%\makeatother
% ----------------------------------------


\makeatletter
\newcommand{\imprimirfolhadeaprovacao}
{%
    \begin{center}
        \large\MakeUppercase{\imprimirautor}\\
    \end{center}

    \vspace*{\fill}

    \begin{center}
        \ABNTEXchapterfont\large\MakeUppercase{\imprimirtitulo}
        \abntex@ifnotempty{\imprimirsubtitulo}
	{%
        	{\ABNTEXchapterfont: }{\large{\imprimirsubtitulo}}
        }
    \end{center}

    \vspace*{\fill}

    \abntex@ifnotempty{\imprimirpreambulo}
    {%
        \SingleSpacing
        \begin{tabular}{p{.25\textwidth}p{.13\textwidth}p{.44\textwidth}}
            & \multicolumn{2}{p{.6\textwidth}}{\small\hyphenpenalty=10000{\imprimirpreambulo}}

        \end{tabular}
    }

    \vspace*{\fill}
    
    \noindent
    DATA DE APROVA\c{C}\~AO: \imprimirdataaprovacao  \\ \\
    CONCEITO: \imprimirconceito
    
    \vspace*{\fill}

    %\assinatura{\imprimirorientador \\ Orientador - \imprimirinstOrientador}
    \assinatura{\imprimirorientador \\ Orientador - FEM/ITEC/UFPA}
    \assinatura{\imprimirnomePrimeiromembro  \\ Membro - \imprimirinstPrimeiromembro}
    \assinatura{\imprimirnomeSegundomembro  \\ Membro - \imprimirinstSegundomembro}
   % \assinatura{\imprimirnomeTerceiromembro  \\ Membro - \imprimirinstTerceiromembro}              % ocultar ou não dependendo do numero de professores na banca
    
    \begin{center}
	\begin{SingleSpacing}
            \MakeUppercase{\imprimirlocal}\\
            \MakeUppercase{\imprimirdata}
	\end{SingleSpacing}
    \end{center}
}
\makeatother



% ----------------------------------------
%% -----------------------------------------------------------------------------
% Dedicatória
% -----------------------------------------------------------------------------
\renewenvironment{dedicatoria}[1][]
{%
    \ifthenelse{\equal{#1}{}}{%
        \PRIVATEbookmarkthis{\dedicatorianame}
    }{\pretextualchapter{#1}}

    \vspace*{\fill}

    \begin{flushright}
        \begin{minipage}{.5\textwidth}
            \begin{SingleSpacing}
                \setlength\parindent{0pt}
                \setlength\parskip{12pt}
}
{%
            \end{SingleSpacing}
        \end{minipage}
    \end{flushright}
}

% -----------------------------------------------------------------------------
% Epígrafe
% -----------------------------------------------------------------------------
\renewenvironment{epigrafe}[1][]
{%
    \ifthenelse{\equal{#1}{}}
    {%
        \PRIVATEbookmarkthis{\epigraphname}
    }{\pretextualchapter{#1}}

    \vspace*{\fill}

    \begin{flushright}
        \begin{minipage}{.5\textwidth}
            \begin{SingleSpacing}
                \setlength\parindent{0pt}
                \setlength\parskip{12pt}
}
{%
            \end{SingleSpacing}
        \end{minipage}
    \end{flushright}
}


%------------------------------------------------------
%Pacotes 

% REFERÊNCIAS------------------------------------------------------------------
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
]{abntex2cite}                  % Configura as citações bibliográficas conforme a norma ABNT

% PACOTES----------------------------------------------------------------------
\usepackage{subcaption}
\usepackage{caption}
\usepackage{varwidth}
\usepackage{rotating}
\usepackage{hyperref}
\usepackage{amsmath}

\usepackage[utf8]{inputenc}                                 % Codificação do documento
\usepackage[T1]{fontenc}                                    % Seleção de código de fonte
\usepackage{booktabs}                                       % Réguas horizontais em tabelas
\usepackage{color, colortbl}                                % Controle das cores
\usepackage{float}                                          % Necessário para tabelas/figuras em ambiente multi-colunas
\usepackage{graphicx}                                       % Inclusão de gráficos e figuras
\usepackage{icomma}                                         % Uso de vírgulas em expressões matemáticas
\usepackage{indentfirst}                                    % Indenta o primeiro parágrafo de cada seção
\usepackage{microtype}                                      % Melhora a justificação do documento
\usepackage{multirow, array}                                % Permite tabelas com múltiplas linhas e colunas
\usepackage{subeqnarray}                                    % Permite subnumeração de equações
\usepackage{lastpage}                                       % Para encontrar última página do documento
\usepackage{verbatim}                                       % Permite apresentar texto tal como escrito no documento, ainda que sejam comandos Latex
\usepackage{amsfonts, amssymb, amsmath}                     % Fontes e símbolos matemáticos
\usepackage[algoruled, portuguese]{algorithm2e}             % Permite escrever algoritmos em português
%\usepackage[scaled]{helvet}                                % Usa a fonte Helvetica
%\usepackage{times}                                          % Usa a fonte Times
%\usepackage{palatino}                                      % Usa a fonte Palatino
\usepackage{lmodern}                                       % Usa a fonte Latin Modern
\usepackage[bottom]{footmisc}                               % Mantém as notas de rodapé sempre na mesma posição
\usepackage{ae, aecompl}                                    % Fontes de alta qualidade
\usepackage{latexsym}                                       % Símbolos matemáticos
\usepackage{lscape}                                         % Permite páginas em modo "paisagem"

%\usepackage{picinpar}                                      % Dispor imagens em parágrafos
%\usepackage{scalefnt}                                      % Permite redimensionar tamanho da fonte
%\usepackage{subfig}                                        % Posicionamento de figuras
%\usepackage{upgreek}                                       % Fonte letras gregas
%\usepackage{amsmath}
%\usepackage{breqn}

% Redefine a fonte para uma fonte similar a Arial (fonte Helvetica)
%\renewcommand*\familydefault{\sfdefault}


%------------------------------------------------------
%Configurações do pdf

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

% REDEFINIÇÃO DE LABELS---------------------------------------------------------
\renewcommand{\algorithmautorefname}{Algoritmo}
\def\equationautorefname~#1\null{Equa\c c\~ao~(#1)\null}

% CRIA ÍNDICE REMISSIVO---------------------------------------------------------
\makeindex

% HIFENIZAÇÃO DE PALAVRAS QUE NÃO ESTÃO NO DICIONÁRIO---------------------------
\hyphenation{%
	qua-dros-cha-ve
	Kat-sa-gge-los
}