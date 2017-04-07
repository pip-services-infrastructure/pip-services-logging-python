# Deployment Guide <br/> Logging Microservice

Logging microservice can be used in different deployment scenarios.

* [Standalone Process](#process)
* [Seneca Plugin](#seneca)

## <a name="process"></a> Standalone Process

The simplest way to deploy the microservice is to run it as a standalone process. 
This microservice is implemented in Python and requires installation of Python 2.7. 
You can get it from the official site at https://www.python.org/downloads/

**Step 1.** Download microservices by following [instructions](Download.md)

**Step 2.** Add **config.yaml** file to the root of the microservice folder and set configuration parameters. 
See [Configuration Guide](Configuration.md) for details.

**Step 3.** Start the microservice using the command:

```bash
python ./bin/run.py
```
