import os
def exit(c):
    os.remove("out.txt")
    f = open('out.txt', "wx")
    for i in c:
        f.write(str(i))
    f.close()
def main():
'''
Only edit code below this comment or your assignment may be invalidated
'''

    #Avoid modifying the return as well.
    return

if __name__=='__main__':
    main()
