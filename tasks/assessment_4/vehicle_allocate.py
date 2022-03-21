import csv
fields=['number','vehicle_type','intime','series']
filename="park.csv"
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
def time_conversion(time_in_hour):
    hh=int(time_in_hour[0:2])
    mm=int(time_in_hour[3:5])
    time = hh*60 +mm
    return time
class vehicle:
    millage=" "
    name=" "
    capacity=0
    width=0
    depth=0
    number=""
    manufacturer=""
    intime=0
    def __init__(self,millage,name,number,manufacturer,intime):
        self.millage=millage
        self.name=name
        self.number=number
        self.manufacturer=manufacturer
        self.intime=intime
class bus(vehicle):
    capacity=30
    width=4
    depth=30
class car(vehicle):
    capacity=5
    width=3
    depth=6
class bike(vehicle):
    capacity=2
    width=1
    depth=4
class lot:
    width=80
    depth=60
    number=0
    series=['A','B','C','D']
    status=[]
    series_capacity=[]
    def __init__(self):
        self.A_dim,self.B_dim,self.C_dim,self.D_dim=[[20,60],[20,60],[20,60],[20,60]]
        for i in range(4):
            self.series_capacity.append([60,10,90])
        for i in range(4):
            self.status.append(['u_o','u_o','u_o'])   
    def vehicle_allocate(self,number,intime,vehicle_type):
        filename="park.csv"
        j=0
        flag=0
        if(vehicle_type=='bus'):
            j=1
        else:
            j=2
        with open(filename,'w') as csvfile:
            csvwriter=csv.writer(csvfile)
            for i in range(4):
                if(self.status[i][j]=='u_o'):
                    self.series_capacity[i][j]=self.series_capacity[i][j]-1
                    if(i==0):
                        csvwriter.writerow([number,vehicle_type,intime,'A'])
                        flag=1
                        if(self.series_capacity[i][j]==0):
                            self.status[i][j]='o'
                        break;
                    elif(i==1):
                        csvwriter.writerow([number,vehicle_type,intime,'B'])
                        flag=1
                        if(self.series_capacity[i][j]==0):
                            self.status[i][j]='o'
                        break;
                    elif(i==2):
                        csvwriter.writerow([number,vehicle_type,intime,'C'])
                        flag=1
                        if(self.series_capacity[i][j]==0):
                            self.status[i][j]='o'
                        break;
                    else:
                        csvwriter.writerow([number,vehicle_type,intime,'D'])
                        flag=1
                        if(self.series_capacity[i][j]==0):
                            self.status[i][j]='o'
                        break;
            if(flag==0):
                print("vehicle cannot be parked  : ")
            else:
                print(" vehicle parked ")
    def vehicle_exit(self,number,outtime):
        filename="park.csv"
        with open(filename,'r') as csvfile:
            i=0
            j=0
            for row in csvfile:
                row=row.split(',')
                if(row[0]==number):
                    print(row)
                    if(row[1]=='bus'):
                        i=1
                    else:
                        i=2
                    if(row[3]=='B'):
                        j=1
                    elif(row[3]=='C'):
                        j=2
                    else:
                        j=3
                    self.series_capacity[j][i]=self.series_capacity[j][i]+1
                    self.status[j][i]='u_o'
                    print(" parking charge is : ",self.vehicle_charge(row[2],outtime))
                    break;
    def vehicle_charge(self,intime,outtime):
        intime=time_conversion(intime)
        outtime=time_conversion(outtime)
        outtime=int(outtime)
        intime=int(intime)
        total_time=outtime-intime
        if(total_time//60==0 and total_time%60<30) :
            return 0
        elif(total_time//60==0 or (total_time//60==1 and total_time%60<30) ):
            return 20
        elif(total_time//60<=11 and total_time%60<30):
            return 20 + ((total_time-60)//60)*10
        else:
            if(total_time%60<30):
                return 120+((total_time-600)//60)*5
            else:
                return 120+((total_time-540)//60)*5
        return 0
operation=input("to park the vehicle enter park ,to unpark enter unpark ,to exit enter quit")
lot1=lot()
while(operation=='park' or operation=='unpark'):
    if(operation=='park'):
        vehicle_type=input(" Enter a vehicle type (car or bus or bike) : ")
        if vehicle_type=='car' :
            details=list(input("enter milage,name,number,manufacturer and intime of vehicle : ").split(','))
            new_car=car(details[0],details[1],details[2],details[3],details[4])
            lot1.vehicle_allocate(details[2],details[4],vehicle_type)
            print(details)
        elif vehicle_type=='bus':




            details=list(input("enter milage,name,number,manufacturer and intime of vehicle : ").split(','))
            new_bus=bus(details[0],details[1],details[2],details[3],details[4])
            lot1.vehicle_allocate(details[2],details[4],vehicle_type)   
        elif vehicle_type=='bike':
            details=list(input("enter milage,name,number,manufacturer and intime of vehicle : ").split(','))
            new_bike=bike(details[0],details[1],details[2],details[3],details[4])
            lot1.vehicle_allocate(details[2],details[4],vehicle_type)
        else:
            print("parking for given vehicle type is not possible")
        operation=input("to park the vehicle enter park ,to unpark enter unpark ,to exit enter quit")
    else:
        details=list(input("enter vehicle number ,outime : ").split(','))
        lot1.vehicle_exit(details[0],details[1])
        operation=input("to park the vehicle enter park ,to unpark enter unpark ,to exit enter quit")
print("exit is successfull")
    
