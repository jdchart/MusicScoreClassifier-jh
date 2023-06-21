from models import TrainingConfiguration
from models.MobileNetV2Configuration import MobileNetV2Configuration
from models.SimpleConfiguration import SimpleConfiguration
from models.VggConfiguration import VggConfiguration
from models.XceptionConfiguration import XceptionConfiguration


class ConfigurationFactory:
    @staticmethod
    def get_configuration_by_name(name: str = "simple") -> TrainingConfiguration:
        configurations = []
        configurations.append(SimpleConfiguration())
        configurations.append(VggConfiguration())
        configurations.append(XceptionConfiguration())
        configurations.append(MobileNetV2Configuration())

        for i in range(len(configurations)):
            if configurations[i].name() == name:
                return configurations[i]

        raise Exception("No configuration found by name {0}".format(name))
