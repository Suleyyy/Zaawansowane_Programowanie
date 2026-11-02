from classes import MyFunctions
import pytest

obj = MyFunctions()


class TestmyTests:

    def test_is_palindrome(self) -> bool:
        assert obj.is_palindrome("kajak") is True
        assert obj.is_palindrome("Kobyła ma mały bok") is True
        assert obj.is_palindrome("python") is False
        assert obj.is_palindrome("") is True
        assert obj.is_palindrome("A") is True

    def test_fibonacci(self):
        assert obj.fibonacci(0) == 0
        assert obj.fibonacci(1) == 1
        assert obj.fibonacci(5) == 5
        assert obj.fibonacci(10) == 55
        assert obj.fibonacci(-1) is None

    def test_count_vowels(self):
        assert obj.count_vowels("Python") == 2
        assert obj.count_vowels("AEIOUY") == 6
        assert obj.count_vowels("bcd") == 0
        assert obj.count_vowels("") == 0
        assert obj.count_vowels("Próba żółwia") == 5

    def test_calculate_discount(self):
        assert obj.calculate_discount(100, 0.2) == 80
        assert obj.calculate_discount(50, 0) == 50
        assert obj.calculate_discount(200, 1) == 0
        with pytest.raises(ValueError):
            obj.calculate_discount(100, -0.1)
            obj.calculate_discount(100, 1.5)

    def test_flatten_list(self):
        assert obj.flatten_list([[1, 2, 3]]) == [1, 2, 3]
        assert obj.flatten_list([[1], [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
        assert obj.flatten_list([]) == []
        assert obj.flatten_list([[[1]]]) == [1]
        assert obj.flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    def test_word_frequencies(self):
        assert obj.word_frequencies("To be or not to be") == {
            "to": 2,
            "be": 2,
            "or": 1,
            "not": 1,
        }
        assert obj.word_frequencies("Hello, hello!") == {"hello": 2}
        assert obj.word_frequencies("") == {}
        assert obj.word_frequencies("Python Python python") == {"python": 3}
        assert obj.word_frequencies("Ala ma kota, a kot ma Ale") == {
            "ala": 1,
            "ma": 2,
            "kota": 1,
            "a": 1,
            "kot": 1,
            "ale": 1,
        }

    def test_is_prime(self):
        assert obj.is_prime(2) is True
        assert obj.is_prime(3) is True
        assert obj.is_prime(4) is False
        assert obj.is_prime(0) is False
        assert obj.is_prime(1) is False
        assert obj.is_prime(5) is True
        assert obj.is_prime(97) is True
