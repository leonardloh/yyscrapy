from pptx import Presentation
from pptx.util import Inches

from pathlib import Path
import requests
import shutil
import pandas as pd
import math


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
        self.template_path = 'template/template.pptx'
    
    def buildSlides(self):
        prs = Presentation(self.template_path)
        ITEMS_PER_SLIDE = 8

        name = self.df.iloc[0, 1]
        price = self.df.iloc[0, 2]
        img_link = self.df.iloc[0, 3]
        img_path = request_and_save_image(name, img_link)

        for collection_name, data in self.df.groupby('collection'):
            grouped_df = pd.DataFrame(data)
            names = grouped_df['name'].to_list()
            prices = grouped_df['price'].to_list()
            images = grouped_df['img'].to_list()
            total_item_count = len(grouped_df)
            number_collection_slides = math.ceil(total_item_count / ITEMS_PER_SLIDE)

            #add collection slide [section slide]
            collection_layout = prs.slide_layouts[0]
            coll_slide = prs.slides.add_slide(collection_layout)
            for shape in coll_slide.placeholders:
                if shape.is_placeholder:
                    #  print(f'{shape.placeholder_format.idx, shape.name, shape.placeholder_format.type}')
                    shape.text = collection_name

            # individual catalogue layout 
            for slide in range(number_collection_slides):
                # for each slide
                catalogue_layout= prs.slide_layouts[1]
                cat_slide = prs.slides.add_slide(catalogue_layout)
                is_name = True
                for shape in cat_slide.placeholders:
                    if shape.is_placeholder:
                        placeholder_type = shape.placeholder_format.type
                        if placeholder_type == 18:
                            shape.insert_picture(img_path)
                        elif is_name:
                            shape.text = name
                            is_name =  False
                        else:
                            shape.text = price
                            is_name = True


        prs.save('test.pptx')