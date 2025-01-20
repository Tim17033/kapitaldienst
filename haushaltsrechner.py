import streamlit as st
import pandas as pd

# Titel der App
st.title("Haushaltsrechner")

# Eingabefelder
einkommen = st.number_input("Geben Sie Ihr monatliches Einkommen ein:", min_value=0, step=100)
miete = st.number_input("Geben Sie Ihre monatliche Miete ein:", min_value=0, step=50)
lebensmittel = st.number_input("Geben Sie Ihre Ausgaben für Lebensmittel ein:", min_value=0, step=50)
sonstiges = st.number_input("Geben Sie Ihre sonstigen monatlichen Ausgaben ein:", min_value=0, step=50)

# Berechnungen
gesamtausgaben = miete + lebensmittel + sonstiges
ersparnisse = einkommen - gesamtausgaben

# Ergebnisse anzeigen
st.write("### Ergebnisse")
st.write(f"Gesamtausgaben: {gesamtausgaben} €")
if ersparnisse >= 0:
    st.write(f"Monatliche Ersparnisse: {ersparnisse} €")
else:
    st.write(f"Defizit: {abs(ersparnisse)} €")

# Tabelle für Übersicht
daten = {
    "Kategorie": ["Einkommen", "Miete", "Lebensmittel", "Sonstiges", "Ersparnisse"],
    "Betrag (€)": [einkommen, miete, lebensmittel, sonstiges, ersparnisse],
}
df = pd.DataFrame(daten)

st.write("### Übersicht")
st.dataframe(df)

