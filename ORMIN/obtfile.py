# lectura de los docuentos compatibles .rmin dentro del directorio actual
import subprocess
import os

#posix linux y macos
#nt windows

class InvalidOs(Exception):
    pass

osname = os.name
if osname == 'posix':
    files = str(subprocess.check_output("ls", shell=True)).replace("b\'", "")
    files = files.replace("\\\\n", " ")
    files = files.split()
    files = str(files).replace("\\\\n", " ").split()
    files[0] = files[0].replace("[\"", "")
    files.remove(files[-1])
    print(files)

elif osname == 'nt':
    print("Windows is not suported yet")
else:
    raise InvalidOs("We couldnt recognice your ÓS")
