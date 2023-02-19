

class Move:

    def __init__(self, row: int, column: int, token: str):

        self._row = row
        self._column = column
        self._token = token

    @property
    def column(self):

        return self._column

    @property
    def row(self):

        return self._row

    @property
    def token(self):

        return self._token
