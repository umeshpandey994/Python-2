def binarySearch(list_s,item):
    first=0
    last=len(list_s)-1
    while first<=last :
       mid=(first+last)//2
       if list_s[mid]==item:
           print mid+1
           break
       else:
            if item<list_s[mid]:
                last=mid-1
            else:
                first=mid+1
