import requests
import json

def format_the_data(data):
    articles = data['articles']

    for i in range(10):
            name = articles[i]['source']['name']
            title = articles[i]['title']
            print(f"{i+1}. _{name}_\n{title}\n")

def print_cat_menu():
    print("Select Your Category:")
    print("1. Business")
    print("2. Entertainment")
    print("3. General")
    print("4. Health")
    print("5. Science")
    print("6. Sports")
    print("7. Technology")

def get_full_article(data, number):
    articles = data['articles']
    content = articles[number]['content']
    link = articles[number]['url']
    title = articles[number]['title']
    
    print(f"\n_Title_: {title}")
    print(f"\n_Article_: {content}")
    print("-" * 70)
    print(f"_Full Article Link_: {link}")
    print("-" * 70)
    

BASE_URL = "https://newsapi.org"
API_KEY = "392dff38dabc450cbbdce04cdfe6407b"

option = input("Browse News By:\n1. Top Headlines\n2: Category\n3: Keyword\nSelect: ").lower()

if option == "1" or option == "top headlines":
    request_url = f"{BASE_URL}/v2/top-headlines?country=us&apikey={API_KEY}"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        data = response.json()
        format_the_data(data)
        option = input("Want To Read a Full Article? Enter Its Number (Enter q to Quit): ")
        if 1 <= int(option) <= 10:
            get_full_article(data, int(option))
        elif option == 'q':
            print("Quitting")
        else:
            print("Wrong Input")                   
    else:
        print("Error Getting The News")

elif option == "2" or option == "category":
    print_cat_menu()
    category = input("Select: ").lower()
    request_url = f"{BASE_URL}/v2/top-headlines?country=us&category={category}&apikey={API_KEY}"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        print(f"\n\nShowing Top 10 Results for {category.upper()} Category\n\n")
        data = response.json()
        format_the_data(data)
        option = input("Want To Read a Full Article? Enter Its Number (Enter q to Quit): ")
        if 1 <= int(option) <= 10:
            get_full_article(data, int(option))
        elif option == 'q':
            print("Quitting")
        else:
            print("Wrong Input")
    else:
        print("Error Getting The News")

elif option == "3" or option == "keyword":
    keyword = input("Enter a Keyword: ").lower()
    request_url = f"{BASE_URL}/v2/top-headlines?q={keyword}&apikey={API_KEY}"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        print(f"\n\nShowing Top 10 Results for {keyword.upper()}\n\n")
        data = response.json()
        print(data)
        format_the_data(data)
        option = input("Want To Read a Full Article? Enter Its Number (Enter q to Quit): ")
        if 1 <= int(option) <= 10:
            get_full_article(data, int(option))
        elif option == 'q':
            print("Quitting")
        else:
            print("Wrong Input")
        
    else:
        print("Error Getting The News")    
else: 
    print("Wrong Input")