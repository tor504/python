import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "In three words I can sum up everything I've learned about life: It goes on. - Robert Frost"
    ]
    return random.choice(quotes)

def main():
    print(get_random_quote())

if __name__ == "__main__":
    main()