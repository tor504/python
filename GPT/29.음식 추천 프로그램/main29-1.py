import random

menu = ["돈까스", "라면", "불고기", "제육볶음", "짜장면", "피자"]

def recommend_menu():
    return random.choice(menu)

if __name__ == "__main__":
    recommended_dish = recommend_menu()
    print(f"오늘 점심은 {recommended_dish} 어떠세요?")
