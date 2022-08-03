import sys, threading
from typing import DefaultDict
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

graph=DefaultDict(list)
rev_graph=DefaultDict(list)
sccs=DefaultDict(list)

finish=1
def add_edge(graph,u,v):
        graph[u].append(v)
        if(v not in graph):
            graph[v]=[]


def second_recursive_search(graph,start,visited,scc):
    if not visited[start]:
        visited[start]=True
        for vertex in graph[start]:
            second_recursive_search(graph,vertex,visited,scc)
        scc.append(start)
        
    

    



            


def recursive_search(graph, start,visited,finish_times):
        global finish
        if not visited[start]:
            
            visited[start]=True
            for vertex in graph[start]:
               # print(vertex)
                
                recursive_search(graph,vertex,visited,finish_times)
            finish_times[finish]=start #eg first index will have the node which finished the first
            finish=finish+1
            
            
            
def main():
    
    file=open(r"/home/sukumar/Desktop/algorithams/test.txt")
    #print(start)
    for line in file:
        edge=line.strip("\n").split(" ")
        
        if len(edge) ==3:
            add_edge(graph,int(edge[0]),int(edge[1]))
            add_edge(rev_graph,int(edge[1]),int(edge[0]))
            
        
    visited= [False]*(len(graph.keys())+1)
    
    
    finish_times=[0]*(len(graph.keys())+1)
    

    for node in rev_graph:
       # print(node)
       recursive_search(rev_graph, node,visited,finish_times)
    
    visited= [False]*(len(graph.keys())+1)
    for node in reversed(finish_times[1:]):
        if not visited[node]:
            sccs[node]=[]


            
            second_recursive_search(graph,node,visited,sccs[node])
    
    l=list()
    for i in sccs:
        l.append(len(sccs[i]))

    l.sort()
    print(l[-5:])
        
        
    
        


   
    

    

   
   
 
    

    
    
        
        
  
    
    
 
  
thread = threading.Thread(target=main)
thread.start()