"""
v1 version apis
"""

from flask import current_app, request
from flask_restplus import Resource

from watch_together.apis import api, ns
from watch_together.utils.custom_exceptions import (
    PayloadParseError, InvalidPayloadError, MissingKeysError)
from watch_together.utils.payload_processing import (
    parse_payload, check_required_keys
)
from watch_together.utils.group_utils import create_group
from watch_together.utils.response import response


@ns.route('/create/group')
class CreateGroup(Resource):
    """
    API for group creation
    """
    @api.doc(False)
    def post(self):
        """
        Create Group
        Method: POST
        Sample payload:
            {
                "group_name": "",
                "start_time": "",
                "video_url": "",
                "users_list": []
            }
        """
        try:
            # Parse Payload
            payload = parse_payload(request)
            # Check required params
            check_required_keys(payload,
                                ["group_name", "video_url", "users_email"]
                                )
            # create group here
            create_group(payload)
        except (InvalidPayloadError, PayloadParseError,
                MissingKeysError) as err:
            current_app.logger.error(
                'POST: create group data error: %s' % err.to_dict()
            )
            return response(error_dict=err.to_dict())

        return response(data=payload)
