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
#   Name: src/spiders/muffato.py
#   Date: 2023-08-09
#   Desc: Scraper for supermuffato.com.br

import scrapy

from scrapy import shell
from scrapy_splash.request import SplashRequest

from os import path

import base64, sys


class MuffatoSpider(scrapy.Spider):
    name = "muffato"
    srcpath = path.dirname(sys.argv[0])
    urls = ["https://www.supermuffato.com.br/"]
    lua_source = open(path.join(srcpath, "splash", f"{name}.lua")).read()

    def start_requests(self):
        for url in self.urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint="execute",
                args={"lua_source": self.lua_source},
            )

    def parse(self, response, **kwargs):
        with open(path.join(self.srcpath, "..", "doc", "example.png"), "wb") as e:
            e.write(base64.b64decode(response.data["png"]))
        print("Done!")
        shell.inspect_response(response=response, spider=self)
