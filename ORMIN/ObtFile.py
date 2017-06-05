import subprocess
import os

"""We crate an exception in case os.name returns something that isn't 'nt' or 'posix"""
class InvalidOs(Exception):
    pass

choice = ""
n = 0

"""We use the os module to discover the os of the machine."""
osname = os.name

"""the eliminate list is a list to keep the files that will not be used, as they
haven't got the .rmin extension"""
eliminate = []

"""If it returns 'posix', it means that the sistem is mac or linux, therefore we
use the ls command to get the data."""
if osname == 'posix':
    
    """with the subprocess.check_output("ls", shell=True), we get returned the
    output that a normal console module would return when using the command ls"""
    files = str(subprocess.check_output("ls", shell=True)).replace("b\'", "")
    
    """We remove all unecessary data from the output of the shell to get a
    clean list of the files and their names"""
    files = files.replace("\\\\n", " ")
    files = files.split()
    files = str(files).replace("\\\\n", " ").split()
    files[0] = files[0].replace("[\"", "")
    files.remove(files[-1])

    """with this for loop, we go through every item on the list that contains the
    files. If it is a .rmin file, it pases, if not, it adds it to a list (eliminate) for later deletion."""
    for file in files:
        if '.rmin' in file:
            pass
        else:
            eliminate.append(file)

    """This for loop deletes from the list that contains the files any file that
    isn't a .rmin file"""        
    for eliminable in eliminate:
        files.remove(eliminable)
    print(files)

"""If os.name returns 'nt' it means ite is a windows machine.""" 
elif osname == 'nt':
    print("Windows is not suported yet")

"""If os.osname doesn't return 'nt' or 'posix' we raise an exception explaining that"""    
else:
    raise InvalidOs("We couldnt recognice your ÓS")
