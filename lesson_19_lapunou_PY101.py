def Cards():

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] #сохдаем список имеющихся карт

    suit_of_cards = ["Diamonds", "Hearts", "Clubs", "Spades"] # создаем список имеющихся мастер карт
    for i in cards:
        for k in suit_of_cards:
            yield str(i) + ' ' + str(k)

allcards = Cards()
print(allcards)

count_ = 1

while count_ <= 52:
    print(count_, '-', next(allcards))
    count_ += 1
    if count_ > 52:
        raise StopIteration


