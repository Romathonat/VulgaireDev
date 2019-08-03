# Vulgaire Dev

This repo holds the code for http://vulgairedev.fr

It uses **Django** with **mysql** and **nginx** as webserver.
All the project is orchestrated by **docker-compose**, and each of the previous components run inside a docker image.

## Blog posts

Blog posts are on github [here](https://github.com/Romathonat/vulgaireDevEntries), so I can edit them easily, and other people can create/update article via pull request. The django app uses the github api to retrieve posts from github. The number of calls is limited, so there is a cache system (3 minutes of cache).

## Deploy

You need to provide env vars presents in docker-compose.yml in a ~/.profile, like this:

``` bash
export VULGAIREDEV_DB_PASSWORD=''
export VULGAIREDEV_GMAIL_PASSWORD=''


# the secret key of the django app
export VULGAIREDEV_SECRET_KEY=''

export GITHUB_PASSWORD=''
export DISQUS_key=''
```

You need to have docker-compose and docker installed, then launch:

``` bash
./launch.sh
``` 
