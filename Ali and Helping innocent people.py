Truck_tag = input()                # Reading input from STDIN

if len(Truck_tag) !=9:
    print("invalid")
else:
    count = 0
    flag = False
    for i in range(len(Truck_tag)-1):

        if Truck_tag[i].isdigit() and Truck_tag[i+1].isdigit() and int(int(Truck_tag[i])+int(Truck_tag[i+1]))%2==0:
            count +=1
        elif Truck_tag[i].isalpha() and Truck_tag[i] not in ["A","E","I","O","U","Y"]:
            flag = True
    if count == 4 and flag==True:
        print("valid")
    else:
        print("invalid")