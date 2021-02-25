from os.path import dirname, realpath, join

from eme.entities import load_settings
from eme.cli import CommandLineInterface

# Init eme ctx & modules
from core.dal import ctx
from modules.modules import modules


class MetaIndexCommandLineInterface(CommandLineInterface):

   def __init__(self):
      script_path = dirname(realpath(__file__))
      conf = load_settings(join(script_path, 'config.ini'))

      super().__init__(conf, script_path)

      assert ctx.get_session() != None
      self.init_modules(modules, conf)
