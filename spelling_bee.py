from itertools import product

def generate_permutations(characters, length):
    return [''.join(p) for p in product(characters, repeat=length)]

def main():
    path = "/Users/aadhav/uni/projects/wordlist.10000"
    special = 'o'
    characters = 'grivly'
    permutations = set()
    for i in range(3,6):
        perms = generate_permutations(characters, i)
        for perm in perms:
            for j in range(i):
                permutations.add(perm[:j] + special + perm[j:])
    answer = []
    with open(path, "r") as word_list:
        words = [s.rstrip('\n') for s in word_list.readlines()]
        for word in list(permutations):
            if word in words:
                answer.append(word)
        
    print(answer)

main()
