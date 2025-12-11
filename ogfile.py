import os
import shutil


def of(source, destination):
    
    source = source.replace("\\", "/") + "/"                                               # Well I don't really know How this line worked. :)
    destination = destination.replace("\\", "/") + "/"
    print(destination,"\n", source)

    all_files = os.listdir(source)

    for file in all_files:
        print(file)
        type = file.split(".")[-1]

        #------------------- Document Files ------------------#

        if type == "pdf" or type == "docx" or type == "xlsx" or type == "csv":
            if os.path.isdir(destination + "~ .docs/"):
                shutil.move(source + file, destination + "~ .docs/")
            else:
                os.mkdir(destination + "~ .docs/")
                shutil.move(source + file, destination + "~ .docs/")

        elif type == "pptx":
            if os.path.isdir(destination + "~ .ppt/"):
                shutil.move(source + file, destination + "~ .ppt/")
            else:  
                os.mkdir(destination + "~ .ppt/")
                shutil.move(source + file, destination + "~ .ppt/")

        #------------------- Media Files ------------------#

        elif type == "jpg" or type == "png" or type == "jpeg" or type == "webp" or type == "avif":
            if os.path.isdir(destination + "~ .img/"):
                shutil.move(source + file, destination + "~ .img/")
            else:
                os.mkdir(destination + "~ .img/")
                shutil.move(source + file, destination + "~ .img/")

        elif type == "mp4" or type == "mkv":
            if os.path.isdir(destination + "~ .vid/"):
                shutil.move(source + file, destination + "~ .vid/")
            else:
                os.mkdir(destination + "~ .vid/")
                shutil.move(source + file, destination + "~ .vid/")

        elif type == "mp3" or type == "wav" or type == "flac" or type == "aac" or type == "m4a":
            if os.path.isdir(destination + "~ .music/"):
                shutil.move(source + file, destination + "~ .music/")
            else:  
                os.mkdir(destination + "~ .music/")
                shutil.move(source + file, destination + "~ .music/")
        #------------------- Other Files ------------------#

        elif type == "exe" or type == "msi":
            if os.path.isdir(destination + "~ .exe/"):
                shutil.move(source + file, destination + "~ .exe/")
            else:  
                os.mkdir(destination + "~ .exe/")
                shutil.move(source + file, destination + "~ .exe/")

        elif type == "zip" or type == "rar":
            if os.path.isdir(destination + "~ .zip/"):
                shutil.move(source + file, destination + "~ .zip/")
            else:  
                os.mkdir(destination + "~ .zip/")
                shutil.move(source + file, destination + "~ .zip/")

        elif type == "blend1" or type == "blend":
            if os.path.isdir(destination + "~ .blender/"):
                shutil.move(source + file, destination + "~ .blender/")
            else:  
                os.mkdir(destination + "~ .blender/")
                shutil.move(source + file, destination + "~ .blender/")
