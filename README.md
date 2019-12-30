# netflixoss-eureka
NetflixOSS Eureka server registry with updated tomcat and eureka version

## Build status
[![Build Status](https://travis-ci.org/dinuta/netflixoss-eureka.svg?branch=master)](https://travis-ci.org/dinuta/netflixoss-eureka)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc6bbd138aea4291ab85cb4d4ad58af5)](https://www.codacy.com/manual/dinuta/netflixoss-eureka?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dinuta/netflixoss-eureka&amp;utm_campaign=Badge_Grade)

## Docker Hub
[![](https://images.microbadger.com/badges/image/dinutac/netflixoss-eureka.svg)](https://microbadger.com/images/dinutac/netflixoss-eureka "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/dinutac/netflixoss-eureka.svg)](https://microbadger.com/images/dinutac/netflixoss-eureka "Get your own version badge on microbadger.com") ![](https://img.shields.io/docker/pulls/dinutac/netflixoss-eureka.svg)

## Docker run
```shell script
docker run -d -p 8080:8080 dinutac/netflixoss-eureka:1.9.15
```

## Docker run with replication
```shell script
docker run -d -p 8080:8080 \   
-e JAVA_OPTS="-Deureka.serviceUrl.default=http://<eureka_replica_ip>:<eureka_replica_port>/eureka/v2/" dinutac/netflixoss-eureka:1.9.15
```

Example:
```shell script
docker run -d -p 8080:8080 -e JAVA_OPTS="-Deureka.serviceUrl.default=http://10.10.10.2:8080/eureka/v2/" dinutac/netflixoss-eureka:1.9.15
```

For multiple eureka servers replication, separate them with comma.

## Browser access
```shell script
curl -i http://localhost:8080/eureka  
```

## Eureka register endpoint
```shell script
curl -i http://localhost:8080/eureka/v2 
``` 

## About versions
Tomcat: 9.0.26, Eureka: 1.9.15