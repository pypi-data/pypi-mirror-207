SubsScraper
---------

Run command for generate urls
```commandline
search
search search.cnt=2 # for 2 urls
search 'search.query="лекции таймкоды"' search.cnt=2 # override cyrillic (more quotes)
```

Run command for subscrape urls
```commandline
subscrape
search scraper.audio_format=mp3 # convert to audio format
search scraper.lvl=text # download only text
```

Default configs
```commandline
search:
  output_folder: data
  result_file: urls.txt
  cnt: 10
  query: машинное обучение лекции таймкоды

scraper:
  output_folder: ${search.output_folder}/dataset
  audio_format: m4a
  lvl: audio # text, audio, video
```

