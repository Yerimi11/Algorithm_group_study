import sys
import collections
input = sys.stdin.readline
def groupAnagrams(strs) :
    anagrams = collections.defaultdict(list) # 만약 존재하지 않는 키를 삽입하려 할 경우 keyerror가 발생하므로, 항상 디폴트를 생성해준다.
    # defaultdict은 생성자로 기본값을 생성해주는 함수이다. 모든 키에 대해서 값이 없는 경우 자동으로 비어있는리스트로 세팅해준다.
    #만약 defaultdict 없으면 anagrams = {} 설정-> if word not in strs: anagrams[0] = [] 로 써야한다.

    for word in strs :
        #정렬하여 딕셔너리에 추가 정렬한 단어가 딕셔너리의 키가 되고 값으로 단어들을 append 한다.
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())    


if __name__ == '__main__' :

    strs = list(input().split())
    print(groupAnagrams(strs))