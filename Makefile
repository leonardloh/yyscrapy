install:
	pip install -r requirements.txt

crawl:
	rm output.csv && scrapy crawl yueyu -O output.csv -t csv

build_slide:
	rm products.pptx && python main.py

all:
	make crawl && make build_slide