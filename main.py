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
            for i in os.listdir():
                print(' '.join(os.listdir()))
                
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
                    
        else:
            print(f"{cmd}: Command not found")

main()
