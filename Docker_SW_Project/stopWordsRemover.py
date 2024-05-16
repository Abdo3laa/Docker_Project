import re
from collections import Counter

# Function to read the contents of a file
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Function to remove stop words from text
def remove_stopwords(text, stopwords):
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if word not in stopwords]

# Function to count word frequency
def count_word_frequency(words):
    return Counter(words)

# Main function
def main():
    # Read the contents of the file
    file_content = read_file("random_paragraphs.txt")
    
    # Define stop words (you can add more as needed)
    stopwords = {"the", "a", "an", "and", "in", "on", "of", "to", "for", "with", "is", "are"}
    
    # Remove stop words
    words_without_stopwords = remove_stopwords(file_content, stopwords)
    
    # Count word frequency
    word_frequency = count_word_frequency(words_without_stopwords)
    
    # Display word frequency count
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
