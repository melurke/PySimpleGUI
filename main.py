import PySimpleGUIWeb as sg
import pyautogui

input_file = open('input.txt','w')
input = ""

sg.theme('Material1')

gender_choices = ('männlich', 'weiblich', 'divers')
day_choices = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
month_choices = ('Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember')
year_choices = (2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004)

layout = [
    [sg.Text('Anmeldung am Dietrich-Bonhoeffer-Gymnasium Eppelheim:', font='Helvetica 24')],
    [sg.Text('')],
    [sg.Text('Schüler/in:', font='Helvetica 18')],
    [sg.Text('Name', size=(30, 1)), sg.InputText()],
    [sg.Text('Vorname', size=(30, 1)), sg.InputText()],
    [sg.Text('Geschlecht', size=(30, 1)), sg.Combo(gender_choices, default_value='')],
    [sg.Text('Geburtsdatum', size=(30, 1)), sg.Combo(day_choices, default_value='', size=(5, 1)), sg.Combo(month_choices, default_value='', size=(11, 1)), sg.Combo(year_choices, default_value='', size=(7, 1))],
    [sg.Text('Geburtsort', size=(30, 1)), sg.InputText()],
    [sg.Text('Straße und Hausnummer', size=(30, 1)), sg.InputText()],
    [sg.Text('Postleitzahl', size=(30, 1)), sg.InputText()],
    [sg.Text('Wohnort', size=(30, 1)), sg.InputText()],
    [sg.Text('Land / Bundesland', size=(30, 1)), sg.InputText()],
    [sg.Text('Antragsdatum', size=(30, 1)), sg.InputText()],
    [sg.Text('Telefonnummern (Festnetz, Mobiltelefon)', size=(30, 1)), sg.InputText()],
    [sg.Text('E-Mail', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Erziehungsberechtigte/r:', font='Helvetica 18')],
    [sg.Text('Name', size=(30, 1)), sg.InputText()],
    [sg.Text('Vorname', size=(30, 1)), sg.InputText()],
    [sg.Text('Straße und Hausnummer', size=(30, 1)), sg.InputText()],
    [sg.Text('Postleitzahl', size=(30, 1)), sg.InputText()],
    [sg.Text('Wohnort', size=(30, 1)), sg.InputText()],
    [sg.Text('Land', size=(30, 1)), sg.InputText()],
    [sg.Text('Telefonnummern (Festnetz, Mobiltelefon)', size=(30, 1)), sg.InputText()],
    [sg.Text('E-Mail', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Angaben zur zuletzt besuchten Schule:', font='Helvetica 18')],
    [sg.Text('Schulart', size=(30, 1)), sg.InputText()],
    [sg.Text('Schulname', size=(30, 1)), sg.InputText()],
    [sg.Text('Ort', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Text('Fächer und Noten:', font='Helvetica 18')],
    [sg.Text('Deutsch', size=(30, 1)), sg.InputText()],
    [sg.Text('Englisch', size=(30, 1)), sg.InputText()],
    [sg.Text('Mathematik', size=(30, 1)), sg.InputText()],
    [sg.Text('')],
    [sg.Submit('Einreichen'), sg.Cancel('Abbrechen')],
    [sg.Text('')],
]

window = sg.Window('Anmeldung am Dietrich-Bonhoeffer-Gymnasium Eppelheim', layout, web_port=3141, web_start_browser=True)
event, values = window.read()
window.close()
pyautogui.keyDown('ctrl')
pyautogui.press('w')
pyautogui.keyUp('ctrl')
print(event, values)
for value in range(0, len(values)):
    input += str(values.get(value))+"\n"
input_file.writelines(input)
input_file.close()
