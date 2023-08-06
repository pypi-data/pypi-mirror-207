from dataclasses import dataclass, Field, fields, field
from typing import Tuple


@dataclass
class ApiUrls:
    ENVIRONMENT: str = "production"

    # Authentication
    AUTH_URL: str = field(init=False, default="/api/v1/token/")

    # Planting Design
    GET_PLANTING_DESIGN_DETAIL: str = field(
        init=False, default="/plantingdesign/api/detail/"
    )
    GET_PLANTING_DESIGN_LIST: str = field(
        init=False, default="/plantingdesign/api/list"
    )

    # May Layers
    GET_MAP_LAYERS: str = field(init=False, default="/rs_dashboard/maplayers")

    # Calibrate
    GET_CALIBRATE_INPUT: str = field(
        init=False, default="/sciencemodel/calibrateinput/"
    )
    UPDATE_CALIBRATE_SCENARIO_PARAMETERS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/calibrate_scenario_update_parameters",
    )
    COMPLETE_SCENARIO_CALIBRATION: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/complete_scenario_calibration",
    )
    GET_PLANTING_DESIGN_CALIBRATE_SCENARIOS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/list_planting_design_calibrate_scenarios/",
    )
    GET_CALIBRATE_SCENARIO_SIBLINGS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/list_siblings_calibrate_scenarios/",
    )

    # Density Analysis
    GET_DA_INPUT: str = field(init=False, default="/sciencemodel/densityanalysisinput/")
    COMPLETE_DA_RUN: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/complete_density_run",
    )

    # FastTrack
    GET_FT_INPUT: str = field(init=False, default="/sciencemodel/fasttrackinput/")
    COMPLETE_FASTTRACK_RUN: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/complete_fasttrack_run",
    )

    # Deprecated

    GET_MODEL_INPUT_FAST_TRACK: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/model_input_fast_track/",
    )
    GET_MODEL_INPUT_CALIBRATE_FAST_TRACK: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/model_input_calibrate_fast_track/",
    )
    GET_MODEL_INPUT_DENSITY_ANALYSES_FAST_TRACK: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/model_input_density_analyses_fast_track/",
    )
    # Cloud Calibrate
    GET_MODEL_INPUT_FOR_SCENARIO_CALIBRATE: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/model_input_for_scenario_calibrate/",
    )
    GET_CALIBRATE_SCENARIO_SETTINGS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/calibrate_scenario_settings/",
    )
    GET_CALIBRATE_SCENARIO_NFI_FILTER: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/nfi_filter_for_calibrate_scenario/",
    )
    GET_CALIBRATE_SCENARIO_STATE_VARS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/calibrate_scenario_state_vars/",
    )
    GET_CALIBRATE_SCENARIO_PARAMETERS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/calibrate_scenario_get_parameters/",
    )
    # Cloud FT
    GET_FASTTRACK_RUN_SETTINGS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/fasttrack_run_settings/",
    )
    # Cloud DA
    GET_DA_RUN_SETTINGS: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/density_run_settings/",
    )

    # START LEGACY ENDPOINTS -----------
    GET_MODEL_INPUT_URL: str = field(
        init=False,
        default="/sciencemodel/fasttrackinput/planting_design_config/",
    )
    GET_OLD_MODEL_INPUT_URL: str = field(
        init=False, default="/api/v1/llcmodel/model_input?model_run_ids"
    )

    # END LEGACY ENDPOINTS -------------

    def __post_init__(self):
        self.make_urls()

    def make_urls(self):
        BASE_URL = self.get_base_url()
        cls_fields: Tuple[Field, ...] = fields(self.__class__)

        for field in cls_fields:
            if field.name != "ENVIRONMENT":
                new_val = BASE_URL + getattr(self, field.name)
                setattr(self, field.name, new_val)

    def get_base_url(self):
        if self.ENVIRONMENT == "production":
            BASE_API_URL = "https://internal-landlifecompany.appspot.com"
        elif self.ENVIRONMENT == "staging":
            BASE_API_URL = (
                "https://staging-dot-internal-landlifecompany.ue.r.appspot.com"
            )
        elif self.ENVIRONMENT == "local":
            BASE_API_URL = "http://127.0.0.1:8000"
        elif self.ENVIRONMENT == "cma_poc":
            # Temp using ngrok for testing
            BASE_API_URL = (
                "https://feat-cma-tool-dot-internal-landlifecompany.ue.r.appspot.com"
            )
            # BASE_API_URL = "https://d31a-195-169-110-166.ngrok.io"
        else:
            # We can pass a custom url to use while testing
            BASE_API_URL = self.ENVIRONMENT

        return BASE_API_URL
