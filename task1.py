myfile = open("Street_Centrelines.csv","r")
def dotuple():
    for f in myfile:
        f = f.split(",")
       # f = f.strip()
        string = (f[2],f[4],f[6],f[7])
        print(string)  
        

dotuple()
