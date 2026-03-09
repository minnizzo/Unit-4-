##def linear_search(items,target):
##    index = 0
##    found = False
##
##    while not found and index < len(items):
##        if target == items[index]:
##            return "Found",index+1
##            found = True
##        else:
##            index = index + 1
##
##    if found == False:
##        print("not found")
##
##linear_search = (["pizza","tacos","apple","pasta"])
##        


##def binary_search(items, search_item):
##    found = False
##    first = 0
##    last = len(items) - 1
##    midpoint = 0
##
##    while first <= last and found == False:
##        midpoint = first + last / 2
##        if items[midpoint] == search_item:
##            print("found")
##            found = True
##        elif items[midpoint] < search_item:
##            first = midpoint + 1
##        else:
##            last = midpoint - 1

def bubble_sort(listt):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range (len(listt), -1):
            if listt[i] > listt[i + 1]:
                temp = listt[i]
                listt[i] = listt [i + 1]
                listt[i + 1] = temp
                swapped = True

return listt
