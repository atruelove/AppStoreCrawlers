import scrapy


class GPReviewsSpider(scrapy.Spider):
    name = "GPReviews"
    start_urls = [
	'https://play.google.com/store/apps/details?id=com.amazon.dee.app',
	'https://play.google.com/store/apps/details?id=com.insteon.insteon3',
	'https://play.google.com/store/apps/details?id=com.nest.android',
	'https://play.google.com/store/apps/details?id=com.philips.lighting.hue2',
	'https://play.google.com/store/apps/details?id=com.belkin.wemoandroid',
	'https://play.google.com/store/apps/details?id=com.unikey.kevo',
    ]

    def parse(self, response):
        for rev in response.css(".single-review"):
            yield {
		'author' : rev.css(".author-name::text").extract_first(),
		'date' : rev.css(".review-date::text").extract_first(),
                'stars' : rev.css(".star-rating-non-editable-container::attr(aria-label)").extract_first(),
                'rtext' : rev.css(".with-review-wrapper").extract_first(),
            }