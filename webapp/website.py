from os.path import realpath, dirname, join
from eme.entities import load_settings
from eme.website import WebsiteApp

# Init eme ctx & modules
from core.dal import ctx
from modules import modules


class MetaIndexWebsite(WebsiteApp):

    def __init__(self):
        # eme/examples/simple_website is the working directory.
        script_path = dirname(realpath(__file__))
        conf = load_settings(join(script_path, 'config.ini'))

        super().__init__(conf, script_path)

        # Initialize database & modules
        assert ctx.get_session() != None
        self.init_modules(modules, conf)


if __name__ == "__main__":
    app = MetaIndexWebsite()
    app.start()
