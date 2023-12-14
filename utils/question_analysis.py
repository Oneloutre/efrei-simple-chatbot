import os
import string
import math
from settings import program_settings
from text_process import *



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
    the_presidents = []
    for word in cleaned_qst:
        for president in tf_dict.keys():
            current_president = tf_dict[president]
            if word in current_president.keys():
                the_presidents.append(president)

    return the_presidents



