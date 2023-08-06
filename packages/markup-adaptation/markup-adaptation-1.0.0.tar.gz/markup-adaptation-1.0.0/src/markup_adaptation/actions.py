
class ActionMixin(object):

    def __init__(self):
        pass

    def __call__(self, configuration, domain):
        pass


class ApplyToMixin(object):

    @property
    def query(self):
        return self.query_

    @query.setter
    def query(self, value):
        self.query_ = value

    def __init__(self):
        self.query_ = None


class Assign(ApplyToMixin, ActionMixin, object):

    @property
    def expression(self):
        return self.expression_

    @expression.setter
    def expression(self, value):
        self.expression_ = value

    def __init__(self):
        super().__init__()
        self.expression_ = None

    def __call__(self, configuration, domain):

        local_domain = self.query.apply_to(domain)

        for location in local_domain:
            location.set(self.expression_(configuration))


class Edit(ApplyToMixin, ActionMixin, object):

    @property
    def actions(self):
        return self.actions_[:]

    def __init__(self):
        super().__init__()
        self.actions_ = []

    def __call__(self, configuration, domain):

        local_domain = self.query.apply_to(domain)

        for action in self.actions_:
            action(configuration, local_domain)

    def add_action(self, action):
        self.actions_.append(action)
