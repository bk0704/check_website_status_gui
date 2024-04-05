import PySimpleGUI as sg

#Design GUI with a text, input field and a button
layout = [
    [sg.Text("Please enter in a valid URL")],
    [sg.Input(key="-I-")],
    [sg.Ok(bind_return_key=True)]
]
#Create Window and name it is "Is It Up"
window = sg.Window("Is It Up", layout)

#Start the Event Loop when the program starts
while True:
    event, values = window.read()
    print(event, values)
    if event =="Ok":
        #If the button "Ok" is pressed then check if the URL is up
        import httpx
        try:
            site = f"{values['-I-']}"
            if site.startswith != "https://www." or "http://www.":
                #check if the URL starts with "https://www." and it not then add it
                if site.startswith("www."):
                    site = f"https://{site}"
                else:
                    site = f"https://www.{site}"
            #try to get the site
            r = httpx.get(site, timeout=5)
            #if the status code is 200 then the URL is up
            if r.status_code == 200:
                sg.Popup("The URL you entered is up", title="Valid")
            #if the status code is not 200 then the URL is not up
            else:
                sg.Popup("The URL you entered is not up", title="Error")
        except Exception as e:
            #if the URL is not valid then show the error
            sg.popup_error_with_traceback('Error in the event loop', e, emoji=sg.EMOJI_BASE64_SCREAM)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
