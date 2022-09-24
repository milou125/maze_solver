from collections import deque
from src.core.graph import expand_node, get_node_number, get_node_coordinates
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node
import math


def a_star_search(maze):


    export_tree = len(maze) <= 6
    
    index_maze_step = 1
   
    cur_node = 1
    
    if export_tree:
        
        Tree_maze.add_root(1)

    objective_node = get_node_number(maze,len(maze)  - 1 ,len(maze[0])-2)
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    frontier = deque([cur_node])
    reached = [cur_node]


    if(cur_node == objective_node): 
        return cur_node

    child_values = {}
    cordenadaP= get_node_coordinates(maze,cur_node)
    h_padre = sum(list(map(lambda x,y: abs(x-y) , cordenadaP, cordinates_objetive)))
    child_values[cur_node]=h_padre
    
    while frontier:
        
        cur_node = frontier.pop()
        children = expand_node(maze, cur_node)
        
        if(len(children)>0):

            cordenadaP= get_node_coordinates(maze,cur_node)
            h_padre = sum(list(map(lambda x,y: abs(x-y) , cordenadaP, cordinates_objetive)))
            c_padre= child_values[cur_node] - h_padre
    
            for child in children:
                
                cordenadaS = get_node_coordinates(maze,child) #calcula la coordenada del hijo
                c = c_padre + 1 #cálcula el costo de llegar hasta el hijo
                h = sum(list(map(lambda x,y: abs(x-y) , cordenadaS, cordinates_objetive))) #calcula la distancia manhattan
                child_values[child] = h + c
                
                if export_tree:
                    Tree_maze.add_node(child, cur_node)

                if(child == objective_node):
                   
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
                    return child 

                if find_node(reached, child): 
                    del child_values[child]
                
                if not find_node(reached, child): 
                    reached.append(child)
                    frontier.append(child)
            
            del child_values[cur_node] #elimina el valor del padre
                    
                
            next_node = min(child_values, key=child_values.get) #encuentro el nodo con distancia manhattan mas chiki
                
            frontier.remove(next_node) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
            frontier.append(next_node)
        
        print_maze(get_maze_step(maze, reached, list(frontier)), index_maze_step)
        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True
    Tree_maze.clear_generated_tree(export_tree)
