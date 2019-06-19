import os
extrawack = True
file = str(input("File to Eddyify:"))
keywords = {"True","False","input","range","if","elif","else","open","for","while","with","break","print","input","as","from","len","str","dict","int","def","in","return","and","or","not","global","ord","chr"}
remap = dict()
c = 1
def rewrite(s,syms):
    if len(syms) > 0:
        return syms[0].join(rewrite(i,syms[1:]) for i in s.split(syms[0]))
    else:
        if "." in s:
            return rewrite(s.split(".")[0],syms)+"."+".".join(s.split(".")[1:])
        if s != "" and not (s[0].isdigit() or s[0] in "\"'") and not s in keywords:
            global c,remap
            if s in remap:
                return remap[s]
            else:
                remap[s] = "_"*c
                c += 1
                return remap[s]
    return s
def restring(s):
    if s == "\"\"" or s == "''":return s
    if not extrawack:return s
    r = ""#s[0]
    skip = False
    for i in s[1:-1]:
        if skip:
            r += i+"\"+"
            skip = False
        elif i == "\\":
            r += "\"\\"
            skip = True
        else:
            r += "chr("+str(ord(i))+")+"
    return r[:-1]
def regen_line(l):
    if len(l) > 3:
        global c,remap
        if l[:4] == "from":
            if " as " in l:
                remap[l.split(" ")[-1]] = "_"*c
                c += 1
                return l.split(" as ")[0]+" as "+"_"*(c-1)                
            remap[l.split(" ")[-1]] = "_"*c
            c += 1
            return l +" as "+"_"*(c-1)
        elif l[:6] == "import":
            if " as " in l:
                remap[l.split(" ")[-1]] = "_"*c
                c += 1
                return l.split(" as ")[0]+" as "+"_"*(c-1)                
            remap[l.split(" ")[-1]] = "_"*c
            c += 1
            return l +" as "+"_"*(c-1)
    sym = [" ",":",",","+","-","*","//","/","%","[","]","(",")","{","}","=",">","<","!"]#,"'","\"","\\"]
    r = ""
    w = l
    i_ = 0
#    print(w)
    while "'" in w or "\"" in w:
        if w[i_] == "#":break
        if w[i_] == "\"":
            j_ = i_ + 1
            while w[j_] != "\"" or (w[j_-1] == "\\" and not (j_ < 2 or w[j_-2] == "\\")):
                j_+=1
            return rewrite(w[:i_],sym)+restring(w[i_:j_+1])+regen_line(w[j_+1:])
        if w[i_] == "'":
            j_ = i_ + 1
            while w[j_] != "'" or w[j_-1] == "\\":
                j_+=1
            return rewrite(w[:i_],sym)+restring(w[i_:j_+1])+regen_line(w[j_+1:])
        i_ += 1
    return rewrite(l.split(chr(35))[0],sym)


if os.path.exists(file):
    if file[-3:].lower() != ".py":
        input("this was designed for python files only; other filetypes probably will get kindof wack.\nHit [Enter] to proceed anyway")
    if os.path.exists(file[:-3]+"_.py"):input(file[:-3]+"_.py already exists.  hit [Enter] to proceed and overwrite it")
    with open(file) as f:d = f.read()
    with open(file[:-3]+"_.py","w+") as f:
        f.write("\n".join(regen_line(i) for i in d.split("\n")))
            
else:print(file+ " doenst seem to exist (aka ur bad)")
