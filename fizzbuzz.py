class Rule:
    def apply(self, number):
        pass

class Fizz(Rule):
    def apply(self, number):
        if '2' in str(number) or number % 2 == 0:
            return "Fizz"
        else:
            return str(number)

class Buzz(Rule):
    def apply(self, number):
        if '5' in str(number) or number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

class FizzBuzz(Rule):
    def apply(self, number):
        if ('2' in str(number) and '5' in str(number)) or (number % 2 == 0 and number % 5 == 0):
            return "Fizz-Buzz"
        elif '2' in str(number) or number % 2 == 0:
            return "Fizz"
        elif '5' in str(number) or number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

class FizzBuzzGame:
    def __init__(self, rules):
        self.rules = rules

    def play(self, number):
        result = str(number)
        for rule in self.rules:
            result = rule.apply(number)
            if result != str(number):
                break
        return result
