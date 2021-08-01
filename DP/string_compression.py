class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        itr = 0
        loop = 0
        for i in range(len(chars)):
            if(chars[loop]==chars[i]):
                count += 1
            elif(chars[loop]!=chars[i]):
                chars[itr] = chars[loop]
                itr += 1
                loop = i
                if(count>1):
                    for c in str(count):
                        chars[itr] = c
                        itr += 1
                # elif(count==1):
                #     itr += 1
                count = 1
        chars[itr] = chars[loop]
        itr += 1
        if(count>1):
            for c in str(count):
                chars[itr] = c
                itr += 1
        return itr
