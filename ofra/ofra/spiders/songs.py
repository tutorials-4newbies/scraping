import scrapy


class SongsSpider(scrapy.Spider):
    name = 'songs'
    allowed_domains = ['shironet.mako.co.il']
    start_urls = ['https://shironet.mako.co.il/artist?type=works&lang=1&prfid=820&class=4&sort=popular']

    def parse(self, response):
        for song in response.css('.artist_player_songlist'):
            song_title = song.css('::text').get()
            song_link = song.xpath(f"//a[contains(text(), '{song_title}' )]")[0]

            yield response.follow(song_link, self.parse_song)

        for next_page in response.xpath("//a[contains(text(), 'הבא') ]"):
            # print(next_page)
            yield response.follow(next_page, self.parse)

    def parse_song(self, response):

        song_title = response.css('.artist_song_name_txt::text').get()
        song_lyrics = response.css('.artist_lyrics_text::text').get()
        
        yield {'title': song_title, 'lyrics': song_lyrics}
