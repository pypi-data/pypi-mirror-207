class I2AOauth2ClientException(Exception):

    def __init__(self, data, *args, **kwargs): # TODO: Refactor it, cus it overwrite message with data.
        super().__init__(*args, **kwargs)
        self.data = data

    def __str__(self):
        return str(self.data)

