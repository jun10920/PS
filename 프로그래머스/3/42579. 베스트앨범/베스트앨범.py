def solution(genres, plays):
    genre_total_plays = {}  # 장르별 총 재생 횟수 저장
    genre_songs = {}  # 장르별 노래 정보 저장 (재생 횟수, 고유 번호)

    # 1단계: 장르별 총 재생 횟수와 노래 정보 계산
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total_plays:
            genre_total_plays[genre] = play
            genre_songs[genre] = [(play, i)]
        else:
            genre_total_plays[genre] += play
            genre_songs[genre].append((play, i))

    # 2단계: 장르를 총 재생 횟수에 따라 정렬
    sorted_genres = sorted(genre_total_plays, key=genre_total_plays.get, reverse=True)

    answer = []
    # 3단계: 각 장르별로 가장 많이 재생된 노래 2개 선택
    for genre in sorted_genres:
        # 장르 내 노래를 재생 횟수와 고유 번호에 따라 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 2곡 (또는 그보다 적은 곡이 있을 경우 모든 곡) 선택
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer
