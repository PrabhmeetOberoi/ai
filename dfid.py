tree = {'A': {
    'B': {
        'D': None,
        'E': None
    },
    'C': {
        'F': None,
        'G': None
    }
}}
q = list(tree.keys())
print(q)

goal = 'G'

def dfid(tree: dict, goal, current_depth, max_depth):
    q = list(tree.keys())
    #print(q)
    for node in q:
        print(node, "-> ", end="")
        if node == goal:
            print("Found")
            return True

        if tree[node]!=None and current_depth<max_depth and dfid(tree[node].copy(), goal, current_depth+1, max_depth):
            return True
    return False

found = False
for i in range(0,4):
    print(f"Searching at depth {i} : ")
    found = dfid(tree, goal, 0, i)
    if found:
        break