# scraping_project_soliman4data
Web scarping for 'soliman4data portfolio's page' by using scrapy
to get each project and its following link.

* Target webpage that used in this project:
https://soliman4data.wordpress.com/portfolio/

### Prerequirments:

### Used softwares:
1. Anaconda Navigator (anaconda3)
2. VSCode

### libraries:
* scrapy

### Usage:
1. Create a virtual environment via Anaconda Navigator, name it, open it, and write down the following commands in it:
2. Install scrapy:
> conda install -c conda-forge scrapy
3. Start a project:
> scrapy startproject test_project
4. Select the project directory:
> cd test_project
5. Generate 1st spider:
> scrapy genspider zspider soliman4data.wordpress.com/portfolio/
6. Open the code on vscode:
> code .
7. Copy ALL Python code exists in zspider.py and paste it in your zspider file
8. Run the following code to run the the first spider on the opened virtual environment:
> scrapy crawl zspider -o zspider_output.csv
9. New CSV file had created and it has first scraped data (project_names and corresponding URLs)
10. Copy ALL Python code exists in zspider2.py and paste it in your zspiders file
11. Run the following code to run the the second spider on the opened virtual environment:
> scrapy crawl zspider2 -o zspider2_output.csv
12. New CSV file had created and it has second scraped data (projects github URLs and page titles)

i.e. zspider_output.csv & zspider2_output.csv are attached here as references.

