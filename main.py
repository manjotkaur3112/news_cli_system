from data import add_news, delete_news, search_news, view_news

while True:
    print("News CLI System")
    print("1. Add News")
    print("2. View All News")
    print("3. Search News")
    print("4. Delete News")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        add_news()
    elif choice == 2:
        view_news()
    elif choice == 3:
        search_news()
    elif choice == 4:
        delete_news()
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice.")


