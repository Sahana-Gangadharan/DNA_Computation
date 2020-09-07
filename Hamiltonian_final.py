import networkx as nx
import random as r

def Hamiltonian_path(G):
    Edges = []
    for line in nx.generate_edgelist(G,data=False):
        x=int(line[0])
        y=int(line[2])
        Edges.append((x,y))
    nn = len(G)
    ne = len(Edges)
    Nodes = ['']*nn
    EdgesDNA = ['']*ne
    
    #Random synthesis of Nodes
    for i in range(nn):
        for j in range(20):
            a = r.randint(1,4);
            if a==1:
                Nodes[i]+='A'
            if a==2:
                Nodes[i]+='T'
            if a==3:
                Nodes[i]+='G'
            if a==4:
                Nodes[i]+='C'

    #Synthesis of DNA Edges according to given list of edges and the nodes synthesized earlier.
    for i in range(ne):
        if Edges[i][0]==0:
            EdgesDNA[i]+=Nodes[0]
            EdgesDNA[i]+=Nodes[Edges[i][1]][:10]
        elif Edges[i][1]==(nn-1):
            EdgesDNA[i]+=Nodes[Edges[i][0]][10:]
            EdgesDNA[i]+=Nodes[-1]
        else:
            EdgesDNA[i]+=Nodes[Edges[i][0]][10:]
            EdgesDNA[i]+=Nodes[Edges[i][1]][:10]
        
    print('Nodes of the graph are synthesized as follows:')
    print(Nodes)
    print('\nEdges between nodes are synthesized as follows:')
    print(EdgesDNA)
    #We now have nodes and edges
    
    #This is how the about sequences will anneal inside a PCR machine.
    
    ctr=ne
    a = ['']*100000
    for i in range(ne):
        a[i]=EdgesDNA[i]
    overall = ne

    while max(len(s) for s in a) <= 20*nn:
        for i in range(nn):
            for j in range(overall):
                for k in range (overall):
                    if Nodes[i]==a[j][-10:]+a[k][:10]:
                        a[ctr]= a[j]+a[k]
#                         print(i,j,k,Nodes[i],a[ctr])
                        ctr+=1
        if max(len(s) for s in a)==20*nn:
            break
        overall = ctr-1
    
    #We now consider only the set since there can be redundant DNA matches as well.        
    final_list = set(a)
        
    pfl = ['']*20 #possible_full_lengths
    p=0
    
    #Actual implementation of the algorithm.
    #IF the annealed DNA sequence's length is exactly what we need, i.e.,
    #length_of_each_node*nn, and if it starts and ends at specified nodes, then,
    #these qualify as possible full length DNA sequences.
    
    for flength in final_list:
        if len(flength)==(20*nn):
            if flength[:20]==Nodes[0] and flength[-20:]==Nodes[nn-1]:
                pfl[p] = flength
                p+=1
    #If a qualified full length DNA sequence also covers all the nodes, then that
    #particular sequence corresponds to the Hamiltonian path between speicifed
    #star and end nodes.            
    for i in range(p):
        order=[0]*nn
        t=0
        for ctl in range(0,nn*20,20):
            s = pfl[i][ctl:ctl+20]
            order[t]=Nodes.index(s)
            t+=1

        if len(set(order))==nn:
            print('\nRESULT!!\nHamiltonian solved from 0 to %d'%(nn-1))
            print(pfl[i])
            print('\nOrder of traversal of nodes:')
            print(order) 
            
G = nx.DiGraph()
G.add_nodes_from([0,1,2,3,4,5,6,7,8])
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8)])

H = nx.DiGraph()
H.add_nodes_from([0,1,2,3,4,5,6])
H.add_edges_from([(0,1),(0,3),(0,6),(1,3),(1,4),(1,2),(2,1),(2,3),(3,2),(3,4),(4,1),(4,5),(5,2),(5,6)])

Hamiltonian_path(G)