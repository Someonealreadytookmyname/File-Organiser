import os
import shutil

path = "C:/Users/hello/Downloads/"
all_files = os.listdir(path)


for file in all_files:
    type = file.split(".")[-1]

    #------------------- Document Files ------------------#

    if type == "pdf" or "docx" or type == "xlsx" or type == "csv":
        if os.path.isdir("D:/~ .docs/"):
            shutil.move(path + file,"D:/~ .docs/")
        else:
            os.mkdir("D:/~ .docs/")
            shutil.move(path + file,"D:/~ .docs/")

    elif type == "pptx":
        if os.path.isdir("D:/~ .ppt/"):
            shutil.move(path + file,"D:/~ .ppt/")
        else:  
            os.mkdir("D:/~ .ppt/")
            shutil.move(path + file,"D:/~ .ppt/")

    #------------------- Media Files ------------------#

    elif type == "jpg" or type == "png" or type == "jpeg" or type == "webp" or type == "avif":
        if os.path.isdir("D:/~ .img/"):
            shutil.move(path + file,"D:/~ .img/")
        else:
            os.mkdir("D:/~ .img/")
            shutil.move(path + file,"D:/~ .img/")

    elif type == "mp4" or type == "mkv":
        if os.path.isdir("D:/~ .vid/"):
            shutil.move(path + file,"D:/~ .vid/")
        else:
            os.mkdir("D:/~ .vid/")
            shutil.move(path + file,"D:/~ .vid/")

    elif type == "mp3" or type == "wav" or type == "flac" or type == "aac" or type == "m4a":
        if os.path.isdir("D:/~ .music/"):
            shutil.move(path + file,"D:/~ .music/")
        else:  
            os.mkdir("D:/~ .music/")
            shutil.move(path + file,"D:/~ .music/")
    #------------------- Other Files ------------------#

    elif type == "exe" or type == "msi":
        if os.path.isdir("D:/~ .exe/"):
            shutil.move(path + file,"D:/~ .exe/")
        else:  
            os.mkdir("D:/~ .exe/")
            shutil.move(path + file,"D:/~ .exe/")

    elif type == "zip" or type == "rar":
        if os.path.isdir("D:/~ .zip/"):
            shutil.move(path + file,"D:/~ .zip/")
        else:  
            os.mkdir("D:/~ .zip/")
            shutil.move(path + file,"D:/~ .zip/")

    elif type == "blend1" or type == "blend":
        if os.path.isdir("D:/~ .blender/"):
            shutil.move(path + file,"D:/~ .blender/")
        else:  
            os.mkdir("D:/~ .blender/")
            shutil.move(path + file,"D:/~ .blender/")

print("All Files are Organized Successfully!")


