<h1 align="center">Calculadora Simples</h1>

<div align="center">
Uma calculadora simples feita com Python e PySide6.
Realiza somente equações simples com a lógica de número da esquerda, operação, número da direita.
O intuito deste projeto foi aplicar os conhecimentos de POO (programação orientada a objeto) e trabalhar com interface gráfica usando PySide6 (sem o QtDesigner)
</div>

###

<div align="center">
<img src="https://github.com/VictorAp12/Calculadora-Simples/assets/148372228/b77e244d-4ae8-4205-ae3c-20684ba65c87" />
</div>

###
A calculadora também funciona com inputs do teclado como na lista a seguir:
- teclas Enter, Igual = equal (realiza o cálculo);
- teclas D, Delete, Backspace = backspace (apaga um caractere por clique);
- teclas C, Esc = clear (apaga tudo, reinicia o cálculo);
- tecla + = plus (operador mais);
- tecla - = minus (operador menos);
- tecla * = multiply (operador para multiplicação);
- tecla / = slash (operador para divisão);
- tecla P = pow (operador para potenciação);


## Conteúdo:
- [Requisitos](#requisitos)
- [Instalação](#instalacao)


## Requisitos
- Python 3.8 ou acima
- Sistema Windows 64 bits (caso for usar o executável ao invés de rodar o projeto)

## Instalação

  ### Como executável do windows

  Simplesmente baixe o arquivo.exe através deste link e comece a usar a aplicação: [Download Calculadora Simples](https://github.com/VictorAp12/Calculadora-Simples/blob/main/Calculadora%20Simples.exe)

  ### Como um projeto Python

  - Baixe o projeto como zip ou usando gitclone https://github.com/VictorAp12/Calculadora-Simples.git

  - Crie o ambiente virtual na pasta do projeto:
    ```bash
    python -m venv venv
    ```

  - Ative o ambiente virtual na pasta do projeto:
    ```bash
    venv\Scripts\activate
    ```

  - Instale as dependencias do projeto:
    ```bash
    pip install -r requirements.txt
    ```

  - Execute o main.py:
    ```bash
    python -m main.py
    ```
