import os
from PIL import Image
from tqdm import tqdm

path = './input'
path_output = './output'
path_rename = './convert'
files = os.listdir(path)


def rename_file(file_ext:str):
    start_with = int(input('input start name:\n'))
    
    for file in tqdm(files):
        file_name = os.path.join(path_output,f'photo_{start_with}.{file_ext}')
        os.rename(os.path.join(path,file),file_name)
        start_with+=1
    


def convert(file_ext:str):          
        for file in tqdm(files) :
            file_name = file.split('.')[0]
            im = Image.open(os.path.join(path_output,file))
            im.save(os.path.join(path_rename,f'{file_name}.{file_ext}'))
        



def main():
    method = input('you want rename? y/n : \n')
    if method == 'y':
        format = input('input format photo \n')
        rename_file(format)
        print('you fail rename and save in output folder')
    is_convert = input('you want to conver in another format? y/n\n')
    if is_convert == 'y':
        format = input('input convert format \n')
        try:
            convert(format)
        except:
            print("Format not suport to convert, last file saved on output dir")
        print('you fai saved on convert folder')
    print('finish')

if __name__ == '__main__':
    main()
