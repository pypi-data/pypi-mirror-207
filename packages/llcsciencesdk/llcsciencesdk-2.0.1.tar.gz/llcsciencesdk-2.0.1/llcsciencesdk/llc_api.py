from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

import requests
import os
import sys
import pandas as pd

from .exceptions import ApiAuthenticationError, ApiTokenError, ApiGeneralError
from .helpers import json_response_to_df
from .parameter_mapping import update_legacy_parameter
from .urls import ApiUrls

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


@dataclass
class ScienceSdk:
    auth_token: str = field(default_factory=str, repr=False)
    environment: str = "production"
    api_urls: ApiUrls = None

    def __post_init__(self):
        self.api_urls = ApiUrls(ENVIRONMENT=self.environment)

    def _get_request(self, url, url_params: Optional[str] = ""):
        if not self.auth_token:
            raise ApiTokenError

        response = requests.get(
            url + str(url_params),
            headers={"Authorization": f"Bearer {self.auth_token}"},
        )

        return response.json()

    def _post_request(self, url, data):
        if not self.auth_token:
            raise ApiTokenError

        response = requests.post(
            url, headers={"Authorization": f"Bearer {self.auth_token}"}, json=data
        )

        return response.json()

    # LIST OF ENDPOINTS

    # Authentication
    def login(self, username: str, password: str):
        r = requests.post(
            self.api_urls.AUTH_URL, data={"username": username, "password": password}
        )

        if r.status_code == 401:
            raise ApiAuthenticationError(r.text)

        elif not r.ok:
            raise ApiGeneralError(r.text)

        self.auth_token = r.json()["access"]

    # Planting Design

    def get_planting_design_detail(self, planting_design_id: int) -> dict:
        url = self.api_urls.GET_PLANTING_DESIGN_DETAIL
        return self._get_request(url, str(planting_design_id))

    def get_planting_design_list(self) -> dict:
        url = self.api_urls.GET_PLANTING_DESIGN_LIST
        return self._get_request(url)

    # Map Layers
    def get_map_layers(self) -> dict:
        return self._get_request(self.api_urls.GET_MAP_LAYERS)

    # Calibrate

    def get_calibrate_input(self, calibrate_scenario_id: int) -> dict:
        return self._get_request(
            self.api_urls.GET_CALIBRATE_INPUT, str(calibrate_scenario_id)
        )

    def update_calibrate_scenario_parameters(
        self, calibrate_scenario_id: int, parameters: list
    ) -> bool:
        """Updates parameters on a calibrate scenario"""

        url = self.api_urls.UPDATE_CALIBRATE_SCENARIO_PARAMETERS
        data = {"scenario_id": calibrate_scenario_id, "updated_parameters": parameters}
        r = self._post_request(url, data)
        return r

    def complete_calibrate_scenario_calibration(
        self, calibrate_scenario_id: int, results: dict
    ) -> bool:
        """
        Signals a scenario calibration has finished with a calibrate output msg

        Parameters
        ----------
            calibrate_scenario_id: int | str
                The id of the calibrate scenario that was calibrated
            results: dict
                A dict with the keys
                    "success": bool
                    "msg": str Message when success is False

        """

        url = self.api_urls.COMPLETE_SCENARIO_CALIBRATION
        data = {"scenario_id": calibrate_scenario_id, **results}
        r = self._post_request(url, data)
        return r

    def get_planting_design_scenarios(self, planting_design_id: int) -> [dict]:
        """
        Fetches all scenarios for a planting design.

        Parameters
        ----------
            planting_design_id:
                The id of the planting design to fetch the scenarios from

        Returns
        -------
            List of dicts with the keys:
                "scenario_id"
                "name": Calibrate Scenario Name
                "description"
                "status": Calibrate run status
                "species": Latin name of the associated spacies
                "use_for_fasttrack": Boolean flag indicating if it was selected for FastTrack
        """
        url = self.api_urls.GET_PLANTING_DESIGN_CALIBRATE_SCENARIOS
        data = self._get_request(url, str(planting_design_id))
        return data

    def get_siblings_for_calibrate_scenario(
        self, calibrate_scenario_id: int
    ) -> list[dict[int, str]]:
        """
        Returns a list of all the sibling scenarios (same Planting and Tree Species) of a given Scenario.

        Parameters
        ----------
            calibrate_scenario_id:
                The id of the calibrate scenario you want the siblings of

        Returns
        -------
            List of dicts with the keys:
                scenario_id: Scenario id
                status: calibrate run status
        """
        url = self.api_urls.GET_CALIBRATE_SCENARIO_SIBLINGS
        data = self._get_request(url, str(calibrate_scenario_id))
        return data

    # Density Analysis

    def get_da_input(self, da_run_id: int) -> dict:
        return self._get_request(self.api_urls.GET_DA_INPUT, str(da_run_id))

    def complete_da_run(self, da_run_id: int, results: dict) -> bool:
        """
        Signals a density analysis run has finished

        Parameters
        ----------
            da_run_id: int | str
                The id of the Density Analysis run that has finished
            results: dict
                A dict with the keys
                    "success": bool
                    "msg": str Error message when success is False
                    "version": str Fasttrack version used
        """
        url = self.api_urls.COMPLETE_DA_RUN
        data = {"da_run_id": da_run_id, **results}
        r = self._post_request(url, data)
        return r

    # FastTrack
    def get_ft_input(self, ft_run_id: int):
        return self._get_request(self.api_urls.GET_FT_INPUT, str(ft_run_id))

    def complete_fasttrack_run(self, fasttrack_run_id: int, results: dict) -> bool:
        """
        Signals a fast track run has finished

        Parameters
        ----------
            fasttrack_run_id: int | str
                The id of the fasttrackRun that has finished
            results: dict
                A dict with the keys
                    "success": bool
                    "msg": str Error message when success is False
                    "version": str Fasttrack version used
        """
        url = self.api_urls.COMPLETE_FASTTRACK_RUN
        data = {"fasttrack_run_id": fasttrack_run_id, **results}
        r = self._post_request(url, data)
        return r

    # Deprecated Endpoints
    def get_model_input_fast_track_json(
        self, site_design_configuration_id: int
    ) -> dict:
        url = self.api_urls.GET_MODEL_INPUT_FAST_TRACK
        return self._get_request(url, str(site_design_configuration_id))

    def get_model_input_fast_track(self, site_design_configuration_id: int) -> dict:
        data = self.get_model_input_fast_track_json(site_design_configuration_id)
        return json_response_to_df(data)

    def get_model_input_calibrate_fast_track_json(
        self, site_design_configuration_id: int
    ) -> dict:
        url = self.api_urls.GET_MODEL_INPUT_CALIBRATE_FAST_TRACK
        return self._get_request(url, str(site_design_configuration_id))

    def get_model_input_calibrate_fast_track(
        self, site_design_configuration_id: int
    ) -> dict:
        data = self.get_model_input_calibrate_fast_track_json(
            site_design_configuration_id
        )
        return json_response_to_df(data)

    def get_model_input_density_analyses_fast_track_json(
        self, site_design_configuration_id: int
    ) -> dict:
        url = self.api_urls.GET_MODEL_INPUT_DENSITY_ANALYSES_FAST_TRACK
        return self._get_request(url, str(site_design_configuration_id))

    def get_model_input_density_analyses_fast_track(
        self, site_design_configuration_id: int
    ) -> dict:
        data = self.get_model_input_density_analyses_fast_track_json(
            site_design_configuration_id
        )
        return json_response_to_df(data)

    # Methods for CMA / Calibrate Cloud

    def get_calibrate_scenario_state_vars(self, calibrate_scenario_id: int) -> dict:
        """
        Returns the init state variables for a calibrate scenario and a exclusion list

        Returns
        -------
            A dict with the keys:
                "state_variables": dict with the state variables as keys
                "excluded_state_variables": [str] List with names of the state variables to exclude from calibrate
        """

        url = self.api_urls.GET_CALIBRATE_SCENARIO_STATE_VARS
        data = self._get_request(url, str(calibrate_scenario_id))
        return data

    def get_calibrate_scenario_nfi_filter(self, calibrate_scenario_id: int):
        """Returns information about the NFI filter to be used to calibrate a scenario"""

        url = self.api_urls.GET_CALIBRATE_SCENARIO_NFI_FILTER
        data = self._get_request(url, str(calibrate_scenario_id))
        return data

    def get_calibrate_scenario_settings(self, calibrate_scenario_id: int):
        """Returns the settings from a calibrate scenario"""

        url = self.api_urls.GET_CALIBRATE_SCENARIO_SETTINGS
        data = self._get_request(url, str(calibrate_scenario_id))
        return data

    def get_model_input_for_calibrate_scenario(
        self, calibrate_scenario_id: int
    ) -> dict:
        """Returns parameters for calibrate as a dict"""

        url = self.api_urls.GET_MODEL_INPUT_FOR_SCENARIO_CALIBRATE
        data = self._get_request(url, str(calibrate_scenario_id))
        return json_response_to_df(data)

    def get_updated_parameters_from_scenario(self, calibrate_scenario_id: int) -> dict:
        """
        Fetches all parameters from a scenario and returns a dict where the keys are the parameters names.
        If a parameter has not been calibrated, its calibrated_value will be None

        Parameters
        ----------
            calibrate_scenario_id:
                The id of the calibrate scenario

        Returns
        -------
            dict
                keys: Parameter name
                value: dict with the keys initial_value, lower, upper, calibrated_value
        """
        url = self.api_urls.GET_CALIBRATE_SCENARIO_PARAMETERS
        data = self._get_request(url, str(calibrate_scenario_id))
        wanted_k = ["initial_value", "lower", "upper", "calibrated_value"]
        params = {}
        for p in data:
            params[p.get("name", "_")] = dict((k, p.get(k)) for k in wanted_k)
        return params

    # FastTrak cloud
    def get_fasttrack_run_settings(self, fasttrack_run_id: int):
        """Returns data needed to configure and run FT"""
        url = self.api_urls.GET_FASTTRACK_RUN_SETTINGS
        data = self._get_request(url, str(fasttrack_run_id))
        return data

    # Density Analysis cloud
    def get_da_run_settings(self, da_run_id: int):
        """Returns data needed to configure and run DA"""
        url = self.api_urls.GET_DA_RUN_SETTINGS
        data = self._get_request(url, str(da_run_id))
        return data

    # START LEGACY METHODS --------------------
    # TODO: remove once all fast track instances use new SDK methods
    def get_model_inputs_as_df(self, config_option: int, legacy_parameters=False):
        data = self.get_model_input_as_json(config_option, legacy_parameters)

        site_info = data["site_info"]
        plot_types = data["plot_types"]
        parameter_data = data["parameter_data"]
        parameter_info = data["parameter_info"]
        species_info = data["species_info"]
        model_info = data["model_info"]

        df_sites_info = pd.json_normalize(site_info)
        df_plot_types = pd.json_normalize(plot_types)
        df_parameter_data = pd.json_normalize(parameter_data)
        df_parameter_info = pd.json_normalize(parameter_info)
        df_species_info = pd.json_normalize(species_info)
        df_model_info = pd.json_normalize(model_info)

        return (
            df_sites_info,
            df_plot_types,
            df_parameter_data,
            df_parameter_info,
            df_species_info,
            df_model_info,
        )

    def get_model_input_as_json(self, config_option, legacy_parameters):
        if not self.auth_token:
            raise ApiTokenError

        url = self.api_urls.GET_MODEL_INPUT_URL + str(config_option)

        if legacy_parameters:
            url = url + "?legacy_parameters"

        data = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.auth_token}"},
        )

        return data.json()

    def get_old_model_inputs(self, model_runs: list, legacy_parameters=False):
        if not self.auth_token:
            raise ApiTokenError

        list_of_runs = ",".join(map(str, model_runs))
        data = requests.get(
            self.api_urls.GET_OLD_MODEL_INPUT_URL + f"={list_of_runs}",
            headers={"Authorization": f"Bearer {self.auth_token}"},
        )

        sites_info = data.json()["sites_info"]
        parameter_data = data.json()["parameter_data"]
        parameter_info = data.json()["parameter_info"]
        species_info = data.json()["species_info"]
        model_info = data.json()["model_info"]

        df_sites_info = pd.json_normalize(sites_info)
        df_parameter_data = pd.json_normalize(parameter_data)
        df_parameter_info = pd.json_normalize(parameter_info)
        df_species_info = pd.json_normalize(species_info)
        df_model_info = pd.json_normalize(model_info)

        if legacy_parameters:
            for i, row in df_parameter_data.iterrows():
                df_parameter_data.at[i, "ParameterName"] = update_legacy_parameter(
                    row["ParameterName"]
                )
            for i, row in df_parameter_info.iterrows():
                df_parameter_info.at[i, "ParameterName"] = update_legacy_parameter(
                    row["ParameterName"]
                )
        return (
            df_sites_info,
            df_parameter_data,
            df_parameter_info,
            df_species_info,
            df_model_info,
        )

    # END LEGACY METHODS --------------------
