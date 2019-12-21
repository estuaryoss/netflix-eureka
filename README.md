# netflixoss-eureka
NetflixOSS Eureka server registry with updated tomcat and eureka version

## Build status
[![Build Status](https://travis-ci.org/dinuta/netflixoss-eureka.svg?branch=master)](https://travis-ci.org/dinuta/netflixoss-eureka)

## Docker Hub
[![](https://images.microbadger.com/badges/image/dinutac/netflixoss-eureka.svg)](https://microbadger.com/images/dinutac/netflixoss-eureka "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/dinutac/netflixoss-eureka.svg)](https://microbadger.com/images/dinutac/netflixoss-eureka "Get your own version badge on microbadger.com") ![](https://img.shields.io/docker/pulls/dinutac/netflixoss-eureka.svg)

## Docker run
docker run -d -p 8080:8080 dinutac/netflixoss-eureka:1.9.15

## Docker run with replication
docker run -d -p 8080:8080 \   
-e JAVA_OPTS="-Deureka.serviceUrl.default=http://<eureka_replica_ip>:<eureka_replica_port>/eureka/v2/" dinutac/netflixoss-eureka:1.9.15

Example:
```
docker run -d -p 8080:8080 -e JAVA_OPTS="-Deureka.serviceUrl.default=http://10.10.10.2:8080/eureka/v2/" dinutac/netflixoss-eureka:1.9.15
```

For multiple eureka servers replication, separate them with comma.

## Browser access
http://localhost:8080/eureka  

## Eureka register endpoint
http://localhost:8080/eureka/v2  

## About versions
Tomcat: 9.0.26  OpenJDK  (Release date: 19.09.2019)  
Eureka: 1.9.15  (Release date: 19.12.2019)

