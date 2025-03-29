import requests
from time import sleep
import random

from word_beater import WordBeater
from word_list import WordList


host = "http://172.18.4.158:8000"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

PLAYER_ID = 'team bogdan'
NUM_ROUNDS = 5


def what_beats(word):
    sleep(random.randint(1, 3))
    return random.randint(1, 60)

def play_game():
    word_beater = WordBeater()

    for round_id in range(1, NUM_ROUNDS+1):
        print(f"#### ROUND {round_id} ####")
        round_num = -1 
        while round_num != round_id:
            response = requests.get(get_url)
            # print(response.json())
            sys_word = response.json()['word']
            round_num = response.json()['round']

            sleep(1)

        if round_id > 1:
            status = requests.get(status_url)
            # print(status.json())

        print(f"System word to beat: '{sys_word}'")
        choosen_word = word_beater.select_best_word(sys_word)
        if choosen_word is None:
            choosen_word = 'Supernova'
        choosen_word_id: int = word_beater.word_list.get_word_id(choosen_word)
        print(f"My algorithm selected to beat '{sys_word}' with '{choosen_word}' of id='{choosen_word_id}'")
        data = {"player_id": PLAYER_ID, "word_id": choosen_word_id, "round_id": round_id}
        response = requests.post(post_url, json=data)
        print(response.json())
        print()


if __name__ == '__main__':
    response = requests.get(get_url)
    print(response.json)
    play_game()
