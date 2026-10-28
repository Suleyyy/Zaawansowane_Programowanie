class MyFunctions:
    def __init__(self):
        pass

    def is_palindrome(self, text: str) -> bool:
        return text.lower().replace(" ", "") == text[::-1].lower().replace(" ", "")

    def fibonacci(self, n: int) -> int:
        if n < 0:
            return None
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def count_vowels(self, text: str) -> int:
        vowels = ['a','e', 'i', 'o', 'u', 'y', 'ó']
        count = 0
        for i in text.lower():
            if i in vowels:
                count +=1
        return count

    def calculate_discount(self, price: float, discount: float) -> float:
        if discount > 1 or discount < 0:
            raise ValueError()
        return price - price*discount

    def flatten_list(self, nested_list: list) -> list:
        return [x for sub in nested_list for x in sub]

    def word_frequencies(self, text: str) -> dict:
        words = {}
        for i in text.lower().split(" "):
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
        return words

    def is_prime(self, n: int) -> bool:
        count = 0
        for i in range(1, n):
            if n % i == 0:
                count +=1
            if count > 2:
                return False
        return True



