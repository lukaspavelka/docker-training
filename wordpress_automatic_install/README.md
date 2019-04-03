# clone from git or download zip file and unzip


$ git clone https://github.com/lukaspavelka/docker-training/



# docker-haproxy-nginx

## Usage

```sh
$ docker-compose up
```

## Find IP address of HaPROXY Container
```sh
docker inspect -f '{{ .NetworkSettings.Networks.wordpress_automatic_install_default.IPAddress }}' wordpress_automatic_install_haproxy_1
```

## edit and start file requests.sh
```sh
vim requests.sh
./requests.sh
```
