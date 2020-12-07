import json

from eme.entities import EntityJSONEncoder

from core.utils import get_game_config


def init(app, conf):
    # Globals in Jinja:
    @app.context_processor
    def inject_dict_for_all_templates():
        return dict(
            # (current_user)
            # (current_token)
            # conf=conf,
            settings=get_game_config().conf,
            js_transpiled=conf['website'].get('js_transpiled', True)
        )

    @app.template_filter()
    def ejson(text):
        """Converts variable to json string using eme's extended encoder."""

        return json.dumps(text, cls=EntityJSONEncoder)

