from config import RU_SYMBOLS, EN_SYMBOLS


class RuEnTranslater:
    def __init__(self, text: str):
        self.text = text
        self.ru_symbols = RU_SYMBOLS
        self.en_symbols = EN_SYMBOLS
        self._translate()

    def _translate(self):
        self.result = str()
        for i in self.text:
            self.result += self.ru_symbols[self.en_symbols.find(i)]

        # self.current_text = str()
        # for letter in self.text:
        #     for index, symbol in enumerate(self.en_symbols):
        #         if letter == symbol:
        #             self.current_text += self.ru_symbols[index]

    def __str__(self) -> str:
        # return self.current_text
        return self.result


# language = input('to english (eng) or to russian (рус)? ')
# text = input('Введите текст для перевода: ')
# print(RuEnTranslater(text))