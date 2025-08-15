# Outline

https://docs.getoutline.com/s/hosting/doc/docker-7pfeLP5a8t

## Setup
```
sudo docker compose run --rm outline yarn db:create --env=production-ssl-disabled
```

```
sudo docker compose run --rm outline yarn db:migrate --env=production-ssl-disabled
```