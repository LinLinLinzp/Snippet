import sys

def Selection(arr):
    length = len(arr)
    for i in range(length):
        m = i
        for j in range(i,length):
            if arr[m] > arr[j]: m = j
        tp = arr[i]
        arr[i] = arr[m]
        arr[m] = tp
    return arr

def Insert(arr):
    length = len(arr)
    for i in range(1,length):
        tp = arr[i]
        k = i-1
        while arr[k] > tp and k>=0:
            arr[k+1] = arr[k]
            k-=1
        arr[k+1]=tp
    return arr
        
def Bubble(arr):
    length = len(arr)
    for i in range(length-1,0,-1):
        change = True
        for j in range(i):
            while arr[j] > arr[j+1]:
                tp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tp
                change = False
        if change: break
    return arr

def Shell(arr):
    length = len(arr)
    g = length//2
    while g >= 1:
        for i in range(g,length):
            tp = arr[i]
            k = i-g
            while arr[k] > tp and k >= 0:
                arr[k+g] = arr[k]
                k -= g
            arr[k+g] = tp
        g //=2
    return arr
    
if __name__ == "__main__":
    while True:
        # line = sys.stdin.readline()
        line = input('input:')
        if line =='': break
        arr = list(map(int,line.split()))
        # print('selection:',Selection(arr))
        # print('insert:',Insert(arr))
        # print('bubble:',Bubble(arr))
        print('shell:',Shell(arr))
    pass