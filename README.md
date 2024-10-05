# Pyshort

Une application pour réduire la taille des liens.

# Installation

Il s'agit d'un application Python Django, suivez les [instructions officielles](https://docs.djangoproject.com/fr/5.1/howto/deployment/) si vous ne souhaitez pas utiliser l'image docker.

Il est important d'utiliser un environnement virtuel pour python et d'installer les paquets de requirements.txt.

```sh
pip install -r requirements.txt # installation des dépendances
python manage.py makemigrations # si il y a des changements de modèles
python manage.py migrate # migration de la BDD à initier lors du premier lancement
```

L'ajout d'un administrateur:

```sh
python manage.py createsuperuser
```

## Docker

Image Docker: reg.rei.ms/wolf/pyshort

Exemple de fichier de composition:

```yaml
services:
  cache:
    image: redis

  pyshort:
    depends_on:
      - cache
    image: reg.rei.ms/wolf/pyshort:arm
    environment:
      REDIS_HOST: cache
      url: https://${PYSHORT_HOST}
      PYSHORT_HOST: ${PYSHORT_HOST}
    networks:
      - internal

networks:
  internal:
    external: false
```

# Feuille de route

- [x] Flask
- [x] Passage à Django
- [x] Frontend
- [ ] Rest Framework

# Documents

- Based on this [DO tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-url-shortener-with-flask-and-sqlite#:~:text=%20How%20To%20Make%20a%20URL%20Shortener%20with,will%20add%20a%20new%20route%20that...%20More%20).
