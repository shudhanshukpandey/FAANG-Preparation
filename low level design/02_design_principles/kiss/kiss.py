"""KISS Principle: Favoring simple, readable solutions over unnecessary complexity."""

from abc import ABC, abstractmethod


# -------------------------------------------------------------
# Anti-Pattern: Over-engineered Palindrome Checker
# -------------------------------------------------------------
class ICharacterEvaluator(ABC):
    @abstractmethod
    def evaluate(self, char1: str, char2: str) -> bool:
        pass


class CaseInsensitiveEvaluator(ICharacterEvaluator):
    def evaluate(self, char1: str, char2: str) -> bool:
        return char1.lower() == char2.lower()


class PalindromeServiceOverengineered:
    def __init__(self, evaluator: ICharacterEvaluator) -> None:
        self.evaluator = evaluator

    def is_palindrome(self, text: str) -> bool:
        left, right = 0, len(text) - 1
        while left < right:
            if not self.evaluator.evaluate(text[left], text[right]):
                return False
            left += 1
            right -= 1
        return True


# -------------------------------------------------------------
# Clean Refactor: KISS
# -------------------------------------------------------------
def is_palindrome_kiss(text: str) -> bool:
    """Clean, pythonic, and immediately understandable in 1 line."""
    cleaned = text.lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_word = "Racecar"

    # Anti-pattern call
    complex_service = PalindromeServiceOverengineered(CaseInsensitiveEvaluator())
    print(f"Overengineered result for '{test_word}': {complex_service.is_palindrome(test_word)}")

    # KISS call
    print(f"KISS result for '{test_word}': {is_palindrome_kiss(test_word)}")
