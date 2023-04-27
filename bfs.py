grap = {"A":["B","C"],
         "B":["D","E"],
         "C":["F","G"],
         "D":[],
         "E":[],
         "F":[],
         "G":[]}

# grap = {"0":["1","2"],
#         "1":["2"],
#         "2":["0","3"],
#         "3":["3"]
#        }

start = 'A'
goal = 'E'
open_list=[]


def bfs(grap, goal):
    open_list.append(start)
    visited = {node: False for node in grap.keys()}

    visited[start] = True
    while len(open_list) > 0:
        current= open_list.pop(0)
        print(current+" ---> ", end="")
        if current==goal:
            print("found")
            break

        for neighbors in grap[current]:
            if not visited[neighbors]:
                visited[neighbors] = True
                open_list.append(neighbors)
        

bfs(grap,goal)