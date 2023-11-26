from text_process import *

president_folder_name = 'speeches 2023'
the_cleaned_folder_name = 'Cleaned'
president_folder_directory = f'../{president_folder_name}'
the_cleaned_folder_directory = f'../{the_cleaned_folder_name}'


matrix_tf_idf,nb_words,nb_docs = tf_idf_matrix(tf_idf_dict,the_cleaned_folder_directory)
tf_idf_matrix_values_only = get_only_values_in_matrix(matrix_tf_idf,nb_words,nb_docs)
tf_dict = tf_score_dict(the_cleaned_folder_directory)
idf_dict = idf_calculator(the_cleaned_folder_directory)

def least_important_words(matrix,lines,rows):
    the_words = []

    for line in range(1,lines):
        line_is_zero = True
        for row in range(1,rows):
            if matrix[line][row] != 0:
                line_is_zero = False
        if line_is_zero :
            the_words.append(matrix[line][0])

    print("The least important words are : ")
    for i in the_words:
        print(i,end=", ")
    print("")


def srch_max_tfidf(matrix,lines):
    max_in_each_line = []
    for line in range(lines):
        max_in_each_line.append(max(matrix[line]))
    return max(max_in_each_line)

srch_max_tfidf(tf_idf_matrix_values_only,nb_words-1)

def word_highest_tfidf(matrix,lines,rows,score):
    the_words = []

    for line in range(lines):
        for row in range(rows):
            if matrix[line][row] == score:
                the_words.append(matrix[line][0])
    print("The words with highest score : ")
    for i in the_words:
        print(i,end=", ")
    print("")


def srch_max_in_dict(dict):
    return (max(dict.values()))

def srch_docs_by_president(president,cleaned_directory):
    the_docs = []
    for file in os.listdir(cleaned_directory):
        if president in file:
            the_docs.append(get_president_name(file))
    return the_docs

def srch_max_from_president(versions,dict):
    max_from_doc = []
    for version in versions:
        max_from_doc.append(srch_max_in_dict(dict[version]))

    return (max(max_from_doc))

def most_words_repeated_by_president(tf_dict,president):
    president_versions = srch_docs_by_president(president,the_cleaned_folder_directory)
    highest_score = srch_max_from_president(president_versions,tf_dict)
    the_repeated_words = []
    for version in president_versions:
        president_doc = tf_dict[version]
        for word in president_doc:
            if president_doc[word] == highest_score:
                the_repeated_words.append(word)

    print("The most repeated words by",president,"are : ")
    for word in the_repeated_words:
        print(word,end=", ")
    print("")


def srch_president_by_word(word,tf_dict):
    the_word = word.lower()
    repeated_total_score = {}
    repeated_total_score_cleaned = {}
    presidents_mentioning_word = []
    presidents_mentioning_word_cleaned = []
    presidents_mentioning_word_cleaned_nodupe = []
    for president in tf_dict.keys():
        selected_president = tf_dict[president]
        repeated_total_score[president] = 0
        for aword in selected_president.keys():
            if the_word in aword:
                presidents_mentioning_word.append(president)
                repeated_total_score[president] = repeated_total_score[president] + selected_president[aword]
    for i in presidents_mentioning_word:
        i = ''.join(filter(lambda z: not z.isdigit(), i))
        presidents_mentioning_word_cleaned.append(i)
    presidents_mentioning_word_cleaned_nodupe = list(dict.fromkeys(presidents_mentioning_word_cleaned))

    for president in presidents_mentioning_word_cleaned_nodupe:
        repeated_total_score_cleaned[president] = 0
        for version in repeated_total_score.keys():
            if version.startswith(president):
                repeated_total_score_cleaned[president] = repeated_total_score_cleaned[president] + repeated_total_score[version]

    max_score = max(repeated_total_score_cleaned.values())

    for president in repeated_total_score_cleaned.keys():
        if repeated_total_score_cleaned[president] == max_score:
            president_repeated_most = president

    print("Presidents mentioning",word,": ")
    for i in presidents_mentioning_word_cleaned_nodupe:
        print(i,end=", ")
    print("")
    print("And it was repeated",max_score,"times by",president_repeated_most)


def presidents_in_order():
    the_list = []
    the_list.append("Giscard dEstaing")
    the_list.append("Mitterrand")
    the_list.append("Chirac")
    the_list.append("Sarkozy")
    the_list.append("Hollande")
    the_list.append("Macron")
    return the_list

president_list_ordered = presidents_in_order()

def first_president_to_mention_word(word,president_list,tf_dict):
    result = False
    nbr_presidents = len(president_list)
    i = 0
    the_word = word.lower()
    president_mentioning = ""
    for president in president_list:
        if not result:
            print("now in", president)
            versions = srch_docs_by_president(president, the_cleaned_folder_directory)
            for version in versions:
                selected_president = tf_dict[version]
                for aword in selected_president.keys():
                    if word in aword:
                        result = True
                        president_mentioning = president
    if president_mentioning == "":
        print("No president mentioned that word")
    else :
        print(president_mentioning)

def get_pure_president_name(file):
    president_name = get_president_name(file)
    president_name = ''.join(filter(lambda z: not z.isdigit(), president_name))
    return president_name

def check_if_word_found_in_other_version(file,word,tf,idf):
    vname = get_president_name(file)
    pure_name = get_pure_president_name(vname)
    is_found = False
    for president in tf.keys():
        if pure_name in president:
            if word in tf[president].keys() and idf[president][word] != 0:
                is_found = True
    return is_found
def words_repeated_by_all_presidents(matrix,lines,rows,tfdict,idfdict):
    the_words = []

    for line in range(1,lines):
        not_nill = True
        for row in range(1,rows):
            if matrix[line][row] == 0:
                if not check_if_word_found_in_other_version(matrix[0][row],matrix[line][0],tfdict,idfdict):
                    not_nill = False

        if not_nill:
            the_words.append(matrix[line][0])

    print("Words repeated by all presidents")
    for word in the_words:
        if len(word)>2:
            print(word)


least_important_words(matrix_tf_idf,nb_words,nb_docs)
word_highest_tfidf(matrix_tf_idf,nb_words,nb_docs,srch_max_tfidf(tf_idf_matrix_values_only,nb_words-1))
most_words_repeated_by_president(tf_dict,"Chirac")

srch_president_by_word("nation",tf_dict)
first_president_to_mention_word("éco",president_list_ordered,tf_dict)

words_repeated_by_all_presidents(matrix_tf_idf,nb_words,nb_docs,tf_dict,idf_dict)

