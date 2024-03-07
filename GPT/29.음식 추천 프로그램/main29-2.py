import random

# 기분에 따른 음식 리스트
mood_menus = {
    "행복": ["피자", "아이스크림", "초밥"],
    "우울": ["라면", "김밥", "커피"],
    "스트레스": ["떡볶이", "치킨", "맥주"],
    "피곤": ["샐러드", "과일", "녹차"],
}

def recommend_menu(mood):
    if mood in mood_menus:
        return random.choice(mood_menus[mood])
    else:
        return "알 수 없는 기분입니다."

if __name__ == "__main__":
    user_mood = input("오늘의 기분은? (행복, 우울, 스트레스, 피곤): ")
    recommended_dish = recommend_menu(user_mood)
    print(f"오늘은 {recommended_dish} 어떠세요?")
