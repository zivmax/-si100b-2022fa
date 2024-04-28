num = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
phase = ['D','C','S','H']
from random import randint
import csv

with open('stacked.in', 'w', newline='') as csvfile:
    cards = []
    for i in range(randint(1, 10)):
        cards.append([])
        for j in range(randint(1, 10)):
            cards[i-1].append(phase[randint(0,3)] + num[randint(0,12)])
    chartWriter = csv.writer(csvfile)
    chartWriter.writerows(cards)