import os

file_list = []
president_list = []
president_list_sorted = []
president_list_sorted_nodupe = []
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



Nameextraction()
