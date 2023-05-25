# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:46:31 2023

@author: LoReF
"""

#Quellen: Streamlit.io, ChatGPT und Google
#Wir haben zum Teil bei Fehlermeldungen Chatgpt gefragt oder gegoogelt. 
#Von Streamlit.io haben wir teils auch gewisse Befehle nachgeschaut.


import streamlit as st
import pandas as pd
import os
import DosierungsrechnerDMLF as dosre
import json
from datetime import date
import altair as alt

from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


st.title('Schmerzmitteldosierungstabelle für Kinder')

    
tab1, tab2 = st.tabs(["Fachperson", "Elternteil"])

with tab1:
    
    st.write("Unten finden Sie 4 verschiedene Schmerzmittelsirupe für Kinder im Alter von 0 bis 16 Jahren und einem Gewicht von 3 bis 60 kg, welche die Dosierung für das kranke Kind berechnet. Ist das Kind unter 1 Jahr alt, geben Sie 0 Jahre ein.")
    st.write("**Hinweis:** Diese Dosierungen werden für den OTC-Verkauft, gemäss Compendium.ch, berechnet.")
    
    # Definierung einer Liste mit verfügbaren Sirup-Optionen
    sirup_options = ["Algifor Sirup 100mg/5ml", "Ben U Ron Sirup", "Dafalgan Sirup", "Irfen Sirup"]
    # Erstellung von Optionenfeld für den Sirup
    selected_sirup = st.selectbox("Wählen Sie ein Schmerzmittelsirup:", sirup_options)
   
    single_dose=()
    age = (0)
    weight = (0)
    
    if selected_sirup == 'Algifor Sirup 100mg/5ml':
        dosre.main_algifor(age, weight)
        dosre.calculate_max_dosage_algifor(single_dose) 
        dosre.calculate_single_dose_algifor(age, weight)
        
    if selected_sirup == 'Ben U Ron Sirup':

        dosre.calculate_max_dosage_benuron(single_dose)
        dosre.calculate_single_dose_benuron(age, weight)
        dosre.main_benuron(age, weight)
        
    if selected_sirup == 'Dafalgan Sirup':

        dosre.calculate_max_dosage_dafalgan(single_dose)
        dosre.calculate_single_dose_dafalgan(age, weight)
        dosre.main_dafalgan(age, weight)
        
    if selected_sirup == 'Irfen Sirup':

        dosre.calculate_max_dosage_irfen(single_dose)
        dosre.calculate_single_dose_irfen(age, weight)
        dosre.main_irfen(age, weight)


with tab2:
    st.write('Liebe Eltern, mit dieser App wird die Dosierung von Schmerzmittelsirupen für Ihr Kind berechnet.')
    ('Ausserdem gibt es ein Schmerzmitteltagebuch, welches Ihre Daten in einem Diagramm speichern kann. Dadurch können Sie sehen, wie viel Mililiter insgesamt Ihr Kind pro Tag an Schmerzmittelsirup eingenommen hat. Dies kann hilfreich sein, um den Fachleuten bei einem nächsten Arztbesuch oder Apothekenbesuch Informationen mitzuteilen.')

    tab3, tab4= st.tabs(["Schmerzmittelsirupe", "Schmerzmitteltagebuch"])

 
with tab3:
    st.header("Schmerzmittelsirupe")
    st.write("Unten finden Sie 4 verschiedene Schmerzmittelsirupe für Kinder im Alter von 0 bis 16 Jahren und einem Gewicht von 3 bis 60 kg, welche die Einnahmedosierung für das kranke Kind berechnet. Ist Ihr Kind unter 1 Jahr alt, geben Sie 0 Jahre ein.")
    st.write("**Einnahmehinweis:** **Dafalgan** und **Ben U Ron** sind beides Paracetamol-Sirupe. **Algifor** und **Irfen** sind beides Ibuprofen-Sirupe. Sirupe welche den **gleichen Wirkstoff** haben, dürfen **nicht** zusammen eingenommen werden.")
    st.write("Sie dürfen aber, wenn die Schmerzen zu stark sind, abwechslungsweise **Paracetamol** und **Ibuprofen** im **Abstand** von **3 Stunden** Ihrem Kind verabreichen.")
    st.write("Es kann sein, dass Ihr Kinderarzt eine höhere Dosierung verschrieben hat. Dieses App berechnet die Dosierung welche im Verkauf gemäss Comendium.ch zugelassen sind.")
    
    # Definierung einer Liste mit verfügbaren Sirup-Optionen
    sirup_options = ["Algifor Sirup 100mg/5ml", "Ben U Ron Sirup ", "Dafalgan Sirup ", "Irfen Sirup "]
    # Erstellung von Optionenfeld für den Sirup
    selected_sirup = st.selectbox("Wählen Sie ein Schmerzmittelsirup:", sirup_options)
    
   
    if selected_sirup == 'Algifor Sirup 100mg/5ml':

        dosre.calculate_max_dosage_algifor1(single_dose) 
        dosre.calculate_single_dose_algifor1(age, weight)
        dosre.main_algifor1(age, weight)


    if selected_sirup == 'Ben U Ron Sirup ':

        dosre.calculate_max_dosage_benuron1(single_dose)
        dosre.calculate_single_dose_benuron1(age, weight)
        dosre.main_benuron1(age, weight)
        

    if selected_sirup == 'Dafalgan Sirup ':

        dosre.calculate_max_dosage_dafalgan1(single_dose)
        dosre.calculate_single_dose_dafalgan1(age, weight)
        dosre.main_dafalgan1(age, weight)

   
    if selected_sirup == 'Irfen Sirup ':

        dosre.calculate_max_dosage_irfen1(single_dose)
        dosre.calculate_single_dose_irfen1(age, weight)
        dosre.main_irfen1(age, weight)
#--------------------------------------------------------------- 
with tab4:
    st.header("Schmerzmitteltagebuch")
    st.write("Für einen neuen Tagebucheintrag notieren Sie den Namen des Kindes, wählen Sie das Einnahmedatum aus, bestimmen Sie den verwendeten Schmerzmittelsirup und tragen Sie die berechnete Schmerzmitteldosierung ein. Um den Tagebucheintrag zu überprüfen, wählen Sie den Namen des Kindes aus.")


    # -------- load secrets for jsonbin.io --------
    jsonbin_secrets = st.secrets["jsonbin"]
    api_key = jsonbin_secrets["api_key"]
    bin_id = jsonbin_secrets["bin_id"]
    
    # -------- user login --------
    
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )
    
    fullname, authentication_status, username = authenticator.login('Login', 'main')
    
    if authentication_status == True:   # login successful
        authenticator.logout('Logout', 'main')   # show logout button
    elif authentication_status == False:
        st.error('Username/password is incorrect')
        st.stop()
    elif authentication_status == None:
        st.warning('Please enter your username and password')
        st.stop()
        
    data = load_key(api_key, bin_id, username)

#------------------------------------------------------------

    # Tabebucheingaben
    # Eingabefelder für den Namen der Person, den Tag, den Sirup und die Dosierung
    name_tagb = st.text_input('Name')
    datum_tagb = st.date_input('Datum', value=date.today())
    sirup_tagb = st.selectbox('Sirup', ('Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen'))
    dosierung_tagb = st.number_input('Dosierung in ml')
    
    # Button zum Abspeichern des JSONbin-Objekts hinzufügen
    if st.button('Speichern'):   
        # Prüfen, ob die Datei bereits vorhanden ist
        try:
            daten = load_key(api_key, bin_id, username)
        except FileNotFoundError:
            daten = {}
    
        # Aktuallisierung oder neuen Eintrag im JSON-Objekt hinzufügen
        if name_tagb in daten and sirup_tagb in daten and datum_tagb.strftime("%d.%m.%Y") in daten[sirup_tagb]:
            # Wenn der Eintrag bereits vorhanden ist, Dosierung aktuallisieren
            daten[name_tagb][sirup_tagb][datum_tagb.strftime("%d.%m.%Y")].append(dosierung_tagb)
        elif name_tagb in daten and sirup_tagb in daten[name_tagb]:
            # Wenn der Sirup-Eintrag bereits vorhanden ist, aber das Datum nicht übereinstimmt neur Datumseintrag hinzufügen
            daten[name_tagb][sirup_tagb][datum_tagb.strftime("%d.%m.%Y")] = [dosierung_tagb]
        elif name_tagb in daten:
            # Wenn der Name bereits vorhanden ist, aber der Sirup-Eintrag nicht, neuen Sirup-Eintrag erstellen
            daten[name_tagb][sirup_tagb] = {datum_tagb.strftime("%d.%m.%Y"): [dosierung_tagb]}
        else:
            # Wenn der Name noch nicht vorhanden ist, neuen Namen mit Sirup-Eintrag erstellen
            daten[name_tagb] = {sirup_tagb: {datum_tagb.strftime("%d.%m.%Y"): [dosierung_tagb]}}
    
        # JSON-Datei speichern
        save_key(api_key, bin_id, username, daten)
    
        st.success('Informationen erfolgreich gespeichert!')
#-------------------------------------------------------------------------------------------- 
    # Tagebuchübersicht               
    st.subheader("Tagebuch Übersicht")
    
    # Liste der Namen aus der JSON-Datei erstellen
    daten = load_key(api_key, bin_id, username)
    
    options = daten.keys()
    
    if options:
        selected_name = st.selectbox('Name auswählen', options)
        daten = load_key(api_key, bin_id, username)

        # DataFrame erstellen
        
        data = []
        for sirup_tagb in ['Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen']:
            if sirup_tagb in daten.get(selected_name, {}):
                for datum_tagb in daten[selected_name][sirup_tagb].keys():
                    dosierung_tagb = sum(daten[selected_name][sirup_tagb][datum_tagb])
                    data.append([pd.to_datetime(datum_tagb, format='%d.%m.%Y'), sirup_tagb, dosierung_tagb])
        df = pd.DataFrame(data, columns=['Datum', 'Sirup', 'Dosierung'])
                
        # Bar-Chart anzeigen
        bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('Datum:T', axis=alt.Axis(title='Datum')),
            y=alt.Y('Dosierung:Q', axis=alt.Axis(title='Dosierung in ml')),
            color=alt.Color('Sirup:N', scale=alt.Scale(domain=['Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen'], 
                                                      range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']))
        )
        
        st.altair_chart(bars, use_container_width=True)

 


         
   
        