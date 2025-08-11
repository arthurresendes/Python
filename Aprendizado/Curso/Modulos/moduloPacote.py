'''
Módulo -> É um único arquivo Python (.py) que pode conter funções, classes e variáveis para serem reutilizadas em outros arquivos.

Pacote -> É um diretório que contém um ou mais módulos (e/ou outros subpacotes). 
Normalmente contém um arquivo especial __init__.py para indicar ao Python que aquela pasta é um pacote.

Nas versões 2.x do Python, o arquivo __init__.py era obrigatório para que o diretório fosse reconhecido como pacote.
Nas versões 3.x, não é mais obrigatório (por causa dos namespace packages — PEP 420), 
mas ainda é muito utilizado para:
    - Tornar o pacote mais explícito e organizado
    - Definir o que será importado quando usar 'import pacote'
    - Inicializar variáveis ou configurar o pacote

O __init__.py pode reunir várias funcionalidades de diferentes módulos e expor apenas o que for necessário. 
Por exemplo, se você tiver vários "subjogos" como módulos separados, pode importar todos dentro do __init__.py para criar um "jogo principal".


Exemplos de importação:

# Importando um módulo inteiro
from pasta import arquivo
print(arquivo.funcao(argumentos))

# Importando apenas uma função de um módulo
from pasta.arquivo import funcao
print(funcao(argumentos))
'''