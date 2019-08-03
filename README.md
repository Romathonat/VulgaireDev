# Vulgaire Dev

This repo holds the code for http://vulgairedev.fr

It uses **Django** with **mysql** and **nginx** as webserver.
All the project is orchestrated by **docker-compose**, and each of the previous components run inside a docker image.

## Blog posts

<<<<<<< HEAD
Blog posts are on github [here](https://github.com/Romathonat/vulgaireDevEntries), so I can edit them easily, other people can create/update article via pull request. The django app uses the github api to retrieve posts from github. The number of calls is limited, so there is a cache system (3 minutes of cache).

## Deploy

Thanks to docker, de deploy is simple.

You just need to provide env vars presents in docker-compose.yml in a ~/.profile, like this:
=======
Blog posts are on github [here](https://github.com/Romathonat/vulgaireDevEntries), so I can edit them easily, and other people can create/update article via pull request. The django app uses the github api to retrieve posts from github. The number of calls is limited, so there is a cache system (3 minutes of cache).

## Deploy

You need to provide env vars presents in docker-compose.yml in a ~/.profile, like this:
>>>>>>> 00871286b9a689729e3ab7d973c4388e718f4c2e

``` bash
export VULGAIREDEV_DB_PASSWORD=''
export VULGAIREDEV_GMAIL_PASSWORD=''


# the secret key of the django app
export VULGAIREDEV_SECRET_KEY=''

export GITHUB_PASSWORD=''
export DISQUS_key=''
```

<<<<<<< HEAD
Then, you just need to have docker-compose and docker installed, then launch:
=======
You need to have docker-compose and docker installed, then launch:
>>>>>>> 00871286b9a689729e3ab7d973c4388e718f4c2e

``` bash
./launch.sh
``` 
