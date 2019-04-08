
def max_list_iter(int_list):  # must use iteration not recursion
   #"""finds the max of a list of numbers and returns the value (not the index)
   #If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    else:
        if len(int_list) == 0:
            return None
        else:
            max_num = int_list[0]
            for i in range(1, len(int_list)):
                if max_num < int_list[i]:
                    max_num = int_list[i]
            return max_num

def reverse_rec(int_list):   # must use recursion
   #"""recursively reverses a list of numbers and returns the reversed list
   #If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    else:
        if len(int_list) == 0:
            return []
        else:
            return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   #"""searches for target in int_list[low..high] and returns index if found
   #If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    else:   
        if len(int_list) == 0:
            return None                                                                    
        mid = (low + high) // 2 
        if target == int_list[mid]:
            return mid
        elif target > int_list[mid] and target <= int_list[high]:                                             
            low = mid + 1
            return bin_search(target, low, high, int_list)                
        elif target <= int_list[mid] and target >= int_list[low]:     
            high = mid
            return bin_search(target, low, high, int_list)                 
        else:                                                                   
            return None                     
