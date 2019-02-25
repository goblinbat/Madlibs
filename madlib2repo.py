"""
Repository
"""

import madlib2
from random import randint

filled = []

class Madlib:
    def review():
        print('REVIEW: \n'
            'Noun: a person, place, or thing (preferably a thing)\n '
            '\t(ex: cat, toast, gnome) \n'
            'Plural Noun: a multiple noun. Usually ends in "s"\n'
            '\t(ex: cats, goblins, sandwiches)\n'
            'Adjective: describes a noun \n'
            '\t(ex: blue, smelly, painted) \n'
            'Verb: something you do. An action word. \n'
            '\t(ex: jump, run, explode)\n'
            'Past Tense Verb: something you did. Usually ends in "ed" \n'
            '\t(ex: jumped, ran, exploded) \n'
            'Adverb: describes a verb; how something is done; generally ends in "ly" \n'
            '\t(ex: happily, funnily, weirdly)\n'
            'Quote: something you can say \n'
            '\t(ex: hi there, i like cake, i dont like that) \n'
            'Exclamation: something said excitedly\n'
            '\t(ex: ow, wow, oh no)\n'
            '================================================================================\n')

class TheLittleBlank(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j

    def save_madlib(a, b, c, d, e, f, g, h, i, j):        
        filled.append(TheLittleBlank(a, b, c, d, e, f, g, h, i, j))
    
    def __repr__(self):
        return f'\nOnce upon a time, there was a little {self.a}. This {self.a} was very {self.b} and never {self.c}. One day, their mother \n' \
        f'told them to {self.d}, but the {self.e} little {self.a} didnt want to {self.d}! Instead, they decided to {self.f}! When their {self.g} mother \n' \
        f'learned of their disobedience, she told them "{self.h}" and {self.i} them without any {self.j}. From that day forth, \n' \
        f'the {self.b} little {self.a} never disobeyed their mother to {self.f} again\n'

class TheNBlanks(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def save_madlib(a, b, c, d, e, f, g, h, i):        
        filled.append(TheNBlanks(a, b, c, d, e, f, g, h, i))
    
    def __repr__(self):
        return f'\nOnce upon a time, there were {self.b} {self.c}s. Of those, only one was {self.d}. This {self.c} was named {self.e}, and he liked \n' \
        f'to {self.a}. Every day, he would {self.f} {self.a} before even {self.g} his {self.h}! Eventually, all his friends get fed up with \n' \
        f'his incessant {self.a}ing, and they issued an ultimatum: stop {self.a}ing or they would {self.i} him. {self.e} tried to stop, \n' \
        f'but ultimately couldnt help but {self.a}. His friends made good on their threat, though, and {self.i}ed him.\n'

class ARecipe(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l 
        self.m = m

    def save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m):        
        filled.append(ARecipe(a, b, c, d, e, f, g, h, i, j, k, l, m))
    
    def __repr__(self):
        return f"\nToday, I will share my {self.a}'s recipe for {self.b}! First, {self.c} the oven to {self.d} degrees. Then mix {self.e}, {self.f}, and {self.g} in \n"\
        f"a {self.h} mixing bowl. Add in {self.i} {self.j} and pour into a {self.k}. Place the {self.k} in the oven for {self.l} minutes. Remove from the oven \n"\
        f"and serve when cool. Serves {self.m}.\n"

class DreamHome(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k 
        self.l = l 
        self.m = m 
        self.n = n 

    def save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m, n):        
        filled.append(DreamHome(a, b, c, d, e, f, g, h, i, j, k, l, m, n))
    
    def __repr__(self):
        return f'\nMy dream home is a {self.a} with {self.b} bed and {self.d} bath. \n' \
            f'In the middle of my home, I want a large {self.e} with a {self.f} in the center. \n' \
            f'Surrounding the {self.f} would be {self.g}.\n' \
            f'In my bedroom I would have {self.d} {self.h} {self.i} arranged in a {self.j}. There would also be a {self.c} {self.k} for my pet \n' \
            f'{self.l}. And of course my home would have a {self.m} {self.n}!\n'

def goldilocks():       # too long for a class; init can only take 14 arguments, goldilocks has 22 
    a = input('noun: ')
    b = input('name: ')
    c = input('location: ')
    d = input('type of building: ')
    e = input('noun: ')
    f = input('number: ')
    g = input('plural noun: ')
    h = input('adjective: ')
    i = input('adjective: ')
    j = input('noun: ')
    k = input('adjective: ')
    l = input('adjective: ')
    m = input('verb: ')
    n = input('plural noun: ')
    o = input('adjective: ')
    p = input('adjective: ')
    q = input('noun: ')
    r = input('familial relation: ')
    s = input('adverb: ')
    t = input('familial relation: ')
    u = input('familial relation: ')
    v = input('exclamation: ')

    prompt = f"\nThere was once a little {a} named {b}. One day, {b} got lost in the {c} and thought for sure they'd never be found. \n" \
            f"But then, they spotted a small {d} a little ways off! Using their trusty {e}, {b} soon found their way inside. \n" \
            f"There, they found {f} bowls of {g}. They were hungry, so they decided to eat some. The first bowl was too {h}, though. \n" \
            f"The secod bowl was too {i}. The third bowl, however, was just right and {b} ate up all the {g}. \n" \
            f"Next, they found {f} {j}s and decided to rest their tired legs. The first {j} was too {k}, and the second was too \n" \
            f"{l}. But the third one was just right and {b} sat on it for a good while. \n" \
            f"After a while, though, {b} started feeling very sleepy, so they went to look for some place to {m}. Upstairs, \n" \
            f"they found {f} {n}. As before the first two were unsuitable, being too {o} or too {p}, but the third was just right \n" \
            f"and {b} was able to {m} soundly. \n" \
            f"Soon, however, the {f} {q}s who lived in the {d} arrived home. There, they found that their home had been broken into! \n" \
            f"'Someone's eaten our {g}!' exclaimed {r} {q} {s}. \n" \
            f"'Someone's sat on our {j}s!' said {t} {q}, dismayed. \n" \
            f"'Someone's {m}ing in my {n}!' cried {u} {q}, surprised. \n" \
            f"All this commotion alerted {b} to the presence of the {q}s. '{v}!' shouted {b} and started to run from the {d}. \n" \
            f"Before they'd gotten very far, however, the {q}s caught them and ate them all up. \n"

    print(prompt)
    filled.append(prompt)

class ANormalDay(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l 
        self.m = m 

    def save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m):        
        filled.append(ANormalDay(a, b, c, d, e, f, g, h, i, j, k, l, m ))
    
    def __repr__(self):
        return f"\nI'd say I lead a very normal life. My day starts when I {self.a}. I then {self.b}. \n" \
            f"For breakfast I eat {self.c} {self.d} and drink a {self.e} of {self.f}. \n" \
            f"Then it's time to leave for work. I get in my {self.g} and {self.h} to my job as a {self.i} \n" \
            f"At work, I {self.j} until noon, then I eat more {self.d} for lunch. I spend the rest of the day \n" \
            f"{self.k}. After work I return home, eat some {self.l} for dinner, and {self.m} until bed. \n" \
            f"After all that, I sleep soundly until morning, ending my completely normal day."

class Clowns(Madlib):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l 
        self.m = m 

    def save_madlib(a, b, c, d, e, f, g, h, i, j, k, l, m):        
        filled.append(Clowns(a, b, c, d, e, f, g, h, i, j, k, l, m ))
    
    def __repr__(self):
        return f"\nMy little brother has always been afraid of clowns. I've tried explaining to him that they're just {self.a} \n" \
            f"{self.b} wearing {self.c} costumes, but he insists that they're actually {self.d}. He thinks they have {self.e} and eat {self.f} kids. \n" \
            f"He thinks they {self.g} {self.h}. I think this all started when he saw a clown {self.i} in a movie, but he claims that he \n" \
            f"saw a {self.j} clown {self.k} a {self.l} in a restaurant when he was younger. I think he's making it up, but this whole thing \n" \
            f"does make it difficult to tell him what our {self.m}'s new job is."
