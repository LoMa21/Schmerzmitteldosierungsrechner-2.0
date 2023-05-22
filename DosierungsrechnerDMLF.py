# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:54:50 2023

@author: LoReF
"""
import streamlit as st

single_dose = st.number_input

#Algifor für Fachpersonen

# Berechnung der maximalen Dosierung pro 24 Stunden für Algifor Sirup
def calculate_max_dosage_algifor(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Algifor Sirup
def calculate_single_dose_algifor(age, weight):
            if age >= 12 and weight >= 40:
                st.write('Das Kind ist alt genug, um auf **Ibuprofen-Tabletten** umzusteigen.')
                st.write('Die Einzeldosis beträgt **200 mg** Ibuprofen.')
                st.write('Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.')
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **800 mg** Ibuprofen.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 2.5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 7 and age <= 9 and weight <=25:
                single_dose = 10
            elif age >= 7 and age <= 9 and weight <=35:
                single_dose = 12.5 
            elif age >= 10 and age <= 12 and weight <=35:
                single_dose =15
            elif age >= 10 and age <= 12 and weight <=45:
                single_dose =17.5
            else:
                single_dose = calculate_single_dose_algifor(age, weight)

            return single_dose

# Streamlit App
def main_algifor(age, weight):
            st.title("Algifor Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
                  
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key675"  # unique key value für Alter
            weight_key = "weight_key675"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)
              
           # Berechnung der Einzeldosis und maximalen Dosierung pro 24 Stunden
            if st.button("Berechnen", key="calculate_button"):
                single_dose = calculate_single_dose_algifor(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_algifor(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")

if __name__ == '__main__':
    pass
            # main(age, weight)
            
        
            
            

#Algifor für Eltern

# Berechnung der maximalen Dosierung pro 24 Stunden für Algifor Sirup
def calculate_max_dosage_algifor1(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Algifor Sirup
def calculate_single_dose_algifor1(age, weight):
            if age >= 12 and weight >= 40:
                st.write('Das Kind ist alt genug, um auf **Ibuprofen-Tabletten** umzusteigen.')
                st.write('Die Einzeldosis beträgt **200 mg** Ibuprofen.')
                st.write('Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.')
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **800 mg** Ibuprofen.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 2.5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 7 and age <= 9 and weight <=25:
                single_dose = 10
            elif age >= 7 and age <= 9 and weight <=35:
                single_dose = 12.5 
            elif age >= 10 and age <= 12 and weight <=35:
                single_dose =15
            elif age >= 10 and age <= 12 and weight <=45:
                single_dose =17.5
            else:
                single_dose = calculate_single_dose_algifor1(age, weight)

            return single_dose

# Streamlit App
def main_algifor1(age, weight):
            st.title("Algifor Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
            
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key65"  # unique key value für Alter
            weight_key = "weight_key65"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)

            # Berechnung der Einzeldosis und maximalen Dosierung pro 24 Stunden
            if st.button("Berechnen", key="calculate_button65"):
                single_dose = calculate_single_dose_algifor1(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_algifor1(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")

if __name__ == '__main__':
    pass
            # main(age, weight)
            
            
            
            
            
            
#Benuron Fachpersonen

# Berechnung der maximalen Dosierung pro 24 Stunden für Ben U Ron Sirup
def calculate_max_dosage_benuron(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Algifor Sirup
def calculate_single_dose_benuron(age, weight):
            if age >= 12 and weight >= 40:
                st.write('Das Kind ist alt genug, um auf **Dafalgan Tabletten** umzusteigen.') 
                st.write('Die Einzeldosis beträgt **500 mg**.') 
                st.write('Der Zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.') 
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **2 g**.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 5
            elif age >= 3 and age <= 6 and weight <=18:
                single_dose = 5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 6 and age <= 9 and weight <=25:
                single_dose = 7.5
            elif age >= 9 and age <= 12 and weight <=35:
                single_dose = 10 
            elif age >= 9 and age <= 12 and weight <=45:
                single_dose =15
            else:
                single_dose = calculate_single_dose_benuron(age, weight)
        
            return single_dose

# Streamlit App
def main_benuron(age, weight):
            st.title("Ben U Ron Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
        
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key2" # unique key value für Alter
            weight_key = "weight_key2" # unique key value für Gewicht
            age_input = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight_input = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)
        
            # Button-Handler mit eindeutigem Schlüssel
            calculate_button_key = "calculate_button_key2" + age_key + "_" + weight_key
            if st.button("Berechnen", key=calculate_button_key):
                single_dose = calculate_single_dose_benuron(age_input, weight_input)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_benuron(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")
                    
if __name__ == '__main__':
    pass
            # main(age, weight) main()
    
    
    
    
    
    

#Benuron Eltern

# Berechnung der maximalen Dosierung pro 24 Stunden für Ben U Ron Sirup
def calculate_max_dosage_benuron1(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Algifor Sirup
def calculate_single_dose_benuron1(age, weight):
            if age >= 12 and weight >= 40:
                st.write('Das Kind ist alt genug, um auf **Dafalgan Tabletten** umzusteigen.') 
                st.write('Die Einzeldosis beträgt **500 mg**.') 
                st.write('Der Zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.') 
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **2 g**.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 5
            elif age >= 3 and age <= 6 and weight <=18:
                single_dose = 5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 6 and age <= 9 and weight <=25:
                single_dose = 7.5
            elif age >= 9 and age <= 12 and weight <=35:
                single_dose = 10 
            elif age >= 9 and age <= 12 and weight <=45:
                single_dose =15
            else:
                single_dose = calculate_single_dose_benuron1(age, weight)
        
            return single_dose

# Streamlit App
def main_benuron1(age, weight):
            st.title("Ben U Ron Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
        
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key345" # unique key value für Alter
            weight_key = "weight_key345" # unique key value für Gewicht
            age_input = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight_input = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)
        
            # Button-Handler mit eindeutigem Schlüssel
            calculate_button_key = "calculate_button_key2" + age_key + "_" + weight_key
            if st.button("Berechnen", key=calculate_button_key):
                single_dose = calculate_single_dose_benuron1(age_input, weight_input)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_benuron1(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")
                    
if __name__ == '__main__':
    pass
            # main(age, weight)
    
    
    
    
    
#Dafalgan Fachperson

# Berechnung der maximalen Dosierung pro 24 Stunden für Dafalgan Sirup
def calculate_max_dosage_dafalgan(single_dose):
            max_dosage = single_dose * 4
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Dafalgan Sirup
def calculate_single_dose_dafalgan(age, weight):
            if age >= 12 and weight >= 41:
                st.write('Das Kind ist alt genug, um auf **Dafalgan Tabletten** umzusteigen.') 
                st.write('Die Einzeldosis beträgt **500 mg**.') 
                st.write('Der Zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.') 
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **2 g**.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 4
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 6
            elif age >= 6 and age <= 9 and weight <=31:
                single_dose = 8
            elif age >= 9 and age <= 12 and weight <=40:
                single_dose = 10 
            else:
                single_dose = calculate_single_dose_dafalgan(age, weight)
        
            return single_dose

# Streamlit App
def main_dafalgan(age, weight):
            st.title("Dafalgan Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
        
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key3"  # unique key value für Alter
            weight_key = "weight_key3"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)
        
            # Button-Handler mit eindeutigem Schlüssel
            if st.button("Berechnen", key="calculate_button3"):
                single_dose = calculate_single_dose_dafalgan(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_dafalgan(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")
                    

if __name__ == '__main__':
    pass
            # main(age, weight)
    
    
    
    


#Dafalgan Eltern

# Berechnung der maximalen Dosierung pro 24 Stunden für Dafalgan Sirup
def calculate_max_dosage_dafalgan1(single_dose):
            max_dosage = single_dose * 4
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Dafalgan Sirup
def calculate_single_dose_dafalgan1(age, weight):
            if age >= 12 and weight >= 41:
                st.write('Das Kind ist alt genug, um auf **Dafalgan Tabletten** umzusteigen.') 
                st.write('Die Einzeldosis beträgt **500 mg**.') 
                st.write('Der Zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.') 
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **2 g**.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 4
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 6
            elif age >= 6 and age <= 9 and weight <=31:
                single_dose = 8
            elif age >= 9 and age <= 12 and weight <=40:
                single_dose = 10 
            else:
                single_dose = calculate_single_dose_dafalgan1(age, weight)
        
            return single_dose

# Streamlit App
def main_dafalgan1(age, weight):
            st.title("Dafalgan Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")
        
            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key553"  # unique key value für Alter
            weight_key = "weight_key553"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)
        
            # Button-Handler mit eindeutigem Schlüssel
            if st.button("Berechnen", key="calculate_button553"):
                single_dose = calculate_single_dose_dafalgan1(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_dafalgan1(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")
                    

if __name__ == '__main__':
    pass
            # main(age, weight)
    
    
  
    
#Irfen Fachpersonen

# Berechnung der maximalen Dosierung pro 24 Stunden für Irfen Sirup
def calculate_max_dosage_irfen(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Irfen Sirup
def calculate_single_dose_irfen(age, weight):
            if age >= 12 and weight >= 41:
                st.write('Das Kind ist alt genug, um auf **Ibuprofen-Tabletten** umzusteigen.')
                st.write('Die Einzeldosis beträgt **200 mg** Ibuprofen.')
                st.write('Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.')
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **800 mg** Ibuprofen.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 2.5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 7 and age <= 9 and weight <=25:
                single_dose = 10
            elif age >= 7 and age <= 9 and weight <=35:
                single_dose = 12.5 
            elif age >= 10 and age <= 12 and weight <=35:
                single_dose =15
            elif age >= 10 and age <= 12 and weight <=45:
                single_dose =17.5
            else:
                single_dose = calculate_single_dose_irfen(age, weight)

            return single_dose

# Streamlit App
def main_irfen(age, weight):
            st.title("Irfen Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")

            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key4"  # unique key value für Alter
            weight_key = "weight_key4"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)

            # Berechnung der Einzeldosis und maximalen Dosierung pro 24 Stunden
            if st.button("Berechnen", key="calculate_button4"):
                single_dose = calculate_single_dose_irfen(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_irfen(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")

if __name__ == '__main__':
    pass
            # main(age, weight)
    
    
    
    
    
    
#Irfen Eltern

# Berechnung der maximalen Dosierung pro 24 Stunden für Irfen Sirup
def calculate_max_dosage_irfen1(single_dose):
            max_dosage = single_dose * 3
            return max_dosage

# Berechnung der Einzeldosis basierend auf dem Alter und Gewicht des Kindes für Irfen Sirup
def calculate_single_dose_irfen1(age, weight):
            if age >= 12 and weight >= 41:
                st.write('Das Kind ist alt genug, um auf **Ibuprofen-Tabletten** umzusteigen.')
                st.write('Die Einzeldosis beträgt **200 mg** Ibuprofen.')
                st.write('Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.')
                st.write('Die maximale Dosierung pro **24 Stunden** beträgt **800 mg** Ibuprofen.')
                return 0
            elif age <= 3 and weight <=15:
                single_dose = 2.5
            elif age >= 3 and age <= 6 and weight <=25:
                single_dose = 7.5
            elif age >= 7 and age <= 9 and weight <=25:
                single_dose = 10
            elif age >= 7 and age <= 9 and weight <=35:
                single_dose = 12.5 
            elif age >= 10 and age <= 12 and weight <=35:
                single_dose =15
            elif age >= 10 and age <= 12 and weight <=45:
                single_dose =17.5
            else:
                single_dose = calculate_single_dose_irfen1(age, weight)

            return single_dose

# Streamlit App
def main_irfen1(age, weight):
            st.title("Irfen Sirup Dosierungsrechner")
            st.subheader("Vor Gebrauch schütteln!")

            # Eingabe von Alter und Gewicht des Kindes
            age_key = "age_key904"  # unique key value für Alter
            weight_key = "weight_key904"  # unique key value für Gewicht
            age = st.number_input("Alter des Kindes in Jahren", min_value=0, max_value=16, step=1, key=age_key)
            weight = st.number_input("Gewicht des Kindes in kg", min_value=0.0, max_value=60.0, step=0.1, key=weight_key)

            # Berechnung der Einzeldosis und maximalen Dosierung pro 24 Stunden
            if st.button("Berechnen", key="calculate_button884"):
                single_dose = calculate_single_dose_irfen1(age, weight)
                if single_dose > 0:
                    max_dosage = calculate_max_dosage_irfen1(single_dose)
                    st.write(f"Die Einzeldosis beträgt **{single_dose} ml**. Der zeitliche Abstand zur nächsten Dosis beträgt mindestens **6 Stunden**.")
                    st.write(f"Die maximale Dosierung pro **24 Stunden** beträgt **{max_dosage} ml**.")

if __name__ == '__main__':
    pass
            # main(age, weight)