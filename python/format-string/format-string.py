# Author: Oscar Parra
# Date: 10/30/2018
# Test case 1
# S = "r"
# K = 1

# Test case 2
S = "2-bA087-4k"
K = 4


def formatString(S, K):
    S = S.upper()
    
    if(len(S) == 1 and K == 1):
        print(S)
    else:
        # Remove dashes from string
        S = S.replace("-","")
        # Convert string to list of chars
        S = list(S)
        print(S)
        
        mod = len(S)%K
        print(mod)
        ngroups = int(len(S)/K)
        print(ngroups)
        newString = ""
        
        if(mod == 0): # ngroups with K chars each
            for i in range(ngroups):
                for j in range(K):
                    newString = newString + S[0]
                    S.pop(0) 
                if(len(S) >= K): # last group K chars to be appended
                    newString = newString + "-"
                else:
                   continue 
        else:
            ngroups = ngroups + 1
            for i in range(ngroups):
                for j in range(mod):
                    newString = newString + S[0]
                    S.pop(0)
                
                
                if(len(S) >= K):
                    newString = newString + "-"
                else: continue
            
                if(i == 0):
                    mod = K
                
        return newString

res = formatString("1-3A0r7-1f", 4)
print(res)
res = formatString("6-2ad0r5-5k", 3)
print(res)
res = formatString("2-3-4-5", 2)
print(res)
res = formatString("2-335", 1)
print(res)
