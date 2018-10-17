"""script to profile different solutions"""
import l370
import l370b
import sys
import random
import string
import time

def generate_input(input_size):
    """generate a random input of input_size 
    proportional to 'input_size' (int) for l370"""
    words = ['balla', 'assdd']
    append_random(words, input_size)
    words.append('areae')
    append_random(words, input_size)
    words.append('lekbc')
    append_random(words, input_size)
    words.append('labyd')
    append_random(words, input_size)
    words.append('aecdz')
    return words

def append_random(words, input_size):
    """append random strings to words"""
    letters = string.letters[:26]
    for _ in xrange(input_size):
        new_string = ""
        for _ in xrange(5):
            new_string += (random.choice(letters))
        words.append(new_string)


if __name__ == "__main__":
    input_size = int(sys.argv[1])
    generated_input = generate_input(input_size)
    print len(generated_input)
    
    solution1 = l370.Solution()
    solution2 = l370b.Solution()

    print "solution1"
    start = time.time()
    res1 = solution1.wordSquares(generated_input)
    end = time.time()
    print end-start
    
    print "solution2"
    start = time.time()
    res2 = solution2.wordSquares(generated_input)
    end = time.time()
    print end-start

    print ""
    print res1
    print res2
