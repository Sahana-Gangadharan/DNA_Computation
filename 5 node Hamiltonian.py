#given nodes, edges, we are designing DNA strands.
import random as r
import re

Edges = [(0,1),(1,4),(3,2),(2,3),(2,1),(3,1),(0,3)]
ne = len(Edges)
nn = 5
Nodes = ['']*nn
EdgesDNA = ['']*ne
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
        
print(Nodes)
print('\n')
print(EdgesDNA)
print('\n')
#We now have nodes and edges

ctr=0
a = ['']*1000
for i in range(nn):
    for j in range(ne):
        for k in range (ne):
            if Edges[j][1]==(nn-1) or Edges[k][1]==(nn-1):
                if Nodes[i]==EdgesDNA[j][-20:-10]+EdgesDNA[k][:10]:
                    a[ctr]= EdgesDNA[j]+EdgesDNA[k][10:]
                    print(i,j,k,Nodes[i],a[ctr])
                    ctr+=1
            if Nodes[i]==EdgesDNA[j][-10:]+EdgesDNA[k][:10]:
                a[ctr]= EdgesDNA[j]+EdgesDNA[k]
                print(i,j,k,Nodes[i],a[ctr])
                ctr+=1
three = ctr-1
print('\n')

for p in range(nn):
    for q in range(three):
        for r in range(three):
#             if a[q][-10:]==a[r][:10]:
#                 if Nodes[p]==a[q][-20:-10]+a[r][:10]:
#                     a[ctr]= a[q]+a[r][10:]
# #                     print(p,q,r,Nodes[p],a[ctr])
#                     ctr+=1
            if Nodes[p]==a[q][-10:]+a[r][:10]:
                a[ctr]= a[q]+a[r]
                print(p,q,r,Nodes[p],a[ctr])
                ctr+=1
                
four = ctr-1
print('\n')

# for p in range(nn):
#     for q in range(four):
#         for r in range(four):
#             if a[q][-10:]==a[r][:10]:
#                 if Nodes[p]==a[q][-20:-10]+a[r][:10]:
#                     a[ctr]= a[q]+a[r][10:]
# #                     print(p,q,r,Nodes[p],a[ctr])
#                     ctr+=1
#             if Nodes[p]==a[q][-10:]+a[r][:10]:
#                 a[ctr]= a[q]+a[r][10:]
# #                 print(p,q,r,Nodes[p],a[ctr])
#                 ctr+=1
                
final = Nodes[0]+Nodes[3]+Nodes[2]+Nodes[1]+Nodes[4]
for str in a:
    if len(str)==100:
        if str[:20]==Nodes[0] and str[-20:]==Nodes[4]:
            print('Hamiltonian solved from 0 to 4')
            print(str)

# print(len(max(a,key = len)))