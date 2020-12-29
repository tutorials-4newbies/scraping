import scrapy


class BlogSpider(scrapy.Spider):
    name = 'ofrapider'
    start_urls = ['https://shironet.mako.co.il/artist?type=works&lang=1&prfid=820&class=4&sort=popular']

    def parse(self, response):
        for song in response.css('.artist_player_songlist'):
            song_title = song.css('::text').get()
            yield {'title': song_title.replace('\t','')}

        
