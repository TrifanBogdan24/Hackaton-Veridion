from typing import List
from word_list import WordList

def select_best_word(wordlist: WordList) -> str:
    best_word = None
    best_score = -1
    best_cost = float('inf')

    # Iterăm prin toate cuvintele (de la 1 la 60)
    for word_id in range(1, 61):
        word_data = wordlist.get_word_data(word_id)
        if not word_data:
            continue

        word_text = word_data["text"]
        word_cost = word_data["cost"]
        weaker_words = wordlist.get_weaker_words(word_id)

        # Calculăm out-degree (câte cuvinte poate învinge)
        out_degree = len(weaker_words)

        # Se aplică logica de selecție:
        # Alegem cuvântul cu cel mai mare out-degree (numărul de cuvinte învinse)
        # Dacă există o legătura între out-degree și cost, alegem cuvântul cu costul minim
        if out_degree > best_score or (out_degree == best_score and word_cost < best_cost):
            best_word = word_text
            best_score = out_degree
            best_cost = word_cost

    return best_word


# Exemplu de utilizare:
if __name__ == '__main__':
    wordlist = WordList()
    best_word = select_best_word(wordlist)
    print("Cel mai bun cuvânt este:", best_word)
