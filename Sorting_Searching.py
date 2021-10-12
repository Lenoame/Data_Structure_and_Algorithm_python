L = [{'name':'John', 'score':83}, 
			{'name':'Paul', 'score':92}]

L.sort(key=lambda x : x['score'], reverse = True)
=> 레코드들을 점수 높은 순으로 정렬

# 선형 탐색(Linear Search)
def linear_search(L, x):
	i = 0
	while i < len(L) and L[i] != x:
		i += 1
	if i < len(L):
		return i
	else:
		return -1

# 이진 탐색 (binary search)
def binary_search(L, x):
    answer = -1
    lower = 0
    upper = len(L) - 1
    
    while lower <= upper:
        mid = (lower + upper)//2
        if L[mid] == x:
            answer = mid
            break
        elif L[mid] < x:
            lower = mid + 1
        else:
            upper = mid - 1
        
    return answer