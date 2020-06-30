import os
import keyword
from random import randrange as rr
obfuscate_strings = True
builtin_f = ['abs', 'dict', 'help', 'min', 'setattr', 'all', 'dir', 'hex', 'next', 'slice', 'any', 'divmod', 'id', 'object', 'sorted', 'ascii', 'enumerate', 'input', 'oct', 'staticmethod', 'bin', 'eval', 'int', 'open', 'str', 'bool', 'exec', 'isinstance', 'ord', 'sum', 'bytearray', 'filter', 'issubclass', 'pow', 'super', 'bytes', 'float', 'iter', 'print', 'tuple', 'callable', 'format', 'len', 'property', 'type', 'chr', 'frozenset', 'list', 'range', 'vars', 'classmethod', 'getattr', 'locals', 'repr', 'zip', 'compile', 'globals', 'map', 'reversed', '__import__', 'complex', 'hasattr', 'max', 'round', 'delattr', 'hash', 'memoryview', 'set']
keywords = keyword.kwlist + builtin_f

file = str(input("File to Eddyify:"))
remap = dict()
c = 1
warnings = set()
def rewrite(s,syms,d_par_count=0):
    while ' =' in s:s=s.replace(' =','=')
    while '= ' in s:s=s.replace('= ','=')
    if d_par_count:
        global par_deep
        par_deep+=d_par_count
    if s=="":return s
    if '(' in s:
        return rewrite(s.split('(')[0],syms) + '(' + '('.join(rewrite(j,syms,1) for j in s.split('(')[1:])
    if ')' in s:
        return rewrite(s.split(')')[0],syms) + ')' + ')'.join(rewrite(j,syms,-1) for j in s.split(')')[1:])
    if len(syms) > 0:
        if par_deep and syms[0]=='=' and s.count('=')==1:
            yn = input('is function parameter '+s.split('=')[0]+' in line '+l__.strip()+' for a function defined in this file? y/n [?] for more info:')
            while not yn in ('y','n'):
                if yn=='?':
                    print('If you are passing an argument using its name to a function being called is defined within this file i need to replace the name. If the function is built in or imported, it will be unchanged. for example i cannot change "sorted(list_,key=func)" for "sorted(__,___=____)"')
                yn=input('you must enter either [y] or [n]:')
            if yn=='y':
                return '='.join(rewrite(j,syms[1:]) for j in s.split('='))
            else:
                return s.split('=')[0]+'='+rewrite(s.split('=')[1],syms[1:])
        return syms[0].join(rewrite(i,syms[1:]) for i in s.split(syms[0]))
    else:
        if "." in s:
            if s[0].isdigit():return s
            return rewrite(s.split(".")[0],syms)+"."+".".join(s.split(".")[1:])
        if s[0].isdigit():
            if all(j.isdigit() for j in s):return renum(int(s))
            return s
        if not s[0] in "\"'" and not s in keywords:
            global c,remap
            if s in remap:
                return remap[s]
            else:
                remap[s] = "_"*c
                c += 1
                return remap[s]
    return s
def renum(i,second=False):
    if second:
        if rr(4)==0:
            return hex(i)
        if rr(3)==0:
            return bin(i)
        if rr(2):
            return oct(i)
        return str(i)
    if i and rr(3):
        r = rr(i)
        return '('+renum(r,True)+'+'+renum(i-r,True)+')'
    return renum(i,True)
def restring(s):
    if s == "\"\"" or s == "''":return s
    if not obfuscate_strings:return s
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
            r += "chr("+renum(ord(i))+")+"
    return r[:-1]

#from
l__ = ''
par_deep = 0#how many parentheses deep you are
def regen_line(l,primary_call=False):
    if primary_call:
        global l__
        l__=l
    if len(l) > 3:
        global c,remap
        if l[:4] == "from" or l[:6] == "import":
            if ',' in l:#from random import random as r,randrange as rr
                return '\n'.join(regen_line(l.split('import ')[0]+'import '+j) for j in l.split('import ')[1].split(','))
            if " as " in l:
                remap[l.split(" ")[-1]] = "_"*c
                c += 1
                return l.split(" as ")[0]+" as "+"_"*(c-1)                
            remap[l.split(" ")[-1]] = "_"*c
            c += 1
            return l +" as "+"_"*(c-1)
    sym = [" ",":",",","+","-","*","//","/","%","[","]","{","}",">","<","!","="]#,"'","\"","\\"]"(",")",
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
        input("this was designed for python files only; other filetypes probably will almost certainly fail.\nHit [Enter] to proceed anyway. Otherwise close this window.")
    if os.path.exists(file[:-3]+"_.py"):input(file[:-3]+"_.py already exists.  hit [Enter] to proceed and overwrite it. Otherwise close this window.")
    with open(file) as f:d = f.read()
    with open(file[:-3]+"_.py","w+") as f:
        f.write("\n".join(regen_line(i,True) for i in d.split("\n")))
            
else:print(file+ " doenst seem to exist")
