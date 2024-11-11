import random
def SelectWords(wordlst, count):
    if not isinstance(wordlst, list):
        print("Error; Input is not a 'list' variable.")
        return
    if count > len(wordlst):
        print("Error; Not enough words in list.")
        return
    if len(wordlst) == 0:
        print("Error; No words in list.")
        return
    chosen = []
    counter = 0
    while counter < count:
        random_int = random.randint(0, len(wordlst) - 1)
        chosen.append(wordlst[random_int])
        counter += 1
    return chosen