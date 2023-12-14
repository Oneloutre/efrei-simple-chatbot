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

def turn_matrix_col_to_arr(mat,col,lines):
    arr = []
    for i in range(1,lines):
        arr.append(mat[i][col])
    return arr

def turn_vect_dict_to_arr(vect):
    arr = []
    for ai in vect:
        arr.append(ai.values())

    return arr

def calc_scalary_product(a_arr,b_arr):
    s = 0
    for ai,bi in a_arr,b_arr:
        s = s+ (ai*bi)
    return s

def calc_vector_length(vect):
    s = 0
    for i in vect:
        s = s+i
    the_length = math.sqrt(s)
    return the_length

def calc_similarity(qst_tf_idf_vect,tf_idf_matrix):
    similarity_dict = {}
    qst_length = len(qst_tf_idf_vect)
    docs = number_of_docs(the_cleaned_folder_directory)
    qst_tf_idf_vect_cleaned = turn_vect_dict_to_arr(qst_tf_idf_vect)
    for row in range(1,docs):
        matrix_row_cleaned = turn_matrix_col_to_arr(tf_idf_matrix,row,qst_length)
        similarity_val = (calc_scalary_product(qst_tf_idf_vect_cleaned,matrix_row_cleaned))/calc_vector_length(qst_tf_idf_vect)*calc_vector_length(matrix_row_cleaned)
        similarity_dict[tf_idf_matrix[0][row]] = similarity_val
    return(similarity_dict)



def qst_test():
    clnd = processing_qst("Comment les presidents evoquent la nation?")

    prsdnts = qst_words_in_docs(clnd)

    return(prsdnts)

