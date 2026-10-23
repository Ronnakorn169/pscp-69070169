"""docstring module"""
def main():
    """main function"""
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    ciphertext = "\n".join(lines)
    common_words = {
        "what", "when", "why", "which", "this", "there", "where",
        "the", "is", "am", "are", "you", "we", "they", "he", "she", "it"
    }
    max_matches = -1
    best_decrypted_text = ciphertext
    for shift in range(26):
        decrypted_chars = []
        for ch in ciphertext:
            if "a" <= ch <= "z":
                decrypted_chars.append(chr((ord(ch) - 97 - shift) % 26 + 97))
            elif "A" <= ch <= "Z":
                decrypted_chars.append(chr((ord(ch) - 65 - shift) % 26 + 65))
            else:
                decrypted_chars.append(ch)

        candidate_text = "".join(decrypted_chars)
        cleaned_chars = []
        for ch in candidate_text.lower():
            ch = ch if "a" <= ch <= "z" else " "
            cleaned_chars.append(ch)
        words = "".join(cleaned_chars).split()
        matches = 0
        for w in words:
            if w in common_words:
                matches += 1
        if matches > max_matches:
            max_matches = matches
            best_decrypted_text = candidate_text
    print(best_decrypted_text)
main()
