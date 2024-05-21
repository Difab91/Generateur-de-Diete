import streamlit as st
from gen import algo
from affichage import affichage
from affichage import affichage2600
from affichage import side



st.header("veuillez rentrer les détail des macronutriments souhaitez :",divider='rainbow')

if 'prot' not in st.session_state:
    st.session_state.prot = ""
if 'glu' not in st.session_state:
    st.session_state.glu = ""
if 'lip' not in st.session_state:
    st.session_state.lip = ""




# Demande de saisie des protéines
prot_placeholder = st.empty()
prot = prot_placeholder.text_input(label="Insérer le nombre de protéines", key="user_input1",
                                   value=st.session_state.prot)

if prot:
    st.session_state.prot = prot
    prot_placeholder.empty()
    glu_placeholder = st.empty()
    glu = glu_placeholder.text_input(label="Insérer le nombre de glucides", key="user_input2",
                                     value=st.session_state.glu)

    if glu:
        st.session_state.glu = glu
        glu_placeholder.empty()
        lip_placeholder = st.empty()
        lip = lip_placeholder.text_input(label="Insérer le nombre de lipides", key="user_input3",
                                         value=st.session_state.lip)

        if lip:
            st.session_state.lip = lip
            lip_placeholder.empty()


if prot and glu and lip :
    proti = int(prot)
    glui = int(glu)
    lipi = int(lip)
    obj = 9 * lipi + 4 * (proti + glui)
    with st.sidebar:
        side(prot,glu,lip,obj)





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







