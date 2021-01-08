###It is not a completed task. Unfortunately there are no tests, and best practices inside etc. 
###Task was not deployed to Aiven hosting, Kafka and Postgres were being used in docker instead.

What I couldn't manage so far:
- [ ] Implement bulk sql request
- [ ] reading from kafka by chunks
- [ ] run with Aiven kafka and postgres
- [ ] write unit tests 
- [ ] try async approach
- [ ] implement comments and docs
- [ ] implement type annotation and logs
- [ ] improve site-cheker metricks


What I have accomplished:
- [x]  It works somehow
- [x] deployment all services 
- [x] faced interesting topic which I didn't face before 
- [x] found some knowledge gaps using generators

Producer container runs by crontab`s schedule and it 
generates messages.

Consumer container runs forever except consumer_timeout_ms, 
after stopping, I hope docker will restart container automatically.

I know it is not wise to manage system like this.

Anyway, it is what is.


##start all containers
`docker-compose up`