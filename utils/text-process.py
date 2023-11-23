import os

file_list = []
president_list = []
def Nameextraction():
    MitterandCount = 0
    for files in os.listdir('../speeches 2023/'):
        file_list.append(files)
    for i in range(len(file_list)):
        president_name = file_list[i].replace('Nomination_','').replace('.txt','')
        if "Giscard dEstaing" in president_name:
            president_name = "Valéry Giscard d'Estaing"
        if "Mitterrand" in president_name:
            MitterandCount += 1
            president_name = "François Mitterrand" + str(MitterandCount)
        if "Chirac" in president_name:
            president_name = "Jacques Chirac"
        if "Sarkozy" in president_name:
            president_name = "Nicolas Sarkozy"
        if "Hollande" in president_name:
            president_name = "François Hollande"
        if "Macron" in president_name:
            president_name = "Emmanuel Macron"
        president_list.append(president_name)
    print(president_list)


Nameextraction()