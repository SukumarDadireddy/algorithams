from typing import DefaultDict
import heapq
graph=DefaultDict(list)
file=open(r"/home/sukumar/Desktop/algorithams/dijkstraData.txt")

for line in file:
    edges=line.split("\t")
    #print(edges)
    for edge in edges[1:-1]:
        #print(edge+"----")
        target_node=int(edge.split(",")[0])
        distance=int(edge.split(",")[1])
        graph[int(edges[0])].append([target_node,distance])




unexplored=[]
visited= [False]*(len(graph.keys())+1)
short_distance=[1000000]*(len(graph.keys())+1)
heapq.heappush(unexplored,(0,1))




while(len(unexplored)!=0):
    #print(unexplored)
    (greedy_score,explored_node)=heapq.heappop(unexplored)
    #print(explored_node)
    if not visited[explored_node]:
        #print("in")
        visited[explored_node]=True
        short_distance[explored_node]=greedy_score

        for unexplored_node in graph[explored_node]:
            heapq.heappush(unexplored,(greedy_score+unexplored_node[1],unexplored_node[0]))


for i in [7,37,59,82,99,115,133,165,188,197]:
    print(short_distance[i],end=",")

    







