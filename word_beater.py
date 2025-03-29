from typing import List
from word_list import WordList


class WordBeater():
    def __init__(self):
        self.word_list = WordList()


    def select_best_word(self, target_word: str) -> str:
        # Căutăm id-ul cuvântului țintă în lista de cuvinte
        target_word_id: int = self.word_list.get_word_id(target_word)
        if not target_word_id:
            raise ValueError(f"Cuvântul '{target_word}' nu a fost găsit în lista de cuvinte.")

        best_word = None
        best_score = -1
        best_cost = float('inf')

        # Iterăm prin toate cuvintele (de la 1 la 60) pentru a găsi cel mai bun cuvânt
        for word_id in range(1, 61):
            word_data = self.word_list.get_word_data(word_id)
            if not word_data:
                continue

            word_text = word_data["text"]
            word_cost = word_data["cost"]
            word_id = self.word_list.get_word_id(word_text)
            stronger_words = self.word_list.get_stronger_words(word_id)

            # Dacă cuvântul curent este în lista de cuvinte puternice ale țintei
            if target_word_id in stronger_words:
                in_degree = len(stronger_words)

                # Alegem cuvântul cu cel mai mare in-degree, iar dacă sunt egale, alegem cuvântul cu costul minim
                if in_degree > best_score or (in_degree == best_score and word_cost < best_cost):
                    best_word = word_text
                    best_score = in_degree
                    best_cost = word_cost

        return best_word


# Exemplu de utilizare:
if __name__ == '__main__':
    wordbeater = WordBeater()
    target_word = "Chalk"  # Exemplu de cuvânt țintă
    best_word = wordbeater.select_best_word(target_word)
    print(f"Cel mai bun cuvânt care bate '{target_word}' este: {best_word}")