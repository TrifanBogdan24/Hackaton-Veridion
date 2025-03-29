import json
from typing import Dict, Union, List
from enum import Enum

STRONGER_WORDS_STR = "stronger words"


class Words(Enum):
    """Constants for all allowed words"""
    FEATHER = "Feather"
    COAL = "Coal"
    PEBBLE = "Pebble"  # Pietricele
    LEAF = "Leaf"
    PAPER = "Paper"
    ROCK = "Rock"
    WATER = "Water"
    TWIG = "Twig"  # Ramura mica
    SWORD = "Sword"
    SHIELD = "Shield"
    GUN = "Gun"
    FLAME = "Flame"
    ROPE = "Rope"
    DISEASE = "Disease"
    CURE = "Cure"
    BACTERIA = "Bacteria"
    SHADOW = "Shadow"
    LIGHT = "Light"
    VIRUS = "Virus"
    SOUND = "Sound"
    TIME = "Time"
    FATE = "Fate"
    EARTHQUAKE = "Earthquake"
    STORM = "Storm"
    VACCINE = "Vaccine"
    LOGIC = "Logic"
    GRAVITY = "Gravity"
    ROBOTS = "Robots"
    STONE = "Stone"
    ECHO = "Echo"
    THUNDER = "Thunder"
    KARMA = "Karma"
    WIND = "Wind"
    ICE = "Ice"
    SANDSTORM = "Sandstorm"
    LASER = "Laser"
    MAGMA = "Magma"
    PEACE = "Peace"
    EXPLOSION = "Explosion"
    WAR = "War"
    ENLIGHTENMENT = "Enlightenment"
    NUCLEAR_BOMB = "Nuclear Bomb"
    VOLCANO = "Volcano"
    WHALE = "Whale"
    EARTH = "Earth"
    MOON = "Moon"
    STAR = "Star"
    TSUNAMI = "Tsunami"
    SUPERNOVA = "Supernova"
    ANTIMATTER = "Antimatter"
    PLAGUE = "Plague"
    REBIRTH = "Rebirth"
    TECTONIC_SHIFT = "Tectonic Shift"
    GAMMA_RAY_BURST = "Gamma-Ray Burst"
    HUMAN_SPIRIT = "Human Spirit"
    APOCALYPTIC_METEOR = "Apocalyptic Meteor"
    EARTHS_CORE = "Earth’s Core"
    NEUTRON_STAR = "Neutron Star"
    SUPERMASSIVE_BLACK_HOLE = "Supermassive Black Hole"
    ENTROPY = "Entropy"


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
            3: {"text": "Pebble", "cost": 1},   # Pietricele
            4: {"text": "Leaf", "cost": 2},
            5: {"text": "Paper", "cost": 2},
            6: {"text": "Rock", "cost": 2},
            7: {"text": "Water", "cost": 3},
            8: {"text": "Twig", "cost": 3},      # Ramura mica
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
        self.word_list[1][STRONGER_WORDS_STR]  = [
            # "Feather" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun"),
            self.get_word_id("Flame"),
            self.get_word_id("Wind"),
            self.get_word_id("Sandstorm")
        ]
        self.word_list[2][STRONGER_WORDS_STR]  = [
            # "Coal" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun")
        ]
        self.word_list[3][STRONGER_WORDS_STR]  = [
            # "Pebble" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun")
        ]
        self.word_list[4][STRONGER_WORDS_STR]  = [
            # "Leaf" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun"),
            self.get_word_id("Flame")
        ]
        self.word_list[5][STRONGER_WORDS_STR]  = [
            # "Paper" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun"),
            self.get_word_id("Flame")
        ]
        self.word_list[6][STRONGER_WORDS_STR]  = [
            # "Rock" is weaker than:
            self.get_word_id("Sword"),
            self.get_word_id("Gun"),
            self.get_word_id("Flame")
        ]
        self.word_list[7][STRONGER_WORDS_STR]  = [
            # "Water" is weaker than:
            self.get_word_id("Fire"),
            self.get_word_id("Thunder"),
            self.get_word_id("Sword")
        ]
        self.word_list[8][STRONGER_WORDS_STR]  = [
            # "Twig" is weaker than:
            self.get_word_id("Rock"),
            self.get_word_id("Sword"),
            self.get_word_id("Gun")
        ]
        self.word_list[9][STRONGER_WORDS_STR]  = [
            # "Sword" is weaker than:
            self.get_word_id("Gun"),
            self.get_word_id("Flame"),
            self.get_word_id("Explosion")
        ]
        self.word_list[10][STRONGER_WORDS_STR] = [
            # "Shield" is weaker than:
            self.get_word_id("Gun"),
            self.get_word_id("Explosion"),
            self.get_word_id("Flame")
        ]
        self.word_list[11][STRONGER_WORDS_STR] = [
            # "Gun" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Flame"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[12][STRONGER_WORDS_STR] = [
            # "Flame" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb"),
            self.get_word_id("Volcano")
        ]
        self.word_list[13][STRONGER_WORDS_STR] = [
            # "Rope" is weaker than:
            self.get_word_id("Gun"),
            self.get_word_id("Flame")
        ]
        self.word_list[14][STRONGER_WORDS_STR] = [
            # "Disease" is weaker than:
            self.get_word_id("Cure"),
            self.get_word_id("Vaccine")
        ]
        self.word_list[15][STRONGER_WORDS_STR] = [
            # "Cure" is weaker than:
            self.get_word_id("Flame"),
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[16][STRONGER_WORDS_STR] = [
            # "Bacteria" is weaker than:
            self.get_word_id("Flame"),
            self.get_word_id("Gun"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[17][STRONGER_WORDS_STR] = [
            # "Shadow" is weaker than:
            self.get_word_id("Light"),
            self.get_word_id("Sun"),
            self.get_word_id("Flame")
        ]
        self.word_list[18][STRONGER_WORDS_STR] = [
            # "Light" is weaker than:
            self.get_word_id("Thunder"),
            self.get_word_id("Explosion")
        ]
        self.word_list[19][STRONGER_WORDS_STR] = [
            # "Virus" is weaker than:
            self.get_word_id("Cure"),
            self.get_word_id("Vaccine")
        ]
        self.word_list[20][STRONGER_WORDS_STR] = [
            # "Sound" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Thunder")
        ]
        self.word_list[21][STRONGER_WORDS_STR] = [
            # "Time" is weaker than:
            self.get_word_id("Gravity"),
            self.get_word_id("Logic")
        ]
        self.word_list[22][STRONGER_WORDS_STR] = [
            # "Fate" is weaker than:
            self.get_word_id("Time"),
            self.get_word_id("Logic")
        ]
        self.word_list[23][STRONGER_WORDS_STR] = [
            # "Earthquake" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[24][STRONGER_WORDS_STR] = [
            # "Storm" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[25][STRONGER_WORDS_STR] = [
            # "Vaccine" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[26][STRONGER_WORDS_STR] = [
            # "Logic" is weaker than:
            self.get_word_id("Time"),
            self.get_word_id("Fate"),
            self.get_word_id("Gravity")
        ]
        self.word_list[27][STRONGER_WORDS_STR] = [
            # "Gravity" is weaker than:
            self.get_word_id("Time"),
            self.get_word_id("Black Hole")
        ]
        self.word_list[28][STRONGER_WORDS_STR] = [
            # "Robots" are weaker than:
            self.get_word_id("Humans"),
            self.get_word_id("AI")
        ]
        self.word_list[29][STRONGER_WORDS_STR] = [
            # "Stone" is weaker than:
            self.get_word_id("Sword"),
            self.get_word_id("Gun")
        ]
        self.word_list[30][STRONGER_WORDS_STR] = [
            # "Echo" is weaker than:
            self.get_word_id("Thunder")
        ]
        self.word_list[31][STRONGER_WORDS_STR] = [
            # "Thunder" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[32][STRONGER_WORDS_STR] = [
            # "Karma" is weaker than:
            self.get_word_id("Fate"),
            self.get_word_id("Destiny")
        ]
        self.word_list[33][STRONGER_WORDS_STR] = [
            # "Wind" is weaker than:
            self.get_word_id("Storm"),
            self.get_word_id("Tornado")
        ]
        self.word_list[34][STRONGER_WORDS_STR] = [
            # "Ice" is weaker than:
            self.get_word_id("Flame"),
            self.get_word_id("Explosion")
        ]
        self.word_list[35][STRONGER_WORDS_STR] = [
            # "Sandstorm" is weaker than:
            self.get_word_id("Storm"),
            self.get_word_id("Explosion")
        ]
        self.word_list[36][STRONGER_WORDS_STR] = [
            # "Laser" is weaker than:
            self.get_word_id("Explosion"),
            self.get_word_id("Nuclear Bomb")
        ]
        self.word_list[37][STRONGER_WORDS_STR] = [
            # "Magma" is weaker than:
            self.get_word_id("Volcano"),
            self.get_word_id("Explosion")
        ]
        self.word_list[38][STRONGER_WORDS_STR] = [
            # "Peace" is weaker than:
            self.get_word_id("War"),
            self.get_word_id("Explosion")
        ]
        self.word_list[39][STRONGER_WORDS_STR] = [
            # "Explosion" is weaker than:
            self.get_word_id("Nuclear Bomb"),
            self.get_word_id("Supernova")
        ]
        self.word_list[40][STRONGER_WORDS_STR] = [
            # "War" is weaker than:
            self.get_word_id("Nuclear Bomb"),
            self.get_word_id("Supernova")
        ]
        self.word_list[41][STRONGER_WORDS_STR] = [
            # "Enlightenment" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Black Hole")
        ]
        self.word_list[42][STRONGER_WORDS_STR] = [
            # "Nuclear Bomb" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Neutron Star")
        ]
        self.word_list[43][STRONGER_WORDS_STR] = [
            # "Volcano" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Neutron Star")
        ]
        self.word_list[44][STRONGER_WORDS_STR] = [
            # "Whale" is weaker than:
            self.get_word_id("Earthquake"),
            self.get_word_id("Tsunami")
        ]
        self.word_list[45][STRONGER_WORDS_STR] = [
            # "Earth" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Black Hole")
        ]
        self.word_list[46][STRONGER_WORDS_STR] = [
            # "Moon" is weaker than:
            self.get_word_id("Neutron Star"),
            self.get_word_id("Supernova")
        ]
        self.word_list[47][STRONGER_WORDS_STR] = [
            # "Star" is weaker than:
            self.get_word_id("Neutron Star"),
            self.get_word_id("Supernova")
        ]
        self.word_list[48][STRONGER_WORDS_STR] = [
            # "Tsunami" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Black Hole")
        ]
        self.word_list[49][STRONGER_WORDS_STR] = [
            # "Supernova" is weaker than:
            self.get_word_id("Black Hole")
        ]
        self.word_list[50][STRONGER_WORDS_STR] = [
            # "Antimatter" is weaker than:
            self.get_word_id("Supermassive Black Hole")
        ]
        self.word_list[51][STRONGER_WORDS_STR] = [
            # "Plague" is weaker than:
            self.get_word_id("Supernova")
        ]
        self.word_list[52][STRONGER_WORDS_STR] = [
            # "Rebirth" is weaker than:
            self.get_word_id("Supernova")
        ]
        self.word_list[53][STRONGER_WORDS_STR] = [
            # "Tectonic Shift" is weaker than:
            self.get_word_id("Supernova")
        ]
        self.word_list[54][STRONGER_WORDS_STR] = [
            # "Gamma-Ray Burst" is weaker than:
            self.get_word_id("Supernova")
        ]
        self.word_list[55][STRONGER_WORDS_STR] = [
            # "Human Spirit" is weaker than:
            self.get_word_id("Neutron Star")
        ]
        self.word_list[56][STRONGER_WORDS_STR] = [
            # "Apocalyptic Meteor" is weaker than:
            self.get_word_id("Supernova")
        ]
        self.word_list[57][STRONGER_WORDS_STR] = [
            # "Earth’s Core" is weaker than:
            self.get_word_id("Neutron Star")
        ]
        self.word_list[57][STRONGER_WORDS_STR] = [
            # "Earth's Core" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Gamma-Ray Burst"),
            self.get_word_id("Neutron Star")
        ]

        self.word_list[58][STRONGER_WORDS_STR] = [
            # "Neutron Star" is weaker than:
            self.get_word_id("Supernova"),
            self.get_word_id("Gamma-Ray Burst"),
            self.get_word_id("Black Hole")
        ]

        self.word_list[59][STRONGER_WORDS_STR] = [
            # "Supermassive Black Hole" is weaker than:
            self.get_word_id("Entropy"),
            self.get_word_id("Supernova"),
            self.get_word_id("Neutron Star")
        ]

        self.word_list[60][STRONGER_WORDS_STR] = [
            # "Entropy" is weaker than:
            self.get_word_id("Supermassive Black Hole"),
            self.get_word_id("Gamma-Ray Burst"),
            self.get_word_id("Big Bang")
        ]


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


    def get_stronger_words(self, word_id: int) -> List[int]:
        if word_id not in self.word_list:
            return None
        return self.word_list[word_id][STRONGER_WORDS_STR]
    

    def print_what_beats_what(self):
        for target_word_id in range(1, 61):
            target_word: str = self.get_word_text(target_word_id)
            print(f"\"{target_word}\" is weaker than: ", end='')
            for weaker_word_id in self.word_list[target_word_id][STRONGER_WORDS_STR]:
                weaker_word: str = self.get_word_text(weaker_word_id)
                print(f"\"{weaker_word}\" ", end='')
            print()



if __name__ == '__main__':
    wordlist = WordList()
    print(wordlist.get_stronger_words(1))
    wordlist.print_what_beats_what()