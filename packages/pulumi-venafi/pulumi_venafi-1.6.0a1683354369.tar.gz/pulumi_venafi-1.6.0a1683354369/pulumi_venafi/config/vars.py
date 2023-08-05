# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('venafi')


class _ExportableConfig(types.ModuleType):
    @property
    def access_token(self) -> Optional[str]:
        """
        Access token for TPP, user should use this for authentication
        """
        return __config__.get('accessToken')

    @property
    def api_key(self) -> Optional[str]:
        """
        API key for Venafi as a Service. Example: 142231b7-cvb0-412e-886b-6aeght0bc93d
        """
        return __config__.get('apiKey')

    @property
    def dev_mode(self) -> Optional[bool]:
        """
        When set to true, the resulting certificate will be issued by an ephemeral, no trust CA rather than enrolling using
        Venafi as a Service or Trust Protection Platform. Useful for development and testing.
        """
        return __config__.get_bool('devMode')

    @property
    def tpp_password(self) -> Optional[str]:
        """
        Password for WebSDK user. Example: password
        """
        return __config__.get('tppPassword')

    @property
    def tpp_username(self) -> Optional[str]:
        """
        WebSDK user for Venafi Platform. Example: admin
        """
        return __config__.get('tppUsername')

    @property
    def trust_bundle(self) -> Optional[str]:
        """
        Use to specify a PEM-formatted file that contains certificates to be trust anchors for all communications with the
        Venafi Web Service. Example: trust_bundle = "${file("chain.pem")}"
        """
        return __config__.get('trustBundle')

    @property
    def url(self) -> Optional[str]:
        """
        The Venafi Web Service URL.. Example: https://tpp.venafi.example/vedsdk
        """
        return __config__.get('url')

    @property
    def zone(self) -> Optional[str]:
        """
        DN of the Venafi Platform policy folder or name of the Venafi as a Service application. Example for Platform:
        testpolicy\\\\vault Example for Venafi as a Service: Default
        """
        return __config__.get('zone')

