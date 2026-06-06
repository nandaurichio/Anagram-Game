# jogo.py
import random
from dados import anagram_db

# --- Códigos ANSI para o estilo retrô ---
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[36m"
WHITE = "\033[97m"

def print_banner():
    """Exibe o cabeçalho retrô."""
    print(f"{CYAN}" + "+" + "-" * 50 + "+")
    print(f"|{WHITE}   WELCOME to the ANAGRAM GAME!                     {CYAN}|")
    print(f"|{WHITE}   System initialized...                            {CYAN}|")
    print(f"{CYAN}" + "+" + "-" * 50 + f"{RESET}\n")

def scramble_word(word):
    """Embaralha a palavra garantindo que não seja igual à original."""
    chars = list(word)
    while True:
        random.shuffle(chars)
        scrambled = "".join(chars)
        if scrambled != word:
            return scrambled

def play_one_round():
    """Executa uma rodada do jogo."""
    word = random.choice(list(anagram_db.keys()))
    clue = anagram_db[word]
    scrambled = scramble_word(word)
    
    attempts = 3
    
    print(f"{GREEN}[INFO]{RESET} Current Task: Unscramble the code.")
    print(f"{CYAN}" + "-" * 55)
    print(f"{BOLD}CLUE:{RESET} {clue}")
    print(f"{BOLD}WORD:{RESET} {GREEN}{scrambled}{RESET}")
    print(f"{CYAN}" + "-" * 55)
    
    while attempts > 0:
        guess = input(f"{CYAN}ENTER_GUESS ({attempts} left) > {RESET}").upper().strip()
        
        if guess == word:
            print(f"\n{GREEN}*** Correct! The word was {word}. ***{RESET}")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"{RED}!!! Incorrect. Try again. !!!{RESET}")
            else:
                print(f"\n{RED}!!! Game Over. The word was {word}. !!!{RESET}")
                return False

def main():
    """Função principal que controla o fluxo do jogo."""
    print_banner()
    while True:
        play_one_round()
        
        # Pergunta se quer jogar novamente
        again = input(f"\n{CYAN}Do you want to play again? (y/n) > {RESET}").lower().strip()
        if again != 'y':
            print(f"\n{WHITE}Thanks for playing! Come back soon!{RESET}")
            break
        print(f"\n{CYAN}--- Restarting System... ---\n{RESET}")

if __name__ == "__main__":
    main()