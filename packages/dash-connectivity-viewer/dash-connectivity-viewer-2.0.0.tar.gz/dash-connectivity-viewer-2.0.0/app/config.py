import os
from dash_connectivity_viewer import (
    cell_type_connectivity,
    cell_type_table,
    connectivity_table,
)
import json

app_config = {
    "datastack": "minnie65_phase3_v1",
    "server_address": "https://global.daf-apis.com",
    "image_black": 0.35,
    "image_white": 0.7,
    "syn_position_column": "ctr_pt",
    "cell_type_dropdown_options": [
        {
            "label": "AIBS Cell Type Classifications",
            "value": "aibs_soma_nuc_metamodel_preds_v117",
        },
        {
            "label": "AIBS Column Cell Subclasses",
            "value": "allen_column_mtypes_v1",
        },
        {
            "label": "BCM Exc/Inh Classifications",
            "value": "baylor_e_i_model_v1",
        }
    ],
    "synapse_aggregation_rules": {
        "mean_size": {
            "column": "size",
            "agg": "mean",
        },
        "net_size": {
            "column": "size",
            "agg": "sum",
        },
    },
    "omit_cell_type_tables": ["nucleus_detection_v0", "nucleus_neuron_svm"],
    "default_cell_type_option": "allen_soma_coarse_cell_class_model_v1",
    'height_bounds': [0, 950],
    'layer_bounds': [106, 276, 411, 535, 768],
}

class BaseConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
    DASH_DATASTACK_SUPPORT = {
        "minnie65_phase3_v1": {
            "cell_type": {
                "create_app": cell_type_table.create_app,
                "config": app_config,
            },
            "connectivity": {
                "create_app": cell_type_connectivity.create_app,
                "config": app_config,
            },
            "basic_connectivity": {
                "create_app": connectivity_table.create_app,
                "config": {},
            },
        },
        "minnie65_public_v117": {
            "cell_type": {
                "create_app": cell_type_table.create_app,
                "config": app_config,
            },
            "connectivity_table": {
                "create_app": connectivity_table.create_app,
                "config": {},
            },
        },
    }


config = {
    "default": "app.config.BaseConfig",
    "development": "app.config.BaseConfig",
    "testing": "app.config.BaseConfig",
    "production": "app.config.BaseConfig",
}


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    # object-based default configuration
    app.config.from_object(config[config_name])
    if "DASH_SETTINGS" in os.environ.keys():
        app.config.from_envvar("DASH_SETTINGS")
    # instance-folders configuration
    app.config.from_pyfile("config.cfg", silent=True)
    return app
