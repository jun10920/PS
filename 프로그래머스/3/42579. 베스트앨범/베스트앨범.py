def solution(genres, plays):
    category_array ={} # 같은 카테고리는 배열로 체이닝
    category_sum ={} # 카테고리별 총합
		
		
    for index in range(len(genres)) : # O(n)
        category = genres[index] # key
        
        # 해시 맵 안에 카테고리로 된 키가 있을 때
        if category in category_array and category in category_sum :
            
            array = category_array[category] # 체이닝 배열 꺼내기.
            array.append(index) #인덱스 삽입 후 정렬
            
            for i in range(len(array)-1) : #선택정렬 
                max = i
                for j in range(i+1,len(array)) :
                    if plays[array[max]] < plays[array[j]] : # 같은 경우는 스왑 x 더 작은 인덱스가 살아 남음.
                        max = j 
                array[i], array[max] = array[max], array[i] # swap

            if len(array) > 2 : array.pop() #정렬 후 배열 길이 2로 유지.

            category_array[category]= array # 다시 넣기
            category_sum[category] += plays[index] # 더하기

        else : # 해시 맵 안에 카테고리로 된 키가 없을 때 -> 초기화
            category_array[category] = [index]
            category_sum[category] = plays[index]
		
		#카테고리별로 재생수 총합 퀵정렬 -> O(nlogn)
    sorted_category = sorted(category_sum.items(), key=lambda item: item[1], reverse=True)

    answer = []

    #카테고리 안에 있는 체이닝 배열 붙혀서 반환.
    for key,value in sorted_category :
        answer += category_array[key]

    return answer