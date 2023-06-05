# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
# Never Gonna Give You Up
POKEMON_LYRICS = "We\'re no strangers to love You know the rules and so do I (do I) A full commitment\'s what I\'m thinking of You wouldn\'t get this from any other guy I just wanna tell you how I\'m feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We\'ve known each other for so long Your heart\'s been aching, but you\'re too shy to say it (say it) Inside, we both know what\'s been going on (going on) We know the game and we\'re gonna play it And if you ask me how I\'m feeling Don\'t tell me you\'re too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We\'ve known each other for so long Your heart\'s been aching, but you\'re too shy to say it (to say it) Inside, we both know what\'s been going on (going on) We know the game and we\'re gonna play it I just wanna tell you how I\'m feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you I did not use the tutoring option because my friend offered to help me out. She did a great job, but I think I struggled during the midterm because there was only 50 minutes and I was unable to solve the problems fast enough. I\'m planning to enroll in the course again during the fall. Is there anything else I need to do to be eligible for grade forgiveness? Thank you for your time and consideration."
# You've Got a Friend in Me
JIGGLE_JIGGLE = "You\'ve got a friend in me You\'ve got a friend in me When the road looks rough ahead And you\'re miles and miles From your nice warm bed You just remember what your old pal said Boy, you\'ve got a friend in me Yeah, you\'ve got a friend in me You\'ve got a friend in me You\'ve got a friend in me You got troubles, I\'ve got \'em too There isn\'t anything I wouldn\'t do for you We stick together and see it through \'Cause you\'ve got a friend in me You\'ve got a friend in me Some other folks might be A little bit smarter than I am Bigger and stronger too Maybe But none of them will ever love you The way I do It\'s me and you, boy And as the years go by Our friendship will never die You\'re gonna see it\'s our destiny You\'ve got a friend in me You\'ve got a friend in me You\'ve got a friend in me"
# Sunflower
ALPHABET = 'Ayy, ayy, ayy, ayy (ooh) Ooh, ooh, ooh, ooh (ooh) Ayy, ayy Ooh, ooh, ooh, ooh Needless to say, I keep her in check She was a bad-bad, nevertheless (yeah) Callin\' it quits now, baby, I\'m a wreck (wreck) Crash at my place, baby, you\'re a wreck (wreck) Needless to say, I\'m keeping her in check She was all bad-bad, nevertheless Callin\' it quits now, baby, I\'m a wreck Crash at my place, baby, you\'re a wreck Thinkin\' in a bad way, losin\' your grip Screamin\' at my face, baby, don\'t trip Someone took a big L, don\'t know how that felt Lookin\' at you sideways, party on tilt Ooh-ooh-ooh Some things you just can\'t refuse She wanna ride me like a cruise And I\'m not tryna lose Then you\'re left in the dust Unless I stuck by ya You\'re the sunflower I think your love would be too much Or you\'ll be left in the dust Unless I stuck by ya You\'re the sunflower You\'re the sunflower Every time I\'m leavin\' on you (ooh) You don\'t make it easy, no (no, no) Wish I could be there for you Give me a reason to, oh (oh) Every time I\'m walkin\' out I can hear you tellin\' me to turn around Fightin\' for my trust and you won\'t back down Even if we gotta risk it all right now, oh (now) I know you\'re scared of the unknown (\'known) You don\'t wanna be alone (alone) I know I always come and go (and go) But it\'s out of my control And you\'ll be left in the dust Unless I stuck by ya You\'re the sunflower I think your love would be too much Or you\'ll be left in the dust Unless I stuck by ya You\'re the sunflower You\'re the sunflower (yeah)'


# DATA - mantras
#Team Rocket
GREEN_LATTERN = "Prepare for trouble! And make it double! To protect the world from devastation! To unite all peoples within our nation! To denounce the evils of truth and love! To extend our reach to the stars above! Jessie! James! Team Rocket blasts off at the speed of light! Surrender now, or prepare to fight! Meowth! That\'s right!"
#Spiderman
JEDI_CODE = 'with great power there must also come – great responsibility'
#Ratatouille
SITH_CODE = "anyone can cook"

# STEP 0 - TODO
## defining our data structures
class Node:  # NOT given to students
    def __init__(self, weight, letter):
        self.weight = weight
        self.letter = letter
        self.left = None
        self.right = None

# the input, what we want to encode
def huffman(message:str) -> float:
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

    def retrieve_codes(v: Node, path: str = ''):
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

    print(len(nodes))


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
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio


# LYRICS

plt.subplot(2, 1, 1)
plt.ylabel("Compression %")



MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## Rick Roll
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = POKEMON_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)


plt.plot(ratios,linestyle='-.' , label = "Rick Roll (n=25)")


## YGAFIM
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = JIGGLE_JIGGLE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,linestyle='-.', label = "You've Got a Friend in Me (n=26)")

## Sunflower
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = ALPHABET[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,linestyle='-.', label = 'Sunflower (n=27)')

plt.title("Lab 7 - Nguyen Analyzing Huffman")
plt.xlabel("x")
plt.legend(loc='upper right')



# PLOT 2x
plt.subplot(2, 1, 2)
plt.ylabel("Compression %")
plt.xlabel("length of message")


## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = SITH_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,linestyle='-.', label="Ratatouille (n=8)")

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = GREEN_LATTERN[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,linestyle='-.', label="Team Rocket (n=23)")

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = JEDI_CODE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,linestyle='-.', label="Spiderman (n=20)")

plt.legend(loc='upper right')

plt.savefig("./figs/lab7_nguyen.png")
plt.show()