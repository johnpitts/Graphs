


















# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None


# 2: Build the Graph

# Load words from dictionary
f = open('words.txt', 'r')
words = f.read().lower().split("\n")
f.close()

def get_nieghbors(word):
    """
    Get all words that are one letter away from the given word
    """
    # Get the same-length words first

    result = []
    

# Create a counter that breaks if it goes higher than one and while loop through...

# Go thru each word and build an adjacency list with each word one letter a...

# Create an equality function
def words_are_neighbors(w1, w2):
    """
    return True if words are one letter apart
    False otherwise
    """
    list_word = list(w1)
    # Go thru each letter in the word
    for i in range(len(list_word)):
    # swap with each lettter in the alphabet
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:

        # check if that equals given word
        temp_word = list_word.copy()
        temp_word[i] = letter
        if "".join(temp_word) == w2:
            return True
        return False

def words_are_neighbors(w1, w2):
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
            return True
    return False

words_are_neighbors("abc", "abd")

nieghbors = {}

# Go through each word
for word in words:
    words[word] = set()
    # go thru each potential nieghbor
    for potential_nieghbor in words:
        # add to nieghbors if they match
        if words_are_neighbors(word, potential_nieghbor):
            nieghbors[word].add(potential_nieghbor)



from util import Stack, Queue # these may come in handy
# 3: Traverse the graph (BFS) (most efficient for finding a fast path)
def word_ladder(self, begin_word, end_word):
    """ return a 

    """

    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While queue is not empty
    while q.size() > 0:
        path - q.dequeue
    