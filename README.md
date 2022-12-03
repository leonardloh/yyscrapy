# Yue Yu Scrapper
A mini project that scrap data from an ecommerce projects and store the relevant information
such as prices, images, and product names into a slide.

# What you need
- Python (>3.0)

# Install
`pip install -r requirements.txt`

# Quick Start
`make crawl`: This is crawl the website, gather information and store them into a file call `output.csv`.  
`make build_slide`: Build a ppt slide based on information available from `output.csv`. This step will also download 
images and store them into `images` folder.  
`make all`: Perform all steps above
