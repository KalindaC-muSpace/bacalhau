# coding: utf-8

"""
    Bacalhau API

    This page is the reference of the Bacalhau REST API. Project docs are available at https://docs.bacalhau.org/. Find more information about Bacalhau at https://github.com/filecoin-project/bacalhau.  # noqa: E501

    OpenAPI spec version: 0.3.18.post4
    Contact: team@bacalhau.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bacalhau_apiclient.configuration import Configuration


class Deal(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'concurrency': 'int',
        'confidence': 'int',
        'min_bids': 'int'
    }

    attribute_map = {
        'concurrency': 'Concurrency',
        'confidence': 'Confidence',
        'min_bids': 'MinBids'
    }

    def __init__(self, concurrency=None, confidence=None, min_bids=None, _configuration=None):  # noqa: E501
        """Deal - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._concurrency = None
        self._confidence = None
        self._min_bids = None
        self.discriminator = None

        if concurrency is not None:
            self.concurrency = concurrency
        if confidence is not None:
            self.confidence = confidence
        if min_bids is not None:
            self.min_bids = min_bids

    @property
    def concurrency(self):
        """Gets the concurrency of this Deal.  # noqa: E501

        The maximum number of concurrent compute node bids that will be accepted by the requester node on behalf of the client.  # noqa: E501

        :return: The concurrency of this Deal.  # noqa: E501
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this Deal.

        The maximum number of concurrent compute node bids that will be accepted by the requester node on behalf of the client.  # noqa: E501

        :param concurrency: The concurrency of this Deal.  # noqa: E501
        :type: int
        """

        self._concurrency = concurrency

    @property
    def confidence(self):
        """Gets the confidence of this Deal.  # noqa: E501

        The number of nodes that must agree on a verification result this is used by the different verifiers - for example the deterministic verifier requires the winning group size to be at least this size  # noqa: E501

        :return: The confidence of this Deal.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Deal.

        The number of nodes that must agree on a verification result this is used by the different verifiers - for example the deterministic verifier requires the winning group size to be at least this size  # noqa: E501

        :param confidence: The confidence of this Deal.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def min_bids(self):
        """Gets the min_bids of this Deal.  # noqa: E501

        The minimum number of bids that must be received before the Requester node will randomly accept concurrency-many of them. This allows the Requester node to get some level of guarantee that the execution of the jobs will be spread evenly across the network (assuming that this value is some large proportion of the size of the network).  # noqa: E501

        :return: The min_bids of this Deal.  # noqa: E501
        :rtype: int
        """
        return self._min_bids

    @min_bids.setter
    def min_bids(self, min_bids):
        """Sets the min_bids of this Deal.

        The minimum number of bids that must be received before the Requester node will randomly accept concurrency-many of them. This allows the Requester node to get some level of guarantee that the execution of the jobs will be spread evenly across the network (assuming that this value is some large proportion of the size of the network).  # noqa: E501

        :param min_bids: The min_bids of this Deal.  # noqa: E501
        :type: int
        """

        self._min_bids = min_bids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Deal, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Deal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Deal):
            return True

        return self.to_dict() != other.to_dict()