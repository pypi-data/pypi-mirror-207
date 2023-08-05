from didigo.constant.version import version
from didigo.command_type import *
# from openxlab.model import download

class Version(BaseCommand):
    """get version version"""

    def get_name(self) -> str:
        return "version"

    def add_arguments(self, parser: ArgumentParser) -> None:
        pass

    def take_action(self, parsed_args: Namespace) -> int:
        print("version %s" % version)
        # download("dong/segement_anything", "ViT-B-32.pt")
        return 0