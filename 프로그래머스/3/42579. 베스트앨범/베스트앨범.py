from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_order = defaultdict(int)
    genre_plays = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres,plays)):
        genre_order[genre] += play
        genre_plays[genre].append((i, play))
    
    sorted_genres = sorted(genre_order, key = genre_order.get, reverse = True)
    for genre in sorted_genres:
        sorted_songs = sorted(genre_plays[genre], key = lambda x: (-x[1], x[0]))
        answer += [song[0] for song in sorted_songs[:2]]                                  
    return answer