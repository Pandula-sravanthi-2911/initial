def find_available(in_time,out_time,duration,meeting):
    meeting.sort()
    available=[]
    if(meeting[0][0]-in_time>=duration):
        available.append([in_time,meeting[0][0]])
    for i in range(len(meeting)-1):
            if meeting[i+1][0]-meeting[i][1] >=duration :
                available.append([meeting[i][1],meeting[i+1][0]])
    if(out_time - meeting[len(meeting)-1][1] >=duration ):
        available.append([meeting[len(meeting)-1][1],out_time])
    return available
def check_available(available_list1,available_list2,duration):
    available_list1.sort()
    available_list2.sort()
    for lst1 in available_list1:
        for ls in available_list2:
            if (lst1[0]>=ls[0]) and (lst1[0] in range(ls[0],ls[1]))and (lst1[0]+duration  in range(ls[0],ls[1]+1)):
                return([lst1[0],lst1[0]+duration])
    for ls in available_list2:
        for lst1 in available_list1:
            if (ls[0]>=lst1[0]) and (ls[0] in range(lst1[0],lst1[1]))and (ls[0]+duration  in range(lst1[0],lst1[1]+1)):
                return ([ls[0],ls[0]+duration])
    return[]
