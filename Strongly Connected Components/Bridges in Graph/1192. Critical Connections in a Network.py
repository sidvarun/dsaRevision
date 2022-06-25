
# we assign a rank ot each node based on the dfs call. root is assigned 0 and and root calls its neighbours and gives it a discovery rank of 1 and so on
# a cycle is presesnt when a high rank node makes a call to a low rank node
# so when we call for dfs of any node if rank if already assigned to that node is rank[] array 



# An edge is a critical connection, if and only if it is not in a cycle.

# Edges that are not a part of the cycle end up being a single route from getting from one part of the graph to the other. 
# Why, you ask? Well if there were multiple ways, then our edge would be a part of the cycle considering this is an undirected graph. 
# Thus, edges not belonging to any cycle end up being a critical connection for the graph.

# Thus, the problem simply boils down to finding all the cycles in the graph and discarding all the edges belonging to such cycles. 
# If we do that, we will only be left with edges that are critical connections in the graph.



# Inside our function dfs:

# We check if the node already has a rank assigned; if so, we return that value.

# Else, we assign the rank of this node i.e. rank[node] to the discoveryRank.

# We iterate over all the neighbors of the node and for each of them, we make a recursive call and we obtain the recursiveRank as the return value and do two things using this value.

# If this recursiveRank is less than the current discoveryRank, that implies this edge is a part of a cycle and can be discarded.
# Second, we record the minimum rank till now from amongst all the neighbors. Let's name this minRank. This is the value we return at the end of the function.
# Note that we don't make a recursive call to the parent node. We detect parent nodes by checking if the rank of the neighboring node is discoveryRank - 1

# Return the minRank.

class Solution:
    
    rank = {}
    graph = defaultdict(list)
    conn_dict = {}
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.formGraph(n, connections)
        self.dfs(0, 0)
        
        result = []
        for u, v in self.conn_dict:
            result.append([u, v])
        
        return result
            
    def dfs(self, node: int, discovery_rank: int) -> int:
        
        # That means this node is already visited. We simply return the rank.
        if self.rank[node]:
            return self.rank[node]
        
        # Update the rank of this node.
        self.rank[node] = discovery_rank
        
        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank
        for neighbor in self.graph[node]:
            
            # Skip the parent.
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue
                
            # Recurse on the neighbor.    
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            
            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]
            
            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)
        
        return min_rank
    
    def formGraph(self, n: int, connections: List[List[int]]):
        
        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}
        
        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None
        
        for edge in connections:
            
            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)
            
            self.conn_dict[(min(u, v), max(u, v))] = 1