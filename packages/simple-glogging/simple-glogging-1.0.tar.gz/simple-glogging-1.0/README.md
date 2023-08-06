# Simple Logging

simple-logging is a Python package that contains methods for interacting with logging package. 

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install simplelogging like below. 
Rerun this command to check for and install  updates .
```bash
pip install simplelogging
```

## Usage

On the host or client code please add a directory at the root level, name it resources.
Create a ymal file for log configuration
below are the simple configuration template

```bash
    handelers:
        file:
            filepath: 'logs/appLog_{:%Y-%m-%d}.json'
            formate: '%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s %(filename)s %(lineno)s %(message)s'
            loglevel: DEBUG
        console:
            formate: '%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s %(filename)s %(lineno)s %(message)s'
            loglevel: DEBUG
        default_loglevel: ERROR
        default_formate: '%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s %(filename)s %(lineno)s %(message)s'
```


##
How to create distribution
* Delete existing dist folder on project root directory
* Execute below command on project root directory
** python3 setup.py sdist

How to upload distribution to pypi
python3 -m twine upload --repository pypi dist/*

#### Usage:
root_log_name = 'ROOT_LOGGER'
sl = SimpleLogging(root_log_name)
sl.logger.info("This is from root logging")
sl.getLogger("Child logger").info("This is child logger")
sl.initializeLogger()
print("==================After Initializing =========================")
log = sl.getLogger("Child1")
log.info("This is info in child 1 logger")
log.error("This is error in child 1 logger")

print("=================== After Updating ============================")
change_settings = {'level':'DEBUG'}
sl.updateLogger(**change_settings)

log = sl.getLogger("Child2")
log.info("This is info in child 2 logger")
log.debug("This is debug in child 2 logger")
log.error("This is error in child 2 logger")


```
