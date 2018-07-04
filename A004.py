input_line=input()
lnm=input_line.split(" ")
l = int(lnm[0])
n = int(lnm[1])
m = int(lnm[2])

lines=[]

"横ラインを[-1,-1,2,5,-1,-1,-1]形式でlinesに追加していく"
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

state0 = {"vart":1,"depth":l}
def clime(state):
    global state0
    dlist=[]
    for line in lines:
        d=line[state["vart"]]
        if 0 < d and d < state["depth"]:
            dlist.append(d)
    if dlist==[]:
        newdepth = 0
        newvart = state["vart"]
    else:
        for line in lines:
            if line[state["vart"]] == max(dlist):
                if line[state["vart"]-1]>0:
                    newvart=state["vart"]-1
                else:
                    newvart=state["vart"]+1
                newdepth=line[newvart]
    state0 = {"vart":newvart,"depth":newdepth}



while state0["depth"]>0:
    clime(state0)

print(state0["vart"])