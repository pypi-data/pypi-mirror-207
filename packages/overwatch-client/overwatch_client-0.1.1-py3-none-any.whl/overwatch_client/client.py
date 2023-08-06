import os, sys
import requests
import time
from typing import Optional, Sequence, Dict
from .utils import generate_uuid


class HTTPClient:
    def __init__(
        self,
        overwatch_server_url: str = "https://overwatch.distributive.network",
        model_registry_url: str = "https://models.overwatch.distributive.network",
        header_key: str = "ovwatch-secret-key",
    ):
        self.ow_server_url = overwatch_server_url
        self.model_registry_url = model_registry_url
        self.header_payload = {"key": header_key}
        self.inference_timer = []
        self.inference_counter = []

    def check_overwatch_server_connection(self) -> bool:
        try:
            response = requests.get(f"{self.ow_server_url}/status", headers=self.header_payload)
            response.raise_for_status()
            return True
        except requests.exceptions.ConnectionError:
            return False

    def __get_file__(self, file_path: str) -> bytes:
        """
        Retrieves the contents of a file from disk and returns it as bytes. 

        :param file_path: The path to the file. 
        :return: The contents of the file as bytes.
        """
        with open(file_path, "rb") as f:
            ret_bytes: bytes = f.read()
        return ret_bytes

    def register_model(
        self,
        model_name: str,
        model_path: str,
        preprocess_path: str,
        postprocess_path: str,
        password: str = "DefaultPassword",
        language: Optional[str] = None,
        packages: Optional[Sequence[str]] = None,
    ) -> requests.Response:
        url = f"{self.model_registry_url}/models"
        data_payload = {
            "modelID": model_name,
            "password": password,
            "reqPackages": packages if packages is not None else [],
            "language": "javascript" if language is None else language,
        }

        files_payload = {
            "model": self.__get_file__(model_path),
            "preprocess": self.__get_file__(preprocess_path),
            "postprocess": self.__get_file__(postprocess_path),
        }

        response = requests.post(
            url,
            headers=self.header_payload,
            data=data_payload,
            files=files_payload,
        )

        response.raise_for_status()

        return response

    def patch_model(
        self,
        model_name: str,
        model_path: str,
        preprocess_path: str,
        postprocess_path: str,
        password: str = "DefaultPassword",
        language: Optional[str] = None,
        packages: Optional[Sequence[str]] = None,
    ) -> requests.Response:
        """
        Patches a specified model from the model registry with provided information.

        :param model_name: The name of the model to patch.
        :param model_path: The path to the model.
        :param preprocess_path: The path to the preprocess file for this model.
        :param postprocess_path: The path to the postprocess file for this model.
        :param password: The password for this model.
        :param language: The language for this model. Can be either javascript or python.
        :param packages: A list of packages required for this model. 
        :return: [TODO:description]
        """
        url = f"{self.model_registry_url}/models/{model_name}"
        data_payload = {
            "modelID": model_name,
            "password": password,
            "reqPackages": packages if packages is not None else [],
            "language": "javascript" if language is None else language,
        }

        files_payload = {
            "model": self.__get_file__(model_path),
            "preprocess": self.__get_file__(preprocess_path),
            "postprocess": self.__get_file__(postprocess_path),
        }

        response = requests.patch(
            url,
            headers=self.header_payload,
            data=data_payload,
            files=files_payload,
        )

        response.raise_for_status()

        return response

    def delete_model(
        self, model_name: str, password: str = "DefaultPassword"
    ) -> requests.Response:
        """
        Deletes the specified model from the model registry.

        :param model_name: The name of the model to delete.
        :param password: The associated password for the modelself.
        :return: The response object from the model registry after deleting the model.
        """
        url = f"{self.model_registry_url}/models/{model_name}"

        header_payload = {
            "key": self.header_payload["key"],
            "password": password,
        }

        response = requests.delete(
            url,
            headers=header_payload,
        )

        response.raise_for_status()

        return response

    def get_model(self, model_name: str) -> requests.Response:
        """
        Retrieves a model from the model registry.

        :param model_name: The model to retrieve.
        :return: A response object containing the response from the model registry.
        """
        url = f"{self.model_registry_url}/models/{model_name}"

        response = requests.get(url, headers=self.header_payload)

        response.raise_for_status()

        return response

    def infer(
        self,
        inputs: Sequence[bytes],
        model_name: str,
        slice_batch: int = 1,
        inference_id: Optional[str] = None,
        compute_group_info: Optional[str] = None,
    ) -> Dict:
        """
        Performs an inference on the provided inputs using the model specified. Returns 
        the inference results as a dictionary.

        :param inputs: A list of inputs in byte format.
        :param model_name: The model name we will be inferencing on.
        :param slice_batch: The number of inputs per slice.
        :param inference_id: A special ID for this inference instance.
        :param compute_group_info: Compute group information in the form of "<joinKey>/<joinSecret>".
        :return: The inference results as a dictionary.
        """
        inference_id = (
            inference_id
            if inference_id is not None
            else f"{model_name}_{generate_uuid()}"
        )
        url = f"{self.ow_server_url}/Prediction/{inference_id}/detect/iterations/{model_name}/{slice_batch}"
        if compute_group_info is not None:
            url = f"{url}/{compute_group_info}"

        files = {}
        for ind, elem in enumerate(inputs):
            files[f"{ind}"] = elem

        start_time = time.time()

        response = requests.post(
            url,
            headers= { "prediction-key": self.header_payload["key"] },
            files=files,
        )

        response.raise_for_status()

        end_time = time.time()

        self.inference_timer.append(end_time - start_time)
        self.inference_counter.append(len(inputs))

        return response.json()
