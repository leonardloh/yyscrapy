import os
from utils.csv_handler import CSVDataHandler
from utils.slides_builder import SlidesBuilder



def main():
    #run scrapy
    # os.system("scrapy crawl yueyu -O output.csv -t csv")
    
    csvDataHander = CSVDataHandler()
    df = csvDataHander.get_preprocessed_data()
    sb = SlidesBuilder(df)
    sb.buildSlides()


if __name__ == "__main__":
    main()