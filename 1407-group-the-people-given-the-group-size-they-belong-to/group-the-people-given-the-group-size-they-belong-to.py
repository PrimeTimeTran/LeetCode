'''Explanations inline''' 


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
		Example input-> groupSizes=[3,3,3,3,3,1,3]
        Store in a dictionary[i] the list of indices of input array groupSizes that belong to a group size i 
		'''
        _dict_=collections.defaultdict(list)
        for idx,i in enumerate(groupSizes):
            _dict_[i].append(idx)
        '''
        print (_dict_)-> defaultdict(<class 'list'>, {3: [0, 1, 2, 3, 4, 6], 1: [5]})
        _dict_[i] has list of indices of input array groupSizes that belong to groupsize i
        Next, create lists of size i parsing through _dict_[i], and append them to answer[].
        Further since a solution is guaranteed to exist, len(_dict_[i])/i will always be perfectly divisible. 
		Infact, len(_dict_[i])/i gives exactly the number of groups of size i
        '''
        answer=[]
        for key, lst in _dict_.items():
            for idx in range(0, len(lst), key):
                answer.append(lst[idx:idx + key])
        return (answer)	