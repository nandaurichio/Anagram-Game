<img width="1534" height="243" alt="anagram game banner" src="https://github.com/user-attachments/assets/b8a9b0e4-7495-4fbb-9329-785834cbdabf" />

<img width="1774" height="887" alt="banner 2" src="https://github.com/user-attachments/assets/4c7100cd-3239-4af8-8ec7-4f55948d4b66" />

### CÓDIGO EXPLICADO

### 1. Preparação e Estilo (Imports e Constantes)

```python
import random

# Códigos ANSI para o estilo retrô
RESET = "\033[0m"
# ... (outras constantes de cores)

```

* **`import random`**: Essa é a biblioteca padrão do Python que nos permite "sortear" coisas. Sem ela, o jogo seria sempre igual. Usamos para escolher a palavra secreta e para embaralhar as letras.
* **As Constantes de Cores**: Aqueles `\033[...]` são códigos de escape ANSI. Eles não são uma biblioteca, são comandos diretos que dizem ao terminal: *"Ei, terminal, mude a cor do que você imprimir a partir de agora"*. Isso torna o código **portável** (funciona em qualquer terminal sem precisar instalar nada externo).

### 2. O Banco de Dados

```python
anagram_db = { ... }

```

* Usamos um **dicionário**. É a estrutura perfeita aqui: a **chave** (`PYTHON`) é o que o usuário precisa acertar, e o **valor** (`"The programming language..."`) é a dica. Se você quiser adicionar 100 palavras novas, é só atualizar esse dicionário, sem precisar tocar na lógica do jogo.

### 3. As Funções de Apoio (O "Motor")

* **`print_banner()`**: É puramente cosmética. Serve para dar o tom de "sistema inicializado" e criar a experiência nostálgica que você gostou.
* **`scramble_word(word)`**: Aqui mora a lógica do desafio.
* Transformamos a string em lista (`list(word)`), pois strings são imutáveis no Python.
* `random.shuffle(chars)` mistura a lista.
* O `while True` é uma salvaguarda: garantimos que, se o sorteio acidentalmente gerar a palavra correta original, ele embaralha de novo até ser diferente.



### 4. A Lógica da Rodada (`play_one_round`)

Esta função contém o coração do jogo:

* **Sorteio**: `random.choice(list(anagram_db.keys()))` pega uma chave aleatória do dicionário.
* **Loop de Tentativas (`while attempts > 0`)**: É aqui que controlamos a "vida" do jogador.
* **Tratamento de Entrada (`.upper().strip()`)**: Isso é uma boa prática fundamental.
* `.upper()`: Se o usuário digitar "python" ou "Python", ele converte tudo para maiúsculo, evitando que a pessoa erre por causa de caixa alta/baixa.
* `.strip()`: Remove espaços em branco acidentais antes ou depois da palavra.



### 5. O Fluxo de Controle (`main`)

```python
def main():
    print_banner()
    while True:
        play_one_round()
        # ... lógica de reiniciar ...

```

* O `while True` aqui cria o **loop principal**. O jogo nunca "acaba" de verdade até o usuário decidir sair.
* **A verificação de saída**: Quando perguntamos `Do you want to play again?`, verificamos se o usuário digitou `y`. Se não for `y`, usamos o `break` para encerrar o loop do `while` e parar o programa.

### 6. O Ponto de Entrada

```python
if __name__ == "__main__":
    main()

```

* Isso é a "assinatura" de um programador experiente. Serve para dizer ao Python: *"Só execute a função `main()` se este arquivo for o arquivo principal que você abriu"*. Se um dia você importar esse arquivo dentro de outro projeto maior, esse código não vai rodar sozinho sem permissão.

### 7. Por que este design?
Optei por não utilizar bibliotecas externas complexas para manter o projeto "portável". O uso de Códigos ANSI permite criar uma interface com bordas e cores no terminal, mantendo o visual "MS-DOS" clássico que facilita o foco do usuário no desafio principal.

### 8. Autor
Desenvolvido por Fernanda Aurichio.
Projeto realizado como parte da jornada de aprendizado no Code in Place 2026.






