# $$\   $$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\
# $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ $$  __$$\
# $$ |  $$ |$$ |      $$ /  \__|$$ /  \__|$$ /  \__|
# $$ |  $$ |$$$$$\    \$$$$$$\  \$$$$$$\  $$ |
# $$ |  $$ |$$  __|    \____$$\  \____$$\ $$ |
# $$ |  $$ |$$ |      $$\   $$ |$$\   $$ |$$ |  $$\
# \$$$$$$  |$$$$$$$$\ \$$$$$$  |\$$$$$$  |\$$$$$$  |
# \______/ \________| \______/  \______/  \______/
#     All rights reserved. Refer to LICENSE.md.
# --------------------------------------------------
#   Author: Lucas Alvarenga (lb.am.alvarenga@uel.br)
#   Name: src/main.py
#   Date: 2023-08-08
#   Desc: Entrypoint for the scraper.

from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from spiders.angeloni import AngeloniSpider
from spiders.muffato import MuffatoSpider


def main():
    settings = Settings()
    settings.set("SPLASH_URL", "http://localhost:8050")
    settings.set(
        "DOWNLOADER_MIDDLEWARES",
        {
            "scrapy_splash.SplashCookiesMiddleware": 723,
            "scrapy_splash.SplashMiddleware": 725,
            "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
        },
    )
    settings.set(
        "SPIDER_MIDDLEWARES",
        {
            "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
        },
    )
    settings.set("DUPEFILTER_CLASS", "scrapy_splash.SplashAwareDupeFilter")
    settings.set("HTTPCACHE_STORAGE", "scrapy_splash.SplashAwareFSCacheStorage")

    process = CrawlerProcess(settings=settings)
    process.crawl(MuffatoSpider)
    process.start()


if __name__ == "__main__":
    main()
