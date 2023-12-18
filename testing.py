from utils.question_analysis import qst_tf_calculator as tf_calc, qst_tf_idf_calculator
from utils.question_analysis import qst_idf_calculator as idf_calc

president_folder_name = 'speeches 2023'
the_cleaned_folder_name = 'Cleaned'
president_folder_directory = f'./{president_folder_name}'
the_cleaned_folder_directory = f'./{the_cleaned_folder_name}'

question = "vive l'écologie écologie"

rep = tf_calc(question)
answer = idf_calc(the_cleaned_folder_directory, rep)

print(qst_tf_idf_calculator(rep, answer))