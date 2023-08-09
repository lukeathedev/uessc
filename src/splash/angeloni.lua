-- $$\   $$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\
-- $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ $$  __$$\
-- $$ |  $$ |$$ |      $$ /  \__|$$ /  \__|$$ /  \__|
-- $$ |  $$ |$$$$$\    \$$$$$$\  \$$$$$$\  $$ |
-- $$ |  $$ |$$  __|    \____$$\  \____$$\ $$ |
-- $$ |  $$ |$$ |      $$\   $$ |$$\   $$ |$$ |  $$\
-- \$$$$$$  |$$$$$$$$\ \$$$$$$  |\$$$$$$  |\$$$$$$  |
-- \______/ \________| \______/  \______/  \______/
--     All rights reserved. Refer to LICENSE.md.
-- --------------------------------------------------
--   Author: Lucas Alvarenga (lb.am.alvarenga@uel.br)
--   Name: src/splash/angeloni.py
--   Date: 2023-08-09
--   Desc: Scraper for angeloni.com.br

function main(splash)
  assert(splash:go(splash.args.url))
  assert(splash:wait(0.5))

  return {
    html = splash:html(),
    png  = splash:png(),
    har  = splash:har()
  }
end
