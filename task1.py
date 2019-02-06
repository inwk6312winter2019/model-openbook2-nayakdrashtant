myfile = open("Street_Centrelines.csv","r")
def dotuple():
    for f in myfile:
        f = f.split(",")
        string = (f[2],f[4],f[6],f[7])
        print(string)  
        
def maintanancehistogram():
    mydict = dict()
    for f in myfile:
        f = f.split(",")
        if f[12] not in mydict:
            mydict[f[12]] = 1
        else:
            mydict[f[12]] += 1
    print(mydict)

#dotuple()
maintanancehistogram()
