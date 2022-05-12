import PySimpleGUI as sg

sg.theme('Topanga')

layout = [
    [sg.Text('Anmeldung am Dietrich-Bonhoeffer-Gymnasium Eppelheim:')],
    [sg.Text('Name', size=(30, 1)), sg.InputText()],
    [sg.Text('Vorname', size=(30, 1)), sg.InputText()],
    [sg.Text('Geschlecht', size=(30, 1)), sg.InputText()],
    [sg.Text('Geburtsdatum', size=(30, 1)), sg.InputText()],
    [sg.Text('Geburtsort', size=(30, 1)), sg.InputText()],
    [sg.Text('Straße und Hausnummer', size=(30, 1)), sg.InputText()],
    [sg.Text('Postleitzahl', size=(30, 1)), sg.InputText()],
    [sg.Text('Wohnort', size=(30, 1)), sg.InputText()],
    [sg.Text('Land / Bundesland', size=(30, 1)), sg.InputText()],
    [sg.Text('Antragsdatum', size=(30, 1)), sg.InputText()],
    [sg.Text('Telefonnummern (Festnetz, Mobiltelefon)', size=(30, 1)), sg.InputText()],
    [sg.Text('E-Mail', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Gesetzliche Vertreterin / Gesetzlicher Vertreter:')],
    [sg.Text('Name', size=(30, 1)), sg.InputText()],
    [sg.Text('Vorname', size=(30, 1)), sg.InputText()],
    [sg.Text('Straße und Hausnummer', size=(30, 1)), sg.InputText()],
    [sg.Text('Postleitzahl', size=(30, 1)), sg.InputText()],
    [sg.Text('Wohnort', size=(30, 1)), sg.InputText()],
    [sg.Text('Land', size=(30, 1)), sg.InputText()],
    [sg.Text('Telefonnummern (Festnetz, Mobiltelefon)', size=(30, 1)), sg.InputText()],#
    [sg.Text('E-Mail', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Angaben zur zuletzt besuchten Schule:')],
    [sg.Text('Schulart', size=(30, 1)), sg.InputText()],
    [sg.Text('Schulname', size=(30, 1)), sg.InputText()],
    [sg.Text('Ort', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Fächer und Noten:')],
    [sg.Text('Deutsch', size=(30, 1)), sg.InputText()],
    [sg.Text('Englisch', size=(30, 1)), sg.InputText()],
    [sg.Text('Mathematik', size=(30, 1)), sg.InputText()],
    [sg.Text('Maßgebliches Fach', size=(30, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
print(event, values)
