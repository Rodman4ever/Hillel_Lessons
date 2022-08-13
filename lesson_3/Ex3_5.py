import random
guesses_made = 0
number = random.randint(1, 10)
while guesses_made < 3:
    _guess_ = int(input('Введи число: '))
    guesses_made += 1
    if _guess_ < number:
        print('Твое число меньше того, что я загадал.')
    if _guess_ > number:
        print('Твое число больше загаданного мной.')
    if _guess_ == number:
        print('You won!')
        break
else:
    print('You lose!')
