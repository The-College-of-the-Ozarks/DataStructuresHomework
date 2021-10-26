import os
def exit(c):
    os.remove("out.py")
    f = open('out.py', "wx")
    for i in c:
        f.write(str(i))
    f.close()
def main():



    exit()

if __name__=='__main__':
    main()
