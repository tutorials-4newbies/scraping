import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class SongsSpider(scrapy.spiders.CrawlSpider):
    name = 'songs'
    allowed_domains = ['shironet.mako.co.il']
    start_urls = ['https://shironet.mako.co.il/artist?type=works&lang=1&prfid=820&class=4&sort=popular']
    rules = [
        Rule(LinkExtractor(restrict_xpaths=("//a[contains(text(), 'הבא') ]"))),
        Rule(LinkExtractor(allow=("type=lyrics")), callback='parse_song'),

    ]

    def parse_song(self, response):
        song_title = response.css('h1.artist_song_name_txt::text').get()
        song_lyrics_list = response.css('.artist_lyrics_text::text').getall()
        song_lyrics = ' '.join(song_lyrics_list).replace('\r\n', '')

        yield {'title': song_title, 'lyrics': song_lyrics}
