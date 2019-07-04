# flask-boilerplate
Minimal setup for building a Python API running with Flask and MongoDB, inside Docker Containers

### Set configs 
configs are read from `app/utils/config.ini`


### On machines with Docker and Docker Compose installed, simply run:

```
bash build.sh
```

### In order to change the port:
change the port from 5000 in `docker-compose.yml`
```yml
ports:
     - "5000:80"
```

Open the instance on `localhost:5000`