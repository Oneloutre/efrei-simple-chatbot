import os

file_list = []
president_list = []
def Nameextraction():
    for files in os.listdir('../speeches 2023/'):
        file_list.append(files)
    for i in range(len(file_list)):
        president_name = file_list[i].replace('Nomination_','').replace('.txt','')
        president_list.append(president_name)
    print(president_list)




Nameextraction()