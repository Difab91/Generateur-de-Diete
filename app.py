import streamlit as st
from gen import algo

def affichage2600(protpt, glupt, lippt, pt, protcol2, glucol2, lipcol2, col2, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2):

    st.markdown(
        f'''
        <p style="font-size: 20px; font-weight: bold;">
            Petit déjeuner 
            <span style="font-size: 16px; font-weight: normal;">
                ({protpt}g de protéines, {glupt}g de glucides, {lippt}g de lipides) :
            </span>
        </p>
        ''',
        unsafe_allow_html=True
    )

    st.write(f"{pt} ")
    st.write(" ")
    st.markdown(
        f'''
            <p style="font-size: 20px; font-weight: bold;">
                Collation du matin  
                <span style="font-size: 16px; font-weight: normal;">
                    ({protcol2}g de protéines, {glucol2}g de glucides, {lipcol2}g de lipides) :
                </span>
            </p>
            ''',
        unsafe_allow_html=True
    )
    st.write(f"{col2} ")
    st.write(" ")
    st.markdown(
        f'''
            <p style="font-size: 20px; font-weight: bold;">
                 Dejeuner 
                <span style="font-size: 16px; font-weight: normal;">
                    ({protdej}g de protéines, {gludej}g de glucides, {lipdej}g de lipides) :
                </span>
            </p>
            ''',
        unsafe_allow_html=True
    )
    st.write(f" {dej} ")
    st.write(" ")
    st.markdown(
        f'''
                <p style="font-size: 20px; font-weight: bold;">
                     Collation de l'aprés midi
                    <span style="font-size: 16px; font-weight: normal;">
                        ({protcol1}g de protéines, {glucol1}g de glucides, {lipcol1}g de lipides) :
                    </span>
                </p>
                ''',
        unsafe_allow_html=True
    )
    st.write(f" {col1} ")
    st.write(" ")
    st.markdown(
        f'''
                    <p style="font-size: 20px; font-weight: bold;">
                         Dinner
                        <span style="font-size: 16px; font-weight: normal;">
                            ({protdin}g de protéines, {gludin}g de glucides, {lipdin}g de lipides) :
                        </span>
                    </p>
                    ''',
        unsafe_allow_html=True
    )
    st.write(f" {din} ")
    st.write(" ")
    st.markdown(
        f'''
        <p style="font-size: 19px; color: blue;">
            Soit un total sur la journée de {protdiet}g de protéines, {gludiet}g de glucides, {lipdiet}g de lipides ce qui fait {cal2} calories.
        </p>
        ''',
        unsafe_allow_html=True
    )
def affichage(protpt, glupt, lippt, pt, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2):
    st.write(f" Petit dejeuner: {pt}  ({protpt}g de protéines, {glupt}g de glucides, {lippt}g de lipides)")
    st.write(f" collation: {col1}  ({protcol1}g de protéines, {glucol1}g de glucides, {lipcol1}g de lipides)")
    st.write(f" déjeuner: {dej}  ({protdej}g de protéines, {gludej}g de glucides, {lipdej}g de lipides)")
    st.write(f" Dinner: {din}  ({protdin}g de protéines, {gludin}g de glucides, {lipdin}g de lipides)")
    st.write(f"Soit un total sur la journée de  {protdiet}g de protéines, {gludiet}g de glucides, {lipdiet}g de lipides ce qui fait {cal2} calories")



st.header("veuillez rentrer les détail des macronutriments souhaitez :",divider='rainbow')

prot = st.text_input(label="inserer le nombre de protéines", key="user_input1")
glu = st.text_input(label="inserer le nombre de glucide", key="user_input2")
lip = st.text_input(label="inserer le nombre de lipide", key="user_input3")

if prot and glu and lip :
    protacons=int(prot)
    gluacons=int(glu)
    lipacons=int(lip)
    bp = (98 / 100) * protacons
    hp = (102 / 100) * protacons
    bg = (98 / 100) * gluacons
    hg = (102 / 100) * gluacons
    bl = (98 / 100) * lipacons
    hl = (102 / 100) * lipacons
    cal = 9 * lipacons + 4 * protacons + 4 * gluacons
    if cal>2600:
        protpt, glupt, lippt, pt, protcol2, glucol2, lipcol2, col2, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2 = algo(bp, hp, hl, bl, hg, bg, cal)
        affichage2600(protpt, glupt, lippt, pt, protcol2, glucol2, lipcol2, col2, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2)
    else:
        protpt, glupt, lippt, pt, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2 = algo(bp, hp, hl, bl, hg, bg, cal)
        affichage(protpt, glupt, lippt, pt, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2)









