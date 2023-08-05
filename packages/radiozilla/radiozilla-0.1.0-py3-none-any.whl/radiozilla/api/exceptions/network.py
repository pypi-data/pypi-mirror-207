""""""


class NetworkFailureException(Exception):
    """"""

    def __init__(self) -> None:
        self.message = "Network failure"

        super().__init__(self.message)