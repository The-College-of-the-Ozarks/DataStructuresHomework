import os
def exit(c):
    os.remove("out.txt")
    f = open('out.txt', "wx")
    for i in c:
        f.write(str(i))
    f.close()
def main():



    exit()

if __name__=='__main__':
    main()
