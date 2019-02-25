"""
UI
"""

from random import randint
import os
import madlib2repo

    
def main_menu():
    usin = input('\nwhat would you like to do? \n'
                    '1) Fill out a madlib \n'
                    '2) Read madlibs \n'
                    '3) Exit \n'
                    '> ')
    if usin == '1':
        fill_out_menu()
    elif usin == '2':
        if len(madlib2repo.filled) > 0:
            os.system('cls||clear')
            print(madlib2repo.filled)
        else:
            print('\nno madlibs have been completed yet \n\n')
    elif usin == '3':
        exit(0)
    else:
        print('invalid input')
        pass

def fill_out_menu():
    mltype = input('\n1) Do a random madlib \n'
                        '2) Choose a madlib \n'
                        '3) Back \n'
                        '> ')
    if mltype == '1':
        random_madlib()
    elif mltype == '2':
        choose_madlib()
    elif mltype == '3':
        os.system('cls||clear')
        main_menu()
    else:
        print('invalid input')
        pass

def random_madlib():
    madlib2repo.Madlib.review()
    x = randint(1, 7)
    if x == 1:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print("\nThe little blank (10 blanks)")
        a = input('noun: ')
        b = input('adjective: ')
        c = input('past tense verb: ')
        d = input('verb: ')
        e = input('adjective: ')
        f = input('verb: ')
        g = input('adjective: ')
        h = input('quote: ')
        i = input('past tense verb: ')
        j = input('noun: ')
        madlib2repo.TheLittleBlank.save_madlib(a, b, c, d, e, f, g, h, i, j)
        print(f'\nOnce upon a time, there was a little {a}. This {a} was very {b} and never {c}. One day, their mother \n' \
                f'told them to {d}, but the {e} little {a} didnt want to {d}! Instead, they decided to {f}! When their {g} mother \n' \
                f'learned of their disobedience, she told them "{h}" and {i} them without any {j}. From that day forth, \n' \
                f'the {b} little {a} never disobeyed their mother to {f} again')
    elif x == 2:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print("\nThe blank who liked to blank (9 blanks)")
        a = input('verb: ')
        b = input('number: ')
        c = input('noun: ')
        d = input('adjective: ')
        e = input('name: ')
        f = input('adverb: ')
        g = input('verb ending in -ing: ')
        h = input('body part: ')
        i = input('verb: ')
        madlib2repo.TheNBlanks.save_madlib(a, b, c, d, e, f, g, h, i)
        print(f'\nOnce upon a time, there were {b} {c}s. Of those, only one was {d}. This {c} was named {e}, and he liked \n' \
                f'to {a}. Every day, he would {f} {a} before even {g} his {h}! Eventually, all his friends get fed up with \n' \
                f'his incessant {a}ing, and they issued an ultimatum: stop {a}ing or they would {i} him. {e} tried to stop, \n' \
                f'but ultimately couldnt help but {a}. His friends made good on their threat, though, and {i}ed him.')
    elif x == 3:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nA recipe (13 blanks)')
        a = input('familial relation: ')
        b = input('food: ')
        c = input('verb: ')
        d = input('number: ')
        e = input('noun: ')
        f = input('noun: ')
        g = input('noun: ')
        h = input('adjective: ')
        i = input('number: ')
        j = input('plural noun: ')
        k = input('noun: ')
        l = input('number: ')
        m = input('number: ')
        madlib2repo.ARecipe.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nToday, I will share my {a}'s recipe for {b}! First, {c} the oven to {d} degrees. Then mix {e}, {f}, and {g} in \n"\
                f"a {h} mixing bowl. Add in {i} {j} and pour into a {k}. Place the {k} in the oven for {l} minutes. Remove from the oven \n"\
                f"and serve when cool. Serves {m}.")
    elif x == 4:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nMy Dream Home (14 blanks)')
        a = input('type of building: ')
        b = input('number: ')
        c = input('adjective: ')
        d = input('number: ')
        e = input('room: ')
        f = input('noun: ')
        g = input('plural noun: ')
        h = input('adjective: ')
        i = input('plural noun: ')
        j = input('shape: ')
        k = input('noun: ')
        l = input('animal: ')
        m = input('adjective: ')
        n = input('noun: ')
        madlib2repo.DreamHome.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m, n)
        print(f'\nMy dream home is a {a} with {b} bed and {d} bath. \n' \
            f'In the middle of my home, I want a large {e} with a {f} in the center. \n' \
            f'Surrounding the {f} would be {g}.\n' \
            f'In my bedroom I would have {d} {h} {i} arranged in a {j}. There would also be a {c} {k} for my pet \n' \
            f'{l}. And of course my home would have a {m} {n}!')
    elif x == 5:
        print('\nGoldilocks (22 blanks)')
        madlib2repo.goldilocks()
    elif x == 6:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nA Normal Day (13 blanks)')
        a = input('verb: ')
        b = input('verb: ')
        c = input('adjective: ')
        d = input('food: ')
        e = input('container: ')
        f = input('liquid: ')
        g = input('vehicle: ')
        h = input('verb: ')
        i = input('occupation: ')
        j = input('verb: ')
        k = input('verb ending in -ing: ')
        l = input('food: ')
        m = input('verb: ')
        madlib2repo.ANormalDay.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nI'd say I lead a very normal life. My day starts when I {a}. I then {b}. \n"
            f"For breakfast I eat {c} {d} and drink a {e} of {f}. \n"
            f"Then it's time to leave for work. I get in my {g} and {h} to my job as a {i} \n"
            f"At work, I {j} until noon, then I eat more {d} for lunch. I spend the rest of the day \n"
            f"{k}. After work I return home, eat some {l} for dinner, and {m} until bed. \n"
            f"After all that, I sleep soundly until morning, ending my completely normal day.")
    elif x == 7:
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nClowns (13 blanks)')
        a = input('adjective: ')
        b = input('plural noun: ')
        c = input('adjective: ')
        d = input('plural noun: ')
        e = input('plural noun: ')
        f = input('adjective: ')
        g = input('verb: ')
        h = input('plural noun: ')
        i = input('verb: ')
        j = input('adjective: ')
        k = input('verb: ')
        l = input('noun: ')
        m = input('familial relation: ')
        madlib2repo.Clowns.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nMy little brother has always been afraid of clowns. I've tried explaining to him that they're just {a} \n" \
            f"{b} wearing {c} costumes, but he insists that they're actually {d}. He thinks they have {e} and eat {f} kids. \n" \
            f"He thinks they {g} {h}. I think this all started when he saw a clown {i} in a movie, but he claims that he \n" \
            f"saw a {j} clown {k} a {l} in a restaurant when he was younger. I think he's making it up, but this whole thing \n" \
            f"does make it difficult to tell him what our {m}'s new job is.")
        
def choose_madlib():
    choice = input('\nChoose a madlib:\n'
                        '1) The Little Blank \t\t\t(10 blanks)\n'
                        '2) The Blank Who Liked to Blank \t(9 blanks)\n'
                        '3) A Recipe \t\t\t\t(13 blanks)\n'
                        '4) My Dream Home \t\t\t(14 blanks)\n'
                        '5) Goldilocks \t\t\t\t(22 blanks)\n'
                        '6) A Normal Day \t\t\t(13 blanks)\n'
                        '7) Clowns \t\t\t\t(13 blanks)\n'
                        '8) Back\n'
                        '> ')
    if choice == '1':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print("\nThe little blank (10 blanks)")
        a = input('noun: ')
        b = input('adjective: ')
        c = input('past tense verb: ')
        d = input('verb: ')
        e = input('adjective: ')
        f = input('verb: ')
        g = input('adjective: ')
        h = input('quote: ')
        i = input('past tense verb: ')
        j = input('noun: ')
        madlib2repo.TheLittleBlank.save_madlib(a, b, c, d, e, f, g, h, i, j)
        print(f'\nOnce upon a time, there was a little {a}. This {a} was very {b} and never {c}. One day, their mother \n' \
                f'told them to {d}, but the {e} little {a} didnt want to {d}! Instead, they decided to {f}! When their {g} mother \n' \
                f'learned of their disobedience, she told them "{h}" and {i} them without any {j}. From that day forth, \n' \
                f'the {b} little {a} never disobeyed their mother to {f} again')
    elif choice == '2':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nThe Blank Who Liked to Blank (9 blanks)')
        a = input('verb: ')
        b = input('number: ')
        c = input('noun: ')
        d = input('adjective: ')
        e = input('name: ')
        f = input('adverb: ')
        g = input('verb ending in -ing: ')
        h = input('body part: ')
        i = input('verb: ')
        madlib2repo.TheNBlanks.save_madlib(a, b, c, d, e, f, g, h, i)
        print(f'\nOnce upon a time, there were {b} {c}s. Of those, only one was {d}. This {c} was named {e}, and he liked \n' \
                f'to {a}. Every day, he would {f} {a} before even {g} his {h}! Eventually, all his friends get fed up with \n' \
                f'his incessant {a}ing, and they issued an ultimatum: stop {a}ing or they would {i} him. {e} tried to stop, \n' \
                f'but ultimately couldnt help but {a}. His friends made good on their threat, though, and {i}ed him.')
    elif choice == '3':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nA recipe (13 blanks)')
        a = input('familial relation: ')
        b = input('food: ')
        c = input('verb: ')
        d = input('number: ')
        e = input('noun: ')
        f = input('noun: ')
        g = input('noun: ')
        h = input('adjective: ')
        i = input('number: ')
        j = input('plural noun: ')
        k = input('noun: ')
        l = input('number: ')
        m = input('number: ')
        madlib2repo.ARecipe.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nToday, I will share my {a}'s recipe for {b}! First, {c} the oven to {d} degrees. Then mix {e}, {f}, and {g} in \n"\
                f"a {h} mixing bowl. Add in {i} {j} and pour into a {k}. Place the {k} in the oven for {l} minutes. Remove from the oven \n"\
                f"and serve when cool. Serves {m}.")
    elif choice == '4':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nMy Dream Home (14 blanks)')
        a = input('type of building: ')
        b = input('number: ')
        c = input('adjective: ')
        d = input('number: ')
        e = input('room: ')
        f = input('noun: ')
        g = input('plural noun: ')
        h = input('adjective: ')
        i = input('plural noun: ')
        j = input('shape: ')
        k = input('noun: ')
        l = input('animal: ')
        m = input('adjective: ')
        n = input('noun: ')
        madlib2repo.DreamHome.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m, n)
        print(f'\nMy dream home is a {a} with {b} bed and {d} bath. \n' \
            f'In the middle of my home, I want a large {e} with a {f} in the center. \n' \
            f'Surrounding the {f} would be {g}.\n' \
            f'In my bedroom I would have {d} {h} {i} arranged in a {j}. There would also be a {c} {k} for my pet \n' \
            f'{l}. And of course my home would have a {m} {n}!')
    elif choice == '5':
        madlib2repo.goldilocks()
    elif choice == '6':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nA Normal Day (13 blanks)')
        a = input('verb: ')
        b = input('verb: ')
        c = input('adjective: ')
        d = input('food: ')
        e = input('container: ')
        f = input('liquid: ')
        g = input('vehicle: ')
        h = input('verb: ')
        i = input('occupation: ')
        j = input('verb: ')
        k = input('verb ending in -ing: ')
        l = input('food: ')
        m = input('verb: ')
        madlib2repo.ANormalDay.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nI'd say I lead a very normal life. My day starts when I {a}. I then {b}. \n"\
            f"For breakfast I eat {c} {d} and drink a {e} of {f}. \n"\
            f"Then it's time to leave for work. I get in my {g} and {h} to my job as a {i} \n"\
            f"At work, I {j} until noon, then I eat more {d} for lunch. I spend the rest of the day \n"\
            f"{k}. After work I return home, eat some {l} for dinner, and {m} until bed. \n"\
            f"After all that, I sleep soundly until morning, ending my completely normal day.")
    elif choice == '7':
        os.system('cls||clear')
        madlib2repo.Madlib.review()
        print('\nClowns (13 blanks)')
        a = input('adjective: ')
        b = input('plural noun: ')
        c = input('adjective: ')
        d = input('plural noun: ')
        e = input('plural noun: ')
        f = input('adjective: ')
        g = input('verb: ')
        h = input('plural noun: ')
        i = input('verb: ')
        j = input('adjective: ')
        k = input('verb: ')
        l = input('noun: ')
        m = input('familial relation: ')
        madlib2repo.Clowns.save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m)
        print(f"\nMy little brother has always been afraid of clowns. I've tried explaining to him that they're just {a} \n" \
            f"{b} wearing {c} costumes, but he insists that they're actually {d}. He thinks they have {e} and eat {f} kids. \n" \
            f"He thinks they {g} {h}. I think this all started when he saw a clown {i} in a movie, but he claims that he \n" \
            f"saw a {j} clown {k} a {l} in a restaurant when he was younger. I think he's making it up, but this whole thing \n" \
            f"does make it difficult to tell him what our {m}'s new job is.")
    elif choice == '8':
        os.system('cls||clear')
        fill_out_menu()
    else:
        print('invalid input')

if __name__ == "__main__":
    while True:
        main_menu()

