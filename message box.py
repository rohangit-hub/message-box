import pyautogui

#for alert box
pyautogui.alert('This is an alert box.')

#for confirmation box
pyautogui.confirm('Shall I proceed?')

#for confirmation but with options.
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])

#for input from user
pyautogui.prompt('What is your name?')

#for password input from user
pyautogui.password('Enter password (text will be hidden)')
