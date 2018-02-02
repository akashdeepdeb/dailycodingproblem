class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        idx=0
        ans = []
        while idx < len(words):
            ans.append([])
            total=0
            flag = 0
            while total <= maxWidth and idx < len(words):
                total+=len(words[idx])
                ans[-1].append(words[idx])
                if len(ans[-1]) >= 2:
                    total+=1
                if total>maxWidth:
                    flag = 1
                    break
                idx+=1
            if flag:
                del ans[-1][-1]
            else:
                idx+=1
                
        spacesArray = []
        for sentence in ans:
            count = 0
            for word in sentence:
                count+=len(word)
            spaces = maxWidth-count
            c = len(sentence)-1
            spacesArray.append([])
            flag = 0
            if not c:
                flag = 1
            while c > 0:
                spacesArray[-1].append(spaces/c*' ')
                spaces -= spaces/c
                c -= 1
            if flag:
                spacesArray[-1].append(spaces*' ')
        sol = []
        for i in range(len(ans)):
            sol.append('')
            for j in range(len(ans[i])):
                sol[-1] += ans[i][j]
                if len(ans[i]) > 1 and j == len(ans[i])-1:
                    break
                sol[-1] += spacesArray[i][::-1][j]
        return sol
                
            
        ## DID THIS WITH >104 FEVER. THIS IS LONG CODE. I KNOW. 