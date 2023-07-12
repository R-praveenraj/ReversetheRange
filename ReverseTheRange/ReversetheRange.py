#Given an array A of N integers 
#and also given two integers B and C. 
#Reverse the elements of the array A within the given inclusive range [B, C].


def Reverse(array,integer1,integer2):
    while integer1<integer2:
        array[integer1],array[integer2]=array[integer2],array[integer1]
        integer1+=1
        integer2-=1
    return array   




array = [1, 2, 3, 4,5]
integer1 = 1
integer2 = 4
print(Reverse(array,integer1,integer2))