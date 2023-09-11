# You are give a list [a,b,c,d,e,f,g]
# you have to sort in such a way that 1st last last term of the list come alternatively
# ie: [a,g,b,f,c,e,d]

def give_me_your_list(list_):
    print(f"Your given list {list_}")
    b=[]
    def checker(x):
        return len(x)==len(list_)
    
    j=len(list_)
    for i in range(len(list_)):
        b.append(list_[i])
        if checker(b):
            break
        b.append(list_[j-1])
        if checker(b):
            break
        j-=1
    return f"your sorted list{b}"

print(give_me_your_list([1,2,3,4,5]))



