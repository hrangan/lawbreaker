![Lawbreaker](https://raw.githubusercontent.com/hrangan/lawbreaker/master/screenshot.png)

# Lawbreaker


Install Steps:
===

### Python dependencies
1. For the web server (along with the command-line tool). This has a dependency on libpq-dev (on Ubuntu 14.04)

`$ pip install .[web]`

2. For only the command line tool.

`$ pip install .`

3. For a development environment where changes are immediately reflected, pass the `-e` flag to `pip install`, or `dev_requirements.txt`

### Database dependencies (if installing the web server)
1. Install postgres and create a database for lawbreaker
```
            [user] $ sudo apt-get install postgresql
            [user] $ sudo -u postgres -i
            [postgres] $ createuser --interactive
            [user] $ createdb lawbreaker
```

2. `$ export DATABASE_URL=postgres:///lawbreaker`
3. Heroku sets this automatically once a Postgres DB is provisioned


Usage:
===

Web
---
`$ knave.web`

Command line
---
```bash
usage: knave [-h] [--level {1,2,3,4,5,6,7,8,9,10}] [--random-name]
             [name [name ...]]

Process some integers.

positional arguments:
  name

optional arguments:
  -h, --help            show this help message and exit
  --level {1,2,3,4,5,6,7,8,9,10}
  --random-name
```
```
$ knave --random-name
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

Heroku
---
Only requires an app dyno and a postgres database node. `Procfile`, `runtime.txt` and `requirements.txt` take care of deployments.

#### Environment Variables
- `DATABASE_URL` - The postgresql DSN. Set automatically by heroku. Needs to be set manually for local development
- `APP_LOCATION` - Set to `heroku` on heroku. Add extra behaviour when running on heroku or any other hosting service
- `KEEP_AWAKE` - Set to `true` on production dyno's. Polls https://lawbreaker.herokuapp.com/keep_awake every 25 minutes. This is to prevent the free dyno from sleeping
