import os
import string

president_folder_name = 'speeches 2023'
the_cleaned_folder_name = 'Cleaned'
president_folder_directory = f'../{president_folder_name}'
the_cleaned_folder_directory = f'../{the_cleaned_folder_name}'

file_list = []
president_list = []
def Nameextraction():
    for files in os.listdir('../speeches 2023/'):
        file_list.append(files)
    for i in range(len(file_list)):
        president_name = file_list[i].replace('Nomination_','').replace('.txt','')
        president_list.append(president_name)
    print(president_list)


def remove_punct(c):
    line = c
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
                    cleaned_text = cleaned_text.replace("\n",'')
                    cleaned_text = remove_punct(cleaned_text)
                    after_cleaning.write(cleaned_text)
        before_cleaning.close()


cleaning_the_texts(president_folder_name,the_cleaned_folder_name,president_folder_directory,the_cleaned_folder_directory)


Nameextraction()