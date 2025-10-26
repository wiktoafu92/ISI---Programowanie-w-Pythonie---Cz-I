class HTTPError(Exception):
    def __init__(self, status_code: int, message: str = 'Błąd HTTP'):
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        return f'[{self.status_code}] {self.args[0]}'


class NotFoundError(HTTPError):
    def __init__(self):
        super().__init__(404, 'Nie znaleziono zasobu')


class AccessDeniedError(HTTPError):
    def __init__(self):
        super().__init__(403, 'Brak dostępu')
