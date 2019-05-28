import csv

count = True
with open('C:/Users/akhil/Documents/PS-1/24-5-2019/regions.csv','rt') as regions:
    regions_data = csv.reader(regions)
    for regions_row in regions_data:
        dic = []
        if count == False:
            print("The region is:",regions_row[1])
        with open('C:/Users/akhil/Documents/PS-1/24-5-2019/territories.csv','rt') as territories:
            territories_data = csv.reader(territories)
            for territories_row in territories_data:
                if regions_row[0] == territories_row[2]:
                    with open('C:/Users/akhil/Documents/PS-1/24-5-2019/employee-territories.csv','rt') as empter:
                        empter_data = csv.reader(empter)
                        for empter_row in empter_data:
                            if empter_row[1] == territories_row[0]:
                                        dic.append(empter_row[0])
                                        count = False
                                            
        s = set(dic)
        print(len(s))

