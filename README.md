![Lawbreaker](https://raw.githubusercontent.com/hrangan/lawbreaker/master/screenshot.png)

# Lawbreaker


Install Steps:
===

### Python dependencies
1. For the web server (along with the command-line tool). This has a dependency on libpq-dev (on Ubuntu 14.04)

`$ pip install -r requirements.py`

2. For only the command line tool.

`$ pip install .`

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
`$ python web/server.py`

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

REST API
---
All lawbreaker URL's serve JSON content if called with `Accept: application/json` in the header.

### Random generation
```sh
$ curl -X GET \
    http://lawbreaker.herokuapp.com \
    -H 'Accept: application/json'
```

### Lookup existing character
```sh
$ curl -X GET \
    http://lawbreaker.herokuapp.com/27a97fadfd0b43bdb0e6bbe1fb3876c2 \
    -H 'Accept: application/json'
```
### Response
```
{
    "id": "27a97fadfd0b43bdb0e6bbe1fb3876c2",
    "name": "Rilia Snow",
    "xp": 0,
    "level": 1,
    "hit_points": 3,
    "attributes": {
        "strength": 11,
        "dexterity": 11,
        "constitution": 11,
        "intelligence": 11,
        "wisdom": 15,
        "charisma": 11
    },
    "armor_defense": 12,
    "inventory": [
        {
            "name": "Halberd",
            "type": "Weapon",
            "slots": 3,
            "equipped": true,
            "hands": 2,
            "quality": 3,
            "damage": "d10"
        },
        {
            "name": "Gambeson",
            "type": "Armor",
            "slots": 1,
            "equipped": true,
            "defense": 1,
            "quality": 3
        },
        {
            "name": "Lantern",
            "type": "Gear",
            "slots": 1,
            "equipped": false
        },
        {
            "name": "Spikes, 5",
            "type": "Gear",
            "slots": 1,
            "equipped": false
        },
        {
            "name": "Tongs",
            "type": "Gear",
            "slots": 1,
            "equipped": false
        },
        {
            "name": "Fish. rod",
            "type": "Gear",
            "slots": 1,
            "equipped": false
        },
        {
            "name": "Travel rations (1 day)",
            "type": "Food",
            "slots": 1,
            "equipped": false
        },
        {
            "name": "Travel rations (1 day)",
            "type": "Food",
            "slots": 1,
            "equipped": false
        }
    ],
    "used_slots": 10,
    "total_slots": 11,
    "traits": {
        "physique": "stout",
        "face": "ratlike",
        "skin": "weathered",
        "hair": "greased",
        "clothing": "livery",
        "virtue": "courageous",
        "vice": "cruel",
        "speech": "cryptic",
        "background": "Cook",
        "misfortune": "blackmailed",
        "alignment": "neutrality"
    }
}
```


Heroku
---
Only requires an app dyno and a postgres database node. `Procfile`, `runtime.txt` and `requirements.txt` take care of deployments.
