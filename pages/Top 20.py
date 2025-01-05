import pandas as pd
import streamlit as st
import plotly.express as px

liste_gen = pd.read_excel('liste_gen.xlsx')[['prénom', 'NOM', 'clé', 'mail']]
liste_ml = pd.read_excel('liste_ml.xlsx')[['prénom', 'NOM', 'clé', 'mail']]


######### LIENS ######################

# ML
lien_resultats_ml = "resultats_ml.xlsx"
resultats_ml = pd.read_excel(lien_resultats_ml)
file = pd.ExcelFile(lien_resultats_ml) 
tables_resultats_ml = file.sheet_names

# FR
lien_resultats_fr = "resultats_fr.xlsx"
resultats_fr = pd.read_excel(lien_resultats_fr)
file = pd.ExcelFile(lien_resultats_fr) 
tables_resultats_fr = file.sheet_names

# Dérivées
lien_resultats_der = "resultats_der.xlsx"
resultats_der = pd.read_excel(lien_resultats_der)
file = pd.ExcelFile(lien_resultats_der) 
tables_resultats_der = file.sheet_names

# Primitives
lien_resultats_prim = "resultats_prim.xlsx"
resultats_prim = pd.read_excel(lien_resultats_prim)
file = pd.ExcelFile(lien_resultats_prim) 
tables_resultats_prim = file.sheet_names

# Systèmes 
lien_resultats_sys = "resultats_sys.xlsx"
resultats_sys = pd.read_excel(lien_resultats_sys)
file = pd.ExcelFile(lien_resultats_sys) 
tables_resultats_sys = file.sheet_names



############ EXAMENS ##########################

####### ML ##########
exam1_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[0])
exam1_ml = exam1_ml[['Clé', 'Note/20,00']]
exam1_ml.columns = ['clé', 'note']
exam1_ml = exam1_ml.groupby(['clé']).max().reset_index()

exam2_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[1])
exam2_ml = exam2_ml[['Clé', 'Note/20,00']]
exam2_ml.columns = ['clé', 'note']
exam2_ml = exam2_ml.groupby(['clé']).max().reset_index()

exam3_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[2])
exam3_ml = exam3_ml[['Clé', 'Note/20,00']]
exam3_ml.columns = ['clé', 'note']
exam3_ml = exam3_ml.groupby(['clé']).max().reset_index()

exam4_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[3])
exam4_ml = exam4_ml[['Clé', 'Note/20,00']]
exam4_ml.columns = ['clé', 'note']
exam4_ml = exam4_ml.groupby(['clé']).max().reset_index()

exam5_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[4])
exam5_ml = exam5_ml[['Clé', 'Note/20,00']]
exam5_ml.columns = ['clé', 'note']
exam5_ml = exam5_ml.groupby(['clé']).max().reset_index()

exam6_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[5])
exam6_ml = exam6_ml[['Clé', 'Note/20,00']]
exam6_ml.columns = ['clé', 'note']
exam6_ml = exam6_ml.groupby(['clé']).max().reset_index()

exam7_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[6])
exam7_ml = exam7_ml[['Clé', 'Note/20,00']]
exam7_ml.columns = ['clé', 'note']
exam7_ml = exam7_ml.groupby(['clé']).max().reset_index()

exam8_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[7])
exam8_ml = exam8_ml[['Clé', 'Note/20,00']]
exam8_ml.columns = ['clé', 'note']
exam8_ml = exam8_ml.groupby(['clé']).max().reset_index()

exam9_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[8])
exam9_ml = exam9_ml[['Clé', 'Note/20,00']]
exam9_ml.columns = ['clé', 'note']
exam9_ml = exam9_ml.groupby(['clé']).max().reset_index()

exam10_ml = pd.read_excel(lien_resultats_ml, sheet_name=tables_resultats_ml[9])
exam10_ml = exam10_ml[['Clé', 'Note/20,00']]
exam10_ml.columns = ['clé', 'note']
exam10_ml = exam10_ml.groupby(['clé']).max().reset_index()

liste_exams_ML = [exam1_ml, exam2_ml, exam3_ml, exam4_ml, exam5_ml, exam6_ml, exam7_ml, exam8_ml, exam9_ml, exam10_ml]

for x in range(len(liste_exams_ML)):
    liste_exams_ML[x].columns = ['clé', 'note_ml_t'+str(x+1)]

ml = liste_ml.merge(exam1_ml, how='left', on='clé')
ml = ml.merge(exam2_ml, how='left', on='clé')
ml = ml.merge(exam3_ml, how='left', on='clé')
ml = ml.merge(exam4_ml, how='left', on='clé')
ml = ml.merge(exam5_ml, how='left', on='clé')
ml = ml.merge(exam6_ml, how='left', on='clé')
ml = ml.merge(exam7_ml, how='left', on='clé')
ml = ml.merge(exam8_ml, how='left', on='clé')
ml = ml.merge(exam9_ml, how='left', on='clé')
ml = ml.merge(exam10_ml, how='left', on='clé')

ml['note_max'] = ml.max(axis='columns', numeric_only=True)

validations_ml = []

for i in range(ml.shape[0]):
    if ml['note_max'].isnull()[i] == True:
        validations_ml.append('pas_de_tentative')
    elif ml['note_max'][i] >= 10:
        validations_ml.append('validé')
    else:
        validations_ml.append('pas_validé')

ml['validation'] = validations_ml

xp = []
for i in range(ml.shape[0]):
    if validations_ml[i] == 'pas_de_tentative':
        xp.append('pas_de_tentative')
    elif validations_ml[i] == 'pas_validé':
        xp.append('pas_validé')
    elif [ml['note_max'][i] for i in range(ml.shape[0])][i] == 20:
         xp.append('Argent')
    else:
        xp.append('Bronze')
ml['xp'] = xp


#### Fonctions réelles ##########


exam1_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[0])
exam1_fr = exam1_fr[['Clé', 'Note/20,00']]
exam1_fr.columns = ['clé', 'note']
exam1_fr = exam1_fr.groupby(['clé']).max().reset_index()

exam2_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[1])
exam2_fr = exam2_fr[['Clé', 'Note/20,00']]
exam2_fr.columns = ['clé', 'note']
exam2_fr = exam2_fr.groupby(['clé']).max().reset_index()

exam3_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[2])
exam3_fr = exam3_fr[['Clé', 'Note/20,00']]
exam3_fr.columns = ['clé', 'note']
exam3_fr = exam3_fr.groupby(['clé']).max().reset_index()

exam4_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[3])
exam4_fr = exam4_fr[['Clé', 'Note/20,00']]
exam4_fr.columns = ['clé', 'note']
exam4_fr = exam4_fr.groupby(['clé']).max().reset_index()

exam5_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[4])
exam5_fr = exam5_fr[['Clé', 'Note/20,00']]
exam5_fr.columns = ['clé', 'note']
exam5_fr = exam5_fr.groupby(['clé']).max().reset_index()

exam6_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[5])
exam6_fr = exam6_fr[['Clé', 'Note/20,00']]
exam6_fr.columns = ['clé', 'note']
exam6_fr = exam6_fr.groupby(['clé']).max().reset_index()

exam7_fr = pd.read_excel(lien_resultats_fr, sheet_name=tables_resultats_fr[6])
exam7_fr = exam7_fr[['Clé', 'Note/20,00']]
exam7_fr.columns = ['clé', 'note']
exam7_fr = exam7_fr.groupby(['clé']).max().reset_index()

liste_exams_FR = [exam1_fr, exam2_fr, exam3_fr, exam4_fr, exam5_fr, exam6_fr, exam7_fr]

for x in range(len(liste_exams_FR)):
    liste_exams_FR[x].columns = ['clé', 'note_fr_t'+str(x+1)]

fr = liste_gen.merge(exam1_fr, how='left', on='clé')
fr = fr.merge(exam2_fr, how='left', on='clé')
fr = fr.merge(exam3_fr, how='left', on='clé')
fr = fr.merge(exam4_fr, how='left', on='clé')
fr = fr.merge(exam5_fr, how='left', on='clé')
fr = fr.merge(exam6_fr, how='left', on='clé')
fr = fr.merge(exam7_fr, how='left', on='clé')

fr['note_max'] = fr.max(axis='columns', numeric_only=True)

validations_fr = []
for i in range(fr.shape[0]):
    if fr['note_max'].isnull()[i] == True:
        validations_fr.append('pas_de_tentative')
    elif fr['note_max'][i] >= 11:
        validations_fr.append('validé')
    else:
        validations_fr.append('pas_validé')
fr['validation'] = validations_fr

xp = []
for i in range(fr.shape[0]):
    if validations_fr[i] == 'pas_de_tentative':
        xp.append('pas_de_tentative')
    elif validations_fr[i] == 'pas_validé':
        xp.append('pas_validé')
    elif [fr['note_max'][i] for i in range(fr.shape[0])][i] == 20:
         xp.append('Argent')
    else:
        xp.append('Bronze')
fr['xp'] = xp


########### Dérivées


exam1_der = pd.read_excel(lien_resultats_der, sheet_name=tables_resultats_der[0])
exam1_der = exam1_der[['Clé', 'Note/20,00']]
exam1_der.columns = ['clé', 'note']
exam1_der = exam1_der.groupby(['clé']).max().reset_index()

exam2_der = pd.read_excel(lien_resultats_der, sheet_name=tables_resultats_der[1])
exam2_der = exam2_der[['Clé', 'Note/20,00']]
exam2_der.columns = ['clé', 'note']
exam2_der = exam2_der.groupby(['clé']).max().reset_index()

exam3_der = pd.read_excel(lien_resultats_der, sheet_name=tables_resultats_der[2])
exam3_der = exam3_der[['Clé', 'Note/20,00']]
exam3_der.columns = ['clé', 'note']
exam3_der = exam3_der.groupby(['clé']).max().reset_index()

exam4_der = pd.read_excel(lien_resultats_der, sheet_name=tables_resultats_der[3])
exam4_der = exam4_der[['Clé', 'Note/20,00']]
exam4_der.columns = ['clé', 'note']
exam4_der = exam4_der.groupby(['clé']).max().reset_index()

exam5_der = pd.read_excel(lien_resultats_der, sheet_name=tables_resultats_der[4])
exam5_der = exam5_der[['Clé', 'Note/20,00']]
exam5_der.columns = ['clé', 'note']
exam5_der = exam5_der.groupby(['clé']).max().reset_index()

liste_exams_der = [exam1_der, exam2_der, exam3_der, exam4_der, exam5_der]

for x in range(len(liste_exams_der)):
    liste_exams_der[x].columns = ['clé', 'note_der_t'+str(x+1)]

der = liste_gen.merge(exam1_der, how='left', on='clé')
der = der.merge(exam2_der, how='left', on='clé')
der = der.merge(exam3_der, how='left', on='clé')
der = der.merge(exam4_der, how='left', on='clé')
der = der.merge(exam5_der, how='left', on='clé')

der['note_max'] = der.max(axis='columns', numeric_only=True)

validations_der = []
for i in range(der.shape[0]):
    if der['note_max'].isnull()[i] == True:
        validations_der.append('pas_de_tentative')
    elif der['note_max'][i] >= 10:
        validations_der.append('validé')
    else:
        validations_der.append('pas_validé')
der['validation'] = validations_der

xp = []
for i in range(der.shape[0]):
    if validations_der[i] == 'pas_de_tentative':
        xp.append('pas_de_tentative')
    elif validations_der[i] == 'pas_validé':
        xp.append('pas_validé')
    elif [der['note_max'][i] for i in range(der.shape[0])][i] == 20:
         xp.append('Argent')
    else:
        xp.append('Bronze')
der['xp'] = xp


############ Primitives

exam1_prim = pd.read_excel(lien_resultats_prim, sheet_name=tables_resultats_prim[0])
exam1_prim = exam1_prim[['Clé', 'Note/20,00']]
exam1_prim.columns = ['clé', 'note']
exam1_prim = exam1_prim.groupby(['clé']).max().reset_index()

exam2_prim = pd.read_excel(lien_resultats_prim, sheet_name=tables_resultats_prim[1])
exam2_prim = exam2_prim[['Clé', 'Note/20,00']]
exam2_prim.columns = ['clé', 'note']
exam2_prim = exam2_prim.groupby(['clé']).max().reset_index()

exam3_prim = pd.read_excel(lien_resultats_prim, sheet_name=tables_resultats_prim[2])
exam3_prim = exam3_prim[['Clé', 'Note/20,00']]
exam3_prim.columns = ['clé', 'note']
exam3_prim = exam3_prim.groupby(['clé']).max().reset_index()

liste_exams_prim = [exam1_prim, exam2_prim, exam3_prim]

for x in range(len(liste_exams_prim)):
    liste_exams_prim[x].columns = ['clé', 'note_prim_t'+str(x+1)]

prim = liste_gen.merge(exam1_prim, how='left', on='clé')
prim = prim.merge(exam2_prim, how='left', on='clé')
prim = prim.merge(exam3_prim, how='left', on='clé')

prim['note_max'] = prim.max(axis='columns', numeric_only=True)

validations_prim = []
for i in range(prim.shape[0]):
    if prim['note_max'].isnull()[i] == True:
        validations_prim.append('pas_de_tentative')
    elif prim['note_max'][i] >= 11:
        validations_prim.append('validé')
    else:
        validations_prim.append('pas_validé')
prim['validation'] = validations_prim

xp = []
for i in range(prim.shape[0]):
    if validations_prim[i] == 'pas_de_tentative':
        xp.append('pas_de_tentative')
    elif validations_prim[i] == 'pas_validé':
        xp.append('pas_validé')
    elif [prim['note_max'][i] for i in range(prim.shape[0])][i] == 20:
         xp.append('Argent')
    else:
        xp.append('Bronze')
prim['xp'] = xp

############ Systèmes d'équations linéaires

exam1_sys= pd.read_excel(lien_resultats_sys, sheet_name=tables_resultats_sys[0])
exam1_sys = exam1_sys[['Clé', 'Note/10,00']]
exam1_sys.columns = ['clé', 'note']
exam1_sys = exam1_sys.groupby(['clé']).max().reset_index()

exam2_sys= pd.read_excel(lien_resultats_sys, sheet_name=tables_resultats_sys[1])
exam2_sys = exam2_sys[['Clé', 'Note/10,00']]
exam2_sys.columns = ['clé', 'note']
exam2_sys = exam2_sys.groupby(['clé']).max().reset_index()

liste_exams_sys = [exam1_sys, exam2_sys]

for x in range(len(liste_exams_sys)):
    liste_exams_sys[x].columns = ['clé', 'note_sys_t'+str(x+1)]

sys = liste_gen.merge(exam1_sys, how='left', on='clé')
sys = prim.merge(exam2_prim, how='left', on='clé')

sys['note_max'] = sys.max(axis='columns', numeric_only=True)

validations_sys = []
for i in range(sys.shape[0]):
    if sys['note_max'].isnull()[i] == True:
        validations_sys.append('pas_de_tentative')
    elif sys['note_max'][i] >= 5.5:
        validations_sys.append('validé')
    else:
        validations_sys.append('pas_validé')
sys['validation'] = validations_sys

xp = []
for i in range(sys.shape[0]):
    if validations_sys[i] == 'pas_de_tentative':
        xp.append('pas_de_tentative')
    elif validations_sys[i] == 'pas_validé':
        xp.append('pas_validé')
    elif [sys['note_max'][i] for i in range(sys.shape[0])][i] == 10:
         xp.append('Argent')
    else:
        xp.append('Bronze')
sys['xp'] = xp




competences = ["Maths du Lycée", "Fonctions Réelles", "Dérivées", "Primitives", "Systèmes d'équations Linéaires"]
df_competences = [ml, fr, der, prim, sys]

ml_valid = pd.DataFrame(ml.validation.value_counts()).reset_index()
ml_valid.columns = ['validation', "Maths du Lycée"]

fr_valid = pd.DataFrame(fr.validation.value_counts()).reset_index()
fr_valid.columns = ['validation', "Fonctions Réelles"]

der_valid = pd.DataFrame(der.validation.value_counts()).reset_index()
der_valid.columns = ['validation', "Dérivées"]

prim_valid = pd.DataFrame(prim.validation.value_counts()).reset_index()
prim_valid.columns = ['validation', "Primimitives"]

sys_valid = pd.DataFrame(sys.validation.value_counts()).reset_index()
sys_valid.columns = ['validation', "Systèmes_eq_linéaires"]

situation_gen = ml_valid.merge(fr_valid, how='left', on='validation')
situation_gen = situation_gen.merge(der_valid, how='left', on='validation')
situation_gen = situation_gen.merge(prim_valid, how='left', on='validation')
situation_gen = situation_gen.merge(sys_valid, how='left', on='validation')
situation_gen = situation_gen.set_index('validation')

ml_note_xp = ml[['clé','mail', 'note_max', 'validation', 'xp']]
tab_gen = liste_gen.merge(ml_note_xp, how='left', on='clé').drop(['mail_y', 'prénom', 'NOM'], axis=1)
tab_gen['validation'] = tab_gen.validation.fillna('pas_concerné')
tab_gen['xp'] = tab_gen.xp.fillna('pas_concerné')
tab_gen = tab_gen.rename(columns={"mail_x": "mail"})
tab_gen['note_max'] = ['pas_concerné' if tab_gen.validation[i] == 'pas_concerné' else tab_gen.note_max[i] for i in range(tab_gen.shape[0])]
tab_gen = tab_gen.rename(columns={"note_max": "Maths_Lycée", "validation": "validation_Maths_Lycée", "xp": "xp_Maths_Lycée"})
tab_gen = tab_gen.merge(fr[['clé', 'note_max', 'validation', 'xp']], how='left', on='clé')
tab_gen = tab_gen.rename(columns={"note_max": "Fonctions_Réelles", "validation": "validation_Fonctions_Réelles", "xp": "xp_Fonctions_Réelles"})
tab_gen = tab_gen.merge(der[['clé', 'note_max', 'validation', 'xp']], how='left', on='clé')
tab_gen = tab_gen.rename(columns={"note_max": "Dérivées", "validation": "validation_Dérivées", "xp": "xp_Dérivées"})
tab_gen = tab_gen.merge(prim[['clé', 'note_max', 'validation', 'xp']], how='left', on='clé')
tab_gen = tab_gen.rename(columns={"note_max": "Primitives", "validation": "validation_Primitives", "xp": "xp_Primitives"})
tab_gen = tab_gen.merge(sys[['clé', 'note_max', 'validation', 'xp']], how='left', on='clé')
tab_gen = tab_gen.rename(columns={"note_max": "Systèmes_eq_linéaires", "validation": "validation_Systèmes", "xp": "xp_Systèmes"})

validations = [[tab_gen['validation_Maths_Lycée'][i], 
                tab_gen['validation_Fonctions_Réelles'][i], 
                tab_gen['validation_Dérivées'][i], 
                tab_gen['validation_Primitives'][i],
                tab_gen['validation_Systèmes'][i]] for i in range(tab_gen.shape[0])]
val_xp = [0, 8, 8, 8, 5]

nb_xp = []
for liste in validations:
    s = 0
    for i in range(len(liste)):
        if liste[i] == 'validé':
            s = s + val_xp[i]
    nb_xp.append(s)

tab_gen['xp_maths'] = nb_xp

qtd_argent = [[tab_gen['xp_Maths_Lycée'][i],
               tab_gen['xp_Fonctions_Réelles'][i],
               tab_gen['xp_Dérivées'][i],
               tab_gen['xp_Primitives'][i],
               tab_gen['xp_Systèmes'][i]].count('Argent') for i in range(tab_gen.shape[0])]

tab_gen['nb_argent'] = qtd_argent

st.title("Le Top 20 en Maths")
st.write("Dernière mise à jour: 06/01/2025") 

top_20 = tab_gen[['clé', 'xp_maths', 'nb_argent']].sort_values(by=['xp_maths', 'nb_argent'], ascending=False).head(20)
top_20.index = ['top '+str(i) for i in range(1,21)]

st.dataframe(top_20)

st.title("Le top 3")
col1, col2, col3 = st.columns(3)
col1.metric(top_20['clé'][0], 'Xp: '+str(top_20['xp_maths'][0]), 'Argents: '+str(top_20['nb_argent'][0]))
col2.metric(top_20['clé'][1], 'Xp: '+str(top_20['xp_maths'][1]), 'Argents: '+str(top_20['nb_argent'][1]))
col3.metric(top_20['clé'][2], 'Xp: '+str(top_20['xp_maths'][2]), 'Argents: '+str(top_20['nb_argent'][2]))
