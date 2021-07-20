## Manga RSS Feed Python

This project has been created with the sole purpose to retrieve new manga chapters scrapped from sites that doesn't have any rss feed available to notify users.

The app uses [python-feedgen](https://feedgen.kiesow.be/) library to create a feed for every entry in **data/data.json**.

This data file is formed by an array of the follows properties:

    [{
        "title": "One Piece",
        "image": "https://mangaplus.shueisha.co.jp/drm/title/100020/title_thumbnail_portrait_list/10711.jpg?key=79918099df56270ef2ba0976e43664ac",
        "description": "Manga feed for One Piece",
        "url": "https://mangaplus.shueisha.co.jp/titles/100020",
        "provider": "mangaplus",
        "selector": "ChapterListItem-module_name_3h9dj",
        "selector_img_article": "",
        "currentChapter": "#1017"
    }]

| Property                 | Description                                                                                                                              |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **title**                | title tag for rss                                                                                                                        |
| **image**                | image used to display in rss feeds                                                                                                       |
| **description**          | description tag to display in rss feeds                                                                                                  |
| **url**                  | the url with the chapters to webscrapping at                                                                                             |
| **provider**             | site that host the url, used to load the proper factory class to retrieve the elements when it builds the articles list for the rss feed |
| **selector**             | selector used to scrap all the elements which match with the chapter titles                                                              |
| **selector_img_article** | to be implemented                                                                                                                        |
| **currentChapter**       | latest chapter found from last execution                                                                                                 |

### Requirements

The project runs under **python 3.9** and it can be bundled with a Dockerfile to dockerize the process however you can run it as a single script with anything more but it's necessary to have a **Chrome Browser** and the **chromedriver** matching the same version of the browser. You can learn more [here](https://chromedriver.chromium.org/)

## How to use

Before you running the app, you need to edit **data/data.json** to add the entries mangas you want to look up. By the moment I'm scrapping and managing content only comming from [MangaPlus](https://mangaplus.shueisha.co.jp/) but you can do a similar implementation for another site in case the DOM tree where the chapters are rendered are done in another fashion way instead of looping through a list of elements matching the same css class as MangaPlus does for every chapter title.

Also you need to introduce the name and email in **data/contributor.json** and the host url the rss feed refers to under **data/host.json** and you'll be ready to go.

#### Running locally

Run the **pip** command to install the dependencies:

`pip install --no-cache-dir -r requirements.txt`

After that you only have to execute `python main.py` and once the execution is done you'll see the rss feeds under the **rss** folder, each one per entry in **data.json**. Also the project will create a dump file for every entry in order to so when the script executes again, it'll dump in memory the content of the **obj** file and rebuilds the **FeedGenerator object** with all the data comming from the last time execution it found new chapters. The reason is implemented this way is because **python-feed-gen** doesn't provide any method to build from an existing source in xml by the moment.

#### Running with docker container

You previously need to build the image with this command:

`docker build -t rss-feed-python .`

Once is done run the **docker run** command with the following flags:

`docker run -it --rm --name rss-feed-python -e TZ=Europe/Madrid -v "<path_to_project>:/usr/src/app" -w /usr/src/app rss-feed-python python main.py`

Bear in mind that if you want to automatize the process through **cron jobs** or similar tools you need to remove the **-it** STDIN flags since it's running as a background job. On the other hand the python image is built with another different **TZ** so you need to stablish the TZ matching with your timezone of preference since this setting it'll be the timestamp updated for every article in the RSS feed.
