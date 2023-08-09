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
--   Name: src/splash/muffato.py
--   Date: 2023-08-09
--   Desc: Scraper for supermuffato.com.br

function main(splash)
  assert(splash:go(splash.args.url))

  assert(splash:runjs("document.querySelector('#s-ch-select-city').value = 15")) -- Londrina - Madre
  local location_btn = splash:select("#s-ch-change-channel")
  assert(location_btn:mouse_click())

  -- TODO: use dynamic waiting
  splash:wait(0.5)

  -- TODO: this is not working...
  assert(splash:runjs("document.querySelector('#header-md-nav-toggle').click()"))

  return {
    html = splash:html(),
    png  = splash:png(),
    har  = splash:har()
  }
end
