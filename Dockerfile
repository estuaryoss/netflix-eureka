FROM tomcat:9.0.26-jdk8-openjdk

ENV EUREKA_VERSION 1.9.15

WORKDIR $CATALINA_HOME/webapps/eureka

RUN wget -q http://repo1.maven.org/maven2/com/netflix/eureka/eureka-server/$EUREKA_VERSION/eureka-server-$EUREKA_VERSION.war &&\
  jar xf eureka-server-$EUREKA_VERSION.war &&\
  rm eureka-server-$EUREKA_VERSION.war

COPY config.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/config.properties
COPY eureka-client.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-client.properties
COPY eureka-server.properties $CATALINA_HOME/webapps/eureka/WEB-INF/classes/eureka-server.properties

EXPOSE 8080

CMD ["catalina.sh", "run"]
