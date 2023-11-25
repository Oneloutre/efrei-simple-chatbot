import os
import string
import math

president_folder_name = 'speeches 2023'
the_cleaned_folder_name = 'Cleaned'
president_folder_directory = f'../{president_folder_name}'
the_cleaned_folder_directory = f'../{the_cleaned_folder_name}'

file_list = []
president_list = []
president_list_sorted = []
def Nameextraction():
    for files in os.listdir('../speeches 2023/'):
        file_list.append(files)
    for i in range(len(file_list)):
        president_name = file_list[i].replace('Nomination_','').replace('.txt','')
        president_list.append(president_name)
    for i in president_list:
        i = ''.join(filter(lambda z: not z.isdigit(), i))
        if "Chirac" in i:
            i = "Jacques Chirac"
        if "Sarkozy" in i:
            i = "Nicolas Sarkozy"
        if "Hollande" in i:
            i = "François Hollande"
        if "Macron" in i:
            i = "Emmanuel Macron"
        if "Mitterrand" in i:
            i = "François Mitterrand"
        if "Giscard" in i:
            i = "Valéry Giscard d'Estaing"
        president_list_sorted.append(i)
    president_list_sorted_nodupe = list(dict.fromkeys(president_list_sorted))
    print(president_list_sorted_nodupe)


def remove_punct(c):
    line = c
    line = line.replace("'"," ")
    line = line.replace(","," ")
    line = line.translate(str.maketrans(' ',' ',string.punctuation))
    line = line.replace("  "," ")
    return line


def cleaning_the_texts(presidentfoldername,cleanedfoldername,presidentfolderdirectory,cleanedfolderdirectory):

    the_folder = presidentfoldername
    the_cleaned_folder = cleanedfoldername
    folder_directory = presidentfolderdirectory
    cleaned_folder_directory = cleanedfolderdirectory


    for file in os.listdir(folder_directory):
        with open(f'{folder_directory}/{file}',"r") as before_cleaning:
            with open(f'{cleaned_folder_directory}/{file}',"w") as after_cleaning:
                reading_before_cleaning = before_cleaning.readlines()
                for i in reading_before_cleaning:
                    cleaned_text = i.lower()
                    cleaned_text = cleaned_text.replace("\n",' ')
                    cleaned_text = remove_punct(cleaned_text)
                    after_cleaning.write(cleaned_text)
        before_cleaning.close()


cleaning_the_texts(president_folder_name,the_cleaned_folder_name,president_folder_directory,the_cleaned_folder_directory)

Nameextraction()

def get_president_name(file):
    president_name = file.replace("Nomination_", "").replace(".txt", "")
    return president_name

def tf_score_dict(the_cleaned_folder_directory):
    presidents = {}
    for file in os.listdir(the_cleaned_folder_directory):
        with open(f'{the_cleaned_folder_directory}/{file}',"r") as test:
            president_name = get_president_name(file)
            president_words = {}
            presidents[president_name] = president_words
            t = test.read()
            t = t.split(" ")
            t_noremoval = t
            t = list(dict.fromkeys(t))
            for i in t:
                president_words[i] = 0
            for word in president_words.keys():
                for i in t_noremoval:
                    if word == i:
                        president_words[word] = president_words[word]+1


            test.close()
    return presidents


president_tf_score_dict = tf_score_dict(the_cleaned_folder_directory)

def number_of_docs(the_cleaned_folder_directory):
    doc_counter = 0
    for file in os.listdir(the_cleaned_folder_directory):
        doc_counter = doc_counter + 1
    return doc_counter



def calculate_occ_word_indocs(word,the_cleaned_folder_directory):
    president_dict = president_tf_score_dict
    word_counter = 0
    for president in president_dict.keys():
        current_president = president_dict[president]
        if word in current_president.keys():
            word_counter = word_counter + 1

    return word_counter



def idf_calculator(the_cleaned_folder_directory):
    doc_count = number_of_docs(the_cleaned_folder_directory)
    president_dict = president_tf_score_dict
    president_idf_dict = {}
    for president in president_dict.keys():
        current_president = president_dict[president]
        idf_dict = {}
        for word in current_president.keys():
            idf_dict[word] = math.log((1+(doc_count))/(1+(calculate_occ_word_indocs(word,the_cleaned_folder_directory))))
        president_idf_dict[president] = idf_dict
    return president_idf_dict
president_idf_score_dict = idf_calculator(the_cleaned_folder_directory)

def tf_idf_calculator(tf_dict,idf_dict):
    president_tf_idf_dict = {}
    for president in tf_dict.keys():
        curr_president_tf = tf_dict[president]
        curr_president_idf = idf_dict[president]
        tf_idf_for_word = {}
        for word in curr_president_tf.keys():
            tf_idf_for_word[word] = curr_president_tf[word]*curr_president_idf[word]
        president_tf_idf_dict[president] = tf_idf_for_word
    return president_tf_idf_dict
tf_idf_dict = tf_idf_calculator(president_tf_score_dict,president_idf_score_dict)