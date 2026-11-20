class TextInput:
    def __init__(self):
        self.value = ""

    def add(self, character):
        self.value += character

    def get_value(self):
        return self.value


class NumericInput(TextInput):
    def add(self, character):
        if character.isdigit():
            super().add(character)   


input = TextInput()
input.add("1")
input.add("a")
input.add("0")
print(input.get_value())