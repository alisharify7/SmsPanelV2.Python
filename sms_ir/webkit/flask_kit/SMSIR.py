from flask import Flask
from flask_kit.exceptions import InvalidInstance, FlaskConfigMissing
from sms_ir.services import SmsIr


class DefaultValues:
    """ 
        Flask config default
    """
    FLASK_SMSIR_DEBUG=False
    FLASK_SMSIR_API_KEY=None
    FLASK_SMS_LINE_NUMBER=None




class flask_smsir(DefaultValues, SmsIr):
    """ 
    init Flask_SMSIR Class For App
    """

    def __init__(
                self,
                API_KEY : str = "",
                LINE_NUMBER : str = "",
                DEBUG : bool
        ) -> None:

        if API_KEY and LINE_NUMBER and DEBUG:
            self.API_KEY = API_KEY
            self.LINE_NUMBER = LINE_NUMBER
            self.DEBUG = DEBUG

            super().__init__(
                api_key = API_KEY,
                linenumber = LINE_NUMBER
            )
        

    def init_app(self, app: Flask = None):
        if app and not isinstance(app, Flask):
            raise InvalidInstance(f"app {type(app)} is not a flask.Flask instance!")
        
        if not app:
            raise ValueError("App is required")

        debug, api_key, linNumber = app.config.get("FLASK_SMSIR_DEBUG", None), app.config.get("FLASK_SMSIR_API_KEY", None), app.config.get("FLASK_SMS_LINE_NUMBER", None)

        if not isinstance(debug, bool):
            raise InvalidInstance("app.config[FLASK_SMSIR_DEBUG] must be a Boolean Value")

        if not api_key:
            raise FlaskConfigMissing('app.config[FLASK_SMSIR_API_KEY] is not set')

        if not linNumber:
            raise FlaskConfigMissing('app.config[FLASK_SMS_LINE_NUMBER] is not set')

        self.__init__(API_KEY=api_key, LINE_NUMBER=linNumber, DEBUG=debug)


