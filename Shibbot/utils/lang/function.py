from .english import English
from .french import French

english_inst = English()
french_inst = French()


def fl(language: str = "en") -> English:
    """Factory language method."""
    languages = {
        "en": english_inst,
        "fr": french_inst,
    }
    return languages[language]
