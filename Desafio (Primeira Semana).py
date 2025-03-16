# (EASY) Read a first name and last name from input, then print "Hello firstname lastname! 
# You just delved into python." with the given names inserted. 

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# (INTERMEDIATE) Read a list of words, counting how many times each word appears while maintaining the order of their first appearance. 
# First, print the number of distinct words. Then, print the occurrence count of each word in order of appearance. 

def word_occurrences():
    n = int(input())  
    words = []  
    counts = {}  

    for i in range(n):
        word = input()
        if word not in counts:
            words.append(word)
            counts[word] = 0  
        counts[word] += 1 
    print(len(counts)) 
    print(" ".join(str(counts[word]) for word in words))  
if __name__ == "__main__":
    word_occurrences()

