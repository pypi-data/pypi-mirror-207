import shutil
import requests
from pathlib import Path
from os import environ
from nanomock.modules.nl_parse_config import ConfigReadWrite
from nanolab.src.github import GitHubAPI


class PathHandler:

    def __init__(self, testcase_alias: str):
        self.conf_rw = ConfigReadWrite()

        self.is_local_path = False
        self.base_path = Path(environ.get("NL_PATH") or str(Path.cwd()))
        self.testcase_name = self._set_testcase_name(testcase_alias.strip())
        self.resources_dir = environ.get("NL_RES_DIR", "resources")
        self.resources_path = self.base_path / self.resources_dir / self.testcase_name
        self.downloads_path = self.base_path / self.resources_dir / self.testcase_name / "dowlnoads"
        self.config_file_path = self.resources_path / "config_copy.json"
        self.resolved_config_file_path = self.resources_path / "resolved_config.json"
        self.snippets_path = self.base_path / "snippets"

        self.resources_path.mkdir(parents=True, exist_ok=True)
        self.downloads_path.mkdir(parents=True, exist_ok=True)

    def _set_testcase_name(self, testcase_alias):
        #for ease of use we allow alias to be either local path to disk, or downloadable alias
        if testcase_alias.endswith(".json"):
            config = self.conf_rw.read_json(testcase_alias)
            testcase_name = config.get("testcase", "unknown_testcase")
            self.is_local_path = True
        else:
            testcase_name = testcase_alias
        return testcase_name

    def get_testcase_name(self):
        return self.testcase_name

    def get_config_path(self):
        return self.resources_path / "config.json"

    def get_resources_path(self):
        return self.resources_path

    def get_snippets_path(self):
        return self.snippets_path

    def download_config_file(self, config_data: str) -> str:
        return self.download_data(config_data, "config.json")

    def download_url(self, url: str) -> str:
        return self.download_data(url.strip(), Path(url).name)

    def download_data(self, data: str, filename: str) -> str:
        destination = self.resources_path / filename

        if not destination.exists():
            if data.startswith("http://") or data.startswith("https://"):
                response = requests.get(data)
                with destination.open("wb") as f:
                    f.write(response.content)
            else:
                with destination.open("w") as f:
                    f.write(data)

        return destination

    def _copy_path(self, path: str) -> str:
        filename = Path(path).name
        destination = self.resources_path / filename

        copy_files = environ.get("NL_COPY_FILES", "True")
        if copy_files.lower() == "true" and not destination.exists():
            shutil.copy(path, destination)
        return destination


class PathResolver():

    def __init__(self, gh_user, gh_repo, gh_path, resource_path,
                 testcase_alias, is_local_path):
        self.testcase_alias = testcase_alias
        self.is_local_path = is_local_path
        self.resource_path = resource_path
        self.github_api = GitHubAPI(gh_user, gh_repo, gh_path)

    def save_config_file(self, destination: Path):
        if self.is_local_path:
            #self.testcase_alias is a filepath to a json file
            return self._copy_path(self.testcase_alias,
                                   destination,
                                   force_copy=True)
        else:
            return self._download_config_file(destination)

    def download_and_replace_resources(self, config: dict,
                                       destination_path: Path):
        global_resources = config.get("global", {})

        for key, value in global_resources.items():
            if value.startswith("http://") or value.startswith("https://"):
                # Download the remote file
                downloaded_path = self._download_url(value, destination_path)
                # Replace the URL with the downloaded file path
                global_resources[key] = str(downloaded_path)
            elif environ.get("NL_COPY_FILES").lower() == "true":
                # Copy the local file to the destination
                copied_path = self._copy_path(
                    value, destination_path / Path(value).name)
                # Replace the local path with the copied file path
                global_resources[key] = str(copied_path)

        return config

    def replace_resources(self, config: dict, destination_path: Path):
        global_resources = config.get("global", {})
        updated_global_resources = {}

        for key, value in global_resources.items():
            if value.startswith("http://") or value.startswith("https://"):
                # Replace the URL with "{destination}/{filename}"
                filename = Path(value).name
                updated_global_resources[
                    key] = f"{destination_path}/{filename}"
            elif environ.get("NL_COPY_FILES").lower() == "true":
                # Replace the local file with "{destination}/{filename}"
                filename = Path(value).name
                updated_global_resources[
                    key] = f"{destination_path}/{filename}"
            else:
                # Keep the local path unchanged
                updated_global_resources[key] = value

        config["global"] = updated_global_resources
        return config

    def list_testcases(self):
        files = self.github_api.get_files()

        if files:
            for file in files:
                if file["name"].endswith(".json"):
                    print(file["name"][:-5])

    def _download_config_file(self, destination: Path) -> str:
        config_data = self.github_api.get_file_content(
            f"{self.testcase_alias}.json")
        return self._download_data(config_data, destination.name,
                                   destination.parent)

    def _download_url(self, url: str, resource_path: Path) -> str:
        return self._download_data(url.strip(), Path(url).name, resource_path)

    def _download_data(self, data: str, filename: str,
                       resource_path: Path) -> str:
        destination = resource_path / filename

        if not destination.exists():
            if data.startswith("http://") or data.startswith("https://"):
                response = requests.get(data)
                with destination.open("wb") as f:
                    f.write(response.content)
            else:
                with destination.open("w") as f:
                    f.write(data)

        return destination

    def _copy_path(self,
                   source_path: str,
                   destination: Path,
                   force_copy=None) -> str:
        source = Path(source_path)

        copy_files = force_copy or environ.get("NL_COPY_FILES", "False")
        if copy_files.lower() == "true" and not destination.exists():
            shutil.copy(source, destination)
        return destination