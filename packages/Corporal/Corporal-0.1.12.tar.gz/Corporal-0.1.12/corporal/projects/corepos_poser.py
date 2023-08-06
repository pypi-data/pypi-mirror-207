# -*- coding: utf-8; -*-
"""
CORE-POS "Poser" project generator
"""

import os

from rattail.projects import ProjectGenerator


class COREPOSPoserProjectGenerator(ProjectGenerator):
    """
    Generator for CORE-POS "Poser" projects
    """
    key = 'corepos_poser'

    def generate_project(self, output, context, **kwargs):

        ##############################
        # office plugins
        ##############################

        office_plugins = os.path.join(output, 'office_plugins')
        os.makedirs(office_plugins)

        demo_plugin = os.path.join(office_plugins, 'PoserDemo')
        os.makedirs(demo_plugin)

        self.generate('office_plugins/PoserDemo/PoserDemo.php',
                      os.path.join(demo_plugin, 'PoserDemo.php'))

        ##############################
        # lane plugins
        ##############################

        lane_plugins = os.path.join(output, 'lane_plugins')
        os.makedirs(lane_plugins)

        demo_plugin = os.path.join(lane_plugins, 'PoserDemo')
        os.makedirs(demo_plugin)

        self.generate('lane_plugins/PoserDemo/PoserDemo.php',
                      os.path.join(demo_plugin, 'PoserDemo.php'))
