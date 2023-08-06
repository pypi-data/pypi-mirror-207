
class AdaptationError(RuntimeError):
    pass


class UndefinedVariableScope(AdaptationError):
    def __init__(self, variable_path):
        super().__init__(variable_path)


class UndefinedVariable(AdaptationError):
    def __init__(self, variable_path):
        super().__init__(variable_path)


class UndefinedPath(AdaptationError):
    def __init__(self):
        super().__init__()
