import csv 

list = []

def read_file():
    list = []
    with open("news.csv","r",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            list.append(row)
    return list


def save_file(list):
    with open("news.csv","w",newline="") as file:
        fieldnames = ["id", "category", "title", "description"]
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)


def add_news():
    category = input("Enter Category: ")
    title = input("Enter Title: ")
    description = input("Enter Description: ")

    news_list = read_file()
    news_id = len(news_list)+1

    with open("news.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([news_id, category, title, description])

    print("News added successfully")


def view_news():
    with open("news.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("-" * 40)
            print("ID:", row["id"])
            print("Category:", row["category"])
            print("Title:", row["title"])
            print("Description:", row["description"])

def search_news():
    word = input("Enter title for search news: ")
    found = False 

    with open("news.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if word in row["title"].lower():
                print()
                print("ID:", row["id"])
                print("Category:", row["category"])
                print("Title:", row["title"])
                print("Description:", row["description"])
                found = True

    if not found:
        print("News Not Found.")


def delete_news():
    news_id = input("Enter news id for delete news: ")

    list = []

    with open("news.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] != news_id:
                list.append(row)

    save_file(list)
    
    print("News deleted successfully.")
