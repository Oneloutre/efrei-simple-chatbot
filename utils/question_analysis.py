# File handling the question analysis and the chatbot.

from utils.text_process import *


president_folder_name, the_cleaned_folder_name, president_folder_directory, the_cleaned_folder_directory = program_settings()

tf_dict = tf_score_dict(the_cleaned_folder_directory)
idf_dict = idf_calculator(the_cleaned_folder_directory,tf_dict)
tf_idf_dict = tf_idf_calculator(tf_dict,idf_dict)
matrix_tf_idf,nb_words,nb_docs = tf_idf_matrix(tf_idf_dict,the_cleaned_folder_directory,tf_dict)
tf_idf_matrix_values_only = get_only_values_in_matrix(matrix_tf_idf,nb_words,nb_docs)

# variables assignment

def processing_qst(the_qst): # function to process the question and manage the punctuation
    cleaned_qst = the_qst.lower()
    cleaned_qst = cleaned_qst.replace("-", " ")
    cleaned_qst = cleaned_qst.replace("'", " ")
    cleaned_qst = remove_punct(cleaned_qst)
    cleaned_qst = list(cleaned_qst.split(" "))
    return cleaned_qst


def qst_words_in_docs(cleaned_qst): # function to find the words in the question in the documents
    qst_dict = {}
    for word in cleaned_qst:
        the_presidents = []
        for president in tf_dict.keys():
            current_president = tf_dict[president]
            for president_word in current_president.keys():
                if president_word == word:
                    the_presidents.append(president)
        if the_presidents:
            qst_dict[word] = the_presidents
    return qst_dict

def qst_tf_calculator(question_string): # function to calculate the TF score of the question
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


def calculate_occ_word_in_docs(word,president_tf_score_dict): # function to calculate the occurence of a word in the documents
    president_dict = president_tf_score_dict
    word_counter = 0
    for president in president_dict.keys():
        same_president = False
        current_president = president_dict[president]
        for president_word in current_president.keys():
            if word in president_word and not same_president:
                word_counter = word_counter + 1
                same_president = True

    return word_counter



def qst_idf_calculator(the_cleaned_folder_directory,list_of_tf): # function to calculate the IDF score of the question
    doc_count = number_of_docs(the_cleaned_folder_directory)
    mots = []
    idf_dict = {}
    for dictionnaire in list_of_tf:
        mot = next(iter(dictionnaire))
        mots.append(mot)
    for i in range(len(mots)):
        current_word = mots[i]
        idf_dict[current_word] = math.log(((1+(doc_count))/(1+(calculate_occ_word_in_docs(current_word,tf_dict)))),10)
    return idf_dict


def qst_tf_idf_calculator(qst_tf_calculator_value, qst_idf_calculator_value): # function to calculate the TF-IDF score of the question
    qst_tf_idf_dict = {}
    qst_tf_calculator_value_dict = {}
    for dictionnaire in qst_tf_calculator_value:
        qst_tf_calculator_value_dict.update(dictionnaire)
    for word in qst_tf_calculator_value_dict:
        qst_tf_idf_dict[word] = qst_tf_calculator_value_dict[word]*qst_idf_calculator_value[word]
    return qst_tf_idf_dict

def create_qst_vect(qst_tf_idf,mat,lines,words_in_doc): # function to create the vector of the question
    the_vect = []

    for i in range(1,lines):
        dict = {}
        the_word = mat[i][0]
        if the_word in words_in_doc.keys():
            dict[the_word] = qst_tf_idf[the_word]
        else:
            dict[the_word] = 0
        the_vect.append(dict)
    return the_vect


def turn_matrix_col_to_arr(mat,col,lines): # function to turn a matrix column into an array
    arr = []
    for i in range(1,lines):
        arr.append(mat[i][col])
    return arr

def turn_vect_dict_to_arr(vect): # function to turn a vector dictionary into an array
    arr = []
    for i in range(len(vect)):
        for word in vect[i].keys():
            arr.append(vect[i][word])

    return arr

def calc_scalary_product(a_arr,b_arr): # function to calculate the scalar product of two arrays
    s = 0
    for i in range(len(b_arr)):
        s = s+(a_arr[i]*b_arr[i])
    return s

def calc_vector_length(vect): # function to calculate the length of a vector
    s = 0
    for i in vect:
        s = s+i
    the_length = math.sqrt(s)
    return the_length

def calc_similarity(qst_tf_idf_vect,tf_idf_matrix): # function to calculate the similarity between the question and the documents.
    similarity_dict = {}
    qst_length = len(qst_tf_idf_vect)
    docs = number_of_docs(the_cleaned_folder_directory)
    qst_tf_idf_vect_cleaned = turn_vect_dict_to_arr(qst_tf_idf_vect)
    for row in range(1,docs):
        matrix_row_cleaned = turn_matrix_col_to_arr(tf_idf_matrix,row,qst_length)
        try:
            similarity_val = (calc_scalary_product(qst_tf_idf_vect_cleaned,matrix_row_cleaned))/calc_vector_length(qst_tf_idf_vect_cleaned)*calc_vector_length(matrix_row_cleaned)
            similarity_dict[tf_idf_matrix[0][row]] = similarity_val
        except ZeroDivisionError:
            similarity_dict[tf_idf_matrix[0][row]] = 0
    s = 0
    for values in similarity_dict.values():
        s = s + values
    if s > 0:
        return similarity_dict
    else:
        return 0

def doc_with_best_similarity(similarity_dict): # function to find the document with the best similarity score
    best_sim = max(similarity_dict.values())
    for key in similarity_dict.keys():
        if similarity_dict[key] == best_sim:
            return key


def most_similar_doc(similarity): # function to find the most similar document
    max_val = max(similarity.values())
    for doc in similarity.keys():
        if similarity[doc] == max_val:
            return doc
def word_in_most_similar_doc(qst_tf_idf,sim,word_in_doc): # function to find the word in the most similar document
    highest_sim = most_similar_doc(sim)
    doc = highest_sim.replace(".txt","").replace("Nomination_","")
    curr_highest = 0
    word_is = ""
    for word in word_in_doc.keys():
        if doc in word_in_doc[word]:
            if qst_tf_idf[word] > curr_highest:
                curr_highest = qst_tf_idf[word]
                word_is = word
    return word_is




def finding_first_sentence_with_word(qst_highest_tf,the_doc,president_dir):# function to find the first sentence with the word in the document

    with open(f'{president_dir}/{the_doc}','r') as president_doc:
        paragraphs = president_doc.read().split('\n')

        for paragraph in paragraphs:
            sentences = paragraph.split('.')
            for sentence in sentences:
                if qst_highest_tf in sentence.lower():
                    return sentence.strip()+'.'


def generate_question(sentence,question): # function to generate the answer to the question
    question_starters = {
        "Peux-tu":"Oui, bien sûr! ",
        "peux-tu": "Oui, bien sûr! ",
        "Parle-moi":"Avec plaisir ! ",
        "parle-moi": "Avec plaisir ! ",
        "Comment": "Après analyse, ",
        "comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "pourquoi": "Car, ",
        "Explique-moi":"Bien sûr, ",
        "explique-moi":"Bien sûr, "
    }
    for starter in question_starters.keys():
        if question.startswith(starter):
            return (question_starters[starter] + sentence.lower())
    return f"réponse : {sentence}"




def chatbot_handler(): # function to handle the chatbot

    question = input("What is your question? : ")
    question_cleaned = processing_qst(question)

    docs_for_question = qst_words_in_docs(question_cleaned)

    qst_tf = qst_tf_calculator(question)
    qst_idf = qst_idf_calculator(the_cleaned_folder_directory,qst_tf)

    qst_tf_idf = qst_tf_idf_calculator(qst_tf,qst_idf)

    qst_vect = create_qst_vect(qst_tf_idf,matrix_tf_idf,nb_words,docs_for_question)


    sim = calc_similarity(qst_vect,matrix_tf_idf)

    if sim == 0:
        print("Sorry but there was an error finding an answer, maybe try being more specific?")

    else:
        the_word = word_in_most_similar_doc(qst_tf_idf, sim, docs_for_question)
        the_doc = most_similar_doc(sim)

        the_sentence = finding_first_sentence_with_word(the_word, the_doc, president_folder_directory)
        answer = generate_question(the_sentence, question)
        print(answer)

