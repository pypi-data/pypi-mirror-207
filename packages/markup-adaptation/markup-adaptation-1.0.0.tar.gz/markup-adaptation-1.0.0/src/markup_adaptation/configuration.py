from .paths import get_path_value, set_path_value


class Configuration(object):

    @property
    def variable_scope(self):
        return self.variable_scope_

    @property
    def embed_images(self):
        return self.embed_images_

    def __init__(self):
        self.variable_scope_ = {}
        self.embed_images_ = False

    def get_variable(self, path, default_value=None):
        return get_path_value(path, self.variable_scope_, default_value, raise_on_undefined=False)


class EditableConfiguration(Configuration):

    @property
    def embed_images(self):
        return self.embed_images_

    @embed_images.setter
    def embed_images(self, value):
        self.embed_images_ = value

    def set_variable(self, path, value):
        set_path_value(path, value, self.variable_scope_, do_create_missing_scopes=True, do_create_variable=True)

