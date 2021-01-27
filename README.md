# Scraping
## Install python stuff

create a virtualenv
linux 
```bash

python -m venv venv
source venv/bin/activate

```

windows

```
python -m venv venv
venv\Scripts\activate.bat
```

After that
```bash
pip install -r requirements.txt
```
## Run

```bash
# Run basic spider
scrapy runspider lib/ofra_spider.py
```

```bash
# Create a project
scrapy startproject ofra
# Create a spider in a project
scrapy genspider songs https://shironet.mako.co.il/artist\?render\=true\&type\=works\&lang\=1\&prfid\=820\&class\=4\&sort\=popular\&page\=1

```
## Learn more

* [scrapy into tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)


## Tags

```bash
git checkout v1  #v1 -> v3

```

## Work in small groups:

* Use the song list the yield the title, music writer and song text for all popular songs
* Process the results and create a top words by songs, top music writer statistics
* Use `Counter` in python for easier wordcount
* Extra credit: persist the results to a db with sqlalchemy (Create a db class)

## Docs for Counter
[Counter docs](https://docs.python.org/3/library/collections.html#collections.Counter)
[Counter module blog post](https://pymotw.com/3/collections/counter.html)
## Docs for sqlalchemy

[the ORM tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[the full ORM docs](https://docs.sqlalchemy.org/en/13/orm/)
