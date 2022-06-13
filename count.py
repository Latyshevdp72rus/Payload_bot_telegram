def count_text(val: int, words: list()):
    if all((val % 10 == 1, val % 100 != 11)):
        return words[0]
    elif all((2 <= val % 10 <= 4,
              any((val % 100 < 10, val % 100 >= 20)))):
        return words[1]

    return words[2]


def seconds_to_words(second: int) -> str:
    day, hour = divmod(second, (60 * 60 * 24))
    hour = hour // (60 * 60)
    return f'{day} ' + count_text(day, ['день', 'дня', 'дней']) + \
           f' {hour} ' + count_text(hour, ['час', 'часа', 'часов'])