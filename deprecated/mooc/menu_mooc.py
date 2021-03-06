from flask import Blueprint
import flask
from cloudmesh.util.logger import LOGGER

import cloudmesh
log = LOGGER(__file__)

menu_mooc_module = Blueprint('menu_mooc_module', __name__)


xsuper_sidebar_pages = [
    ["Cloudmesh",
        [
            ["Home", "/"],
            ["Status", "/status"],
            ["Profile", "/profile/"],
            ["Keys", "/keys/"],
        ],
    ],
    ["Provision",
        [
            ["Policy", "/provision/policy"],
            ["Overview", "/provision/summary/"],
            ["Form", "/provision/"],
            ["Workflow", "/provision/workflow"],
        ],
    ],
    ["Clouds",
        [
            ["Register", "/mesh/register/clouds"],
            ["Refresh", "/cm/refresh"],
            ["VMs", "/mesh/servers"],
            ["Images", "/mesh/images"],
            ["Flavors", "/mesh/flavors/"],
            ["Users", "/mesh/users/"],
        ],
    ],
    ["HPC",
        [
            ["Queues", "/mesh/qstat"],
            ["Users", "/users/ldap"],
            ["Admin", "/hpc"]
        ]
    ],
    ["Launcher",
        [
            ["Launcher", "/cm/launch"],
            ["Register", "/cm/register"]
        ]
    ],
]


flask.Flask.app_ctx_globals_class.super_sidebar_pages = super_sidebar_pages

app_topbar = [
    ["Home", "/"],
    ["Profile", "/profile/"],
    ["About", "/about/"],
    ["Contact", "/contact/"],
]

app_externalbar = [
    ["FutureGrid", "https://portal.futuregrid.org"],
    ["-- Manual", "http://manual.futuregrid.org"],
    ["Cloudmesh", "https://github.com/cloudmesh/cloudmesh"],
    ["Blog", "http://cloudmesh.blogspot.com"],
]


topbar_pages = []
for page in app_topbar:
    topbar_pages.append({'name': page[0], 'url': page[1]})

# registering topbar into the global g
flask.Flask.app_ctx_globals_class.topbar_pages = topbar_pages


# log.info("{0}".format(str(flask.Flask.app_ctx_globals_class.topbar_pages)))

externalbar_pages = []
for page in app_externalbar:
    externalbar_pages.append({'name': page[0], 'url': page[1]})

# registering externalbar   into the global g
flask.Flask.app_ctx_globals_class.externalbar_pages = externalbar_pages


# log.info("{0}".format(str(flask.Flask.app_ctx_globals_class.externalbar_pages)))


#
# ACTIVATE STRUCTURE
#

# @menu_mooc_module.context_processor
# def inject_sidebar():

#    print "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"

    #    return dict(sidebar_pages=g.sidebar_pages)
