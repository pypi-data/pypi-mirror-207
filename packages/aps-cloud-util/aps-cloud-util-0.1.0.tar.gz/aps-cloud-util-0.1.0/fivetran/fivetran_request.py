from flask import Flask, request


class FivetranRequest:
    """Class that takes a flask request object and converts to a FivetranRequest object."""
    def __init__(self, five_tran_request: request):
        self.__flask_request = five_tran_request
        self.__json = five_tran_request.get_json()
        if self.__json.get("agent",None) is None:
            raise ValueError("Request does not appear to be from Fivetran.")
        self.agent = self.__json.get("agent").split("/")[0]
        self.external_id = self.__json.get("agent").split("/")[1]
        self.schema = self.__json.get("agent").split("/")[2]
        self.state = self.__json.get("state", None)
        self.secrets = self.__json.get("secrets", None)
        self.sync_id = self.__json.get("sync_id", None)
        self.config = self.secrets.get("config", None)
