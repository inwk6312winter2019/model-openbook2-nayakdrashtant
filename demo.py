import csv
def subtaskone(clas,accessible):
    sfdid = []
    bfdid = []
    uniq = []
    reader1 = open('Street_Centrelines.csv', 'r')
    reader2 = open('Bus_Stops.csv', 'r')
    r1 = csv.DictReader(reader1)
    for r in r1:
        if r["ST_CLASS"] != None:
            if r["ST_CLASS"] == clas:
                if r["FDMID"] not in sfdid:
                    sfdid.append(r["FDMID"])
    r2 = csv.DictReader(reader2)
    for k in r2:
        if k["ACCESSIBLE"] != None:
            if k["ACCESSIBLE"] == accessible:
                if k["FDMID"] not in bfdid:
                    bfdid.append(k["FDMID"])

    for sf in sfdid:
        for bf in bfdid:
            if(sf == bf):
                if bf not in uniq:
                    uniq.append(bf)

    openr = open('Bus_Stops.csv','r')
    print("-------------------------------------------------------------")
    print("| Stop Number |          Location          |      FCODE     |")
    print("-------------------------------------------------------------")
    r3 = csv.DictReader(openr)
    for u in uniq:
        for p in r3:
            if (u == p["FDMID"]):
                print("   " + p["STOPNUMBER"] + "  " +  p["LOCATION"] + "  " + p["FCODE"] )      
            

x = input("enter class:")
y = input("enter accessible:") 
subtaskone(x,y)
