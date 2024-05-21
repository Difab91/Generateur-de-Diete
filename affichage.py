import streamlit as st
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
    st.write(" ")
    st.markdown(
        f'''
        <p style="font-size: 19px; font-weight: bold;">
            Soit un total sur la journée de {protdiet}g de protéines, {gludiet}g de glucides, {lipdiet}g de lipides ce qui fait {cal2} calories.
        </p>
        ''',
        unsafe_allow_html=True
    )
def affichage(protpt, glupt, lippt, pt, protdej, gludej, lipdej, dej, protcol1, glucol1, lipcol1, col1, protdin, gludin, lipdin, din, protdiet, gludiet, lipdiet, cal2):
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
                       ({protcol1}g de protéines, {glucol1}g de glucides, {lipcol1}g de lipides) :
                   </span>
               </p>
               ''',
        unsafe_allow_html=True
    )
    st.write(f"{col1} ")
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
    st.write(" ")
    st.markdown(
        f'''
           <p style="font-size: 19px; font-weight: bold;">
               Soit un total sur la journée de {protdiet}g de protéines, {gludiet}g de glucides, {lipdiet}g de lipides ce qui fait {cal2} calories.
           </p>
           ''',
        unsafe_allow_html=True
    )

def reset_inputs():
    st.session_state.prot = ""
    st.session_state.glu = ""
    st.session_state.lip = ""

def side(prot,glu,lip,obj):
    st.markdown("<p style='font-size: 20px; font-weight: bold; text-decoration: underline;'>Objectif visé</p>",
                unsafe_allow_html=True)
    st.write(" ")
    st.markdown(
        f'''
                        <p style="font-size: 16px; font-weight: bold;">
                            Protéines:  
                            <span style="font-size: 16px; font-weight: normal;">
                                  {prot} grammes 
                            </span>
                        </p>
                        ''',
        unsafe_allow_html=True
    )
    st.markdown(
        f'''
                                <p style="font-size: 16px; font-weight: bold;">
                                    Glucides:  
                                    <span style="font-size: 16px; font-weight: normal;">
                                          {glu} grammes 
                                    </span>
                                </p>
                                ''',
        unsafe_allow_html=True
    )
    st.markdown(
        f'''
                                <p style="font-size: 16px; font-weight: bold;">
                                    Lipides:  
                                    <span style="font-size: 16px; font-weight: normal;">
                                          {lip} grammes 
                                    </span>
                                </p>
                                ''',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
                                    <p style="font-size: 16px; font-weight: bold;">
                                        Calories:  
                                        <span style="font-size: 16px; font-weight: normal;">
                                              {obj}
                                        </span>
                                    </p>
                                    ''',
        unsafe_allow_html=True
    )

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button(":blue[Cette génération ne me convient pas]"):
        st.experimental_rerun()

    if st.button(":green[je modifie mes apports]"):
        reset_inputs()
        st.experimental_rerun()
