#choosing file script
def choosef(files):
    global choice
    n = 1
    for file in files:
        print("%i. %s" % (n, file))
        n += 1

    while True:
        choice = input("Choose the file\n")
        try:
            int(choice)
            if int(choice) <= len(files):
                print(files[int(choice)-1])
                break
        except:
            if file == choice:
                break
            else:
                print("no se ha encontrado el archivo")
