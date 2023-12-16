import os
import string
import math
from settings import program_settings
from utils.text_process import *



president_folder_name, the_cleaned_folder_name, president_folder_directory, the_cleaned_folder_directory = program_settings()

tf_dict = tf_score_dict(the_cleaned_folder_directory)
idf_dict = idf_calculator(the_cleaned_folder_directory,tf_dict)
tf_idf_dict = tf_idf_calculator(tf_dict,idf_dict)
matrix_tf_idf,nb_words,nb_docs = tf_idf_matrix(tf_idf_dict,the_cleaned_folder_directory,tf_dict)
tf_idf_matrix_values_only = get_only_values_in_matrix(matrix_tf_idf,nb_words,nb_docs)

def processing_qst(the_qst):
    cleaned_qst = the_qst.lower()
    cleaned_qst = remove_punct(the_qst)
    cleaned_qst = list(cleaned_qst.split(" "))
    return cleaned_qst


def qst_words_in_docs(cleaned_qst):

    qst_dict = {}
    for word in cleaned_qst:
        the_presidents = []
        for president in tf_dict.keys():
            current_president = tf_dict[president]
            if word in current_president.keys():
                the_presidents.append(president)
        if the_presidents:
            qst_dict[word] = the_presidents

    return qst_dict

def qst_tf_calculator(question_string):
    question_string = processing_qst(question_string)
    list_of_tf = []
    list_question_string = question_string
    for words in list_question_string:
        dico = {}
        counter = list_question_string.count(words)
        dico[words] = counter
        if dico not in list_of_tf:
            list_of_tf.append(dico)

    return list_of_tf


def calculate_occ_word_in_docs(word,the_cleaned_folder_directory,president_tf_score_dict):
    president_dict = president_tf_score_dict
    word_counter = 0
    for president in president_dict.keys():
        current_president = president_dict[president]
        if word in current_president.keys():
            word_counter = word_counter + 1

    return word_counter



def qst_idf_calculator(the_cleaned_folder_directory,list_of_tf):
    doc_count = number_of_docs(the_cleaned_folder_directory)
    mots = []
    idf_dict = {}
    for dictionnaire in list_of_tf:
        mot = next(iter(dictionnaire))
        mots.append(mot)
    for i in range(len(mots)):
        current_word = mots[i]
        idf_dict[current_word] = math.log((1+(doc_count)/(1+(calculate_occ_word_in_docs(current_word, the_cleaned_folder_directory,tf_dict)))), 10)
    return idf_dict


def qst_tf_idf_calculator(qst_tf_calculator_value, qst_idf_calculator_value):
    qst_tf_idf_dict = {}
    qst_tf_calculator_value_dict = {}
    for dictionnaire in qst_tf_calculator_value:
        qst_tf_calculator_value_dict.update(dictionnaire)
    for word in qst_tf_calculator_value_dict:
        print(word)
        qst_tf_idf_dict[word] = qst_tf_calculator_value_dict[word]*qst_idf_calculator_value[word]
    return qst_tf_idf_dict