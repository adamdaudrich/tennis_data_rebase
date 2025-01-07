from rapidfuzz import fuzz, process

def compare_strings(string1, string2):
    """Compares two strings and returns their similarity score."""
    score = fuzz.ratio(string1, string2)
    return score

# Example usage
string1 = "Roger Federer"
string2 = "Federer"
similarity_score = compare_strings(string1, string2)

print(f"Similarity Score: {similarity_score}")
