'''
depth first search
breadth first search

*explore*:
    print this node
    *explore* all its unvisited neighbors
    return

explore
explore
explore
explore
explore
'''

def dft_recursive(self, start_vert, visited=None):
    print(start_vert)

    if visited is None:
        visited = set()

    visited.add(start_vert)

    for child_vert in self.vertices[start_vert]:
        if child_vert not in visited:
            self.dft_recursive(child_vert, visited)

def dfs_recursive(self, start_vert, visited=None, path=None):
    print(start_vert)

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(start_vert)

    # make a copy of the list, adding the new vert
    path = path + [start_vert]

    # base case
    if start_vert == target.value:
        return path

    for child_vert in self.vertices[start_vert]:
        if child_vert not in visited:
            new_path = self.dfs_recursive(child_vert, target_value, visited, path)

            if new_path:
                return new_path
        
    return None

g.dft_recursive(99)

'''
how to solve any graph problem
1. translate the problem into graph terminology
2. build the graph
3. traverse it

word ladders problem
begin: hit
end: cog

hit  > hot > cot > cog

begin: sail
end: boat

sail > bail > bait > b

begin: hungry
end: happy

None
'''

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            # did we react the end word?
            if v == end_word:
                return path
            
            for neighbor in get_neightbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)

                q.enqueue(path_copy)

# read all the words into a list
with open('words.txt') as f:
    word = f.read().split()

# put all words ina set for 0(1) access
word_set = set()

for w in words:
    word_set.ass(w.lower())

def get_neighbors(word):
    # we will return this
    neighbors = []

    # ['w', 'o', 'r', 'd']
    string_worod =  list(word)

    # for each letter...
    for i in range(len(string_word)):
        for letter in letters:
            # make a copy of the word so we can munge it up
            temp_word = list(string_word)
            # change into a new candidate word
            temp_word[i] = letter

            w = ''.join(temp_word)

            # if it is a valid word, it is a neighbor (but do not add a word as a neighbor to itself)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors