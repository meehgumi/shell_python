import os

def main():
    
    exit = False
    
    while not exit:
        print(os.getcwd() + " >", end=" ")
        x = input()
        user_input = x.split()
        if len(user_input) == 0:
            continue
        cmd = user_input[0]
        args = user_input[1:]
        
        
        #Commandes du shell
        if cmd.lower() == "exit":
            exit = True
        elif cmd == "echo":
            print(' '.join(args))
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd =="ls":
            liste_ls = os.listdir()
            for i in range(len(liste_ls)):
                print(liste_ls[i])                
                
        elif cmd== "cd":
            if len(args) == 0:
                os.chdir("..")
            else:
                try:
                    os.chdir(path=' '.join(args))
                except FileNotFoundError:
                    print(f"cd: {' '.join(args)}: No such file or directory")
                    
        elif cmd=="mkdir":
            if len(args)==0:
                print("usage: mkdir [directory_name] ...")
            else:
                try:
                    os.mkdir(' '.join(args))
                except FileExistsError:
                    print(f"mkdir: {' '.join(args)} File already exists")
                    
        elif cmd=="cat":
            if len(args) == 0:
                #Manque le nom du fichier
                print("missing file name")
            else:
                try:
                    #Ouvre le fichier en qst
                    fd = os.open(' '.join(args),  os.O_RDWR)
                    #Récupére la taille du fichier
                    f_size = os.path.getsize(' '.join(args))
                    ret = os.read(fd, f_size)
                    #Print l'intérieur du fichier
                    print(ret)
                    #Ferme le fichier
                    os.close(fd)
                except FileNotFoundError:
                        print(f"cd: {' '.join(args)}: No such file or directory")           
                        
        elif cmd =="":
            pass
        else:
            print(f"{cmd}: Command not found")

main()
