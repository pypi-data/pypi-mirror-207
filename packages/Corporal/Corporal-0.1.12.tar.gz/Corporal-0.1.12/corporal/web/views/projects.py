# -*- coding: utf-8; -*-
"""
Project views
"""

from tailbone.views import ViewSupplement


class GeneratedProjectViewSupplement(ViewSupplement):
    """
    View supplement for generating projects
    """
    route_prefix = 'generated_projects'

    def configure_form_corporal(self, f):

        f.set_grouping([
            ("Naming", [
                'name',
                'pkg_name',
                'pypi_name',
                'organization',
            ]),
            ("Core", [
                'extends_config',
                'has_cli',
            ]),
            ("Database", [
                'extends_db',
            ]),
        ])

        # default settings
        f.set_default('extends_config', False)
        f.set_default('extends_db', False)


def includeme(config):
    GeneratedProjectViewSupplement.defaults(config)
