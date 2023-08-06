# encoding: utf-8
"""
dtalarm.client
------------------

This module contains the create of Dtalarm' teams alarm.
"""
import requests
from plotly.graph_objs._figure import Figure
import mimetypes

from .base import BaseCli
from .config import DTAlarmConfig


class TeamsChannelAlarm(BaseCli):

    def __init__(self, secret_key=None, channel_address=None, template=None):
        super(TeamsChannelAlarm, self).__init__()
        self.secret_key = secret_key
        self.template = template
        self.channel_address = channel_address

    def _argsparser(self):
        """
        Parse the parameters assigned to the alarm object.

        The attribute in the images list must be a plotly figure object.
        :return:
        """

        for figure in self.images:
            if isinstance(figure, Figure) is False:
                raise Exception("Images should be a plotly graph object list.")

    def _gen_msgiv2(self):
        """
        Generate a request body with the teams channel template name message+image_v2.

        Detail:
        {
            "secret_key": "",
            "platform": "teams",
            "platform_subitem": "channel",
            "data": {
                "channel_URI": "",
                "template": "message+image_v2",
                "content": {
                    "alarm_title": "",
                    "alarm_type": "",
                    "image_base64": [],
                    "message_title": "",
                    "message_text": "",
                    "buttons": [],
                    "table": df.to_json()
                },
                "severity": 0,
                "additional_functions": [],
                "status_buttons": []
            }
        }
        :return:
        """
        self._argsparser()
        payload = {
            "secret_key": self.secret_key,
            "platform": "teams",
            "platform_subitem": "channel",
            "data": {
                "channel_URI": self.channel_address,
                "template": "message+image_v2",
                "content": {}
            }
        }

        # fill data.content
        if self.title:
            payload["data"]["content"]["alarm_title"] = self.title
        if self.message_title:
            payload["data"]["content"]["message_title"] = self.message_title
        if self.message_text:
            payload["data"]["content"]["message_text"] = self.message_text
        if self.images:
            images = self._compression_img(self.images)
            payload["data"]["content"]["image_base64"] = images
        if self.type:
            payload["data"]["content"]["alarm_type"] = self.type
        if self.buttons:
            payload["data"]["content"]["buttons"] = self.buttons
        if self.table:
            payload["data"]["content"]["table"] = self.table

        # fill data.*
        if self.severity is not None:
            payload["data"]["severity"] = self.severity
        if self.status_buttons:
            payload["data"]["status_buttons"] = self.status_buttons
        if self.additional_functions is not None:
            payload["data"]["additional_functions"] = self.additional_functions

        return payload

    def send(self, **kwargs):
        """
        :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        :return: :class:`Response <Response>` object
        """
        payload = self._gen_kwargs()
        kwargs.update({
            "json": payload
        })

        response = requests.post(DTAlarmConfig.SERVER, **kwargs)
        return response


class TeamsPersonalAlarm(BaseCli):

    def __init__(self, secret_key=None, accepter=None, template=None):
        super(TeamsPersonalAlarm, self).__init__()
        self.secret_key = secret_key
        self.template = template
        self.accepter = accepter

    def _argsparser(self):
        """
        Parse the parameters assigned to the alarm object.

        The attribute in the images list must be a plotly figure object.
        Aaccepter need to be a list, and the maximum number cannot exceed 10.
        :return:
        """

        if isinstance(self.accepter, list) is False:
            raise Exception("Accpter should be a list.")

        if len(self.accepter) > DTAlarmConfig.MAX_ACCEPTER or len(self.accepter) < 1:
            raise Exception("Accpter should have at least 1 person and at most 10 persons.")

        for figure in self.images:
            if isinstance(figure, Figure) is False:
                raise Exception("Images should be a plotly graph object list.")

    def _gen_msgiv2(self):
        """
        Generate a request body with the teams personal template name message+image_v2.

        Detail:
        {
            "secret_key": "",
            "platform": "teams",
            "platform_subitem": "personal",
            "data": {
                "accepter": "",
                "template": "message+image_v2",
                "content": {
                    "alarm_title": "",
                    "alarm_type": "",
                    "image_base64": [],
                    "message_title": "",
                    "message_text": "",
                    "buttons": [],
                    "table": df.to_json()
                },
                "severity": 0,
                "additional_functions": [],
                "status_buttons": []
            }
        }
        :return:
        """

        self._argsparser()
        payload = {
            "secret_key": self.secret_key,
            "platform": "teams",
            "platform_subitem": "personal",
            "data": {
                "accepter": self.accepter,
                "template": "message+image_v2",
                "content": {}
            }
        }

        # fill data.content
        if self.title:
            payload["data"]["content"]["alarm_title"] = self.title
        if self.message_title:
            payload["data"]["content"]["message_title"] = self.message_title
        if self.message_text:
            payload["data"]["content"]["message_text"] = self.message_text
        if self.images:
            images = self._compression_img(self.images)
            payload["data"]["content"]["image_base64"] = images
        if self.type:
            payload["data"]["content"]["alarm_type"] = self.type
        if self.buttons:
            payload["data"]["content"]["buttons"] = self.buttons
        if self.table:
            payload["data"]["content"]["table"] = self.table

        # fill data.*
        if self.severity is not None:
            payload["data"]["severity"] = self.severity
        if self.status_buttons:
            payload["data"]["status_buttons"] = self.status_buttons
        if self.additional_functions is not None:
            payload["data"]["additional_functions"] = self.additional_functions

        return payload

    def send(self, **kwargs):
        """
        :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        :return: :class:`Response <Response>` object
        """
        payload = self._gen_kwargs()
        kwargs.update({
            "json": payload
        })

        response = requests.post(DTAlarmConfig.SERVER, **kwargs)
        return response


class Alarm(BaseCli):

    def __init__(self, secret_key=None):
        super(Alarm, self).__init__()
        self.secret_key = secret_key

        self.table = None
        self.attachment = []
        self.attachment_from_file = []

    def _argsparser(self):
        """
        Parse the parameters assigned to the alarm object.

        The attribute in the images list must be a plotly figure object.
        Accepter need to be a list, and the maximum number cannot exceed 10.
        :return:
        """

        for figure in self.images:
            if isinstance(figure, Figure) is False:
                raise Exception("Images should be a plotly graph object list.")

    def attachment_upload(self, bytes_or_fp_buffer):
        """

        :param fp_bytes:
        :return:
        """
        files = {
            'file': bytes_or_fp_buffer
        }

        # obtain the DRIVE server address due to historical reasons...
        ServerAddress = DTAlarmConfig.SERVER.split('/alarm')[0]

        res = requests.post(f'{ServerAddress}{DTAlarmConfig.ATTACHMENT_UPLOAD_ROUTE}', files=files)

        if res.json()['status'] is not True:
            raise Exception(res.json())
        return res.json()["data"]["key"]

    def _attach_files(self) -> list:
        """
        Upload attachment and record the key meta information.

        :return: [{
                    "key": "s3 key",
                    "filename": ""
                }]
        """
        attachment_meta = []

        memory_meta = self._upload_attachment_from_memory()
        local_file_meta = self._upload_attachment_from_file()

        attachment_meta.extend(memory_meta)
        attachment_meta.extend(local_file_meta)

        return attachment_meta

    def _upload_attachment_from_memory(self) -> list:
        """
        Upload objects in memory.
        :return:
        """
        attachment_meta = []

        for dic in self.attachment:
            key = self.attachment_upload(dic["file"])

            attachment_meta.append({
                "key": key,
                "filename": dic.get("filename", key),
            })

        return attachment_meta

    def _upload_attachment_from_file(self) -> list:
        """
        Upload local file.
        :return:
        """
        attachment_meta = []

        for filename in self.attachment_from_file:
            fp = open(filename, 'rb')
            key = self.attachment_upload(fp)

            attachment_meta.append({
                "key": key,
                "filename": filename,
            })

        return attachment_meta

    def _gen_alarm_payload(self):
        """
        Generate a request body with the template message+image_v2.

        # New format of the Email alarm.
        {
            "secret_key": self.secret_key,
            "presetting": True,
            # "platform": "teams",
            # "platform_subitem": "personal",
            "data": {
                # "accepter": "",
                # "template": "message+image_v2",
                "content": {
                    "alarm_title": self.title,
                    "message_title": self.message_title,
                    "message_text": self.message_text,
                    "image_base64": [
                    ],
                    "buttons": self.buttons,
                    "table": self.table.to_json(),
                    "table_h5": self.table.to_html(),
                    "alarm_type": self.type,

                    "attachment": [{
                        "key": "",
                        "filename": ""
                    }]
                },
                "additional_functions": self.additional_functions,
                "status_buttons": self.status_buttons,
                "severity": self.severity
            }
        }

        :return:
        """

        self._argsparser()
        payload = {
            "secret_key": self.secret_key,
            "presetting": True,
            "data": {
                "content": {}
            }
        }

        # fill data.content
        if self.title:
            payload["data"]["content"]["alarm_title"] = self.title
        if self.message_title:
            payload["data"]["content"]["message_title"] = self.message_title
        if self.message_text:
            payload["data"]["content"]["message_text"] = self.message_text

        if self.images:
            images = self._compression_img(self.images)
            payload["data"]["content"]["image_base64"] = images

        if self.buttons:
            payload["data"]["content"]["buttons"] = self.buttons

        if self.table is not None:
            payload["data"]["content"]["table"] = self.table.to_json()
            payload["data"]["content"]["table_h5"] = self.table.to_html(index=False)

        if self.type:
            payload["data"]["content"]["alarm_type"] = self.type

        # add attachment information if any
        if self.attachment or self.attachment_from_file:
            attachment_meta = self._attach_files()
            payload["data"]["content"]["attachment"] = attachment_meta

        # fill data.*
        if self.severity is not None:
            payload["data"]["severity"] = self.severity
        if self.status_buttons:
            payload["data"]["status_buttons"] = self.status_buttons
        if self.additional_functions is not None:
            payload["data"]["additional_functions"] = self.additional_functions

        return payload

    def send(self, **kwargs):
        """
        :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        :return: :class:`Response <Response>` object
        """

        payload = self._gen_alarm_payload()
        kwargs.update({
            "json": payload
        })

        response = requests.post(DTAlarmConfig.SERVER, **kwargs)
        return response
