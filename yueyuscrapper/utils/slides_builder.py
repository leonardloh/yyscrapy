from pptx import Presentation
from pptx.util import Inches

from pathlib import Path
import requests
import shutil


# image_folder_path = Path('images')
# url = df.iloc[0, 3]
# res = requests.get(url, stream = True)
# if res.status_code == 200:
#     with open(f'{image_folder_path}/{df.iloc[0, 1]}.jpg', 'wb') as f:
#         shutil.copyfileobj(res.raw, f)

def request_and_save_image(img_name, url, img_folder='images'):
    res = requests.get(url, stream = True)
    file_path_name = f'{img_folder}/{img_name}.jpg'
    if res.status_code == 200:
        with open(file_path_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        return file_path_name


class SlidesBuilder:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def buildSlides(self):
        prs = Presentation('template.pptx')

        collection = self.df.iloc[0, 0]
        name = self.df.iloc[0, 1]
        price = self.df.iloc[0, 2]
        img_link = self.df.iloc[0, 3]
        img_path = request_and_save_image(name, img_link)
        slide1 = prs.slides.add_slide(prs.slide_layouts[0])

        for shape in slide1.placeholders:
            print('%d %s' % (shape.placeholder_format.idx, shape.name))


        slide1.placeholders[10].insert_picture(img_path)
        slide1.placeholders[11].text = name
        slide1.placeholders[12].text = price



        prs.save('test.pptx')