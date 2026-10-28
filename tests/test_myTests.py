from main import MyFunctions
import pytest

obj = MyFunctions()

class TestmyTests:


    def test_is_palindrome(self) -> bool:
        assert obj.is_palindrome("kajak") == True
        assert obj.is_palindrome("Kobyła ma mały bok") == True
        assert obj.is_palindrome("python") == False
        assert obj.is_palindrome("") == True
        assert obj.is_palindrome("A") == True

    def test_fibonacci(self):
        assert obj.fibonacci(0) == 0
        assert obj.fibonacci(1) == 1
        assert obj.fibonacci(5) == 5
        assert obj.fibonacci(10) == 55
        assert obj.fibonacci(-1) == None

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
