# Python-Array-Problem-1 You are provided a ndim aaray such 
# that you have to retun the same ndim array with same size  but in place
#  of each element with product of all element of 
# that row except for that element Example a=[1,2,3,4] and you have to return [24,12,8,6]

import numpy as np

def give_me_your_array(array):
    def multiplication(*args):
        multi=1
        for items in args:
            multi*=items
        return(multi)
    # from modules.functions import multiplication as mp
    b=[]
    shape=array.shape
    for rows in array:
        for items in rows:
            def check(*args):
                for numbers in args:
                    return numbers!=items
            filtered_list=list(filter(check,rows))
            b.append(multiplication(*filtered_list))

    b=np.reshape(b,shape) 
    return f"\nYour given array\n {array}\n your product aaray\n{b}"
        
a = np.array([[93, 16, 51, 98, 14, 17, 71, 78],
              [39, 84, 35, 27, 11, 84, 36, 27],
              [53, 91, 53,  3, 36, 72, 63, 83],
              [78, 26, 13, 29, 80, 75, 41, 57]])
 
x = np.array([[9, 2, 4],
              [6, 7, 10],
              [3, 8, 7]])    
print(give_me_your_array(a))