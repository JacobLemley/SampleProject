# A module is another python file that can be imported into another python files
# https://docs.python.org/3/py-modindex.html (these are stored in lib folder inside python folder)
#lots of 3rd party modules exist as well
#pip can be used to install python modules. It is a package manager.
    #modules installed using pip are stored in site-packages folder
    #they are still imported using the name of the module
import useful_tools #file made by us and stored in same folder as this program


print(useful_tools.roll_dice(6))
