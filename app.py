import socket
import random as r

all_tramps = {'someone':+1,
              'perfect draw':'a+f'}
all_cards = [1,2,3,4,5,6,7,8,9,10,11]

def deal(type_deal:str,quantity:int):

    if 'c' == type_deal:
        dealed = r.sample(all_cards, quantity)
        for card_dealt in dealed:
            all_cards.pop(all_cards.index(card_dealt))
        return dealed
    if 't'== type_deal:return r.choices(list(all_tramps.keys()),k=quantity)


class Player:
    #hand Cards / hand tramps
    def __init__(self,name,deck_C:list[int],deck_T:list[str]):
        self.name_P = name
        self.hand_C = deck_C
        self.hand_T = deck_T

