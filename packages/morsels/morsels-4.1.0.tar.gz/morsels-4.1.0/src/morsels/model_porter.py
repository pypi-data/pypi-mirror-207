from model_porter.config import ModelPorterConfig

from .models import Morsel


def load_morsel(*, identifier):
    result = Morsel.objects.get(identifier=identifier)
    return result


class MorselsConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(MorselsConfig, self).__init__(app_label, module)
        self.register_function_action(load_morsel)
