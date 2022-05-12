def score(pos, sector=None):
    scoring = {
        "Яблочко": 50,
        "Зеленое кольцо": 25,
        "Внешнее кольцо": {
            "1": 8,
            "2": 6,
            "3": 42,
            "20": 50
        },
        "Внутреннее кольцо": {
            "1": 2,
            "2": 9,
            "3": 56,
            "20": 3
        }
    }
    if sector is None:
        return scoring.get(pos)
    return scoring.get(pos)[sector]


print(score("Внешнее кольцо", "1"))