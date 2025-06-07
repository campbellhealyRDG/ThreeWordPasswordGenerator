import random
import requests

# URL to a raw word list (plaintext, one word per line)
WORD_LIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"  # ~10K common English words

def load_remote_word_list(url, min_len=3, max_len=8):
    """Download and filter a remote word list."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        words = [word.strip().lower() for word in response.text.splitlines() if word.isalpha()]
        return [word for word in words if min_len <= len(word) <= max_len]
    except requests.RequestException as e:
        print(f"Error fetching word list: {e}")
        return []

def generate_passphrases(word_list, count=10):
    """Generate passphrases in 'word-word-word' format."""
    return ['-'.join(random.sample(word_list, 3)) for _ in range(count)]

if __name__ == "__main__":
    words = load_remote_word_list(WORD_LIST_URL)
    if not words:
        print("Failed to load word list.")
    else:
        passphrases = generate_passphrases(words)
        for phrase in passphrases:
            print(phrase)
