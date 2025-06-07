import random

def load_word_list(path="/usr/share/dict/words", min_len=3, max_len=8):
    """Loads a list of words from a file with length filtering."""
    with open(path) as f:
        words = [word.strip().lower() for word in f if word.isalpha()]
    return [word for word in words if min_len <= len(word) <= max_len]

def generate_passphrase(word_list, count=10):
    """Generates a list of passphrases in the word-word-word format."""
    return [
        '-'.join(random.sample(word_list, 3))
        for _ in range(count)
    ]

if __name__ == "__main__":
    words = load_word_list()
    passphrases = generate_passphrase(words)
    for phrase in passphrases:
        print(phrase)
