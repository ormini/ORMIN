# lectura de los docuentos compatibles .rmin dentro del directorio actual
import subprocess
import os

#posix linux y macos
#nt windows

class InvalidOs(Exception):
    pass

osname = os.name
if osname == 'posix':
    files = str(subprocess.check_output("dir", shell=True)).replace("b\'", "")
    files = files.replace("\\n'", "").split()
    for file in files:
        if '.rmin' not in file:
            files.remove(file)
        else:
            pass
    print(files)
    
elif osname == 'nt':
    print("Windows is not suported yet")
else:
    raise InvalidOs("We couldnt recognice your ÓS")
