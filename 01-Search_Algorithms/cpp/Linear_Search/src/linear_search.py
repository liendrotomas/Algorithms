
def linear_search(arr, x:int):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1

if __name__=="__main__":
    arr = [1,2,4,10,20]
    x = 10
    res = linear_search(arr, x)
    if (res == -1)
        cout << "Not present";
    else    
        cout << "Present at index " << res
    return 0