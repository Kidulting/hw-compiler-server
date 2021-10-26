import os
import configparser
from flask_script import Manager
from com.kidulting.hw-compiler import create_app
from com import blueprint_v1

dirname = os.path.dirname(__file__)
config_filename = os.path.join(dirname, 'configuration/config.properties')
config = configparser.RawConfigParser()
config.read(config_filename)

app = create_app()

app.register_blueprint(blueprint_v1, url_prefix='/v1')
app.app_context().push()
manager = Manager(app)

@manager.command
def run():
    config_host = config.get('Address', 'address.host')
    config_port = int(config.get('Address', 'address.port'))

    app.run(host=config_host, port=config_port)

if __name__ == '__main__':
    manager.run()
