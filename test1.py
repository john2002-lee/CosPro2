#You may use import as below.
#import math

def solution(shirt_size):
    #Write code here.
    # answer = [0 for _ in range(6)]
    answer = [0,0,0,0,0,0]
    # i=0
    for i in shirt_size:
        if "XS" == i:
            answer[0] += 1
        elif "S" ==i:
            answer[1] +=1
        elif "M" == i:    
            answer[2] +=1
        elif "L" == i:    
            answer[3] +=1
        elif "XL" == i:    
            answer[4] +=1
        elif "XXL" == i:    
            answer[5] +=1

    return answer 
    # size_counter = [0 for _ in range(6)]
    # for ss in shirt_size:
    #     if ss == "XS":
    #         size_counter[0] += 1
    #     elif ss == "S":
    #         size_counter[1] += 1
    #     elif ss == "M":
    #         size_counter[2] += 1
    #     elif ss == "L":
    #         size_counter[3] += 1
    #     elif ss == "XL":
    #         size_counter[4] += 1
    #     elif ss == "XXL":
    #         size_counter[5] += 1

    # return size_counter
#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")