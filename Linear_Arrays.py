L = ['Bob', 'Cat', 'Spam', 'Programmers']
L.append('New')

['Bob', 'Cat', 'Spam', 'Programmers', 'New']
# L.pop() => 끝에서 하나의 원소를 꺼냄(리스트의 변화)

# (1) 원소 삽입하기
L = [20, 37, 58, 72, 91]
L.insert(3, 65) # 리스트 3번째 자리에 65를 삽입하라.
insert(인덱스 위치, 삽입할 원소)
# insert의 순서 => 리스트의 길이가 길면 오래 걸리는 일 ⇒ 리스트의 길이에 비례(선형 시간) (삽입할 자리를 만들기 위에 끝의 원소를 밀어서 자리를 만들기 때문에 길이가 길 수록 시간이 오래 걸림) ⇒ O(N)
insert(3, 65)
[20, 37, 58, 65, 72, 91]

# (2) 원소 삭제하기

del(L[2]) # 리스트 L의 index 2 위치 (세 번째) 원소를 삭제하라
# del의 순서 => 삭제할 위치의 오른쪽 원소를 앞으로 당기고 그 다음 오른쪽 원소를 계속 당기는걸 반복

# (3) 원소 탐색하기

L = ['Bob', 'Cat', 'Spam', 'Programmers']
L.index('Spam') = 2
