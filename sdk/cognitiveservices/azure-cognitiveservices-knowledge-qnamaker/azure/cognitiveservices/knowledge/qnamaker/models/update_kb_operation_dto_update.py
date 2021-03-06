# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .update_kb_contents_dto import UpdateKbContentsDTO


class UpdateKbOperationDTOUpdate(UpdateKbContentsDTO):
    """An instance of UpdateKbContentsDTO for Update Operation.

    :param name: Friendly name for the knowledgebase.
    :type name: str
    :param qna_list: List of Q-A (UpdateQnaDTO) to be added to the
     knowledgebase.
    :type qna_list:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.UpdateQnaDTO]
    :param urls: List of existing URLs to be refreshed. The content will be
     extracted again and re-indexed.
    :type urls: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'qna_list': {'key': 'qnaList', 'type': '[UpdateQnaDTO]'},
        'urls': {'key': 'urls', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UpdateKbOperationDTOUpdate, self).__init__(**kwargs)
