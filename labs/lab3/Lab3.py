import MyWorkWithFiles as mw


# Existing groups -> КиТ-16а and КиТ-16б
def main():
    try:
        print("Choice option - > \n",
              "1 = Print all from file \n",
              "2 = Append record to file \n",
              "3 = Rewrite or create new file \n",
              "4 = Search record by index at file and print \n",
              "5 = Sort records by rating and print \n",
              "6 = Search files at directory \n")
        choice = int(input("Your choice -> "))
        mw.choice_option(choice)
    except ValueError:
        print("Enter only number")


if __name__ == "__main__":
    main()
