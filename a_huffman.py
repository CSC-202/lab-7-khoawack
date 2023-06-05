# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'
message = message.upper()

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0
## defining our data structures
class Node:  # NOT given to students
    def __init__(self, weight, letter):
        self.weight = weight
        self.letter = letter
        self.left = None
        self.right = None

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str = ''):
    global coding
    if v.letter is not None:
        coding[v.letter] = path
    else:
        retrieve_codes(v.left, path + '0')
        retrieve_codes(v.right, path + '1')


# STEP 1
## counting the frequencies - TODO
for i in message:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1


# STEP 2
## initialize the nodes - TODO
nodes = []
for letter, frequency in freq.items():
    nodes.append(Node(frequency, letter))


# STEP 3 
## combine nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a = nodes.pop()

    ## get the second min
    min_b = nodes.pop()

    ## combine the two
    combined = Node(min_a.weight + min_b.weight, None)
    combined.left = min_a
    combined.right = min_b

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)


# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
result = ''
for letter in message:
    result += coding[letter]


# STEP 5
## analyze compression performance
n_original_bits = len(message) * 8
n_encoded_bits = len(result)
compression_ratio = (1 - n_encoded_bits / n_original_bits) * 100

print(freq)
print(message)
print(coding)
print(result)
print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')
