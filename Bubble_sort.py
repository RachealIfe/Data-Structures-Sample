def bubble_sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for j in range(passnum):
            if nlist[j]>nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

nlist = [14,46,56,3,24,55,3,35,32,43,5,7,9,1,5,8,64,76,23]
bubble_sort(nlist)
print(nlist)
