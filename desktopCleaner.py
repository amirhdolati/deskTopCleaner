import os
import shutil
import re
import datetime
import random
import stat


desktop_paths = [os.path.join(os.environ['USERPROFILE'], 'Desktop'),
                os.path.join(os.environ['PUBLIC'], 'Desktop')] 

dist_path = input("Give a path for backup:( for example : C:\\desktopBackup ) ")


ignore_list = ['desktopCleaner.py']
with open('desktopCleaner.py','r') as f:
    my_code = f.read()
while(True):
    ans = input('Do you have ignore file?[Y/n]: ')
    if ans.lower() != 'y':
        break
    else:
        data = input('Give me your file name: ')
        p = my_code.find('ignore_list = [')
        p += len('ignore_list = [')
        my_code = my_code[:p] + "'{}', ".format(data) + my_code[p:]
        ignore_list.append(data)
        if ignore_list.__len__() % 4 == 0:
            my_code = my_code[:p] + "\n" + my_code[p:]    
        with open('desktopCleaner.py','w') as f:
            f.write(my_code)

               
print("Your ignore list is :\n{}".format(ignore_list))


category = ['music', 'video', 'docoument', 'shortcut',
            'folder', 'picture', 'executable', 'code',
            'compressed', 'other']

for folder in category:
    new_path = os.path.join(dist_path,folder)
    if not os.path.exists(path= new_path):
        os.mkdir(path= new_path)   


time = datetime.date.today()

changed = 0
moved_list = []


for desktop_path in desktop_paths:
    files = os.listdir(path = desktop_path)
    for File in files:
        source_path = os.path.join(desktop_path,File)
        if File not in ignore_list:
            try:
                os.chmod(source_path, stat.S_IWRITE)
                if os.path.isdir(source_path):
                    for root, dirs, _files in os.walk(source_path, topdown=False):
                        for fname in _files:
                            full_path = os.path.join(root, fname)
                            os.chmod(full_path ,stat.S_IWRITE)
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'folder'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'folder'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path ,os.path.join(dist_path,'folder'))
                elif re.search('^.*\.(txt|docx|doc|odm|dot|dotx|wri|pdf)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'docoument'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'docoument'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path,os.path.join(dist_path,'docoument'))
                elif re.search('^.*\.(3gp|avi|mpeg|mpg|mpe|mp4|mkv|srt)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'video'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'video'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path,os.path.join(dist_path,'video'))
                elif re.search('^.*\.(mp3|ogg|wma|wav)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'music'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'music'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path,os.path.join(dist_path,'music'))
                elif re.search('^.*\.(url|lnk|sym)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'shortcut'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'shortcut'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:    
                        shutil.move(source_path ,os.path.join(dist_path,'shortcut'))
                elif re.search('^.*\.(7z|apk|appx|bin|apk|appx|iso|rar|zip|xap|jar|lzip)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'compressed'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'compressed'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:    
                        shutil.move(source_path ,os.path.join(dist_path,'compressed'))        
                elif re.search('^.*\.(bmp|gif|ico|icon|png|jgp|psd|pdd|tiff|jpg|svg)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'picture'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'picture'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path ,os.path.join(dist_path,'picture'))
                elif re.search('^.*\.(exe)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'executable'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'executable'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))   
                    else: 
                        shutil.move(source_path,os.path.join(dist_path,'executable'))
                elif re.search('^.*\.(py|c|h|cpp|htm|html|css|js|php|java|vb|css)$',File):
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'code'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'code'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))        
                    else:      
                        shutil.move(source_path ,os.path.join(dist_path,'code'))
                else:
                    changed+=1
                    if os.path.exists(os.path.join(os.path.join(dist_path,'other'),File)):
                        shutil.move(source_path,os.path.join(os.path.join(dist_path,'other'),'{}-{}-{}_{}{}_'.format(time.year,time.month,time.day,chr(random.randint(97,122)),random.randint(1,100)) + File))
                    else:
                        shutil.move(source_path ,os.path.join(dist_path,'other'))
                moved_list.append(File)
            except PermissionError:
                print("Access Denied ! give me Access to move this {} !".format(File))    
            except:
                print("Something wrong!")      
                      

print("Done! {} file moved to desktopBackup folder!".format(changed))
print("Moved file :\n{} ".format(moved_list))
input("(Enter/return to exit)")