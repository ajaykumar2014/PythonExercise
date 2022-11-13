class BaseEmailService:
    def __init__(self):
        raise Exception('Could not send email')
        super().__init__()

    @staticmethod
    def sendEmail(toEmail: str, body: str) -> None:
        try:
            if not toEmail and not body:
                print(f'Sending Email done!')
            else:
                raise Exception('Email ID is not valid')
        except Exception as e:
            print(f'Exception {str(e)}')
