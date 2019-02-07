import csv
def subtaskone():
    street = []
    nstreet = []
    reader1 = open('Street_Centrelines.csv', 'r')
    reader2 = open('Bus_Stops.csv', 'r')
    for rea in reader1:
        nrea = rea.split(",")
        if nrea[10] == "LOCAL STREET":
            stee = nrea[4].strip()
            stee = stee.lower()
            if stee not in street:
                 street.append(stee)
    for stre in street:
         if stre not in nstreet:
             nstreet.append(stre)
    
    buss = []
    for st in nstreet:
        for der in reader2:
            nder = der.split(",")
            if nder[7] == "Non-Standard":
                haystack = nder[6].strip()
                haystack = haystack.lower()
                if haystack.find(st) >= 0:
                     buss.append(nder[2])
		
#    print(buss)
    print("Stop Number    |    Location    |    FCODE")
    for bus in buss:
        for re in open('Bus_Stops.csv', 'r'):
            nre = re.split(",")
            if nre[2].find(bus) >= 0:
                print(nre[4],"",nre[6],"",nre[10])
    

subtaskone()
