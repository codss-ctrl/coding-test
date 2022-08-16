def replace(notes): # 뒤에 #이 붙는 음들을 모두 문제에서 입력되는 음정 데이터와 겹치지 않는 알파벳으로 치환하는 함수
    for a,b in zip(["A#", "C#", "D#", "F#", "G#"], ["Z","Y","X","W","U"]): # zip 함수로 묶어 ("A#","Z")... 형태가 되도록 한다.
        notes = notes.replace(a,b)
    return notes

def solution(m, musicinfos):
    music = [] # 필요한 데이터 가공해서 저장할 변수
    titles = [] # 들어온 순서(인덱스 순서)로 음악 제목만 저장
    for idx, info in enumerate(musicinfos): # 들어온 순서 저장하기 위해 enumerate로 인덱스도 같이 추출
        start, end, title, notes = info.split(",")  # 재생시각, 종료시각, 제목, 악보
        elapsed = (int(end[:2]) * 60 + int(end[3:])) - (int(start[:2]) * 60 + int(start[3:]))  # 시작, 종료 시간을 시간*60+분으로 계산하여 빼기 -> 실행시간 분으로 저장
        notes = replace(notes) # #붙는 음들 전처리해서 저장
        notes_whole = (elapsed//len(notes))*notes + notes[:elapsed%len(notes)] # 실행시간/악보 길이 == 전체 악보가 반복된 정도, 실행시간mod악보 길이 == 전체를 반복하지 못하고 남은 음들
        music.append([notes_whole, elapsed, idx])  # 악보,재생길이,재생순서 저장
        titles.append(title)  # 들어온 순서대로 노래 제목 저장
    answer = []
    for ele in music: # ele = [notes_whole, elapsed, idx]
        if replace(m) in ele[0]: # 실행시간 만큼 반복한 악보에 replace() 처리한 m의 음정들이 있다면
            answer.append([ele[1],ele[2]]) # answer에 재생시간, 인덱스 저장
    if not answer: # 일치하는 악보가 없다면
        return "(None)"
    else: # 일치하는 악보가 있다면
        answer.sort(key=lambda x: x[0],reverse=True) # 1. 재생시간 Desc, 인덱스 Asc 정렬
        # answer.sort(key=lambda x: (x[0],-x[1]),reverse=True) # 이미 15번째 line에서 asc 순서로 인덱스가 저장되어 정렬할 필요 없음(답은 같음)
        return titles[answer[0][1]] # 실행시간이 가장 긴 곡의 인덱스로 title을 인덱싱