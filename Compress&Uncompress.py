import shutil
import os
import sys

def com():
    print ("The available compression formats are \n" + "######  tar(1), bztar(2), zip(3), gztar(4), xztar(5)  #######\n**** high is best ****")
    print("Make your files in a folder")
    folderzip=input("Enter the name of the folder to compress\n")
    cotype=input("Enter the compression type\n")
    print("Compressing file...")
    print("File path " + str(shutil.make_archive(folderzip, cotype, root_dir=folderzip)))
    print("Compresstion done\n" + "Made by Faroni\n")
    main()
    
def decom():
    print("Supported file formats\n#######  tar(tar), bztar(tar.bz2), zip(zip), gztar(tar.gz), xztar(tar.xz)  #######")
    folderdzip=input("Enter the name of the folder to decompress include format\n")
    dfor=input("Enter compresstion type\n")
    ddir=input("Enter folder name to extract to\n")
    os.mkdir(ddir)
    print("Decompressing file...")
    #print("file path " + str(shutil.unpack_archive(folderdzip, extract_dir='./folderdzip', format=dfor)))
    shutil.unpack_archive(folderdzip, extract_dir=ddir, format=dfor)
    print("Decompresstion done\n" + "Made by Faroni\n")
    main()
    
def main():
    print("######################## Welcome to faroni compression and decompression ########################\n######################## Made by luel-4013 aka Faroni ########################\n")
	#print('######################## Made by luel-4013 aka Faroni ########################')
	
    choose=input("1.Compress\n2.Decompress\n")
    if choose == '1':
        com()
    elif choose == '2':
        decom()
    else:
        print("Invalid input you MORON!")
        main()
        #sys.exit()
main()