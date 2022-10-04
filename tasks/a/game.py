"""
Игра "Быки и коровы"

Компьютер загадывает строку из n цифр.
Каждый ход игрок вводит догадку - тоже строку из n цифр, и получает в ответ
- количество "быков" - верно угаданных цифр на своих позициях
- количество "коров" - верно угаданных цифр, поставленных на неверные позиции

Например, при загаданной строке "4271" и догадке "1234" есть
- 1 бык - цифра "2" на второй позиции
- 2 коровы - цифры "1" и "4"

Реализуйте вспомогательные функции для этой игры:
- [a] create_secret, score, validate
- [b] computer
- [*] сделайте так, чтобы игрок-компьютер опирался на результаты
  предыдущих ходов и пытался делать основанные на них ходы
    > вам придется заметно изменить структуру игры, чтобы
      иметь возможность сообщать игроку результаты по-разному
      в зависимости от того, человек это или компьютер
"""

from typing import Callable
import random


def create_secret(n: int) -> str:
    """
    Функция принимает длину загадываемого числа
    и возвращает случайную строку из различных(!) цифр указанной длины
    """
    #string = ""
    #for i in range(0, n):
    #    string += str(random.randint(1, 9))
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    string = ""
    random.shuffle(numbers)
    for i in range(0, n):
        string += str(numbers[i])
    return string


def score(secret: str, guess: str) -> tuple[int, int]:
    """
    Функция принимает загаданную строку и догадку игрока
    и возвращает пару из количества "быков" и количества "коров"
        > можно для каждой цифры от '0' до '9' посмотреть на позиции
          ее вхождения в secret и guess
        > для нахождения числа общих позиций может быть полезно
          воспользоваться структурой данных "множество" (set)
    """
    bulls, cows = 0, 0
    for i_guess in range(0, len(guess)):
        for i_secret in range(0, len(secret)):
            bulls += (secret[i_secret] == guess[i_guess] and i_secret == i_guess)
            cows += (secret[i_secret] == guess[i_guess] and i_secret != i_guess)
    
    return bulls, cows


def validate_len(n: int, guess: str) -> bool:
    """
    Функция принимает параметр игры - длину загаданной строки, и догадку игрока
    и возвращает, правда ли игрок ввел корректную догадку (строку длины n из цифр)
    """        
    return (len(guess) == n)


def validate_distinct(n: int, guess: str) -> bool:
    """
    check if distinct
    """        
    s = set()

    for i in range(0, n):
        s.add(guess[i])

    return (len(s) == n)


def computer_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, генерирующую догадки
    """

    def guess():
        pass

    return guess


def real_player(n: int) -> Callable:
    """
    Функция принимает параметр игры - длину загаданной строки,
    и возвращает ФУНКЦИЮ, получающую догадку от реального игрока
    """
    print(f'The secret word has length {n}')
    return input


def play(n: int, player: Callable):
    """
    Функция реализует процесс игры с заданной длиной слова и игроком
    """
    secret = create_secret(n)
    attempts = 0
    print(secret)
    while True:
        guess = player()
        attempts += 1
        if not validate_len(n, guess):
            print(f'Your guess should be a string of {n} digits')
            continue
        if not validate_distinct(n, guess):
            print('Your guess should be a string of distinct digits')
            continue
        bulls, cows = score(secret, guess)
        if bulls == n:
            print(f'Correct! You\'ve won in {attempts} guesses')
            break
        else:
            print(f'Your guess has {bulls=} and {cows=}')


if __name__ == '__main__':
    n = 4
    play(n, real_player(n))
