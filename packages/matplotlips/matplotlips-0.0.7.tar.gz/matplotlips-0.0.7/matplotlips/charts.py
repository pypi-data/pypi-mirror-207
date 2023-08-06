def graph():
    ans = '''
    import networkx as nx

    def greedy_coloring(G):
        # Create a dictionary to store the color assigned to each node
        node_color = {}
        # Iterate over the nodes of the graph
        for node in G.nodes:
            # Initialize the set of used colors to be empty
            used_colors = set()
            # Iterate over the neighbors of the current node
            for neighbor in G.neighbors(node):
                # If the neighbor has already been colored, add its color to the set of used colors
                if neighbor in node_color:
                    used_colors.add(node_color[neighbor])
            # Find the minimum unused color
            for color in range(len(G)):
                if color not in used_colors:
                    break
            # Assign the minimum unused color to the current node
            node_color[node] = color
        # Return the dictionary of node colors
        return node_color

    # Example usage:
    G = nx.Graph()
    G.add_nodes_from([1,2,3,4,5])
    G.add_edges_from([(1,2), (1,3), (2,4), (3,5), (4,5)])

    node_color = greedy_coloring(G)
    num_colors = max(node_color.values()) + 1

    print("Minimum number of colors required:", num_colors)
    '''
    return(ans)

def banana():
    ans = '''
    dp = [[-1 for i in range(3001)] for j in range(1001)]
    def recBananaCnt(A, B, C):
        if (B <= A):
            return 0
        if (B <= C):
            return B - A
        if (A == 0):
            return B
        if (dp[A][B] != -1):
            return dp[A][B]
        maxCount = -2**32
        tripCount = ((2 * B) // C) - 1 if (B % C == 0) else ((2 * B) // C) + 1
        for i in range(1, A+1):
            curCount = recBananaCnt(A - i, B - tripCount * i, C)
            if (curCount > maxCount):
                maxCount = curCount
                dp[A][B] = maxCount
        return maxCount


    def maxBananaCnt(A, B, C):
        print("Calculating...")
        return recBananaCnt(A, B, C)


    A = 1000
    B = 3000
    C = 1000
    print(maxBananaCnt(A, B, C))
    '''
    return(ans)


def nlp():
    ans = '''
    import nltk
    nltk.download('vader_lexicon')

    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    # Initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Sample text for analysis
    text = "I really enjoyed this movie. The acting was great and the plot was engaging."

    # Calculate the sentiment score for the text
    score = sia.polarity_scores(text)

    # Print the sentiment score
    print("negative = ", score["neg"])
    print("neutral = ", score["neu"])
    print("positive = ", score["pos"])
    print("compound = ", score["compound"])
    ''' 
    return(ans)

def logistic():
    ans = '''
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    # Load the breast cancer dataset
    cancer = load_breast_cancer()

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, test_size=0.2, random_state=42)

    # Create a logistic regression model
    lr_model = LogisticRegression()

    # Train the model on the training data
    lr_model.fit(X_train, y_train)

    # Predict the target values for the test data
    y_pred = lr_model.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = lr_model.score(X_test, y_test)

    # Print the accuracy as a percentage
    print("Logistic Regression Accuracy: {:.2f}%".format(accuracy*100))
    ''' 
    return(ans)


# Monty Hall Game in Python
def montyhall():
    ans = '''
    import random

    def play_monty_hall(choice):
        # Prizes behind the door
        # initial ordering doesn't matter
        prizes = ['goat', 'car', 'goat']
        
        # Randomizing the prizes
        random.shuffle(prizes) 
        
        # Determining door without car to open
        while True:
            opening_door = random.randrange(len(prizes))
            if prizes[opening_door] != 'car' and choice-1 != opening_door:
                break
        
        opening_door = opening_door + 1
        print('We are opening the door number-%d' % (opening_door))
        
        # Determining switching door
        options = [1,2,3]
        options.remove(choice)
        options.remove(opening_door)
        switching_door = options[0]
            # Asking for switching the option
        print('Now, do you want to switch to door number-%d? (yes/no)' %(switching_door))
        answer = input()
        if answer == 'yes':
            result = switching_door - 1
        else:
            result = choice - 1
        
        # Displaying the player's prize 
        print('And your prize is ....', prizes[result].upper())
        
    # Reading initial choice
    choice = int(input('Which door do you want to choose? (1,2,3): '))

    # Playing game
    play_monty_hall(choice)
    ''' 
    return(ans)


def astar():
    ans = '''
    from queue import PriorityQueue


    class Graph:
        def _init_(self, adjacency_list):
            self.adjacency_list = adjacency_list

        def get_neighbors(self, v):
            return self.adjacency_list[v]

        def h(self, n):
            H = {
                'A': 1,
                'B': 1,
                'C': 1,
                'D': 1
            }

            return H[n]

        def best_first_search(self, start, goal):
            explored = []
            pq = PriorityQueue()
            pq.put((0, start))
            parents = {start: None}

            while not pq.empty():
                current = pq.get()[1]

                if current == goal:
                    path = []
                    while current is not None:
                        path.append(current)
                        current = parents[current]
                    path.reverse()
                    print(f"Best-First Search path: {path}")
                    return path

                explored.append(current)

                for neighbor, weight in self.get_neighbors(current):
                    if neighbor not in explored and neighbor not in [i[1] for i in pq.queue]:
                        parents[neighbor] = current
                        pq.put((self.h(neighbor), neighbor))

            print("Path not found!")
            return None

        def a_star_algorithm(self, start_node, stop_node):
            open_list = set([start_node])
            closed_list = set([])
            g = {}

            g[start_node] = 0
            parents = {}
            parents[start_node] = start_node

            while len(open_list) > 0:
                n = None
                for v in open_list:
                    if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                        n = v

                if n == None:
                    print('Path does not exist!')
                    return None
                if n == stop_node:
                    reconst_path = []

                    while parents[n] != n:
                        reconst_path.append(n)
                        n = parents[n]

                    reconst_path.append(start_node)

                    reconst_path.reverse()

                    print('A* path: {}'.format(reconst_path))
                    return reconst_path

                for (m, weight) in self.get_neighbors(n):
                    if m not in open_list and m not in closed_list:
                        open_list.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n

                            if m in closed_list:
                                closed_list.remove(m)
                                open_list.add(m)
                open_list.remove(n)
                closed_list.add(n)

            print('Path does not exist!')
            return None


    adjacency_list = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }
    graph1 = Graph(adjacency_list)
    graph1.best_first_search('A', 'D')
    graph1.a_star_algorithm('A', 'D')
    ''' 
    return(ans)


def bfsdfs():
    ans = '''
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    visited_bfs = []
    queue = []


    def bfs(visited_bfs, graph, node):
    visited_bfs.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
        if neighbour not in visited_bfs:
            visited_bfs.append(neighbour)
            queue.append(neighbour)


    visited = set()


    def dfs(visited, graph, node):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)


    print("BFS:", end=" ")
    bfs(visited_bfs, graph, 'A')
    print('\n')
    print("DFS:", end=" ")
    dfs(visited, graph, 'A')
    ''' 
    return(ans)


def help():
    ans = '''
    EXP1: CAMEL BANANA PROBLEM ***code : print(charts.banana())***
    EXP2: GRAPH COLOURING ***code : print(charts.graph())***
    EXP3: 
    EXP4: DEPTH FIRST SEARCH/ BREADTH FIRST SEARCH ***code : print(charts.bfs())***
    EXP5: BEST FIRST SEARCH / A* ALGORITHM ***code: print(charts.astar())***
    EXP6: MONTY HALL PROBLEM ***code: print(charts.montyhall())***
    EXP7:
    EXP8: LOGISTIC REGRESSION ***code : print(charts.logistic())***
    EXP9: NLP ***code : print(charts.nlp())***
    EXP10: DL ***code : print(charts.dl())***
    ''' 
    return(ans)

def menu():
    ans = '''
    EXP1: CAMEL BANANA PROBLEM ***code : print(charts.banana())***
    EXP2: GRAPH COLOURING ***code : print(charts.graph())***
    EXP3: 
    EXP4: DEPTH FIRST SEARCH/ BREADTH FIRST SEARCH ***code : print(charts.bfs())***
    EXP5: BEST FIRST SEARCH / A* ALGORITHM ***code: print(charts.astar())***
    EXP6: MONTY HALL PROBLEM ***code: print(charts.montyhall())***
    EXP7:
    EXP8: LOGISTIC REGRESSION ***code : print(charts.logistic())***
    EXP9: NLP ***code : print(charts.nlp())***
    EXP10: DL ***code : print(charts.dl())***
    ''' 
    return(ans)


def all():
    ans = '''
    EXP1: CAMEL BANANA PROBLEM ***code : print(charts.banana())***
    EXP2: GRAPH COLOURING ***code : print(charts.graph())***
    EXP3: 
    EXP4: DEPTH FIRST SEARCH/ BREADTH FIRST SEARCH ***code : print(charts.bfs())***
    EXP5: BEST FIRST SEARCH / A* ALGORITHM ***code: print(charts.astar())***
    EXP6: MONTY HALL PROBLEM ***code: print(charts.montyhall())***
    EXP7:
    EXP8: LOGISTIC REGRESSION ***code : print(charts.logistic())***
    EXP9: NLP ***code : print(charts.nlp())***
    EXP10: DL ***code : print(charts.dl())***
    ''' 
    return(ans)