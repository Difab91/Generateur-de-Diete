import streamlit as st
from gen import algo

st.header("veuillez rentrer les détail des macronutriments souhaitez :")
prot = st.text_input(label="inserer le nombre de protéines",max_chars=3 , key="user_input1")
glu = st.text_area(label="inserer le nombre de glucide", key="user_input2")
lip = st.text_area(label="inserer le nombre de lipide", key="user_input3")


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
    resultat_repas = algo(bp, hp, hl, bl, hg, bg, cal)
    st.write({resultat_repas})







