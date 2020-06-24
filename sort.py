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

def Merge(arr,left,right):
    if left < right:
        mid = (left+right)//2
        arr = Merge(arr,left,mid)
        arr = Merge(arr,mid+1,right)
        # Merge
        l, r = left, mid+1
        subarr = []
        while True:
            if arr[l] > arr[r]:
                subarr.append(arr[r])
                r += 1
            else:
                subarr.append(arr[l])
                l += 1
            while (l > mid) ^ (r > right):
                if l<=mid:
                    subarr.append(arr[l])
                    l+=1
                if r <=right:
                    subarr.append(arr[r])
                    r+=1
            if l > mid and r > right: break
        arr[left:right+1] = subarr
    return arr
    
def Quick(arr,left,right):
    if left < right:
        i, j = left+1, right
        while True:
            while arr[i] <= arr[left] and i<j : i +=1
            while arr[j] >= arr[left] and i<=j : j -=1
            if i >= j :break
            tp = arr[j]
            arr[j] = arr[i]
            arr[i] = tp
        tp = arr[j]
        arr[j] = arr[left]
        arr[left] = tp
        arr = Quick(arr,left,j-1)
        arr = Quick(arr,j+1,right)
    return arr

def Heap(arr):
    length = len(arr)
    for j in range(length-1,0,-1):
        for i in range((j-1)//2,-1,-1):
            child = i * 2 + 1
            if child + 1 <= j:
                if arr[child] < arr[child+1]: child+=1
            if arr[i] < arr[child]:
                tp = arr[i]
                arr[i] = arr[child]
                arr[child] = tp
        tp = arr[0]
        arr[0] = arr[j]
        arr[j] = tp
    return arr

def Counting(arr):
    length = len(arr)
    maxi, mini = max(arr), min(arr)
    r = (maxi-mini+1)
    countlist = [0]*r
    for i in arr:
        countlist[i-mini] +=1
    newarr = []
    for i in range(r):
        for j in range(countlist[i]):
            newarr.append(mini+i)
    return newarr

def Bucket(arr):
    length = len(arr)
    maxi, mini = max(arr), min(arr)
    r = (maxi - mini)/ 5
    buckets = [ [] for i in range(5)]
    for v in arr:
        if v == maxi: buckets[-1].append(v)
        else:
            buckets[int((v-mini)//r)].append(v)
    newarr = []
    for b in buckets:
        # we can use any kind of sort algorithm
        b = Shell(b)
        newarr += b
    return newarr

def Radix(arr):
    length = len(arr)
    maxi, mini = max(arr), min(arr)
    n = 1
    while maxi // (10**n)  > 0 :n +=1
    for i in range(1,n+1):
        buckets = [[] for i in range(20)]
        newarr = []
        for v in arr:
            if v >=0 :
                buckets[v % 10 ** i // 10 ** (i-1)+10].append(v)
            else:
                buckets[v % 10 ** i // 10 ** (i-1)].append(v)
        for j in range(20): newarr+=buckets[j]
        arr = newarr
    return arr

if __name__ == "__main__":
    while True:
        line = input('input:')
        if line =='': break
        arr = list(map(int,line.split()))
        print('select:\t',Selection(arr))
        print('insert:\t',Insert(arr))
        print('bubble:\t',Bubble(arr))
        print('shell:\t',Shell(arr))
        print('merge:\t',Merge(arr,0,len(arr)-1))
        print('quick:\t',Quick(arr,0,len(arr)-1))
        print('heap:\t',Heap(arr))
        print('count:\t',Counting(arr))
        print('bucket:\t',Bucket(arr))
        print('Radix:\t',Radix(arr))
    pass