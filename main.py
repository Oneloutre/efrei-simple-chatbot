import utils_chat.text_process as process
import useless_robots.useless_robot_selector as useless

def launch():
    print(useless.useless_robot_selector())
    print("\n========================== { Welcome to the Chatbot ! } ==========================")
    print("Menu :\n 1. Extract the president's names \n 2. Display the list of least important words. \n 3. Display the word(s) with the highest TF-IDF score. \n  \n 9. Exit")
    choice = int(input())
    if choice == 1:
        process.Nameextraction()
    #elif choice == 2:
        #process.Leastimportantwords()
    #elif choice == 3:
        #process.TFIDF()
    #elif choice == 9:
        #exit()
    else:
        print("Please enter a valid number.")
        launch()
    #process.TextExtract()



if __name__ == "__main__":
    launch()