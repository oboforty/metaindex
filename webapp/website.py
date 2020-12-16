from os.path import realpath, dirname, join
from eme.entities import load_settings
from eme.website import WebsiteApp

from modules import modules


class MetaIndexWebsite(WebsiteApp):

    def __init__(self):
        # eme/examples/simple_website is the working directory.
        script_path = dirname(realpath(__file__))
        conf = load_settings(join(script_path, 'config.ini'))

        super().__init__(conf, script_path)

        self.init_modules(modules, conf)


if __name__ == "__main__":
    app = MetaIndexWebsite()
    app.start()
