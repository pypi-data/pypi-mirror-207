import PySimpleGUI as sg

layout = [
    [sg.Multiline(size=(70, 6), expand_x=True, expand_y=True, enable_events=True, right_click_menu=[
        ['&Edit', ['&Copy', '&Paste']],
    ], key='-PROGRESS-LOG-')]
]

window = sg.Window('Right-Click Menu Example', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == '-PROGRESS-LOG-':
        # Get clipboard data
        clipboard_data = sg.tkinter.Tk().clipboard_get()
        
        # Enable or disable menu items based on clipboard data and selection
        menu_state = [('Copy', bool(clipboard_data)), ('Paste', bool(values['-PROGRESS-LOG-'].get_indexes()))]
        
        # Update right-click menu state
        window['-PROGRESS-LOG-'].Widget.tk_popup_menu.postcommand = lambda: window['-PROGRESS-LOG-'].Widget.tk_popup_menu.entryconfigure(0, state=menu_state[0])
        window['-PROGRESS-LOG-'].Widget.tk_popup_menu.postcommand = lambda: window['-PROGRESS-LOG-'].Widget.tk_popup_menu.entryconfigure(1, state=menu_state[1])

window.close()
