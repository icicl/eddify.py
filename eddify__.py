import os as _
__ = False
___ = str(input("File to Eddyify:"))
____ = {"True","False","input","range","if","elif","else","open","for","while","with","break","print","input","as","from","len","str","dict","int","def","in","return","and","or","not","global","ord","chr"}
_____ = dict()
______ = 1
def _______(________,_________):
    if len(_________) > 0:
        return _________[0].join(_______(__________,_________[1:]) for __________ in ________.split(_________[0]))
    else:
        if "." in ________:
            return _______(________.split(".")[0],_________)+"."+".".join(________.split(".")[1:])
        if ________ != "" and not (________[0].isdigit() or ________[0] in "\"'") and not ________ in ____:
            global ______,_____
            if ________ in _____:
                return _____[________]
            else:
                _____[________] = "_"*______
                ______ += 1
                return _____[________]
    return ________
def ___________(________):
    if ________ == "\"\"" or ________ == "''":return ________
    if not __:return ________
    ____________ = ""
    _____________ = False
    for __________ in ________[1:-1]:
        if _____________:
            ____________ += __________+"\"+"
            _____________ = False
        elif __________ == "\\":
            ____________ += "\"\\"
            _____________ = True
        else:
            ____________ += "chr("+str(ord(__________))+")+"
    return ____________[:-1]
def ______________(_______________):
    if len(_______________) > 3:
        global ______,_____
        if _______________[:4] == "from":
            if " as " in _______________:
                _____[_______________.split(" ")[-1]] = "_"*______
                ______ += 1
                return _______________.split(" as ")[0]+" as "+"_"*(______-1)                
            _____[_______________.split(" ")[-1]] = "_"*______
            ______ += 1
            return _______________ +" as "+"_"*(______-1)
        elif _______________[:6] == "import":
            if " as " in _______________:
                _____[_______________.split(" ")[-1]] = "_"*______
                ______ += 1
                return _______________.split(" as ")[0]+" as "+"_"*(______-1)                
            _____[_______________.split(" ")[-1]] = "_"*______
            ______ += 1
            return _______________ +" as "+"_"*(______-1)
    ________________ = [" ",":",",","+","-","*","//","/","%","[","]","(",")","{","}","=",">","<","!"]
    ____________ = ""
    _________________ = _______________
    __________________ = 0

    while "'" in _________________ or "\"" in _________________:
        if _________________[__________________] == "#":break
        if _________________[__________________] == "\"":
            ___________________ = __________________ + 1
            while _________________[___________________] != "\"" or (_________________[___________________-1] == "\\" and not (___________________ < 2 or _________________[___________________-2] == "\\")):
                ___________________+=1
            return _______(_________________[:__________________],________________)+___________(_________________[__________________:___________________+1])+______________(_________________[___________________+1:])
        if _________________[__________________] == "'":
            ___________________ = __________________ + 1
            while _________________[___________________] != "'" or _________________[___________________-1] == "\\":
                ___________________+=1
            return _______(_________________[:__________________],________________)+___________(_________________[__________________:___________________+1])+______________(_________________[___________________+1:])
        __________________ += 1
    return _______(_______________.split(chr(35))[0],________________)


if _.path.exists(___):
    if ___[-3:].lower() != ".py":
        input("this was designed for python files only; other filetypes probably will get kindof wack.\nHit [Enter] to proceed anyway")
    if _.path.exists(___[:-3]+"_.py"):input(___[:-3]+"_.py already exists.  hit [Enter] to proceed and overwrite it")
    with open(___) as ____________________:_____________________ = ____________________.read()
    with open(___[:-3]+"_.py","w+") as ____________________:
        ____________________.write("\n".join(______________(__________) for __________ in _____________________.split("\n")))
            
else:print(___+ " doenst seem to exist (aka ur bad)")