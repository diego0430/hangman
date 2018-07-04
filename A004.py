input_line=input()
lnm=input_line.split(" ")
l = int(lnm[0])
n = int(lnm[1])
m = int(lnm[2])

lines=[]

"横ラインを[-1,-1,x,y,-1,-1,-1]形式でlinesに追加していく"
for ind in range(1,m+1):
    input_line_ind = input()
    abc=input_line_ind.split(" ")
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    line = [-1]
    for n_i in range(1,n+1):
        if n_i == a:
            line.append(b)
        elif n_i == a+1:
            line.append(c)
        else:
            line.append(-1)
    line.append(-1)
    lines.append(line)


"最初の状態（１番目の一番下）を記録"
state0 = {"vert":1,"depth":l}


"今の状態stateから一つ上に行き、横棒を伝って移動した後の状態をstate0に返す"
def climb(state):
    global state0
    dlist=[]
    for line in lines:
        d=line[state["vert"]]
        if 0 < d and d < state["depth"]:
            dlist.append(d)
    if dlist==[]:
        newdepth = 0
        newvert = state["vert"]
    else:
        for line in lines:
            if line[state["vert"]] == max(dlist):
                if line[state["vert"]-1]>0:
                    newvert=state["vert"]-1
                else:
                    newvert=state["vert"]+1
                newdepth=line[newvert]
    state0 = {"vert":newvert,"depth":newdepth}



"深さが0になるまで登る"
while state0["depth"]>0:
    climb(state0)

print(state0["vert"])
