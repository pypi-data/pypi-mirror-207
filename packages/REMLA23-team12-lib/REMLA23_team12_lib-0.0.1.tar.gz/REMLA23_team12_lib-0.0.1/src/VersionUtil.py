import subprocess


class VersionUtil:
    @staticmethod
    def get_version():
        try:
            version = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
        except subprocess.CalledProcessError:
            version = "Unknown"

        return version


## How to call this function to check the version:

# from lib.versionutil import VersionUtil
#
# version = VersionUtil.get_version()
# print(f"Library version: {version}")