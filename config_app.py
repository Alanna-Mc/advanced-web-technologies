import configparser
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, url_for

app = Flask(__name__)

def init(app):
    config = configparser.ConfigParser()    
    config_location = "etc/defaults.cfg"
    config.read(config_location)

    # Config for the Flask app
    app.config["DEBUG"] = config.get("config", "debug") 
    app.config["ip_address"] = config.get("config", "ip_address")
    app.config["port"] = config.get("config", "port")
    app.config["url"] = config.get("config", "url") 
    
    # Config for logging
    app.config['log_file'] = config.get('logging', 'name')
    app.config["log_location"] = config.get("logging", "location")
    app.config["log_level"] = config.get("logging", "level").upper()


def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(
        log_pathname, maxBytes=1024*1024*10, backupCount=10
    )
    file_handler.setLevel(app.config["log_level"])
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel(app.config["log_level"])
    app.logger.addHandler(file_handler)


# Initialise configuration and logging
init(app)
logs(app)


@app.route("/")
def root():
    return "Hello from the configuration testing app with logging!"


@app.route("/config/")
def config():
    app.logger.info('Accessed config route')
    s =[]
    s.append("debug:"+str(app.config["DEBUG"]))
    s.append("port:"+app.config["port"])
    s.append("url: "+app.config["url"])
    s.append("ip_address:"+app.config["ip_address"])
    return ",".join(s)


if __name__ == "__main__":
    init(app)
    logs(app)
    app.run(
        host=app.config["ip_address"],
        port=int(app.config["port"]))
