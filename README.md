# Buser lab based on d-jà vue - (https://github.com/evolutio/djavue)

This is just a CRUD example using a decoupling architecture


### Example architecture
* [Nuxt.js] frontend on S3 bucket
* [Python-Django] backend on EC2 with docker container
* [Postgres] db running on docker (it's just a example, ok?)

# DEV Start

`docker-compose -f docker-compose.dev.yaml up --build`

# PROD setup

### 1) compose file:
- config a compose file without frontend container
- fill the backend env vars correctly to access your environment

*OBS) Using Dockerize* (https://github.com/jwilder/dockerize):
- wait for a db connection to launch the container
- set the template of env vars


### 2) frontend:
- config a static website on s3 bucket
- with the s3 website url fill the compose var `DJANGO_CORS_ORIGIN_WHITELIST`
- npm run build && npm run generate
- deploy dist/ to s3 bucket 
- automate things as you wish (scripts/frontend.sh is example to automate using aws-cli)
- file /frontend/plugins/api.js needs a `baseURL` to reach server

*OBS) Cors*:
- the variable `CORS_ORIGIN_WHITELIST` controls the allowed origins to reach backend (fill the compose file, usage on `settings.py` file)

### 3) backend:
- install docker and docker-compose
- run docker-compose file on server: `docker-compose -f docker-compose.prod.yaml up --build` or detached

## Image
- https://ibb.co/jzndFKS
- 
### Improvements

- make it lean
- Scale out
- remove volume bindings to prod env
- evict 'latest' versions
- log structure
- remove other env structure of current env
- https connection
- CDN to make s3 bucket private
#
... and a lot of things that I need to learn yet
