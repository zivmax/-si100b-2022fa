cardSet = {"D2", "C2", "H2", "S2", "D3", "C3", "H3", "S3", "D4", "C4", "H4", "S4", "D5", "C5", "H5", "S5", "D6", "C6", "H6", "S6", "D7", "C7", "H7", "S7", "D8", "C8", "H8", "S8", "D9", "C9", "H9", "S9", "DT", "CT", "HT", "ST", "DJ", "CJ", "HJ", "SJ", "DQ", "CQ", "HQ", "SQ", "DK", "CK", "HK", "SK", "DA", "CA", "HA", "SA"}
from random import randint
with open("geninput4.txt", 'w') as f:
    n = randint(3, 30)
    output = []
    for i in range(n): output.append(cardSet.pop())
    for k in range(len(output)): 
        f.write(output[k])
        if k < len(output) - 1: f.write(', ')