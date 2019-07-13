import webbrowser
import easygui

location = easygui.enterbox('File location?')

try:
    file = open(location, 'r')
except FileNotFoundError:
    print("File not found")
else:
    if file.mode == 'r':
        contents = file.read()

    file.close()

    links = contents.split()

    for link in links:
        webbrowser.open_new_tab(link)
