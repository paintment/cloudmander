# cloudmander // main.py

# packages
import os
import fade

# variables
cloudmander_ascii = """
  ░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░███████╗██████╗░
  ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗
  ██║░░╚═╝██║░░░░░██║░░██║██║░░░██║██║░░██║██╔████╔██║███████║██╔██╗██║██║░░██║█████╗░░██████╔╝
  ██║░░██╗██║░░░░░██║░░██║██║░░░██║██║░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
  ╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝███████╗██║░░██║
  ░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                      d e v e l o p e d  b y  s t a n t r i c  o n  g i t h u b
                                                       ----------------------------------------
"""

command_legend = """
    [gui], [connect -ip -auth], [savelog], [log], [openlog],
    [closegui], [disconnect], [serverinfo], [saveserver], [saved],
    [deletesaves], [saveanddisconnect], [redbutton], [reset]
    ---
    For help on how to use a command, use [help --command {command}]
    Use Ctrl + G to open the GUI faster
    Thanks for using cloudmander!
"""

# intro
os.system("cls")
print(fade.purplepink(cloudmander_ascii))
print(fade.purplepink(command_legend))
