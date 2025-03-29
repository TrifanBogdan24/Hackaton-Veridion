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
        self.word_list[1][WEAKER_WORDS_STR] = [1, 2, 3]
        self.word_list[2][WEAKER_WORDS_STR] = [0]
        self.word_list[3][WEAKER_WORDS_STR] = [0]
        self.word_list[4][WEAKER_WORDS_STR] = [0]
        self.word_list[5][WEAKER_WORDS_STR] = [0]
        self.word_list[6][WEAKER_WORDS_STR] = [0]
        self.word_list[7][WEAKER_WORDS_STR] = [0]
        self.word_list[8][WEAKER_WORDS_STR] = [0]
        self.word_list[9][WEAKER_WORDS_STR] = [0]
        self.word_list[10][WEAKER_WORDS_STR] = [0]
        self.word_list[11][WEAKER_WORDS_STR] = [0]
        self.word_list[12][WEAKER_WORDS_STR] = [0]
        self.word_list[13][WEAKER_WORDS_STR] = [0]
        self.word_list[14][WEAKER_WORDS_STR] = [0]
        self.word_list[15][WEAKER_WORDS_STR] = [0]
        self.word_list[16][WEAKER_WORDS_STR] = [0]
        self.word_list[17][WEAKER_WORDS_STR] = [0]
        self.word_list[18][WEAKER_WORDS_STR] = [0]
        self.word_list[19][WEAKER_WORDS_STR] = [0]
        self.word_list[20][WEAKER_WORDS_STR] = [0]
        self.word_list[21][WEAKER_WORDS_STR] = [0]
        self.word_list[22][WEAKER_WORDS_STR] = [0]
        self.word_list[23][WEAKER_WORDS_STR] = [0]
        self.word_list[24][WEAKER_WORDS_STR] = [0]
        self.word_list[25][WEAKER_WORDS_STR] = [0]
        self.word_list[26][WEAKER_WORDS_STR] = [0]
        self.word_list[27][WEAKER_WORDS_STR] = [0]
        self.word_list[28][WEAKER_WORDS_STR] = [0]
        self.word_list[29][WEAKER_WORDS_STR] = [0]
        self.word_list[30][WEAKER_WORDS_STR] = [0]
        self.word_list[31][WEAKER_WORDS_STR] = [0]
        self.word_list[32][WEAKER_WORDS_STR] = [0]
        self.word_list[33][WEAKER_WORDS_STR] = [0]
        self.word_list[34][WEAKER_WORDS_STR] = [0]
        self.word_list[35][WEAKER_WORDS_STR] = [0]
        self.word_list[36][WEAKER_WORDS_STR] = [0]
        self.word_list[37][WEAKER_WORDS_STR] = [0]
        self.word_list[38][WEAKER_WORDS_STR] = [0]
        self.word_list[39][WEAKER_WORDS_STR] = [0]
        self.word_list[40][WEAKER_WORDS_STR] = [0]
        self.word_list[41][WEAKER_WORDS_STR] = [0]
        self.word_list[42][WEAKER_WORDS_STR] = [0]
        self.word_list[43][WEAKER_WORDS_STR] = [0]
        self.word_list[44][WEAKER_WORDS_STR] = [0]
        self.word_list[45][WEAKER_WORDS_STR] = [0]
        self.word_list[46][WEAKER_WORDS_STR] = [0]
        self.word_list[47][WEAKER_WORDS_STR] = [0]
        self.word_list[48][WEAKER_WORDS_STR] = [0]
        self.word_list[49][WEAKER_WORDS_STR] = [0]
        self.word_list[50][WEAKER_WORDS_STR] = [0]
        self.word_list[51][WEAKER_WORDS_STR] = [0]
        self.word_list[52][WEAKER_WORDS_STR] = [0]
        self.word_list[53][WEAKER_WORDS_STR] = [0]
        self.word_list[54][WEAKER_WORDS_STR] = [0]
        self.word_list[55][WEAKER_WORDS_STR] = [0]
        self.word_list[56][WEAKER_WORDS_STR] = [0]
        self.word_list[57][WEAKER_WORDS_STR] = [0]
        self.word_list[58][WEAKER_WORDS_STR] = [0]
        self.word_list[59][WEAKER_WORDS_STR] = [0]
        self.word_list[60][WEAKER_WORDS_STR] = [0]



        

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