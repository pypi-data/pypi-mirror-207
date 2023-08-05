import sys
from pathlib import Path
from typing import Optional


scripts_dir_path = Path(__file__).parents[1]
sys.path.insert(0, str(scripts_dir_path))

import Shared.certoraUtils as Cu


class ExtensionInfoWriter:
    """
    A class that generates a JSON file containing information for the VSCode extension, such as the verification report
    link.
    It will always generate the file, either via an explicit call to close, or when this object is deleted from
    memory. The file should only be written once.
    """
    def __init__(self, report_url: Optional[str] = None):
        self.verification_report_url = report_url
        self.closed = False

    def set_verification_report_url(self, link: str) -> None:
        self.verification_report_url = link

    def __dump_to_log(self) -> None:
        json_data = {
            "verification_report_url": self.verification_report_url
        }
        Cu.write_json_file(json_data, Cu.get_extension_info_file())

    def close(self) -> None:
        if not self.closed:
            self.__dump_to_log()
            self.closed = True

    def __del__(self) -> None:
        self.close()
