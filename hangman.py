# hangman.py
# Простая игра "Виселица" для терминала.
# Требования: Python 3.6+
# Запуск: python hangman.py

import random
import sys

WORDS = [
    "python", "компьютер", "программа", "разработка", "интернет",
    "игра", "школа", "университет", "музыка", "кино"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

MAX_WRONG = len(HANGMAN_PICS) - 1

def choose_word():
    return random.choice(WORDS).lower()

def display_state(wrong_guesses, guessed_letters, secret_word):
    print(HANGMAN_PICS[len(wrong_guesses)])
    print()
    # Покажем слово с подчеркиваниями
    revealed = " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])
    print("Слово: ", revealed)
    print()
    print("Ошибочные буквы: ", " ".join(wrong_guesses))
    print("Угаданные буквы: ", " ".join(sorted(guessed_letters)))
    print(f"Осталось попыток: {MAX_WRONG - len(wrong_guesses)}")
    print()

def get_guess(all_guesses):
    while True:
        guess = input("Введи букву или целиком слово: ").strip().lower()
        if not guess:
            print("Пустой ввод — попробуй ещё.")
            continue
        if guess in all_guesses:
            print("Эта буква/слово уже вводились — попробуй другое.")
            continue
        # Если введено более одного символа — считаем попыткой отгадать слово
        if len(guess) > 1 and not guess.isalpha():
            print("Только буквы пожалуйста.")
            continue
        if len(guess) == 1 and not guess.isalpha():
            print("Вводи букву (кириллица или латиница).")
            continue
        return guess

def play():
    secret = choose_word()
    wrong_guesses = []
    guessed_letters = set()
    all_guesses = set()

    print("=== Добро пожаловать в Виселицу! ===")
    print("Угадайте слово по буквам. Можно попытаться ввести целиком слово.")
    print()

    while True:
        display_state(wrong_guesses, guessed_letters, secret)

        # Проверка победы
        if all(ch in guessed_letters for ch in secret):
            print("Поздравляю! Вы отгадали слово:", secret)
            break
        if len(wrong_guesses) >= MAX_WRONG:
            print("К сожалению, вы проиграли. Было загаданно слово:", secret)
            break

        guess = get_guess(all_guesses)
        all_guesses.add(guess)

        if len(guess) == 1:
            # буква
            if guess in secret:
                guessed_letters.add(guess)
                print("Верно! Буква есть в слове.")
            else:
                wrong_guesses.append(guess)
                print("Нет, такой буквы нет.")
        else:
            # попытка угадать слово целиком
            if guess == secret:
                print("Ух ты! Вы отгадали слово целиком:", secret)
                break
            else:
                wrong_guesses.append(guess)
                print("Неправильное слово.")

        print()

def main():
    while True:
        play()
        ans = input("Играть ещё? (д/н): ").strip().lower()
        if ans and ans[0] == "д" or ans and ans[0] == "y":
            continue
        else:
            print("Спасибо за игру! Пока.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВыход. Пока!")
        sys.exit(0)

