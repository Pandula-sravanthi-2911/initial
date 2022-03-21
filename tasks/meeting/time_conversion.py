def hour_min_conversion(list_in_hours):
    list_in_mins=[]
    for i in range(0,len(list_in_hours)):
        hh=int((list_in_hours[i])[0:2])
        mm=int((list_in_hours[i])[3:5])
        time = hh*60 +mm
        list_in_mins.append(time)
    return list_in_mins
def min_hour_conversion(time_in_min):
    time_in_hour=time_in_min//60
    time_min=time_in_min%60
    if(time_in_hour<10):
        time_in_hour="".join(['0',str(time_in_hour)])
        print(time_in_hour,':',end='')
        if(time_min<10):
            time_min="".join(['0',str(time_min)])
            print(time_min,end='')
        else:
            print(time_min,end='')
    else:
        print(time_in_hour,':',end='')
        if(time_min<10):
            time_min="".join(['0',str(time_min)])
            print(time_min,end='')
        else:
            print(time_min,end='')    
