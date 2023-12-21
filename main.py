import utils.text_analysis as analysis
import utils.text_process as process
import utils.question_analysis as chatbot
import useless_robots.useless_robot_selector as useless

def launch():


    print("\n========================== { Welcome to the Chatbot ! } ==========================")
    print("Menu :\n1. Display the list of least important words. \n2. Display the word(s) with the highest TF-IDF score. \n3. Identify the word(s) most frequently repeated by President Chirac.\n4. Identify the name(s) of the president(s) who have spoken about the 'Nation' and the one who has repeated it the most times.\n5. Identify the first president to discuss climate and/or ecology.\n6. Excluding words labeled as 'non-important', what word(s) have all presidents mentioned.\n7. Launch Chatbot.\n\n8. Exit")
    choice = int(input())
    if choice == 1:
        analysis.fonct_least_important_words()
        launch()
    elif choice == 2:
        analysis.fonct_word_highest_tfidf()
        launch()
    elif choice == 3:
        analysis.fonct_most_words_repeated_by_president()
        launch()
    elif choice == 4:
        analysis.fonct_srch_president_by_word()
        launch()
    elif choice == 5:
        analysis.fonct_first_president_to_mention_word()
        launch()
    elif choice == 6:
        analysis.fonct_words_repeated_by_all_presidents()
        launch()
    elif choice == 7:
        chatbot.chatbot_handler()
        launch()
    elif choice == 8:
        exit()
    else:
        print("Please enter a valid number.")
        launch()



if __name__ == "__main__":

    process.launch_text_process()
    print(useless.useless_robot_selector())
    launch()