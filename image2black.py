import math
import os 
from PIL import Image
from cofig import *
import numpy as np
import shutil
from tqdm import trange,tqdm

class BlackChange:
    def __init__(self,dir_forder: str,sort_output: str,output: str, pdf_name: str = PDFNAME):
        '''
        记录dir_forder
        用来处理文件夹图片文件
        '''
        self.dir_forder = dir_forder
        self.sort_output = sort_output
        self.output = output
        self.images=[]
        self.value = VALUE
        self.value_black_downline = VALUEBLACKDOWN
        self.value_black_upline = VALUEBLACKUP
        self.sigma = TIME_PASSING
        self.pdf_name = pdf_name+'.pdf'
        
    def number_sort(self):
        '''
        打开self.dir_forder
        并给放入列表和排序
        重命名为s{i}
        '''
        list = os.listdir(self.dir_forder)
        
        length = len(list)
        layer = int( math.log(length,10) )+1
        def num2name(num):
            '将数字根据文件数量转成相应文件名'
            string = ''
            for k in range(layer):
                string = str(num%10) + string
                num //= 10
            string = 's' + string + '.jpg'
            
            return string
        
        j=0
        for i in list:
            j+=1
            image_path = os.path.join(self.dir_forder,i)
            image = Image.open(image_path)
            
            output_name = num2name(j)
            output_path = os.path.join(self.sort_output,output_name)
            image.save(output_path)
            
        return self
    
    def manner1_image2value(self,image,m,n)-> bool:
        '''
        判别image[m,n]为黑或白
        '''

        self.value = np.mean(image[m-DIMETION if m>DIMETION else m:m+DIMETION if m>DIMETION else m+DIMETION,
                                       n-DIMETION if n>DIMETION else n:n+DIMETION if n>DIMETION else n+DIMETION])*VALUE/256
        if image[m,n]>self.value:
            return 2
        else:
            return 0
        
    def manner2_image2value(self,image,m,n)-> bool:
        '''
        判别image[m,n]为黑或白
        '''

        self.value = np.mean(image[m-DIMETION if m>DIMETION else m:m+DIMETION if m>DIMETION else m+DIMETION,
                                       n-DIMETION if n>DIMETION else n:n+DIMETION if n>DIMETION else n+DIMETION]).mean()
        if self.value > self.value_black_upline:
            return 2
        elif self.value> self.value_black_downline:
            return 1
        else:
            return 0
    
    def transform_single_block(self,i,image,rows,cols,function):
        image_path = os.path.join(self.sort_output,i)
        new_file = np.array(Image.open(image_path).convert('L'))
        for m in trange(rows, leave=False):
                for n in range(cols):
                    num = function(image,m,n)
                    if num == 2:
                        new_file[m,n]=OUT_VALUE
                    elif num ==0 :
                        new_file[m,n]=IN_VALUE
                    else :
                        new_file[m,n]=image[m,n]
        return new_file
    
    def black_change(self):
        '''
        处理为黑白图像
        '''
        list = os.listdir(self.sort_output)
        list.sort()
        
        for i in tqdm(list):
            image_path = os.path.join(self.sort_output,i)
            image = np.array(Image.open(image_path).convert('L'))
            
            rows,cols = image.shape
            
            
            image = self.transform_single_block(i,image,rows,cols,self.manner1_image2value)
            image = self.transform_single_block(i,image,rows,cols,self.manner2_image2value)
            
            output_name = 'p' + i
            output_path = os.path.join(self.output,output_name)
            img = Image.fromarray(image,mode='L')
            img.save(output_path)
            self.images.append(img)
            
        return self
    
    def save2pdf(self):
        '''
        储存为pdf
        '''
        list = os.listdir(self.output)
        self.images = [Image.open(os.path.join(self.output,i)) for i in list]
        
        im1 = Image.open(os.path.join(self.output, list[0]))
        self.images.pop(0)
    
        im1.save(self.pdf_name, "PDF", resolution=100.0, save_all=True, append_images=self.images)
        
        return self
    
    def clear_file(self):
        '''
        清空文件夹文件
        '''
        if not os.path.exists(self.sort_output):
            os.mkdir(self.sort_output)
        else:
            shutil.rmtree(self.sort_output)
            os.mkdir(self.sort_output)
        
        if not os.path.exists(self.output):
            os.mkdir(self.output)
        else:
            shutil.rmtree(self.output)
            os.mkdir(self.output)
        
        return self
        
if __name__ == '__main__':
    
    list = os.listdir('./image')
    
    x = {}
    
    for i in list:
        x[i] = BlackChange('image/'+i+'/image', 'image/'+i+'/sort', 'image/'+i+'/black', i)
        
    for i in tqdm(list):
        x[i].clear_file()
        x[i].number_sort()
        #input('请确定排序顺序')
        x[i].black_change()
    
    input('请确定保存顺序')
    for i in list:
        print('开始保存',end='')
        x[i].save2pdf()
        print('\r',f'已保存到{i}.pdf')
        
    input('已完成，按回车键关闭')

