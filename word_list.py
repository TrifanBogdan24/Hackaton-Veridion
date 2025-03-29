import json
from typing import Dict, Union, List

WEAKER_WORDS_STR = "weaker words"

class WordList:
    """
    Se stie de la bun inceput ca WordList-ul are o lungime fixam de 60 de cuvinte,
    fiecare cuvant avand urmatoarele campuri:
    - "text" -> str
    - "cost" -> int
    """
    def __init__(self):
        # Hard-coded, it is what it is
        self.word_list = {
            1: {"text": "Feather", "cost": 1},
            2: {"text": "Coal", "cost": 1},
            3: {"text": "Pebble", "cost": 1},
            4: {"text": "Leaf", "cost": 2},
            5: {"text": "Paper", "cost": 2},
            6: {"text": "Rock", "cost": 2},
            7: {"text": "Water", "cost": 3},
            8: {"text": "Twig", "cost": 3},
            9: {"text": "Sword", "cost": 4},
            10: {"text": "Shield", "cost": 4},
            11: {"text": "Gun", "cost": 5},
            12: {"text": "Flame", "cost": 5},
            13: {"text": "Rope", "cost": 5},
            14: {"text": "Disease", "cost": 6},
            15: {"text": "Cure", "cost": 6},
            16: {"text": "Bacteria", "cost": 6},
            17: {"text": "Shadow", "cost": 7},
            18: {"text": "Light", "cost": 7},
            19: {"text": "Virus", "cost": 7},
            20: {"text": "Sound", "cost": 8},
            21: {"text": "Time", "cost": 8},
            22: {"text": "Fate", "cost": 8},
            23: {"text": "Earthquake", "cost": 9},
            24: {"text": "Storm", "cost": 9},
            25: {"text": "Vaccine", "cost": 9},
            26: {"text": "Logic", "cost": 10},
            27: {"text": "Gravity", "cost": 10},
            28: {"text": "Robots", "cost": 10},
            29: {"text": "Stone", "cost": 11},
            30: {"text": "Echo", "cost": 11},
            31: {"text": "Thunder", "cost": 12},
            32: {"text": "Karma", "cost": 12},
            33: {"text": "Wind", "cost": 13},
            34: {"text": "Ice", "cost": 13},
            35: {"text": "Sandstorm", "cost": 13},
            36: {"text": "Laser", "cost": 14},
            37: {"text": "Magma", "cost": 14},
            38: {"text": "Peace", "cost": 14},
            39: {"text": "Explosion", "cost": 15},
            40: {"text": "War", "cost": 15},
            41: {"text": "Enlightenment", "cost": 15},
            42: {"text": "Nuclear Bomb", "cost": 16},
            43: {"text": "Volcano", "cost": 16},
            44: {"text": "Whale", "cost": 17},
            45: {"text": "Earth", "cost": 17},
            46: {"text": "Moon", "cost": 17},
            47: {"text": "Star", "cost": 18},
            48: {"text": "Tsunami", "cost": 18},
            49: {"text": "Supernova", "cost": 19},
            50: {"text": "Antimatter", "cost": 19},
            51: {"text": "Plague", "cost": 20},
            52: {"text": "Rebirth", "cost": 20},
            53: {"text": "Tectonic Shift", "cost": 21},
            54: {"text": "Gamma-Ray Burst", "cost": 22},
            55: {"text": "Human Spirit", "cost": 23},
            56: {"text": "Apocalyptic Meteor", "cost": 24},
            57: {"text": "Earth’s Core", "cost": 25},
            58: {"text": "Neutron Star", "cost": 26},
            59: {"text": "Supermassive Black Hole", "cost": 35},
            60: {"text": "Entropy", "cost": 45},
        }

        # Hard-coded, it is what it is
        self.word_list[1][WEAKER_WORDS_STR]  = [2, 3]  # Feather bate Coal și Pebble
        self.word_list[2][WEAKER_WORDS_STR]  = [3]     # Coal bate Pebble
        self.word_list[3][WEAKER_WORDS_STR]  = [4]     # Pebble bate Leaf
        self.word_list[4][WEAKER_WORDS_STR]  = [5, 6]  # Leaf bate Paper și Rock
        self.word_list[5][WEAKER_WORDS_STR]  = [6]     # Paper bate Rock
        self.word_list[6][WEAKER_WORDS_STR]  = [7, 8]  # Rock bate Water și Twig
        self.word_list[7][WEAKER_WORDS_STR]  = [8]     # Water bate Twig
        self.word_list[8][WEAKER_WORDS_STR]  = [9, 10] # Twig bate Sword și Shield
        self.word_list[9][WEAKER_WORDS_STR]  = [11]    # Sword bate Gun
        self.word_list[10][WEAKER_WORDS_STR] = [11, 12] # Shield bate Gun și Flame
        self.word_list[11][WEAKER_WORDS_STR] = [13]   # Gun bate Rope
        self.word_list[12][WEAKER_WORDS_STR] = [13]   # Flame bate Rope
        self.word_list[13][WEAKER_WORDS_STR] = [14]   # Rope bate Disease
        self.word_list[14][WEAKER_WORDS_STR] = [15]   # Disease bate Cure
        self.word_list[15][WEAKER_WORDS_STR] = [16]   # Cure bate Bacteria
        self.word_list[16][WEAKER_WORDS_STR] = [17]   # Bacteria bate Shadow
        self.word_list[17][WEAKER_WORDS_STR] = [18]   # Shadow bate Light
        self.word_list[18][WEAKER_WORDS_STR] = [19]   # Light bate Virus
        self.word_list[19][WEAKER_WORDS_STR] = [20]   # Virus bate Sound
        self.word_list[20][WEAKER_WORDS_STR] = [21]   # Sound bate Time
        self.word_list[21][WEAKER_WORDS_STR] = [22]   # Time bate Fate
        self.word_list[22][WEAKER_WORDS_STR] = [23]   # Fate bate Earthquake
        self.word_list[23][WEAKER_WORDS_STR] = [24]   # Earthquake bate Storm
        self.word_list[24][WEAKER_WORDS_STR] = [25]   # Storm bate Vaccine
        self.word_list[25][WEAKER_WORDS_STR] = [26]   # Vaccine bate Logic
        self.word_list[26][WEAKER_WORDS_STR] = [27]   # Logic bate Gravity
        self.word_list[27][WEAKER_WORDS_STR] = [28]   # Gravity bate Robots
        self.word_list[28][WEAKER_WORDS_STR] = [29]   # Robots bate Stone
        self.word_list[29][WEAKER_WORDS_STR] = [30]   # Stone bate Echo
        self.word_list[30][WEAKER_WORDS_STR] = [31]   # Echo bate Thunder
        self.word_list[31][WEAKER_WORDS_STR] = [32]   # Thunder bate Karma
        self.word_list[32][WEAKER_WORDS_STR] = [33]   # Karma bate Wind
        self.word_list[33][WEAKER_WORDS_STR] = [34]   # Wind bate Ice
        self.word_list[34][WEAKER_WORDS_STR] = [35]   # Ice bate Sandstorm
        self.word_list[35][WEAKER_WORDS_STR] = [36]   # Sandstorm bate Laser
        self.word_list[36][WEAKER_WORDS_STR] = [37]   # Laser bate Magma
        self.word_list[37][WEAKER_WORDS_STR] = [38]   # Magma bate Peace
        self.word_list[38][WEAKER_WORDS_STR] = [39]   # Peace bate WAr
        self.word_list[39][WEAKER_WORDS_STR] = [40]   # Explosion bate War
        self.word_list[40][WEAKER_WORDS_STR] = [41]   # War bate Enlightenment
        self.word_list[41][WEAKER_WORDS_STR] = [42]   # Enlightenment bate Nuclear Bomb
        self.word_list[42][WEAKER_WORDS_STR] = [43]   # Nuclear Bomb bate Volcano
        self.word_list[43][WEAKER_WORDS_STR] = [44]   # Volcano bate Whale
        self.word_list[44][WEAKER_WORDS_STR] = [45]   # Whale bate Earth
        self.word_list[45][WEAKER_WORDS_STR] = [46]   # Earth bate Moon
        self.word_list[46][WEAKER_WORDS_STR] = [47]   # Moon bate Star
        self.word_list[47][WEAKER_WORDS_STR] = [48]   # Star bate Tsunami
        self.word_list[48][WEAKER_WORDS_STR] = [49]   # Tsunami bate Supernova
        self.word_list[49][WEAKER_WORDS_STR] = [50]   # Supernova bate Antimatter
        self.word_list[50][WEAKER_WORDS_STR] = [51]   # Antimatter bate Plague
        self.word_list[51][WEAKER_WORDS_STR] = [52]   # Plague bate Rebirth
        self.word_list[52][WEAKER_WORDS_STR] = [53]   # Rebirth bate Tectonic Shift
        self.word_list[53][WEAKER_WORDS_STR] = [54]   # Tectonic Shift bate Gamma-Ray Burst
        self.word_list[54][WEAKER_WORDS_STR] = [55]   # Gamma-Ray Burst bate Human Spirit
        self.word_list[55][WEAKER_WORDS_STR] = [56]   # Human Spirit bate Apocalyptic Meteor
        self.word_list[56][WEAKER_WORDS_STR] = [57]   # Apocalyptic Meteor bate Earth’s Core
        self.word_list[57][WEAKER_WORDS_STR] = [58]   # Earth’s Core bate Neutron Star
        self.word_list[58][WEAKER_WORDS_STR] = [59]   # Neutron Star bate Supermassive Black Hole
        self.word_list[59][WEAKER_WORDS_STR] = [60]   # Supermassive Black Hole bate Entropy
        self.word_list[60][WEAKER_WORDS_STR] = []     # Entropy nu bate niciun alt cuvânt


    def get_word_id(self, word: str) -> int:
        for word_id, word_data in self.word_list.items():
            if word_data["text"].lower() == word.lower():
                return word_id
        return -1
        

    def get_word_data(self, word_id: int) -> Dict[str, Union[str, int]]:
        if word_id not in self.word_list:
            return None
        return self.word_list[word_id]

    def get_word_text(self, word_id: int) -> str:
        if word_id not in self.word_list:
            return None
        return self.word_list[word_id]["text"]
        
    def get_word_cost(self, word_id: int) -> str:
        if word_id not in self.word_list:
            return None
        return self.word_list[word_id]["cost"]


    def get_weaker_words(self, word_id: int) -> List[int]:
        if word_id not in self.word_list:
            return None
        return self.word_list[word_id][WEAKER_WORDS_STR]



if __name__ == '__main__':
    wordlist = WordList()
    print(wordlist.get_weaker_words(1))
    