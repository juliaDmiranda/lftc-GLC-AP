# Trabalho de Implementação
## LFTC - Conversão de Automato para Gramatica
Este repositório é a implementação de um trabalho de Linguagens Formais e Teoria da Computação do curso de Ciência da Computação na UFF-PURO no período de 2022.1.
<br>
O grupo composto por Gabriel Ribeiro(@Tetr4k), Júlia Miranda(@juliaDmiranda) e Raphael Yoshiki(@RaphaelYoshiki) deve implementar um programa que converta uma gramática livre de contexto(GLC) em um autômato de pilha(AP).

## Uso

Para usar o programa tenha arquivos texto criados com as gramáticas que você quer converter, sendo:

* A um símbolo não terminal;
* B qualquer cadeia;
* @ uma cadeia vazia;

no seguinte formato:

```
  A -> B
  A -> @
```

Em seguida, no seu sistema operacional preferido, abra o terminal ou prompt de comando, va para o diretório onde está o programa e digite:

```
  py converte.py (gramatica1.txt) [(gramatica2.txt), ..., (gramaticaN.txt)]
```

O programa irá converter cada gramática e exibir na tela a gramática e seu respectivo autômato.
