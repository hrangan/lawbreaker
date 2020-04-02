![Lawbreaker](https://raw.githubusercontent.com/hrangan/lawbreaker/master/screenshot.png)

##### Setting up a development environment,
(Warning: Not for production use)
``` bash
$ docker-compose up
```
##### Optional command line usage,
```bash
$ knave -h
usage: knave [-h] [--level {1 - 10}] [name]

Create a random character for the Knave roleplaying game

positional arguments:
  name              name your character (optional)

optional arguments:
  -h, --help        show this help message and exit
  --level {1 - 10}  select a character level (optional)
```
```
$ knave
Name:   Natjanus Harper    XP:      0   Level: 1


Hit Points: 6 / 6

    Defense          Ability            Bonus
--------------------------------------------------
      12             Strength             2
      12            Dexterity             2
      12           Constitution           2
      11           Intelligence           1
      11              Wisdom              1
      11             Charisma             1

      12              Armor               2


Item                     Type        Slots 8/12
--------------------------------------------------
* Cudgel                 Weapon           1
* Gambeson               Armor            1
Grap. hook               Gear             1
Tent                     Gear             1
Fish. rod                Gear             1
Bellows                  Gear             1
Travel rations (1 day)   Food             1
Travel rations (1 day)   Food             1


Traits
--------------------------------------------------
Pickpocket.  Wears foreign clothes, and has booming speech.
Has a gaunt physique, a broken face, war paint skin and oily hair.
Is serene, but gluttonous. Has been abandoned in the past.
Favours neutrality.
```

##### Deploying to Heroku,
Only requires an app dyno and a postgres database node. The included `Procfile`, `runtime.txt` and `requirements.txt` take care of deployments.

###### Environment variables used on Heroku
- `DATABASE_URL` - DSN for the postgresql server. (`docker-compose up` configures this for local environments)
- `APP_LOCATION` - Does the following if set to `heroku`
  - Redirects incoming HTTP requests to HTTPS
  - Periodically removes expired permalinks
  - If set along with `KEEP_AWAKE = true|false`, will poll itself every 25 minutes to bypass Heroku's free dyno sleeping
