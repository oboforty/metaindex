from os.path import realpath, dirname, join
from eme.entities import load_settings, load_handlers
from eme.website import WebsiteApp

# Init eme ctx & modules
from core.dal import ctx
from modules.modules import modules


class MetaIndexWebsite(WebsiteApp):

    def __init__(self):
        # eme/examples/simple_website is the working directory.
        script_path = dirname(realpath(__file__))
        conf = load_settings(join(script_path, 'config.ini'))

        super().__init__(conf, script_path)

        self.load_controllers(load_handlers(self, 'Api', module_path='api', path=join(script_path, 'api')), conf=conf.get('routing', {}))

        # Initialize database & modules
        assert ctx.get_session() != None
        self.init_modules(modules, conf)


if __name__ == "__main__":
    app = MetaIndexWebsite()
    app.start()
