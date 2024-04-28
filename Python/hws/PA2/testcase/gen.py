import os
import random
from random import randint, random
from turtle import pos

suits = ['D', 'C', 'H', 'S']
val = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
all_cards = [s + v for s in suits for v in val]

def Act1(num_files, num_lines, max_ele, targ_dir=''):
    if targ_dir != '':
        os.makedirs(targ_dir, exist_ok=True)
    for i in range(num_files):
        rand_index = [randint(0,51) for j in range(randint(10,25))]
        drop_card = set([all_cards[i] for i in rand_index])
        card = list(set(all_cards) - drop_card)        
        testcase = ''
        for _ in range(num_lines):
            k = randint(0, max_ele)
            for _ in range(k):
                testcase += card[randint(0, len(card) - 1)] + ','
            if k and random() < 0.5:
                testcase += card[randint(0, len(card) - 1)]
            if random() < 0.5:
                for _ in range(randint(0, max_ele - k)):
                    testcase += ','
            testcase += '\n'
        with open(os.path.join(targ_dir, f'{i:0>2}.csv'), 'w') as f:
            f.write(testcase)
    return

def Act2(num_files, max_turns, max_HP, max_cards, targ_dir=''):
    if targ_dir != '':
        os.makedirs(targ_dir, exist_ok=True)

    for i in range(num_files):
        vis = [False for _ in all_cards]
        testcase = ''
        n = randint(1, max_turns)
        m = randint(1, max_HP)
        k = randint(1, max_cards)
        handcards = []
        while len(handcards) < k:
            idx = randint(0, len(all_cards) - 1)
            if not vis[idx]:
                handcards.append(all_cards[idx])
                vis[idx] = True
        attacks = []
        for _ in range(n):
            for _ in range(10):
                attack_comb = randint(1,4)
                possible_choices = []
                for j in range(13):
                    cnt = 4 - sum(vis[j::13])
                    if cnt >= attack_comb:
                        possible_choices.append(j)
                if len(possible_choices):
                    j = possible_choices[randint(0, len(possible_choices) - 1)]
                    idx = []
                    while len(idx) < attack_comb:
                        id = j + randint(0,3) * 13
                        if id not in idx and not vis[id]: idx.append(id)
                    attacks.append([all_cards[id] for id in idx])
                    for id in idx:
                        vis[id] = True
                    break
        n = len(attacks)
        testcase += str(n) + ',' + str(m) + '\n'
        testcase += str(handcards).replace(' ', '').replace("'",'')[1:-1] + '\n'
        for atk in attacks:
            testcase += str(atk).replace(' ', '').replace("'",'')[1:-1] + '\n'
        with open(os.path.join(targ_dir, f'{i:0>2}.in'), 'w') as f:
            f.write(testcase)
    return

def Act3(num_files, max_turns, max_HP, max_cards, targ_dir=''):
    if targ_dir != '':
        os.makedirs(targ_dir, exist_ok=True)

    for i in range(num_files):
        vis = [False for _ in all_cards]
        testcase = ''
        n = randint(1, max_turns)
        m = randint(1, max_HP)
        k = randint(1, max_cards)
        handcards = []
        while len(handcards) < k:
            idx = randint(0, len(all_cards) - 1)
            if not vis[idx]:
                handcards.append(all_cards[idx])
                vis[idx] = True
        attacks = []
        for _ in range(n):
            for _ in range(10):
                attack_comb = randint(1,5)
                possible_choices = []
                if attack_comb == 5:
                    possible_choices.append([])
                    possible_choices.append([])
                for j in range(13):
                    cnt = 4 - sum(vis[j::13])
                    if attack_comb == 5:
                        if cnt >= 2:
                            possible_choices[0].append(j)
                        if cnt >= 3:
                            possible_choices[1].append(j)
                    if cnt >= attack_comb:
                        possible_choices.append(j)
                if attack_comb == 5 and len(possible_choices[0]) * len(possible_choices[1]):
                    a = 0
                    b = 0
                    for _ in range(10):                    
                        a = possible_choices[0][randint(0, len(possible_choices[0]) - 1)]
                        b = possible_choices[1][randint(0, len(possible_choices[1]) - 1)]
                        if a != b: break
                    if a == b:
                        continue
                    idx = []
                    if random() < 0.5:
                        while len(idx) < 2:
                            id = a + randint(0,3) * 13
                            if id not in idx and not vis[id]: idx.append(id)
                        while len(idx) < attack_comb:
                            id = b + randint(0,3) * 13
                            if id not in idx and not vis[id]: idx.append(id)
                    else:
                        while len(idx) < 3:
                            id = b + randint(0,3) * 13
                            if id not in idx and not vis[id]: idx.append(id)
                        while len(idx) < attack_comb:
                            id = a + randint(0,3) * 13
                            if id not in idx and not vis[id]: idx.append(id)
                    attacks.append([all_cards[id] for id in idx])
                    for id in idx:
                        vis[id] = True
                    break
                if attack_comb != 5 and len(possible_choices):
                    j = possible_choices[randint(0, len(possible_choices) - 1)]
                    idx = []
                    while len(idx) < attack_comb:
                        id = j + randint(0,3) * 13
                        if id not in idx and not vis[id]: idx.append(id)
                    attacks.append([all_cards[id] for id in idx])
                    for id in idx:
                        vis[id] = True
                    break
        n = len(attacks)
        testcase += str(n) + ',' + str(m) + '\n'
        testcase += str(handcards).replace(' ', '').replace("'",'')[1:-1] + '\n'
        for atk in attacks:
            testcase += str(atk).replace(' ', '').replace("'",'')[1:-1] + '\n'
        with open(os.path.join(targ_dir, f'{i:0>2}.in'), 'w') as f:
            f.write(testcase)
    return

def Act4(num_files, max_cards, targ_dir=''):
    if targ_dir != '':
        os.makedirs(targ_dir, exist_ok=True)
    for i in range(num_files):
        vis = [False for _ in all_cards]
        k = randint(1, max_cards)
        handcards = []
        while len(handcards) < k:
            idx = randint(0, len(all_cards) - 1)
            if not vis[idx]:
                handcards.append(all_cards[idx])
                vis[idx] = True
        testcase = str(handcards).replace(' ', '').replace("'",'')[1:-1]
        with open(os.path.join(targ_dir, f'{i:0>2}.in'), 'w') as f:
            f.write(testcase)
    return


Act4(10, 50, targ_dir="Task4")