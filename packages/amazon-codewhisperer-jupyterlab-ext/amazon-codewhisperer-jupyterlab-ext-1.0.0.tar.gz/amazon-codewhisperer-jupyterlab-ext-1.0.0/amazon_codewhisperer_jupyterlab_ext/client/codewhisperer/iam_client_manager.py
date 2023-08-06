from abc import ABC
import logging
from amazon_codewhisperer_jupyterlab_ext.client.codewhisperer.client_manager import CodeWhispererClientManager
from amazon_codewhisperer_jupyterlab_ext.constants import (
    REQUEST_OPTOUT_HEADER_NAME,
    RTS_PROD_ENDPOINT,
    RTS_PROD_REGION,
    SIGV4
)

logging.basicConfig(format="%(levelname)s: %(message)s")


class CodeWhispererIamClientManager(CodeWhispererClientManager, ABC):

    def __init__(self):
        super().__init__()
        self._client = self.session.client(
            service_name=SIGV4,
            endpoint_url=RTS_PROD_ENDPOINT,
            region_name=RTS_PROD_REGION,
            verify=False,
        )
        self._opt_out = False
        self._client.meta.events.register_first("before-sign.*.*", self._add_header)

    def _add_header(self, request, **kwargs):
        request.headers.add_header(REQUEST_OPTOUT_HEADER_NAME, f"{self._opt_out}")

    def invoke_recommendations(self, request, opt_out):
        self._opt_out = opt_out
        return self._client.generate_recommendations(**request)
