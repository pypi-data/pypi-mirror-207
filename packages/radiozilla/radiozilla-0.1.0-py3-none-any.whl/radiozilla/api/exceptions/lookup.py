""""""


class LookupException(Exception):
    """"""

    def __init__(self, ip: str) -> None:
        self.ip = ip
        self.message = f"There was an error with lookup for ip: {ip}"

        super().__init__(self.message)