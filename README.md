# Vulgaire Dev

This repo holds the code for http://vulgairedev.fr

It uses **Django** with **mysql** and **nginx** as webserver.
All the project is orchestrated by **docker-compose**, and each of the previous components run inside a docker image.

## Blog posts

Blog posts are on github [here](https://github.com/Romathonat/vulgaireDevEntries), so I can edit them easily, other people can create/update article via pull request.

## Deploy

Thanks to docker, the deploy is simple.

You just need to provide env vars presents in docker-compose.yml in a ~/.profile, like this:

Blog posts are on github [here](https://github.com/Romathonat/vulgaireDevEntries), so I can edit them easily, and other people can create/update article via pull request. All markdown files are pulled from github (sync). 

## Deploy

You need to provide env vars presents in docker-compose.yml in a ~/.profile, like this:

``` bash
export VULGAIREDEV_DB_PASSWORD=''
export VULGAIREDEV_GMAIL_PASSWORD=''

# the secret key of the django app
export VULGAIREDEV_SECRET_KEY=''

export DISQUS_key=''
```
Then 
```bash
git clone --recurse-submodules https://github.com/Romathonat/VulgaireDev.git
```


You also need to add the a line to the crontab (crontab -e) in order to sync data each minute:

``` bash
*/1 * * * * cd /webApps/VulgaireDev/src/static/vulgaireDevEntries && git fetch && git merge origin/master
```


Then, you just need to have docker-compose and docker installed, then launch:
``` bash
./launch.sh
``` 

## Dev
The simplest way is to launch it like in production, just changing in settings debug to True.
It is probably not the best way to do it (do not have enough time to do better right now).
