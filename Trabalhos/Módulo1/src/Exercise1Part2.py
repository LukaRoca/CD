import math
from collections import Counter
import matplotlib.pyplot as plt
import os

def calculate_entropy_and_frequent(text):
    if not text:
        return None, 0.0, {}
    
    freq = Counter(text)
    length = len(text)
    entropy = 0.0
    
    for count in freq.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
        
    most_frequent = freq.most_common(1)[0][0]
    return most_frequent, entropy, freq

def invert_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    inverted_content = content[::-1]
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(inverted_content)
            
    mf_in, ent_in, _ = calculate_entropy_and_frequent(content)
    mf_out, ent_out, _ = calculate_entropy_and_frequent(inverted_content)
    
    print(f"(h) Input {os.path.basename(input_filename)}: Most Frequent='{mf_in}', Entropy={ent_in:.4f}")
    print(f"(h) Output {os.path.basename(output_filename)}: Most Frequent='{mf_out}', Entropy={ent_out:.4f}")

def file_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    mf, ent, _ = calculate_entropy_and_frequent(content)
    print(f"(i) File {os.path.basename(filename)}: Most Frequent='{mf}', Entropy={ent:.4f}")

def plot_histogram_and_entropy(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    mf, ent, freq = calculate_entropy_and_frequent(content)
    print(f"(j) File {os.path.basename(filename)}: Entropy={ent:.4f}. Generating histogram...")
    
    symbols = list(freq.keys())
    counts = list(freq.values())
    
    plt.figure(figsize=(8, 4))
    plt.bar(symbols, counts, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of Symbols - {os.path.basename(filename)}")
    plt.xlabel("Symbols")
    plt.ylabel("Frequency")
    plt.show()

def setup_test_files(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    directory = os.path.join("Módulo1", "results")
    os.makedirs(directory, exist_ok=True)

    tf1 = os.path.join(directory, "test_file_1.txt")
    tf2 = os.path.join(directory, "test_file_2.txt")
    tf3 = os.path.join(directory, "test_file_3.txt")

    of1 = os.path.join(directory, "output_file_1.txt")
    of2 = os.path.join(directory, "output_file_2.txt")
    of3 = os.path.join(directory, "output_file_3.txt")

    setup_test_files(tf1, "ABCD1234")
    setup_test_files(tf2, "AAAAABBBCC")
    setup_test_files(tf3, "python programming is fun")

    print("--- Tests for (h) ---")
    invert_file(tf1, of1)
    invert_file(tf2, of2)
    invert_file(tf3, of3)

    print("\n--- Tests for (i) ---")
    file_statistics(tf1)
    file_statistics(tf2)
    file_statistics(tf3)

    print("\n--- Tests for (j) ---")
    plot_histogram_and_entropy(tf1)
    plot_histogram_and_entropy(tf2)
    plot_histogram_and_entropy(tf3)