'''
# `azurerm_windows_web_app_slot`

Refer to the Terraform Registory for docs: [`azurerm_windows_web_app_slot`](https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class WindowsWebAppSlot(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlot",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot azurerm_windows_web_app_slot}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        app_service_id: builtins.str,
        name: builtins.str,
        site_config: typing.Union["WindowsWebAppSlotSiteConfig", typing.Dict[builtins.str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        auth_settings_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2", typing.Dict[builtins.str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union["WindowsWebAppSlotBackup", typing.Dict[builtins.str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_certificate_exclusion_paths: typing.Optional[builtins.str] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsWebAppSlotIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["WindowsWebAppSlotLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        service_plan_id: typing.Optional[builtins.str] = None,
        storage_account: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
        zip_deploy_file: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot azurerm_windows_web_app_slot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_service_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        :param auth_settings_v2: auth_settings_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings_v2 WindowsWebAppSlot#auth_settings_v2}
        :param backup: backup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.
        :param client_certificate_exclusion_paths: Paths to exclude when using client certificates, separated by ; Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_exclusion_paths WindowsWebAppSlot#client_certificate_exclusion_paths}
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#id WindowsWebAppSlot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        :param service_plan_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_plan_id WindowsWebAppSlot#service_plan_id}.
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tags WindowsWebAppSlot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ddd99522bfde6c5bc60be25b59ee4010853a70b7bb83e5d9bbb79a54001d42)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WindowsWebAppSlotConfig(
            app_service_id=app_service_id,
            name=name,
            site_config=site_config,
            app_settings=app_settings,
            auth_settings=auth_settings,
            auth_settings_v2=auth_settings_v2,
            backup=backup,
            client_affinity_enabled=client_affinity_enabled,
            client_certificate_enabled=client_certificate_enabled,
            client_certificate_exclusion_paths=client_certificate_exclusion_paths,
            client_certificate_mode=client_certificate_mode,
            connection_string=connection_string,
            enabled=enabled,
            https_only=https_only,
            id=id,
            identity=identity,
            key_vault_reference_identity_id=key_vault_reference_identity_id,
            logs=logs,
            service_plan_id=service_plan_id,
            storage_account=storage_account,
            tags=tags,
            timeouts=timeouts,
            virtual_network_subnet_id=virtual_network_subnet_id,
            zip_deploy_file=zip_deploy_file,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthSettings")
    def put_auth_settings(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        active_directory: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsActiveDirectory", typing.Dict[builtins.str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsFacebook", typing.Dict[builtins.str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGithub", typing.Dict[builtins.str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGoogle", typing.Dict[builtins.str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsMicrosoft", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsTwitter", typing.Dict[builtins.str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github WindowsWebAppSlot#github}
        :param google: google block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google WindowsWebAppSlot#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        value = WindowsWebAppSlotAuthSettings(
            enabled=enabled,
            active_directory=active_directory,
            additional_login_parameters=additional_login_parameters,
            allowed_external_redirect_urls=allowed_external_redirect_urls,
            default_provider=default_provider,
            facebook=facebook,
            github=github,
            google=google,
            issuer=issuer,
            microsoft=microsoft,
            runtime_version=runtime_version,
            token_refresh_extension_hours=token_refresh_extension_hours,
            token_store_enabled=token_store_enabled,
            twitter=twitter,
            unauthenticated_client_action=unauthenticated_client_action,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthSettings", [value]))

    @jsii.member(jsii_name="putAuthSettingsV2")
    def put_auth_settings_v2(
        self,
        *,
        login: typing.Union["WindowsWebAppSlotAuthSettingsV2Login", typing.Dict[builtins.str, typing.Any]],
        active_directory_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2", typing.Dict[builtins.str, typing.Any]]] = None,
        apple_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2AppleV2", typing.Dict[builtins.str, typing.Any]]] = None,
        auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        azure_static_web_app_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2", typing.Dict[builtins.str, typing.Any]]] = None,
        config_file_path: typing.Optional[builtins.str] = None,
        custom_oidc_v2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotAuthSettingsV2CustomOidcV2", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        excluded_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        facebook_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2FacebookV2", typing.Dict[builtins.str, typing.Any]]] = None,
        forward_proxy_convention: typing.Optional[builtins.str] = None,
        forward_proxy_custom_host_header_name: typing.Optional[builtins.str] = None,
        forward_proxy_custom_scheme_header_name: typing.Optional[builtins.str] = None,
        github_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2GithubV2", typing.Dict[builtins.str, typing.Any]]] = None,
        google_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2GoogleV2", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route_api_prefix: typing.Optional[builtins.str] = None,
        microsoft_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2MicrosoftV2", typing.Dict[builtins.str, typing.Any]]] = None,
        require_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        twitter_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2TwitterV2", typing.Dict[builtins.str, typing.Any]]] = None,
        unauthenticated_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param login: login block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login WindowsWebAppSlot#login}
        :param active_directory_v2: active_directory_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory_v2 WindowsWebAppSlot#active_directory_v2}
        :param apple_v2: apple_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#apple_v2 WindowsWebAppSlot#apple_v2}
        :param auth_enabled: Should the AuthV2 Settings be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_enabled WindowsWebAppSlot#auth_enabled}
        :param azure_static_web_app_v2: azure_static_web_app_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_static_web_app_v2 WindowsWebAppSlot#azure_static_web_app_v2}
        :param config_file_path: The path to the App Auth settings. **Note:** Relative Paths are evaluated from the Site Root directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#config_file_path WindowsWebAppSlot#config_file_path}
        :param custom_oidc_v2: custom_oidc_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_oidc_v2 WindowsWebAppSlot#custom_oidc_v2}
        :param default_provider: The Default Authentication Provider to use when the ``unauthenticated_action`` is set to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param excluded_paths: The paths which should be excluded from the ``unauthenticated_action`` when it is set to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#excluded_paths WindowsWebAppSlot#excluded_paths}
        :param facebook_v2: facebook_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook_v2 WindowsWebAppSlot#facebook_v2}
        :param forward_proxy_convention: The convention used to determine the url of the request made. Possible values include ``ForwardProxyConventionNoProxy``, ``ForwardProxyConventionStandard``, ``ForwardProxyConventionCustom``. Defaults to ``ForwardProxyConventionNoProxy`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_convention WindowsWebAppSlot#forward_proxy_convention}
        :param forward_proxy_custom_host_header_name: The name of the header containing the host of the request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_host_header_name WindowsWebAppSlot#forward_proxy_custom_host_header_name}
        :param forward_proxy_custom_scheme_header_name: The name of the header containing the scheme of the request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_scheme_header_name WindowsWebAppSlot#forward_proxy_custom_scheme_header_name}
        :param github_v2: github_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github_v2 WindowsWebAppSlot#github_v2}
        :param google_v2: google_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google_v2 WindowsWebAppSlot#google_v2}
        :param http_route_api_prefix: The prefix that should precede all the authentication and authorisation paths. Defaults to ``/.auth``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_route_api_prefix WindowsWebAppSlot#http_route_api_prefix}
        :param microsoft_v2: microsoft_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft_v2 WindowsWebAppSlot#microsoft_v2}
        :param require_authentication: Should the authentication flow be used for all requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_authentication WindowsWebAppSlot#require_authentication}
        :param require_https: Should HTTPS be required on connections? Defaults to true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_https WindowsWebAppSlot#require_https}
        :param runtime_version: The Runtime Version of the Authentication and Authorisation feature of this App. Defaults to ``~1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param twitter_v2: twitter_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter_v2 WindowsWebAppSlot#twitter_v2}
        :param unauthenticated_action: The action to take for requests made without authentication. Possible values include ``RedirectToLoginPage``, ``AllowAnonymous``, ``Return401``, and ``Return403``. Defaults to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_action WindowsWebAppSlot#unauthenticated_action}
        '''
        value = WindowsWebAppSlotAuthSettingsV2(
            login=login,
            active_directory_v2=active_directory_v2,
            apple_v2=apple_v2,
            auth_enabled=auth_enabled,
            azure_static_web_app_v2=azure_static_web_app_v2,
            config_file_path=config_file_path,
            custom_oidc_v2=custom_oidc_v2,
            default_provider=default_provider,
            excluded_paths=excluded_paths,
            facebook_v2=facebook_v2,
            forward_proxy_convention=forward_proxy_convention,
            forward_proxy_custom_host_header_name=forward_proxy_custom_host_header_name,
            forward_proxy_custom_scheme_header_name=forward_proxy_custom_scheme_header_name,
            github_v2=github_v2,
            google_v2=google_v2,
            http_route_api_prefix=http_route_api_prefix,
            microsoft_v2=microsoft_v2,
            require_authentication=require_authentication,
            require_https=require_https,
            runtime_version=runtime_version,
            twitter_v2=twitter_v2,
            unauthenticated_action=unauthenticated_action,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthSettingsV2", [value]))

    @jsii.member(jsii_name="putBackup")
    def put_backup(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["WindowsWebAppSlotBackupSchedule", typing.Dict[builtins.str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        value = WindowsWebAppSlotBackup(
            name=name,
            schedule=schedule,
            storage_account_url=storage_account_url,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putConnectionString")
    def put_connection_string(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4eed8de5e1f235bbe89a43eaf4c70ba4cc7a8e366c1718580459a49078a2a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConnectionString", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.
        '''
        value = WindowsWebAppSlotIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putLogs")
    def put_logs(
        self,
        *,
        application_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogs", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        value = WindowsWebAppSlotLogs(
            application_logs=application_logs,
            detailed_error_messages=detailed_error_messages,
            failed_request_tracing=failed_request_tracing,
            http_logs=http_logs,
        )

        return typing.cast(None, jsii.invoke(self, "putLogs", [value]))

    @jsii.member(jsii_name="putSiteConfig")
    def put_site_config(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigApplicationStack", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSetting", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_swap_slot_name: typing.Optional[builtins.str] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cors: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigCors", typing.Dict[builtins.str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestriction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        virtual_application: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        :param auto_swap_slot_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.
        :param ip_restriction: ip_restriction block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.
        :param scm_ip_restriction: scm_ip_restriction block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.
        :param virtual_application: virtual_application block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.
        '''
        value = WindowsWebAppSlotSiteConfig(
            always_on=always_on,
            api_definition_url=api_definition_url,
            api_management_api_id=api_management_api_id,
            app_command_line=app_command_line,
            application_stack=application_stack,
            auto_heal_enabled=auto_heal_enabled,
            auto_heal_setting=auto_heal_setting,
            auto_swap_slot_name=auto_swap_slot_name,
            container_registry_managed_identity_client_id=container_registry_managed_identity_client_id,
            container_registry_use_managed_identity=container_registry_use_managed_identity,
            cors=cors,
            default_documents=default_documents,
            ftps_state=ftps_state,
            health_check_eviction_time_in_min=health_check_eviction_time_in_min,
            health_check_path=health_check_path,
            http2_enabled=http2_enabled,
            ip_restriction=ip_restriction,
            load_balancing_mode=load_balancing_mode,
            local_mysql_enabled=local_mysql_enabled,
            managed_pipeline_mode=managed_pipeline_mode,
            minimum_tls_version=minimum_tls_version,
            remote_debugging_enabled=remote_debugging_enabled,
            remote_debugging_version=remote_debugging_version,
            scm_ip_restriction=scm_ip_restriction,
            scm_minimum_tls_version=scm_minimum_tls_version,
            scm_use_main_ip_restriction=scm_use_main_ip_restriction,
            use32_bit_worker=use32_bit_worker,
            virtual_application=virtual_application,
            vnet_route_all_enabled=vnet_route_all_enabled,
            websockets_enabled=websockets_enabled,
            worker_count=worker_count,
        )

        return typing.cast(None, jsii.invoke(self, "putSiteConfig", [value]))

    @jsii.member(jsii_name="putStorageAccount")
    def put_storage_account(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08bdec799d80ac734028040beb76e6a2bed953d161f5945628cca2e0dd75a5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageAccount", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#create WindowsWebAppSlot#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#delete WindowsWebAppSlot#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#read WindowsWebAppSlot#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#update WindowsWebAppSlot#update}.
        '''
        value = WindowsWebAppSlotTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAppSettings")
    def reset_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSettings", []))

    @jsii.member(jsii_name="resetAuthSettings")
    def reset_auth_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSettings", []))

    @jsii.member(jsii_name="resetAuthSettingsV2")
    def reset_auth_settings_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSettingsV2", []))

    @jsii.member(jsii_name="resetBackup")
    def reset_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackup", []))

    @jsii.member(jsii_name="resetClientAffinityEnabled")
    def reset_client_affinity_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAffinityEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateEnabled")
    def reset_client_certificate_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateEnabled", []))

    @jsii.member(jsii_name="resetClientCertificateExclusionPaths")
    def reset_client_certificate_exclusion_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateExclusionPaths", []))

    @jsii.member(jsii_name="resetClientCertificateMode")
    def reset_client_certificate_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateMode", []))

    @jsii.member(jsii_name="resetConnectionString")
    def reset_connection_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionString", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHttpsOnly")
    def reset_https_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetKeyVaultReferenceIdentityId")
    def reset_key_vault_reference_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultReferenceIdentityId", []))

    @jsii.member(jsii_name="resetLogs")
    def reset_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogs", []))

    @jsii.member(jsii_name="resetServicePlanId")
    def reset_service_plan_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePlanId", []))

    @jsii.member(jsii_name="resetStorageAccount")
    def reset_storage_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccount", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @jsii.member(jsii_name="resetZipDeployFile")
    def reset_zip_deploy_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZipDeployFile", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authSettings")
    def auth_settings(self) -> "WindowsWebAppSlotAuthSettingsOutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsOutputReference", jsii.get(self, "authSettings"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsV2")
    def auth_settings_v2(self) -> "WindowsWebAppSlotAuthSettingsV2OutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsV2OutputReference", jsii.get(self, "authSettingsV2"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "WindowsWebAppSlotBackupOutputReference":
        return typing.cast("WindowsWebAppSlotBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> "WindowsWebAppSlotConnectionStringList":
        return typing.cast("WindowsWebAppSlotConnectionStringList", jsii.get(self, "connectionString"))

    @builtins.property
    @jsii.member(jsii_name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomainVerificationId"))

    @builtins.property
    @jsii.member(jsii_name="defaultHostname")
    def default_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultHostname"))

    @builtins.property
    @jsii.member(jsii_name="hostingEnvironmentId")
    def hosting_environment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostingEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "WindowsWebAppSlotIdentityOutputReference":
        return typing.cast("WindowsWebAppSlotIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> "WindowsWebAppSlotLogsOutputReference":
        return typing.cast("WindowsWebAppSlotLogsOutputReference", jsii.get(self, "logs"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="outboundIpAddressList")
    def outbound_ip_address_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "outboundIpAddressList"))

    @builtins.property
    @jsii.member(jsii_name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "possibleOutboundIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="possibleOutboundIpAddressList")
    def possible_outbound_ip_address_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "possibleOutboundIpAddressList"))

    @builtins.property
    @jsii.member(jsii_name="siteConfig")
    def site_config(self) -> "WindowsWebAppSlotSiteConfigOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigOutputReference", jsii.get(self, "siteConfig"))

    @builtins.property
    @jsii.member(jsii_name="siteCredential")
    def site_credential(self) -> "WindowsWebAppSlotSiteCredentialList":
        return typing.cast("WindowsWebAppSlotSiteCredentialList", jsii.get(self, "siteCredential"))

    @builtins.property
    @jsii.member(jsii_name="storageAccount")
    def storage_account(self) -> "WindowsWebAppSlotStorageAccountList":
        return typing.cast("WindowsWebAppSlotStorageAccountList", jsii.get(self, "storageAccount"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WindowsWebAppSlotTimeoutsOutputReference":
        return typing.cast("WindowsWebAppSlotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="appServiceIdInput")
    def app_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSettingsInput")
    def app_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "appSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsInput")
    def auth_settings_input(self) -> typing.Optional["WindowsWebAppSlotAuthSettings"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettings"], jsii.get(self, "authSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="authSettingsV2Input")
    def auth_settings_v2_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2"], jsii.get(self, "authSettingsV2Input"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["WindowsWebAppSlotBackup"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotBackup"], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAffinityEnabledInput")
    def client_affinity_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientAffinityEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabledInput")
    def client_certificate_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clientCertificateEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateExclusionPathsInput")
    def client_certificate_exclusion_paths_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateExclusionPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateModeInput")
    def client_certificate_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateModeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionStringInput")
    def connection_string_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]], jsii.get(self, "connectionStringInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsOnlyInput")
    def https_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "httpsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["WindowsWebAppSlotIdentity"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityIdInput")
    def key_vault_reference_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultReferenceIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInput")
    def logs_input(self) -> typing.Optional["WindowsWebAppSlotLogs"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotLogs"], jsii.get(self, "logsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePlanIdInput")
    def service_plan_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePlanIdInput"))

    @builtins.property
    @jsii.member(jsii_name="siteConfigInput")
    def site_config_input(self) -> typing.Optional["WindowsWebAppSlotSiteConfig"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfig"], jsii.get(self, "siteConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountInput")
    def storage_account_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]], jsii.get(self, "storageAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="zipDeployFileInput")
    def zip_deploy_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zipDeployFileInput"))

    @builtins.property
    @jsii.member(jsii_name="appServiceId")
    def app_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appServiceId"))

    @app_service_id.setter
    def app_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a029239dc53304a99ba881342b6dfc3fbca9ca02af1e57469ae33d96fd5023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="appSettings")
    def app_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "appSettings"))

    @app_settings.setter
    def app_settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94ad378f16bac67ab6bf9605ded3dda132aeb4f2f33762e23428a778317778c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSettings", value)

    @builtins.property
    @jsii.member(jsii_name="clientAffinityEnabled")
    def client_affinity_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "clientAffinityEnabled"))

    @client_affinity_enabled.setter
    def client_affinity_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0ec27cfc15cfc90031ce83eda8c427714b35c7abb51f84a08f9948b780ff1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAffinityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabled")
    def client_certificate_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "clientCertificateEnabled"))

    @client_certificate_enabled.setter
    def client_certificate_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e24ec14a5703c54e3a7e4425e258d1245fd3fed982ab84944d217b366683e8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateExclusionPaths")
    def client_certificate_exclusion_paths(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateExclusionPaths"))

    @client_certificate_exclusion_paths.setter
    def client_certificate_exclusion_paths(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf28c0023e4468181f0a42e5e56fbae3f2bfc34dd64f88ea4cad7d5713c4206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateExclusionPaths", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateMode")
    def client_certificate_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCertificateMode"))

    @client_certificate_mode.setter
    def client_certificate_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf2cf019814029ad51efe32299138233b9bd59e0df2548216ecac6aef02115ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79aad3add9fb3d9d4e213ea7abe359455bda185b23005937e7cc3c3a8350ff2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpsOnly")
    def https_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "httpsOnly"))

    @https_only.setter
    def https_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa499da99b7c6df7e783ec1eac60314ad45be717f44423f0a748c30326468932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11826114989e5ff2c8e1caefab935d70243bfccfcc6ac0d37b86bc5cf2f7df70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultReferenceIdentityId")
    def key_vault_reference_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultReferenceIdentityId"))

    @key_vault_reference_identity_id.setter
    def key_vault_reference_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec2ef5fada5887ed6b4306c81d2ace3ee5d01c6961333f1edf220d9c9d902ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultReferenceIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b443a4f2710131e2ef520657a4d853230612b40cbb9a7c85a942d0463311d467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="servicePlanId")
    def service_plan_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePlanId"))

    @service_plan_id.setter
    def service_plan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__359f08939091be0ba2c15eac57a97f979cdb4c0bf1e176f29ca1ad95a61b5f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePlanId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e6b5c63b8c681792bb85075853c8e3bacf98659a58c9a8f041923eb3acb09f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b793dea2ea9f15d2199130fdea7188a76ebd330e3693673aa473b61b5ad26c0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="zipDeployFile")
    def zip_deploy_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zipDeployFile"))

    @zip_deploy_file.setter
    def zip_deploy_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a3cee88ef2c0f7903d6124de73c7132ff600b5c0fefb28352007a15bcf4d25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zipDeployFile", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "active_directory": "activeDirectory",
        "additional_login_parameters": "additionalLoginParameters",
        "allowed_external_redirect_urls": "allowedExternalRedirectUrls",
        "default_provider": "defaultProvider",
        "facebook": "facebook",
        "github": "github",
        "google": "google",
        "issuer": "issuer",
        "microsoft": "microsoft",
        "runtime_version": "runtimeVersion",
        "token_refresh_extension_hours": "tokenRefreshExtensionHours",
        "token_store_enabled": "tokenStoreEnabled",
        "twitter": "twitter",
        "unauthenticated_client_action": "unauthenticatedClientAction",
    },
)
class WindowsWebAppSlotAuthSettings:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        active_directory: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsActiveDirectory", typing.Dict[builtins.str, typing.Any]]] = None,
        additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        facebook: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsFacebook", typing.Dict[builtins.str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGithub", typing.Dict[builtins.str, typing.Any]]] = None,
        google: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsGoogle", typing.Dict[builtins.str, typing.Any]]] = None,
        issuer: typing.Optional[builtins.str] = None,
        microsoft: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsMicrosoft", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        twitter: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsTwitter", typing.Dict[builtins.str, typing.Any]]] = None,
        unauthenticated_client_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Should the Authentication / Authorization feature be enabled? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        :param active_directory: active_directory block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        :param additional_login_parameters: Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        :param allowed_external_redirect_urls: Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param default_provider: The default authentication provider to use when multiple providers are configured. Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param facebook: facebook block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        :param github: github block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github WindowsWebAppSlot#github}
        :param google: google block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google WindowsWebAppSlot#google}
        :param issuer: The OpenID Connect Issuer URI that represents the entity which issues access tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        :param microsoft: microsoft block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        :param runtime_version: The RuntimeVersion of the Authentication / Authorization feature in use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param token_refresh_extension_hours: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        :param token_store_enabled: Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param twitter: twitter block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        :param unauthenticated_client_action: The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        if isinstance(active_directory, dict):
            active_directory = WindowsWebAppSlotAuthSettingsActiveDirectory(**active_directory)
        if isinstance(facebook, dict):
            facebook = WindowsWebAppSlotAuthSettingsFacebook(**facebook)
        if isinstance(github, dict):
            github = WindowsWebAppSlotAuthSettingsGithub(**github)
        if isinstance(google, dict):
            google = WindowsWebAppSlotAuthSettingsGoogle(**google)
        if isinstance(microsoft, dict):
            microsoft = WindowsWebAppSlotAuthSettingsMicrosoft(**microsoft)
        if isinstance(twitter, dict):
            twitter = WindowsWebAppSlotAuthSettingsTwitter(**twitter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3707bd7e3fca64e5e38479177f06ea1beead785566d51b0106177ac84c1946)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument active_directory", value=active_directory, expected_type=type_hints["active_directory"])
            check_type(argname="argument additional_login_parameters", value=additional_login_parameters, expected_type=type_hints["additional_login_parameters"])
            check_type(argname="argument allowed_external_redirect_urls", value=allowed_external_redirect_urls, expected_type=type_hints["allowed_external_redirect_urls"])
            check_type(argname="argument default_provider", value=default_provider, expected_type=type_hints["default_provider"])
            check_type(argname="argument facebook", value=facebook, expected_type=type_hints["facebook"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument google", value=google, expected_type=type_hints["google"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument microsoft", value=microsoft, expected_type=type_hints["microsoft"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument token_refresh_extension_hours", value=token_refresh_extension_hours, expected_type=type_hints["token_refresh_extension_hours"])
            check_type(argname="argument token_store_enabled", value=token_store_enabled, expected_type=type_hints["token_store_enabled"])
            check_type(argname="argument twitter", value=twitter, expected_type=type_hints["twitter"])
            check_type(argname="argument unauthenticated_client_action", value=unauthenticated_client_action, expected_type=type_hints["unauthenticated_client_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if active_directory is not None:
            self._values["active_directory"] = active_directory
        if additional_login_parameters is not None:
            self._values["additional_login_parameters"] = additional_login_parameters
        if allowed_external_redirect_urls is not None:
            self._values["allowed_external_redirect_urls"] = allowed_external_redirect_urls
        if default_provider is not None:
            self._values["default_provider"] = default_provider
        if facebook is not None:
            self._values["facebook"] = facebook
        if github is not None:
            self._values["github"] = github
        if google is not None:
            self._values["google"] = google
        if issuer is not None:
            self._values["issuer"] = issuer
        if microsoft is not None:
            self._values["microsoft"] = microsoft
        if runtime_version is not None:
            self._values["runtime_version"] = runtime_version
        if token_refresh_extension_hours is not None:
            self._values["token_refresh_extension_hours"] = token_refresh_extension_hours
        if token_store_enabled is not None:
            self._values["token_store_enabled"] = token_store_enabled
        if twitter is not None:
            self._values["twitter"] = twitter
        if unauthenticated_client_action is not None:
            self._values["unauthenticated_client_action"] = unauthenticated_client_action

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Should the Authentication / Authorization feature be enabled?

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def active_directory(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsActiveDirectory"]:
        '''active_directory block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory WindowsWebAppSlot#active_directory}
        '''
        result = self._values.get("active_directory")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsActiveDirectory"], result)

    @builtins.property
    def additional_login_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies a map of Login Parameters to send to the OpenID Connect authorization endpoint when a user logs in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#additional_login_parameters WindowsWebAppSlot#additional_login_parameters}
        '''
        result = self._values.get("additional_login_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def allowed_external_redirect_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of External URLs that can be redirected to as part of logging in or logging out of the Windows Web App.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        '''
        result = self._values.get("allowed_external_redirect_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_provider(self) -> typing.Optional[builtins.str]:
        '''The default authentication provider to use when multiple providers are configured.

        Possible values include: ``AzureActiveDirectory``, ``Facebook``, ``Google``, ``MicrosoftAccount``, ``Twitter``, ``Github``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        '''
        result = self._values.get("default_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def facebook(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsFacebook"]:
        '''facebook block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook WindowsWebAppSlot#facebook}
        '''
        result = self._values.get("facebook")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsFacebook"], result)

    @builtins.property
    def github(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github WindowsWebAppSlot#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsGithub"], result)

    @builtins.property
    def google(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsGoogle"]:
        '''google block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google WindowsWebAppSlot#google}
        '''
        result = self._values.get("google")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsGoogle"], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''The OpenID Connect Issuer URI that represents the entity which issues access tokens.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#issuer WindowsWebAppSlot#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsMicrosoft"]:
        '''microsoft block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft WindowsWebAppSlot#microsoft}
        '''
        result = self._values.get("microsoft")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsMicrosoft"], result)

    @builtins.property
    def runtime_version(self) -> typing.Optional[builtins.str]:
        '''The RuntimeVersion of the Authentication / Authorization feature in use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        '''
        result = self._values.get("runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_refresh_extension_hours(self) -> typing.Optional[jsii.Number]:
        '''The number of hours after session token expiration that a session token can be used to call the token refresh API.

        Defaults to ``72`` hours.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_hours WindowsWebAppSlot#token_refresh_extension_hours}
        '''
        result = self._values.get("token_refresh_extension_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_store_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the Windows Web App durably store platform-specific security tokens that are obtained during login flows? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        '''
        result = self._values.get("token_store_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def twitter(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"]:
        '''twitter block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter WindowsWebAppSlot#twitter}
        '''
        result = self._values.get("twitter")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"], result)

    @builtins.property
    def unauthenticated_client_action(self) -> typing.Optional[builtins.str]:
        '''The action to take when an unauthenticated client attempts to access the app. Possible values include: ``RedirectToLoginPage``, ``AllowAnonymous``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_client_action WindowsWebAppSlot#unauthenticated_client_action}
        '''
        result = self._values.get("unauthenticated_client_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsActiveDirectory",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "allowed_audiences": "allowedAudiences",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsActiveDirectory:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868bcbff896a41ff3890f6b0d0601b2f1a303fb12bc3e577e43d2d849d9daf86)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the Client to use to authenticate with Azure Active Directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsActiveDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed289310ecff6c955de81db5153b619f7caa14d4f75fb4098eba7fc547b3e451)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2ce9c0bbccece442b7a83e96eeef0d61d5a23182f21bd748b2878bd4135229)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43b29d40be4746b425c09e0d4bf0dfc26f4b95b119632005ff873581a85d490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24e62a1ac05668fa288a2c1b72a1be047eb4175210533602acf5af53b58f1653)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189f910e3b91b348ac33b19d7a80645a20ccfd7ee33f34d645960d370c876e20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9898f499a466a1c3b0c31ec6d099f3595e2727fb6f583ee9bbcd5b9ff6ea996c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsFacebook",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "app_secret": "appSecret",
        "app_secret_setting_name": "appSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsFacebook:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca9f25873d1e129b0ae705e1dce0ff35833907fb6fe72fe5567e5daea47b0ee)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument app_secret", value=app_secret, expected_type=type_hints["app_secret"])
            check_type(argname="argument app_secret_setting_name", value=app_secret_setting_name, expected_type=type_hints["app_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
        }
        if app_secret is not None:
            self._values["app_secret"] = app_secret
        if app_secret_setting_name is not None:
            self._values["app_secret_setting_name"] = app_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The App ID of the Facebook app used for login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_secret(self) -> typing.Optional[builtins.str]:
        '''The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        '''
        result = self._values.get("app_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        '''
        result = self._values.get("app_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsFacebook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsFacebookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsFacebookOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8e9add771a8a85989b1aeed94b740a3f6342ed4eb48a5b19255bc293b54fc95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAppSecret")
    def reset_app_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSecret", []))

    @jsii.member(jsii_name="resetAppSecretSettingName")
    def reset_app_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="appIdInput")
    def app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecretInput")
    def app_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingNameInput")
    def app_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f955dc7abfd911398f0ba03d070fabdb282ae521987bd57ad94585019aeb999f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="appSecret")
    def app_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecret"))

    @app_secret.setter
    def app_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__342c2ce6f2e2f28abdf8fff1781671e757400f423851a112cabd5924444dbb10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecret", value)

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingName")
    def app_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecretSettingName"))

    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f5689e7a343f2bf6bcb2c1a579308869ed54345f72d962ce89bc95a2a38106)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53358f627d3237750f6c6543c7309d497060bc0498e21351987b4efc4478effa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsFacebook]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsFacebook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsFacebook],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd16bb15c55c7d93a42e8337589a8c62239d35949574ea9dafb711453f96e6c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGithub",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsGithub:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e08b71235b42267cc6710c8859abb40328e4aefd175d880b63548b0a35402eb1)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the GitHub app used for login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsGithubOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGithubOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958385d0779e84ef976cc8f93ef614e046da13040cd3213a4d801489a62e9ebb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fbe5ff91489ac2f9a5ea9a9d012f8a963bd1a730c3dac489ab60a86377b1ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95da73fc61f3e60daa462919be59d2d1e1aca04d1a961d90b89d14b009217cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eace5adb99fb1e404287ba5710925293c8c234ce25581515028133812fa58f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb3c2c9b1eb55b3b37731dfe29fcb8e94d1383024318489fa5294e7a651cade1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGithub]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsGithub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7c46688222b0d5eddf4f3f4429f5d6c28d92ca87b2177aa9adc725ec6bfcd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGoogle",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsGoogle:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fc9456e5a2b99d9c9d5fa404d92dc48d3a36b1907f11626586d013d237fe11)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OpenID Connect Client ID for the Google web application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The client secret associated with the Google web application.  Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsGoogle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsGoogleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsGoogleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed29c3a27bddbc446426ecb6d7dca0df18515e01370f96d03feba8b4c8cf7b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda8a5ccef6453e903afbc63eee6965db1805bf60874a470a9313063b22f0531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8dabeae006496ca4deb7d5dbc56a381201a14488e980d5d73016559b77992f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f77e0f15bebc554d3feda2ae8cd56b81d556d9b51c70af883a8d8bff63d1dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7de0137cdeeeb6751f9acd8454c3d47824abf70102402ae2f2df339bdaa6d033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGoogle]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGoogle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsGoogle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca92677b504b665e9d813011fba7af2fb92d671f5e6a7164f090a01f001604f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsMicrosoft",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_setting_name": "clientSecretSettingName",
        "oauth_scopes": "oauthScopes",
    },
)
class WindowsWebAppSlotAuthSettingsMicrosoft:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7642d3c6eb8db232d8f86a85763b579dd7bc58cb0f5c5c7065696673e9c569)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OAuth 2.0 client ID that was created for the app used for authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsMicrosoft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsMicrosoftOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsMicrosoftOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c356a1dd04e2858ce3c979247edadd6b8002277976fad1313767d7350718bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8898984aaa845b60b7c4728d9cc1e29e1f02674bdeb277a34e4edd5fe1b75f6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822673928abaf834d2bd34c53e947a4ede76f9bb62107aafa9f6e8af30e2ca2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__039ac8b50caad86d2c52b9338304deb24f7a91eec29aa0a282d8451f19cf08d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__007ca8cb3ccde7773ba5cc3799e8a5101e06ced17d262e3c012a17f5bc90f257)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83fc4c8c5e645b9dcd9d60680dd8d41ea6e68b3ecceb6520acabe9d51c249eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotAuthSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b15be9e2db1b6e4c7275431eb30d674c0b3ad1ad2c4df36bfa0bbfd84f95ba3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectory")
    def put_active_directory(
        self,
        *,
        client_id: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param client_secret: The Client Secret for the Client ID. Cannot be used with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Cannot be used with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsActiveDirectory(
            client_id=client_id,
            allowed_audiences=allowed_audiences,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectory", [value]))

    @jsii.member(jsii_name="putFacebook")
    def put_facebook(
        self,
        *,
        app_id: builtins.str,
        app_secret: typing.Optional[builtins.str] = None,
        app_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret: The App Secret of the Facebook app used for Facebook Login. Cannot be specified with ``app_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret WindowsWebAppSlot#app_secret}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Cannot be specified with ``app_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsFacebook(
            app_id=app_id,
            app_secret=app_secret,
            app_secret_setting_name=app_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putFacebook", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The Client Secret of the GitHub app used for GitHub Login. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsGithub(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGoogle")
    def put_google(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The client secret associated with the Google web application. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. If not specified, "openid", "profile", and "email" are used as default scopes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsGoogle(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGoogle", [value]))

    @jsii.member(jsii_name="putMicrosoft")
    def put_microsoft(
        self,
        *,
        client_id: builtins.str,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret: The OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret WindowsWebAppSlot#client_secret}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Cannot be specified with ``client_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param oauth_scopes: The list of OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. If not specified, ``wl.basic`` is used as the default scope. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#oauth_scopes WindowsWebAppSlot#oauth_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsMicrosoft(
            client_id=client_id,
            client_secret=client_secret,
            client_secret_setting_name=client_secret_setting_name,
            oauth_scopes=oauth_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putMicrosoft", [value]))

    @jsii.member(jsii_name="putTwitter")
    def put_twitter(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsTwitter(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            consumer_secret_setting_name=consumer_secret_setting_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTwitter", [value]))

    @jsii.member(jsii_name="resetActiveDirectory")
    def reset_active_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectory", []))

    @jsii.member(jsii_name="resetAdditionalLoginParameters")
    def reset_additional_login_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalLoginParameters", []))

    @jsii.member(jsii_name="resetAllowedExternalRedirectUrls")
    def reset_allowed_external_redirect_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExternalRedirectUrls", []))

    @jsii.member(jsii_name="resetDefaultProvider")
    def reset_default_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultProvider", []))

    @jsii.member(jsii_name="resetFacebook")
    def reset_facebook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacebook", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGoogle")
    def reset_google(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogle", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetMicrosoft")
    def reset_microsoft(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoft", []))

    @jsii.member(jsii_name="resetRuntimeVersion")
    def reset_runtime_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeVersion", []))

    @jsii.member(jsii_name="resetTokenRefreshExtensionHours")
    def reset_token_refresh_extension_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenRefreshExtensionHours", []))

    @jsii.member(jsii_name="resetTokenStoreEnabled")
    def reset_token_store_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenStoreEnabled", []))

    @jsii.member(jsii_name="resetTwitter")
    def reset_twitter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTwitter", []))

    @jsii.member(jsii_name="resetUnauthenticatedClientAction")
    def reset_unauthenticated_client_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnauthenticatedClientAction", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectory")
    def active_directory(
        self,
    ) -> WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference, jsii.get(self, "activeDirectory"))

    @builtins.property
    @jsii.member(jsii_name="facebook")
    def facebook(self) -> WindowsWebAppSlotAuthSettingsFacebookOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsFacebookOutputReference, jsii.get(self, "facebook"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> WindowsWebAppSlotAuthSettingsGithubOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="google")
    def google(self) -> WindowsWebAppSlotAuthSettingsGoogleOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsGoogleOutputReference, jsii.get(self, "google"))

    @builtins.property
    @jsii.member(jsii_name="microsoft")
    def microsoft(self) -> WindowsWebAppSlotAuthSettingsMicrosoftOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsMicrosoftOutputReference, jsii.get(self, "microsoft"))

    @builtins.property
    @jsii.member(jsii_name="twitter")
    def twitter(self) -> "WindowsWebAppSlotAuthSettingsTwitterOutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsTwitterOutputReference", jsii.get(self, "twitter"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryInput")
    def active_directory_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory], jsii.get(self, "activeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalLoginParametersInput")
    def additional_login_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalLoginParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrlsInput")
    def allowed_external_redirect_urls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedExternalRedirectUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultProviderInput")
    def default_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="facebookInput")
    def facebook_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsFacebook]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsFacebook], jsii.get(self, "facebookInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGithub]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="googleInput")
    def google_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsGoogle]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsGoogle], jsii.get(self, "googleInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftInput")
    def microsoft_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft], jsii.get(self, "microsoftInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeVersionInput")
    def runtime_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHoursInput")
    def token_refresh_extension_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenRefreshExtensionHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabledInput")
    def token_store_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tokenStoreEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="twitterInput")
    def twitter_input(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsTwitter"], jsii.get(self, "twitterInput"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientActionInput")
    def unauthenticated_client_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unauthenticatedClientActionInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalLoginParameters")
    def additional_login_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalLoginParameters"))

    @additional_login_parameters.setter
    def additional_login_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17e6c60d7cd7bd61917f2f9a03292633e71c71a21e2707e10798ff239173a73e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalLoginParameters", value)

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedExternalRedirectUrls"))

    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a3b3bc2742c2114b7846df8935b2867674c2ee56dece631917934aa77cd7c26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExternalRedirectUrls", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProvider")
    def default_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProvider"))

    @default_provider.setter
    def default_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d2faf3b4ce6c3a3631ad0a3fbe6a121b8a3d2c4444bf0e422b263f8578564f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProvider", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c632f4491f14332a3ec9f7656f325054396f3dd0ed85813acd5aff43ab7f05b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__164a5b65e87a8ea7aebe06d5ec2611aa41cb6a89815a62be0c84d03f7c21bb75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6986d8782f275cf905124ef5943def4166c5134fce85069fef61e31332f2274e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenRefreshExtensionHours"))

    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e442b2395a1e63d79c38d2ef81398cfeec43c26b47483551767d9108fe5a4618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenRefreshExtensionHours", value)

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabled")
    def token_store_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tokenStoreEnabled"))

    @token_store_enabled.setter
    def token_store_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5e1ee24229cf65dfd2a19f5aee313dd64ef8d02aebd9c456653ce5f59dbacc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthenticatedClientAction"))

    @unauthenticated_client_action.setter
    def unauthenticated_client_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9728715065674c928b89ba81ab3faf282edfa242f3c5964dcdf8b53fb46e3c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticatedClientAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettings]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d868d9f7f0d39984400f12321681721d7ca7e72e5c6f843488650a657360f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsTwitter",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_key": "consumerKey",
        "consumer_secret": "consumerSecret",
        "consumer_secret_setting_name": "consumerSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsTwitter:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret: typing.Optional[builtins.str] = None,
        consumer_secret_setting_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret: The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a4ef8866204511f52f39cf00216c2ace2b0650f706d141e2645eb12c732a44e)
            check_type(argname="argument consumer_key", value=consumer_key, expected_type=type_hints["consumer_key"])
            check_type(argname="argument consumer_secret", value=consumer_secret, expected_type=type_hints["consumer_secret"])
            check_type(argname="argument consumer_secret_setting_name", value=consumer_secret_setting_name, expected_type=type_hints["consumer_secret_setting_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_key": consumer_key,
        }
        if consumer_secret is not None:
            self._values["consumer_secret"] = consumer_secret
        if consumer_secret_setting_name is not None:
            self._values["consumer_secret_setting_name"] = consumer_secret_setting_name

    @builtins.property
    def consumer_key(self) -> builtins.str:
        '''The OAuth 1.0a consumer key of the Twitter application used for sign-in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        '''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret(self) -> typing.Optional[builtins.str]:
        '''The OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret_setting_name``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret WindowsWebAppSlot#consumer_secret}
        '''
        result = self._values.get("consumer_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consumer_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Cannot be specified with ``consumer_secret``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        result = self._values.get("consumer_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsTwitter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsTwitterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsTwitterOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0954efc04d8af6ef74d8b6836c5ad6440d09fd5b78aaffce0c06f9f6b6236c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConsumerSecret")
    def reset_consumer_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerSecret", []))

    @jsii.member(jsii_name="resetConsumerSecretSettingName")
    def reset_consumer_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsumerSecretSettingName", []))

    @builtins.property
    @jsii.member(jsii_name="consumerKeyInput")
    def consumer_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerSecretInput")
    def consumer_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingNameInput")
    def consumer_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerKey")
    def consumer_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerKey"))

    @consumer_key.setter
    def consumer_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fce152f2a983733ec38726861f15e82715e96c614fc2464e1ae43b46cf5f948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerKey", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecret")
    def consumer_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecret"))

    @consumer_secret.setter
    def consumer_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff0b199e9c7dffb97b9c3fc6c38ec83d6ce072caa04a89a8df8e9cfca6242835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecretSettingName"))

    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7d701758c8c079963482f6d359860283486bce84788f4976fec6b38d7f36f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsTwitter]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsTwitter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsTwitter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a049663d59c01556f8cffb1f2a84ccc2bb3ae5e2ee253bb509e75213d41da2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2",
    jsii_struct_bases=[],
    name_mapping={
        "login": "login",
        "active_directory_v2": "activeDirectoryV2",
        "apple_v2": "appleV2",
        "auth_enabled": "authEnabled",
        "azure_static_web_app_v2": "azureStaticWebAppV2",
        "config_file_path": "configFilePath",
        "custom_oidc_v2": "customOidcV2",
        "default_provider": "defaultProvider",
        "excluded_paths": "excludedPaths",
        "facebook_v2": "facebookV2",
        "forward_proxy_convention": "forwardProxyConvention",
        "forward_proxy_custom_host_header_name": "forwardProxyCustomHostHeaderName",
        "forward_proxy_custom_scheme_header_name": "forwardProxyCustomSchemeHeaderName",
        "github_v2": "githubV2",
        "google_v2": "googleV2",
        "http_route_api_prefix": "httpRouteApiPrefix",
        "microsoft_v2": "microsoftV2",
        "require_authentication": "requireAuthentication",
        "require_https": "requireHttps",
        "runtime_version": "runtimeVersion",
        "twitter_v2": "twitterV2",
        "unauthenticated_action": "unauthenticatedAction",
    },
)
class WindowsWebAppSlotAuthSettingsV2:
    def __init__(
        self,
        *,
        login: typing.Union["WindowsWebAppSlotAuthSettingsV2Login", typing.Dict[builtins.str, typing.Any]],
        active_directory_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2", typing.Dict[builtins.str, typing.Any]]] = None,
        apple_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2AppleV2", typing.Dict[builtins.str, typing.Any]]] = None,
        auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        azure_static_web_app_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2", typing.Dict[builtins.str, typing.Any]]] = None,
        config_file_path: typing.Optional[builtins.str] = None,
        custom_oidc_v2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotAuthSettingsV2CustomOidcV2", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_provider: typing.Optional[builtins.str] = None,
        excluded_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        facebook_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2FacebookV2", typing.Dict[builtins.str, typing.Any]]] = None,
        forward_proxy_convention: typing.Optional[builtins.str] = None,
        forward_proxy_custom_host_header_name: typing.Optional[builtins.str] = None,
        forward_proxy_custom_scheme_header_name: typing.Optional[builtins.str] = None,
        github_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2GithubV2", typing.Dict[builtins.str, typing.Any]]] = None,
        google_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2GoogleV2", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route_api_prefix: typing.Optional[builtins.str] = None,
        microsoft_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2MicrosoftV2", typing.Dict[builtins.str, typing.Any]]] = None,
        require_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        runtime_version: typing.Optional[builtins.str] = None,
        twitter_v2: typing.Optional[typing.Union["WindowsWebAppSlotAuthSettingsV2TwitterV2", typing.Dict[builtins.str, typing.Any]]] = None,
        unauthenticated_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param login: login block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login WindowsWebAppSlot#login}
        :param active_directory_v2: active_directory_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory_v2 WindowsWebAppSlot#active_directory_v2}
        :param apple_v2: apple_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#apple_v2 WindowsWebAppSlot#apple_v2}
        :param auth_enabled: Should the AuthV2 Settings be enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_enabled WindowsWebAppSlot#auth_enabled}
        :param azure_static_web_app_v2: azure_static_web_app_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_static_web_app_v2 WindowsWebAppSlot#azure_static_web_app_v2}
        :param config_file_path: The path to the App Auth settings. **Note:** Relative Paths are evaluated from the Site Root directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#config_file_path WindowsWebAppSlot#config_file_path}
        :param custom_oidc_v2: custom_oidc_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_oidc_v2 WindowsWebAppSlot#custom_oidc_v2}
        :param default_provider: The Default Authentication Provider to use when the ``unauthenticated_action`` is set to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        :param excluded_paths: The paths which should be excluded from the ``unauthenticated_action`` when it is set to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#excluded_paths WindowsWebAppSlot#excluded_paths}
        :param facebook_v2: facebook_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook_v2 WindowsWebAppSlot#facebook_v2}
        :param forward_proxy_convention: The convention used to determine the url of the request made. Possible values include ``ForwardProxyConventionNoProxy``, ``ForwardProxyConventionStandard``, ``ForwardProxyConventionCustom``. Defaults to ``ForwardProxyConventionNoProxy`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_convention WindowsWebAppSlot#forward_proxy_convention}
        :param forward_proxy_custom_host_header_name: The name of the header containing the host of the request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_host_header_name WindowsWebAppSlot#forward_proxy_custom_host_header_name}
        :param forward_proxy_custom_scheme_header_name: The name of the header containing the scheme of the request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_scheme_header_name WindowsWebAppSlot#forward_proxy_custom_scheme_header_name}
        :param github_v2: github_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github_v2 WindowsWebAppSlot#github_v2}
        :param google_v2: google_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google_v2 WindowsWebAppSlot#google_v2}
        :param http_route_api_prefix: The prefix that should precede all the authentication and authorisation paths. Defaults to ``/.auth``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_route_api_prefix WindowsWebAppSlot#http_route_api_prefix}
        :param microsoft_v2: microsoft_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft_v2 WindowsWebAppSlot#microsoft_v2}
        :param require_authentication: Should the authentication flow be used for all requests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_authentication WindowsWebAppSlot#require_authentication}
        :param require_https: Should HTTPS be required on connections? Defaults to true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_https WindowsWebAppSlot#require_https}
        :param runtime_version: The Runtime Version of the Authentication and Authorisation feature of this App. Defaults to ``~1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        :param twitter_v2: twitter_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter_v2 WindowsWebAppSlot#twitter_v2}
        :param unauthenticated_action: The action to take for requests made without authentication. Possible values include ``RedirectToLoginPage``, ``AllowAnonymous``, ``Return401``, and ``Return403``. Defaults to ``RedirectToLoginPage``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_action WindowsWebAppSlot#unauthenticated_action}
        '''
        if isinstance(login, dict):
            login = WindowsWebAppSlotAuthSettingsV2Login(**login)
        if isinstance(active_directory_v2, dict):
            active_directory_v2 = WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2(**active_directory_v2)
        if isinstance(apple_v2, dict):
            apple_v2 = WindowsWebAppSlotAuthSettingsV2AppleV2(**apple_v2)
        if isinstance(azure_static_web_app_v2, dict):
            azure_static_web_app_v2 = WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2(**azure_static_web_app_v2)
        if isinstance(facebook_v2, dict):
            facebook_v2 = WindowsWebAppSlotAuthSettingsV2FacebookV2(**facebook_v2)
        if isinstance(github_v2, dict):
            github_v2 = WindowsWebAppSlotAuthSettingsV2GithubV2(**github_v2)
        if isinstance(google_v2, dict):
            google_v2 = WindowsWebAppSlotAuthSettingsV2GoogleV2(**google_v2)
        if isinstance(microsoft_v2, dict):
            microsoft_v2 = WindowsWebAppSlotAuthSettingsV2MicrosoftV2(**microsoft_v2)
        if isinstance(twitter_v2, dict):
            twitter_v2 = WindowsWebAppSlotAuthSettingsV2TwitterV2(**twitter_v2)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e8a09f2123e8647e82ec4f6e0b012ee1e4d024999873b2d62140e78a2fe00d)
            check_type(argname="argument login", value=login, expected_type=type_hints["login"])
            check_type(argname="argument active_directory_v2", value=active_directory_v2, expected_type=type_hints["active_directory_v2"])
            check_type(argname="argument apple_v2", value=apple_v2, expected_type=type_hints["apple_v2"])
            check_type(argname="argument auth_enabled", value=auth_enabled, expected_type=type_hints["auth_enabled"])
            check_type(argname="argument azure_static_web_app_v2", value=azure_static_web_app_v2, expected_type=type_hints["azure_static_web_app_v2"])
            check_type(argname="argument config_file_path", value=config_file_path, expected_type=type_hints["config_file_path"])
            check_type(argname="argument custom_oidc_v2", value=custom_oidc_v2, expected_type=type_hints["custom_oidc_v2"])
            check_type(argname="argument default_provider", value=default_provider, expected_type=type_hints["default_provider"])
            check_type(argname="argument excluded_paths", value=excluded_paths, expected_type=type_hints["excluded_paths"])
            check_type(argname="argument facebook_v2", value=facebook_v2, expected_type=type_hints["facebook_v2"])
            check_type(argname="argument forward_proxy_convention", value=forward_proxy_convention, expected_type=type_hints["forward_proxy_convention"])
            check_type(argname="argument forward_proxy_custom_host_header_name", value=forward_proxy_custom_host_header_name, expected_type=type_hints["forward_proxy_custom_host_header_name"])
            check_type(argname="argument forward_proxy_custom_scheme_header_name", value=forward_proxy_custom_scheme_header_name, expected_type=type_hints["forward_proxy_custom_scheme_header_name"])
            check_type(argname="argument github_v2", value=github_v2, expected_type=type_hints["github_v2"])
            check_type(argname="argument google_v2", value=google_v2, expected_type=type_hints["google_v2"])
            check_type(argname="argument http_route_api_prefix", value=http_route_api_prefix, expected_type=type_hints["http_route_api_prefix"])
            check_type(argname="argument microsoft_v2", value=microsoft_v2, expected_type=type_hints["microsoft_v2"])
            check_type(argname="argument require_authentication", value=require_authentication, expected_type=type_hints["require_authentication"])
            check_type(argname="argument require_https", value=require_https, expected_type=type_hints["require_https"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument twitter_v2", value=twitter_v2, expected_type=type_hints["twitter_v2"])
            check_type(argname="argument unauthenticated_action", value=unauthenticated_action, expected_type=type_hints["unauthenticated_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "login": login,
        }
        if active_directory_v2 is not None:
            self._values["active_directory_v2"] = active_directory_v2
        if apple_v2 is not None:
            self._values["apple_v2"] = apple_v2
        if auth_enabled is not None:
            self._values["auth_enabled"] = auth_enabled
        if azure_static_web_app_v2 is not None:
            self._values["azure_static_web_app_v2"] = azure_static_web_app_v2
        if config_file_path is not None:
            self._values["config_file_path"] = config_file_path
        if custom_oidc_v2 is not None:
            self._values["custom_oidc_v2"] = custom_oidc_v2
        if default_provider is not None:
            self._values["default_provider"] = default_provider
        if excluded_paths is not None:
            self._values["excluded_paths"] = excluded_paths
        if facebook_v2 is not None:
            self._values["facebook_v2"] = facebook_v2
        if forward_proxy_convention is not None:
            self._values["forward_proxy_convention"] = forward_proxy_convention
        if forward_proxy_custom_host_header_name is not None:
            self._values["forward_proxy_custom_host_header_name"] = forward_proxy_custom_host_header_name
        if forward_proxy_custom_scheme_header_name is not None:
            self._values["forward_proxy_custom_scheme_header_name"] = forward_proxy_custom_scheme_header_name
        if github_v2 is not None:
            self._values["github_v2"] = github_v2
        if google_v2 is not None:
            self._values["google_v2"] = google_v2
        if http_route_api_prefix is not None:
            self._values["http_route_api_prefix"] = http_route_api_prefix
        if microsoft_v2 is not None:
            self._values["microsoft_v2"] = microsoft_v2
        if require_authentication is not None:
            self._values["require_authentication"] = require_authentication
        if require_https is not None:
            self._values["require_https"] = require_https
        if runtime_version is not None:
            self._values["runtime_version"] = runtime_version
        if twitter_v2 is not None:
            self._values["twitter_v2"] = twitter_v2
        if unauthenticated_action is not None:
            self._values["unauthenticated_action"] = unauthenticated_action

    @builtins.property
    def login(self) -> "WindowsWebAppSlotAuthSettingsV2Login":
        '''login block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login WindowsWebAppSlot#login}
        '''
        result = self._values.get("login")
        assert result is not None, "Required property 'login' is missing"
        return typing.cast("WindowsWebAppSlotAuthSettingsV2Login", result)

    @builtins.property
    def active_directory_v2(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2"]:
        '''active_directory_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#active_directory_v2 WindowsWebAppSlot#active_directory_v2}
        '''
        result = self._values.get("active_directory_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2"], result)

    @builtins.property
    def apple_v2(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2AppleV2"]:
        '''apple_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#apple_v2 WindowsWebAppSlot#apple_v2}
        '''
        result = self._values.get("apple_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2AppleV2"], result)

    @builtins.property
    def auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the AuthV2 Settings be enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_enabled WindowsWebAppSlot#auth_enabled}
        '''
        result = self._values.get("auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def azure_static_web_app_v2(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2"]:
        '''azure_static_web_app_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_static_web_app_v2 WindowsWebAppSlot#azure_static_web_app_v2}
        '''
        result = self._values.get("azure_static_web_app_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2"], result)

    @builtins.property
    def config_file_path(self) -> typing.Optional[builtins.str]:
        '''The path to the App Auth settings. **Note:** Relative Paths are evaluated from the Site Root directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#config_file_path WindowsWebAppSlot#config_file_path}
        '''
        result = self._values.get("config_file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_oidc_v2(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotAuthSettingsV2CustomOidcV2"]]]:
        '''custom_oidc_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_oidc_v2 WindowsWebAppSlot#custom_oidc_v2}
        '''
        result = self._values.get("custom_oidc_v2")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotAuthSettingsV2CustomOidcV2"]]], result)

    @builtins.property
    def default_provider(self) -> typing.Optional[builtins.str]:
        '''The Default Authentication Provider to use when the ``unauthenticated_action`` is set to ``RedirectToLoginPage``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_provider WindowsWebAppSlot#default_provider}
        '''
        result = self._values.get("default_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excluded_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The paths which should be excluded from the ``unauthenticated_action`` when it is set to ``RedirectToLoginPage``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#excluded_paths WindowsWebAppSlot#excluded_paths}
        '''
        result = self._values.get("excluded_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def facebook_v2(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2FacebookV2"]:
        '''facebook_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#facebook_v2 WindowsWebAppSlot#facebook_v2}
        '''
        result = self._values.get("facebook_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2FacebookV2"], result)

    @builtins.property
    def forward_proxy_convention(self) -> typing.Optional[builtins.str]:
        '''The convention used to determine the url of the request made.

        Possible values include ``ForwardProxyConventionNoProxy``, ``ForwardProxyConventionStandard``, ``ForwardProxyConventionCustom``. Defaults to ``ForwardProxyConventionNoProxy``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_convention WindowsWebAppSlot#forward_proxy_convention}
        '''
        result = self._values.get("forward_proxy_convention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forward_proxy_custom_host_header_name(self) -> typing.Optional[builtins.str]:
        '''The name of the header containing the host of the request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_host_header_name WindowsWebAppSlot#forward_proxy_custom_host_header_name}
        '''
        result = self._values.get("forward_proxy_custom_host_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forward_proxy_custom_scheme_header_name(self) -> typing.Optional[builtins.str]:
        '''The name of the header containing the scheme of the request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#forward_proxy_custom_scheme_header_name WindowsWebAppSlot#forward_proxy_custom_scheme_header_name}
        '''
        result = self._values.get("forward_proxy_custom_scheme_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def github_v2(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2GithubV2"]:
        '''github_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#github_v2 WindowsWebAppSlot#github_v2}
        '''
        result = self._values.get("github_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2GithubV2"], result)

    @builtins.property
    def google_v2(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2GoogleV2"]:
        '''google_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#google_v2 WindowsWebAppSlot#google_v2}
        '''
        result = self._values.get("google_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2GoogleV2"], result)

    @builtins.property
    def http_route_api_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix that should precede all the authentication and authorisation paths. Defaults to ``/.auth``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_route_api_prefix WindowsWebAppSlot#http_route_api_prefix}
        '''
        result = self._values.get("http_route_api_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_v2(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2MicrosoftV2"]:
        '''microsoft_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#microsoft_v2 WindowsWebAppSlot#microsoft_v2}
        '''
        result = self._values.get("microsoft_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2MicrosoftV2"], result)

    @builtins.property
    def require_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the authentication flow be used for all requests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_authentication WindowsWebAppSlot#require_authentication}
        '''
        result = self._values.get("require_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should HTTPS be required on connections? Defaults to true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#require_https WindowsWebAppSlot#require_https}
        '''
        result = self._values.get("require_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def runtime_version(self) -> typing.Optional[builtins.str]:
        '''The Runtime Version of the Authentication and Authorisation feature of this App. Defaults to ``~1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#runtime_version WindowsWebAppSlot#runtime_version}
        '''
        result = self._values.get("runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def twitter_v2(self) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2TwitterV2"]:
        '''twitter_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#twitter_v2 WindowsWebAppSlot#twitter_v2}
        '''
        result = self._values.get("twitter_v2")
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2TwitterV2"], result)

    @builtins.property
    def unauthenticated_action(self) -> typing.Optional[builtins.str]:
        '''The action to take for requests made without authentication.

        Possible values include ``RedirectToLoginPage``, ``AllowAnonymous``, ``Return401``, and ``Return403``. Defaults to ``RedirectToLoginPage``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#unauthenticated_action WindowsWebAppSlot#unauthenticated_action}
        '''
        result = self._values.get("unauthenticated_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "tenant_auth_endpoint": "tenantAuthEndpoint",
        "allowed_applications": "allowedApplications",
        "allowed_audiences": "allowedAudiences",
        "allowed_groups": "allowedGroups",
        "allowed_identities": "allowedIdentities",
        "client_secret_certificate_thumbprint": "clientSecretCertificateThumbprint",
        "client_secret_setting_name": "clientSecretSettingName",
        "jwt_allowed_client_applications": "jwtAllowedClientApplications",
        "jwt_allowed_groups": "jwtAllowedGroups",
        "login_parameters": "loginParameters",
        "www_authentication_disabled": "wwwAuthenticationDisabled",
    },
)
class WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        tenant_auth_endpoint: builtins.str,
        allowed_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret_certificate_thumbprint: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        jwt_allowed_client_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        jwt_allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        www_authentication_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param tenant_auth_endpoint: The Azure Tenant Endpoint for the Authenticating Tenant. e.g. ``https://login.microsoftonline.com/v2.0/{tenant-guid}/``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tenant_auth_endpoint WindowsWebAppSlot#tenant_auth_endpoint}
        :param allowed_applications: The list of allowed Applications for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_applications WindowsWebAppSlot#allowed_applications}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param allowed_groups: The list of allowed Group Names for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_groups WindowsWebAppSlot#allowed_groups}
        :param allowed_identities: The list of allowed Identities for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_identities WindowsWebAppSlot#allowed_identities}
        :param client_secret_certificate_thumbprint: The thumbprint of the certificate used for signing purposes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_certificate_thumbprint WindowsWebAppSlot#client_secret_certificate_thumbprint}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param jwt_allowed_client_applications: A list of Allowed Client Applications in the JWT Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_client_applications WindowsWebAppSlot#jwt_allowed_client_applications}
        :param jwt_allowed_groups: A list of Allowed Groups in the JWT Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_groups WindowsWebAppSlot#jwt_allowed_groups}
        :param login_parameters: A map of key-value pairs to send to the Authorisation Endpoint when a user logs in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_parameters WindowsWebAppSlot#login_parameters}
        :param www_authentication_disabled: Should the www-authenticate provider should be omitted from the request? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#www_authentication_disabled WindowsWebAppSlot#www_authentication_disabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f9f7a6815cb1b45d489e3bb8ca0dc6c07276bf2fc742c168233d2fccaad84d3)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument tenant_auth_endpoint", value=tenant_auth_endpoint, expected_type=type_hints["tenant_auth_endpoint"])
            check_type(argname="argument allowed_applications", value=allowed_applications, expected_type=type_hints["allowed_applications"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument allowed_groups", value=allowed_groups, expected_type=type_hints["allowed_groups"])
            check_type(argname="argument allowed_identities", value=allowed_identities, expected_type=type_hints["allowed_identities"])
            check_type(argname="argument client_secret_certificate_thumbprint", value=client_secret_certificate_thumbprint, expected_type=type_hints["client_secret_certificate_thumbprint"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument jwt_allowed_client_applications", value=jwt_allowed_client_applications, expected_type=type_hints["jwt_allowed_client_applications"])
            check_type(argname="argument jwt_allowed_groups", value=jwt_allowed_groups, expected_type=type_hints["jwt_allowed_groups"])
            check_type(argname="argument login_parameters", value=login_parameters, expected_type=type_hints["login_parameters"])
            check_type(argname="argument www_authentication_disabled", value=www_authentication_disabled, expected_type=type_hints["www_authentication_disabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "tenant_auth_endpoint": tenant_auth_endpoint,
        }
        if allowed_applications is not None:
            self._values["allowed_applications"] = allowed_applications
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if allowed_groups is not None:
            self._values["allowed_groups"] = allowed_groups
        if allowed_identities is not None:
            self._values["allowed_identities"] = allowed_identities
        if client_secret_certificate_thumbprint is not None:
            self._values["client_secret_certificate_thumbprint"] = client_secret_certificate_thumbprint
        if client_secret_setting_name is not None:
            self._values["client_secret_setting_name"] = client_secret_setting_name
        if jwt_allowed_client_applications is not None:
            self._values["jwt_allowed_client_applications"] = jwt_allowed_client_applications
        if jwt_allowed_groups is not None:
            self._values["jwt_allowed_groups"] = jwt_allowed_groups
        if login_parameters is not None:
            self._values["login_parameters"] = login_parameters
        if www_authentication_disabled is not None:
            self._values["www_authentication_disabled"] = www_authentication_disabled

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the Client to use to authenticate with Azure Active Directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_auth_endpoint(self) -> builtins.str:
        '''The Azure Tenant Endpoint for the Authenticating Tenant. e.g. ``https://login.microsoftonline.com/v2.0/{tenant-guid}/``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tenant_auth_endpoint WindowsWebAppSlot#tenant_auth_endpoint}
        '''
        result = self._values.get("tenant_auth_endpoint")
        assert result is not None, "Required property 'tenant_auth_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_applications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of allowed Applications for the Default Authorisation Policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_applications WindowsWebAppSlot#allowed_applications}
        '''
        result = self._values.get("allowed_applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of allowed Group Names for the Default Authorisation Policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_groups WindowsWebAppSlot#allowed_groups}
        '''
        result = self._values.get("allowed_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of allowed Identities for the Default Authorisation Policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_identities WindowsWebAppSlot#allowed_identities}
        '''
        result = self._values.get("allowed_identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_secret_certificate_thumbprint(self) -> typing.Optional[builtins.str]:
        '''The thumbprint of the certificate used for signing purposes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_certificate_thumbprint WindowsWebAppSlot#client_secret_certificate_thumbprint}
        '''
        result = self._values.get("client_secret_certificate_thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_setting_name(self) -> typing.Optional[builtins.str]:
        '''The App Setting name that contains the client secret of the Client.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jwt_allowed_client_applications(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Allowed Client Applications in the JWT Claim.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_client_applications WindowsWebAppSlot#jwt_allowed_client_applications}
        '''
        result = self._values.get("jwt_allowed_client_applications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jwt_allowed_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Allowed Groups in the JWT Claim.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_groups WindowsWebAppSlot#jwt_allowed_groups}
        '''
        result = self._values.get("jwt_allowed_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key-value pairs to send to the Authorisation Endpoint when a user logs in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_parameters WindowsWebAppSlot#login_parameters}
        '''
        result = self._values.get("login_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def www_authentication_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the www-authenticate provider should be omitted from the request? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#www_authentication_disabled WindowsWebAppSlot#www_authentication_disabled}
        '''
        result = self._values.get("www_authentication_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1556cba47f961b57421b7e526f6d60662821cd5bf44505a61fd44fe41e8d3c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedApplications")
    def reset_allowed_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedApplications", []))

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetAllowedGroups")
    def reset_allowed_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedGroups", []))

    @jsii.member(jsii_name="resetAllowedIdentities")
    def reset_allowed_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedIdentities", []))

    @jsii.member(jsii_name="resetClientSecretCertificateThumbprint")
    def reset_client_secret_certificate_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretCertificateThumbprint", []))

    @jsii.member(jsii_name="resetClientSecretSettingName")
    def reset_client_secret_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretSettingName", []))

    @jsii.member(jsii_name="resetJwtAllowedClientApplications")
    def reset_jwt_allowed_client_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtAllowedClientApplications", []))

    @jsii.member(jsii_name="resetJwtAllowedGroups")
    def reset_jwt_allowed_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtAllowedGroups", []))

    @jsii.member(jsii_name="resetLoginParameters")
    def reset_login_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginParameters", []))

    @jsii.member(jsii_name="resetWwwAuthenticationDisabled")
    def reset_www_authentication_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWwwAuthenticationDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="allowedApplicationsInput")
    def allowed_applications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedApplicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedGroupsInput")
    def allowed_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedIdentitiesInput")
    def allowed_identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretCertificateThumbprintInput")
    def client_secret_certificate_thumbprint_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretCertificateThumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtAllowedClientApplicationsInput")
    def jwt_allowed_client_applications_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jwtAllowedClientApplicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtAllowedGroupsInput")
    def jwt_allowed_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jwtAllowedGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="loginParametersInput")
    def login_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "loginParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantAuthEndpointInput")
    def tenant_auth_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantAuthEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="wwwAuthenticationDisabledInput")
    def www_authentication_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wwwAuthenticationDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedApplications")
    def allowed_applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedApplications"))

    @allowed_applications.setter
    def allowed_applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74d3bd055d37baceb955b29dc65f9258235d685c2214bd92707449eda7ea7e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedApplications", value)

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f23254bb6c9986ecd343adadb1c5558d47e01ebc9c3c928df25be4a151be02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="allowedGroups")
    def allowed_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedGroups"))

    @allowed_groups.setter
    def allowed_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb49e3c2f62e4f02a4fa3dea9b1ec93106fcd5ae1fc6223cad418a7284c35d33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedGroups", value)

    @builtins.property
    @jsii.member(jsii_name="allowedIdentities")
    def allowed_identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedIdentities"))

    @allowed_identities.setter
    def allowed_identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__609f73dae80aabb7caab2f7c83ede01cdd2d26a34e77ab59906b9ec608cadaf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedIdentities", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96400477d50776117db2057e7ed727da79519d145f8f7fdbb5c893e094ddfdce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretCertificateThumbprint"))

    @client_secret_certificate_thumbprint.setter
    def client_secret_certificate_thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f27a7ce68c5a257d9f6b8df97435ef34a97700a466f10ec560965c9552c502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretCertificateThumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16cf01d1192bb12f5b486306bd68b771514e0ff3e0df0f401adbc97e49b7ccad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="jwtAllowedClientApplications")
    def jwt_allowed_client_applications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jwtAllowedClientApplications"))

    @jwt_allowed_client_applications.setter
    def jwt_allowed_client_applications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648d650fce3295bc1a6b84a5b5052c4bbcd0f0ee885c673c0360ba1203d3d4c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jwtAllowedClientApplications", value)

    @builtins.property
    @jsii.member(jsii_name="jwtAllowedGroups")
    def jwt_allowed_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jwtAllowedGroups"))

    @jwt_allowed_groups.setter
    def jwt_allowed_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd7ed5f106fffa50d29b3951d3995d7fd7388ea4376d63904777911327064342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jwtAllowedGroups", value)

    @builtins.property
    @jsii.member(jsii_name="loginParameters")
    def login_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "loginParameters"))

    @login_parameters.setter
    def login_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27822f172a4bb33d8d802400d9b8782b2646573d9b1873ce5069fcb962373ccc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginParameters", value)

    @builtins.property
    @jsii.member(jsii_name="tenantAuthEndpoint")
    def tenant_auth_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantAuthEndpoint"))

    @tenant_auth_endpoint.setter
    def tenant_auth_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3315d791dee383f93c68f0ff3d94c6c6e25a32edbee6370a65c6c412cb69cbff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantAuthEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="wwwAuthenticationDisabled")
    def www_authentication_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wwwAuthenticationDisabled"))

    @www_authentication_disabled.setter
    def www_authentication_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c1ee7c035919f16217b723cffd7607d6826836821e603f13fdaa0731b60cbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wwwAuthenticationDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc8416685b4bab62699ea8d02c27968b8156b56a736d35b9c8a09701c813eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2AppleV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_setting_name": "clientSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsV2AppleV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Apple web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Apple Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1554237578e1cf1d1379e5ca212b816dce611ada09983328f819c2b0a540c74)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_setting_name": client_secret_setting_name,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OpenID Connect Client ID for the Apple web application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_setting_name(self) -> builtins.str:
        '''The app setting name that contains the ``client_secret`` value used for Apple Login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        assert result is not None, "Required property 'client_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2AppleV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2AppleV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2AppleV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3557a05cb0419c0fa89408e0c1ae17b046794a93936b84f5f13e9c6e70e0bc79)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="loginScopes")
    def login_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginScopes"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f767acb1039b5d5ffa950650261b4fb778bd1fe2c9d8fbe8d74f34fc37712fd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e540aecd7032280628d5082bba112bb6e1baa82fdff281c343317b84de4cecd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b01dd51be2ddd751e2d5bd39cc94a81808f17f4f4535e581a9c81e390e037ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId"},
)
class WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2:
    def __init__(self, *, client_id: builtins.str) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Static Web App Authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d85945d65fac243ea635cee683c472398569537618fdd2c1ab133daabe20da)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the Client to use to authenticate with Azure Static Web App Authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072c0cfed72d0ea8d5cb3a71f699a5a0643da7baee1b0846460c365c21ece9ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd9cb3493147605ccc9f30005a5b8c02e1f2dc77160ac229b82941973428a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d538708f033774c14b558f450a219623e6c44bdfbd3d5e6a4cf62dbea2d90ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2CustomOidcV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "name": "name",
        "openid_configuration_endpoint": "openidConfigurationEndpoint",
        "name_claim_type": "nameClaimType",
        "scopes": "scopes",
    },
)
class WindowsWebAppSlotAuthSettingsV2CustomOidcV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        name: builtins.str,
        openid_configuration_endpoint: builtins.str,
        name_claim_type: typing.Optional[builtins.str] = None,
        scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with this Custom OIDC. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param name: The name of the Custom OIDC Authentication Provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param openid_configuration_endpoint: The endpoint that contains all the configuration endpoints for this Custom OIDC provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#openid_configuration_endpoint WindowsWebAppSlot#openid_configuration_endpoint}
        :param name_claim_type: The name of the claim that contains the users name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name_claim_type WindowsWebAppSlot#name_claim_type}
        :param scopes: The list of the scopes that should be requested while authenticating. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scopes WindowsWebAppSlot#scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bbe18c12566a75723bfd946074bb46e7a18afe8e7b8a64d7d857f3c8b9d8832)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument openid_configuration_endpoint", value=openid_configuration_endpoint, expected_type=type_hints["openid_configuration_endpoint"])
            check_type(argname="argument name_claim_type", value=name_claim_type, expected_type=type_hints["name_claim_type"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "name": name,
            "openid_configuration_endpoint": openid_configuration_endpoint,
        }
        if name_claim_type is not None:
            self._values["name_claim_type"] = name_claim_type
        if scopes is not None:
            self._values["scopes"] = scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the Client to use to authenticate with this Custom OIDC.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Custom OIDC Authentication Provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def openid_configuration_endpoint(self) -> builtins.str:
        '''The endpoint that contains all the configuration endpoints for this Custom OIDC provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#openid_configuration_endpoint WindowsWebAppSlot#openid_configuration_endpoint}
        '''
        result = self._values.get("openid_configuration_endpoint")
        assert result is not None, "Required property 'openid_configuration_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name_claim_type(self) -> typing.Optional[builtins.str]:
        '''The name of the claim that contains the users name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name_claim_type WindowsWebAppSlot#name_claim_type}
        '''
        result = self._values.get("name_claim_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of the scopes that should be requested while authenticating.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scopes WindowsWebAppSlot#scopes}
        '''
        result = self._values.get("scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2CustomOidcV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2CustomOidcV2List(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2CustomOidcV2List",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff206d7cd860b94ecbbc2141e4cd47c7d042e0aad841dfdcea598d29a596c891)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotAuthSettingsV2CustomOidcV2OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b11dca0380b39bbea0dc46c98fdcd4fec1931f8e5272574df89f8e59656454)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotAuthSettingsV2CustomOidcV2OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d55f23be1373ab362fd71b3bc75e6abea99d09bed52578811aabe2f6e8dcd0c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899bed833414dfa767e7d3e1d9ed1e9b68553810a1a7b7d6828ee54bcfc4fbc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c5dce477f1c78cd1ffdc583f03917f722cb131472e3baf7d2d7d8d1d213841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc3a34919c53f53af3c879f7e97c78d76f861c47654c994898282d991750a62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotAuthSettingsV2CustomOidcV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2CustomOidcV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb68115b8d04972acca01b743b56ba82db5e86219862038f8532586f2944a73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNameClaimType")
    def reset_name_claim_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameClaimType", []))

    @jsii.member(jsii_name="resetScopes")
    def reset_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScopes", []))

    @builtins.property
    @jsii.member(jsii_name="authorisationEndpoint")
    def authorisation_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorisationEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="certificationUri")
    def certification_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificationUri"))

    @builtins.property
    @jsii.member(jsii_name="clientCredentialMethod")
    def client_credential_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCredentialMethod"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @builtins.property
    @jsii.member(jsii_name="issuerEndpoint")
    def issuer_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="tokenEndpoint")
    def token_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameClaimTypeInput")
    def name_claim_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameClaimTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConfigurationEndpointInput")
    def openid_configuration_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "openidConfigurationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="scopesInput")
    def scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91aa3f316da337a14d411235c6ca85d7659957c787d427d52051f10e9c3586a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c237a8bd4760390a9563cda5de9400ab121902e5ec908c53539460bed64e5be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nameClaimType")
    def name_claim_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameClaimType"))

    @name_claim_type.setter
    def name_claim_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832cee9a4c9bb5ec5a0a6dd8554236d22a2858910897739bfd8ed5077447abf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameClaimType", value)

    @builtins.property
    @jsii.member(jsii_name="openidConfigurationEndpoint")
    def openid_configuration_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "openidConfigurationEndpoint"))

    @openid_configuration_endpoint.setter
    def openid_configuration_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e3e9cecfb5b6a579b0659006cbb05e28afd0d116d1d9d69458d01224dc024f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openidConfigurationEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c0ae64130264e7433da8ff21fa01181bfab2495fff062a84a44f99f593c382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c30d8db8d789fc767d4d7ad62a83092c8b162e78091973e0649140066df6095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2FacebookV2",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "app_secret_setting_name": "appSecretSettingName",
        "graph_api_version": "graphApiVersion",
        "login_scopes": "loginScopes",
    },
)
class WindowsWebAppSlotAuthSettingsV2FacebookV2:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        app_secret_setting_name: builtins.str,
        graph_api_version: typing.Optional[builtins.str] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param graph_api_version: The version of the Facebook API to be used while logging in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#graph_api_version WindowsWebAppSlot#graph_api_version}
        :param login_scopes: Specifies a list of scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225e39c41b6f3cf019296c60524ccdfb8701001b27c00b916fc96a8812d14cc2)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument app_secret_setting_name", value=app_secret_setting_name, expected_type=type_hints["app_secret_setting_name"])
            check_type(argname="argument graph_api_version", value=graph_api_version, expected_type=type_hints["graph_api_version"])
            check_type(argname="argument login_scopes", value=login_scopes, expected_type=type_hints["login_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "app_secret_setting_name": app_secret_setting_name,
        }
        if graph_api_version is not None:
            self._values["graph_api_version"] = graph_api_version
        if login_scopes is not None:
            self._values["login_scopes"] = login_scopes

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The App ID of the Facebook app used for login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_secret_setting_name(self) -> builtins.str:
        '''The app setting name that contains the ``app_secret`` value used for Facebook Login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        '''
        result = self._values.get("app_secret_setting_name")
        assert result is not None, "Required property 'app_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def graph_api_version(self) -> typing.Optional[builtins.str]:
        '''The version of the Facebook API to be used while logging in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#graph_api_version WindowsWebAppSlot#graph_api_version}
        '''
        result = self._values.get("graph_api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of scopes to be requested as part of Facebook Login authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        result = self._values.get("login_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2FacebookV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2FacebookV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2FacebookV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a63613bc24845698f7ed2734f617a96f45b09d859170759cbc4e216a7bf806)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGraphApiVersion")
    def reset_graph_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraphApiVersion", []))

    @jsii.member(jsii_name="resetLoginScopes")
    def reset_login_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginScopes", []))

    @builtins.property
    @jsii.member(jsii_name="appIdInput")
    def app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingNameInput")
    def app_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="graphApiVersionInput")
    def graph_api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "graphApiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="loginScopesInput")
    def login_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6826eb97e195eb1084225f23167363de78e123e529f87e12459eeddf64120d57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="appSecretSettingName")
    def app_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecretSettingName"))

    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904a6e84cc1dc09fe5d1d42ed4d84b2da6bd415298ebfb2d3a599530b039ec63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="graphApiVersion")
    def graph_api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "graphApiVersion"))

    @graph_api_version.setter
    def graph_api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db47302076551b931193454e06c210d8af98048004594fc4bff9d545a811498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphApiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="loginScopes")
    def login_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginScopes"))

    @login_scopes.setter
    def login_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ab645da0a3d2cad080f85959e59971667bcaedf124a87019da17725edfc114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a3c42ebbfeda4169fdbee33f90b4ab8b044f28246ca56c5ffa879ca04b04d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2GithubV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_setting_name": "clientSecretSettingName",
        "login_scopes": "loginScopes",
    },
)
class WindowsWebAppSlotAuthSettingsV2GithubV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param login_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b734b01ed37534954fe022a65732f9e7d054ca6a159d91f383e646a5869758)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument login_scopes", value=login_scopes, expected_type=type_hints["login_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_setting_name": client_secret_setting_name,
        }
        if login_scopes is not None:
            self._values["login_scopes"] = login_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ID of the GitHub app used for login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_setting_name(self) -> builtins.str:
        '''The app setting name that contains the ``client_secret`` value used for GitHub Login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        assert result is not None, "Required property 'client_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def login_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        result = self._values.get("login_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2GithubV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2GithubV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2GithubV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ca89e23f5742b2e38126cb11f0dd848ea2628a82bd3f91d11e71dfd868f240)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLoginScopes")
    def reset_login_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginScopes", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loginScopesInput")
    def login_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__538f2effcc0138034b9930812f48ef6727f489bd9df393c7023278e2bffa8f67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e9f7bc95fbf2d1818a75a24cd889195e715b5d993f85ca5903e5483fc2be15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="loginScopes")
    def login_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginScopes"))

    @login_scopes.setter
    def login_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdde59b2b18866164fee00a157a8e3d8f9dd513c6c4112bafa31df5ccb154662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8001d9030cc987a7e44a3e8242af649fe61a0a45ac278d93eebe5339d83f458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2GoogleV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_setting_name": "clientSecretSettingName",
        "allowed_audiences": "allowedAudiences",
        "login_scopes": "loginScopes",
    },
)
class WindowsWebAppSlotAuthSettingsV2GoogleV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param allowed_audiences: Specifies a list of Allowed Audiences that will be requested as part of Google Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param login_scopes: Specifies a list of Login scopes that will be requested as part of Google Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c76f816facfb937c9bb85a9795333d2d4551814ee6acc94df7f5246f7d0c591)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument login_scopes", value=login_scopes, expected_type=type_hints["login_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_setting_name": client_secret_setting_name,
        }
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if login_scopes is not None:
            self._values["login_scopes"] = login_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OpenID Connect Client ID for the Google web application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_setting_name(self) -> builtins.str:
        '''The app setting name that contains the ``client_secret`` value used for Google Login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        assert result is not None, "Required property 'client_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed Audiences that will be requested as part of Google Sign-In authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Login scopes that will be requested as part of Google Sign-In authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        result = self._values.get("login_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2GoogleV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2GoogleV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2GoogleV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61115394e33d80e6acb7cfe5cc134958422229878df51a022e1fbfbe3b40f8ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetLoginScopes")
    def reset_login_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginScopes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loginScopesInput")
    def login_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798eba42177ce830e6cbc402fde2393d9e62518615add3535dbe73afce679d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17fc6ebcf2736d53fb374dfef150512b0c1b5a75092a605f87ef0ddaa3885d92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1f8c60530177081ecb0bf18fa1d8ee0fb244e5ecf7436161aa0cb99dea65375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="loginScopes")
    def login_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginScopes"))

    @login_scopes.setter
    def login_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__829e4b401385be1c0af4b14998d70d2c3c53427c14a14b49de4dca8da96e4b62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a9d47927c87c3a5a5ca692c789581cc214692c199e66d264972b4a40a7d1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2Login",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_external_redirect_urls": "allowedExternalRedirectUrls",
        "cookie_expiration_convention": "cookieExpirationConvention",
        "cookie_expiration_time": "cookieExpirationTime",
        "logout_endpoint": "logoutEndpoint",
        "nonce_expiration_time": "nonceExpirationTime",
        "preserve_url_fragments_for_logins": "preserveUrlFragmentsForLogins",
        "token_refresh_extension_time": "tokenRefreshExtensionTime",
        "token_store_enabled": "tokenStoreEnabled",
        "token_store_path": "tokenStorePath",
        "token_store_sas_setting_name": "tokenStoreSasSettingName",
        "validate_nonce": "validateNonce",
    },
)
class WindowsWebAppSlotAuthSettingsV2Login:
    def __init__(
        self,
        *,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        cookie_expiration_convention: typing.Optional[builtins.str] = None,
        cookie_expiration_time: typing.Optional[builtins.str] = None,
        logout_endpoint: typing.Optional[builtins.str] = None,
        nonce_expiration_time: typing.Optional[builtins.str] = None,
        preserve_url_fragments_for_logins: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token_refresh_extension_time: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token_store_path: typing.Optional[builtins.str] = None,
        token_store_sas_setting_name: typing.Optional[builtins.str] = None,
        validate_nonce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_external_redirect_urls: External URLs that can be redirected to as part of logging in or logging out of the app. This is an advanced setting typically only needed by Windows Store application backends. **Note:** URLs within the current domain are always implicitly allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param cookie_expiration_convention: The method by which cookies expire. Possible values include: ``FixedTime``, and ``IdentityProviderDerived``. Defaults to ``FixedTime``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_convention WindowsWebAppSlot#cookie_expiration_convention}
        :param cookie_expiration_time: The time after the request is made when the session cookie should expire. Defaults to ``08:00:00``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_time WindowsWebAppSlot#cookie_expiration_time}
        :param logout_endpoint: The endpoint to which logout requests should be made. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logout_endpoint WindowsWebAppSlot#logout_endpoint}
        :param nonce_expiration_time: The time after the request is made when the nonce should expire. Defaults to ``00:05:00``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#nonce_expiration_time WindowsWebAppSlot#nonce_expiration_time}
        :param preserve_url_fragments_for_logins: Should the fragments from the request be preserved after the login request is made. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#preserve_url_fragments_for_logins WindowsWebAppSlot#preserve_url_fragments_for_logins}
        :param token_refresh_extension_time: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_time WindowsWebAppSlot#token_refresh_extension_time}
        :param token_store_enabled: Should the Token Store configuration Enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param token_store_path: The directory path in the App Filesystem in which the tokens will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_path WindowsWebAppSlot#token_store_path}
        :param token_store_sas_setting_name: The name of the app setting which contains the SAS URL of the blob storage containing the tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_sas_setting_name WindowsWebAppSlot#token_store_sas_setting_name}
        :param validate_nonce: Should the nonce be validated while completing the login flow. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#validate_nonce WindowsWebAppSlot#validate_nonce}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1819e90a271fb232c22bdf76d4255c6bd0def46d79aa83c37774d6ad2a85732)
            check_type(argname="argument allowed_external_redirect_urls", value=allowed_external_redirect_urls, expected_type=type_hints["allowed_external_redirect_urls"])
            check_type(argname="argument cookie_expiration_convention", value=cookie_expiration_convention, expected_type=type_hints["cookie_expiration_convention"])
            check_type(argname="argument cookie_expiration_time", value=cookie_expiration_time, expected_type=type_hints["cookie_expiration_time"])
            check_type(argname="argument logout_endpoint", value=logout_endpoint, expected_type=type_hints["logout_endpoint"])
            check_type(argname="argument nonce_expiration_time", value=nonce_expiration_time, expected_type=type_hints["nonce_expiration_time"])
            check_type(argname="argument preserve_url_fragments_for_logins", value=preserve_url_fragments_for_logins, expected_type=type_hints["preserve_url_fragments_for_logins"])
            check_type(argname="argument token_refresh_extension_time", value=token_refresh_extension_time, expected_type=type_hints["token_refresh_extension_time"])
            check_type(argname="argument token_store_enabled", value=token_store_enabled, expected_type=type_hints["token_store_enabled"])
            check_type(argname="argument token_store_path", value=token_store_path, expected_type=type_hints["token_store_path"])
            check_type(argname="argument token_store_sas_setting_name", value=token_store_sas_setting_name, expected_type=type_hints["token_store_sas_setting_name"])
            check_type(argname="argument validate_nonce", value=validate_nonce, expected_type=type_hints["validate_nonce"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_external_redirect_urls is not None:
            self._values["allowed_external_redirect_urls"] = allowed_external_redirect_urls
        if cookie_expiration_convention is not None:
            self._values["cookie_expiration_convention"] = cookie_expiration_convention
        if cookie_expiration_time is not None:
            self._values["cookie_expiration_time"] = cookie_expiration_time
        if logout_endpoint is not None:
            self._values["logout_endpoint"] = logout_endpoint
        if nonce_expiration_time is not None:
            self._values["nonce_expiration_time"] = nonce_expiration_time
        if preserve_url_fragments_for_logins is not None:
            self._values["preserve_url_fragments_for_logins"] = preserve_url_fragments_for_logins
        if token_refresh_extension_time is not None:
            self._values["token_refresh_extension_time"] = token_refresh_extension_time
        if token_store_enabled is not None:
            self._values["token_store_enabled"] = token_store_enabled
        if token_store_path is not None:
            self._values["token_store_path"] = token_store_path
        if token_store_sas_setting_name is not None:
            self._values["token_store_sas_setting_name"] = token_store_sas_setting_name
        if validate_nonce is not None:
            self._values["validate_nonce"] = validate_nonce

    @builtins.property
    def allowed_external_redirect_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''External URLs that can be redirected to as part of logging in or logging out of the app.

        This is an advanced setting typically only needed by Windows Store application backends. **Note:** URLs within the current domain are always implicitly allowed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        '''
        result = self._values.get("allowed_external_redirect_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cookie_expiration_convention(self) -> typing.Optional[builtins.str]:
        '''The method by which cookies expire. Possible values include: ``FixedTime``, and ``IdentityProviderDerived``. Defaults to ``FixedTime``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_convention WindowsWebAppSlot#cookie_expiration_convention}
        '''
        result = self._values.get("cookie_expiration_convention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cookie_expiration_time(self) -> typing.Optional[builtins.str]:
        '''The time after the request is made when the session cookie should expire. Defaults to ``08:00:00``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_time WindowsWebAppSlot#cookie_expiration_time}
        '''
        result = self._values.get("cookie_expiration_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logout_endpoint(self) -> typing.Optional[builtins.str]:
        '''The endpoint to which logout requests should be made.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logout_endpoint WindowsWebAppSlot#logout_endpoint}
        '''
        result = self._values.get("logout_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nonce_expiration_time(self) -> typing.Optional[builtins.str]:
        '''The time after the request is made when the nonce should expire. Defaults to ``00:05:00``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#nonce_expiration_time WindowsWebAppSlot#nonce_expiration_time}
        '''
        result = self._values.get("nonce_expiration_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_url_fragments_for_logins(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the fragments from the request be preserved after the login request is made. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#preserve_url_fragments_for_logins WindowsWebAppSlot#preserve_url_fragments_for_logins}
        '''
        result = self._values.get("preserve_url_fragments_for_logins")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def token_refresh_extension_time(self) -> typing.Optional[jsii.Number]:
        '''The number of hours after session token expiration that a session token can be used to call the token refresh API.

        Defaults to ``72`` hours.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_time WindowsWebAppSlot#token_refresh_extension_time}
        '''
        result = self._values.get("token_refresh_extension_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_store_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the Token Store configuration Enabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        '''
        result = self._values.get("token_store_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def token_store_path(self) -> typing.Optional[builtins.str]:
        '''The directory path in the App Filesystem in which the tokens will be stored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_path WindowsWebAppSlot#token_store_path}
        '''
        result = self._values.get("token_store_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_store_sas_setting_name(self) -> typing.Optional[builtins.str]:
        '''The name of the app setting which contains the SAS URL of the blob storage containing the tokens.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_sas_setting_name WindowsWebAppSlot#token_store_sas_setting_name}
        '''
        result = self._values.get("token_store_sas_setting_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_nonce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the nonce be validated while completing the login flow. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#validate_nonce WindowsWebAppSlot#validate_nonce}
        '''
        result = self._values.get("validate_nonce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2Login(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2LoginOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2LoginOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac56f5a2de09b1232fb36885229f7870f78a420471fc102a6abf5371378ef83)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExternalRedirectUrls")
    def reset_allowed_external_redirect_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExternalRedirectUrls", []))

    @jsii.member(jsii_name="resetCookieExpirationConvention")
    def reset_cookie_expiration_convention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieExpirationConvention", []))

    @jsii.member(jsii_name="resetCookieExpirationTime")
    def reset_cookie_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieExpirationTime", []))

    @jsii.member(jsii_name="resetLogoutEndpoint")
    def reset_logout_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoutEndpoint", []))

    @jsii.member(jsii_name="resetNonceExpirationTime")
    def reset_nonce_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonceExpirationTime", []))

    @jsii.member(jsii_name="resetPreserveUrlFragmentsForLogins")
    def reset_preserve_url_fragments_for_logins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveUrlFragmentsForLogins", []))

    @jsii.member(jsii_name="resetTokenRefreshExtensionTime")
    def reset_token_refresh_extension_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenRefreshExtensionTime", []))

    @jsii.member(jsii_name="resetTokenStoreEnabled")
    def reset_token_store_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenStoreEnabled", []))

    @jsii.member(jsii_name="resetTokenStorePath")
    def reset_token_store_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenStorePath", []))

    @jsii.member(jsii_name="resetTokenStoreSasSettingName")
    def reset_token_store_sas_setting_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenStoreSasSettingName", []))

    @jsii.member(jsii_name="resetValidateNonce")
    def reset_validate_nonce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateNonce", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrlsInput")
    def allowed_external_redirect_urls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedExternalRedirectUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationConventionInput")
    def cookie_expiration_convention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieExpirationConventionInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationTimeInput")
    def cookie_expiration_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieExpirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="logoutEndpointInput")
    def logout_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoutEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="nonceExpirationTimeInput")
    def nonce_expiration_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nonceExpirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveUrlFragmentsForLoginsInput")
    def preserve_url_fragments_for_logins_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preserveUrlFragmentsForLoginsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionTimeInput")
    def token_refresh_extension_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenRefreshExtensionTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabledInput")
    def token_store_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tokenStoreEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenStorePathInput")
    def token_store_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenStorePathInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenStoreSasSettingNameInput")
    def token_store_sas_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenStoreSasSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="validateNonceInput")
    def validate_nonce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "validateNonceInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedExternalRedirectUrls"))

    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4417ca3890410aa61b36c04c22fa6208003cd0cd3830a9a4d77c277a2a0a9a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExternalRedirectUrls", value)

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationConvention")
    def cookie_expiration_convention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieExpirationConvention"))

    @cookie_expiration_convention.setter
    def cookie_expiration_convention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7132540967c78955b1bdb69a2c0f1fb829eb4f14e557eba4de828687ade5daf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieExpirationConvention", value)

    @builtins.property
    @jsii.member(jsii_name="cookieExpirationTime")
    def cookie_expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieExpirationTime"))

    @cookie_expiration_time.setter
    def cookie_expiration_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3242000455594468b865842becff74609684d42513968328814a9491f60cdd5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieExpirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="logoutEndpoint")
    def logout_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoutEndpoint"))

    @logout_endpoint.setter
    def logout_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597195d049837207b77b086078071ea0902c000da472c1454b0dd22b1c68a6c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoutEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="nonceExpirationTime")
    def nonce_expiration_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nonceExpirationTime"))

    @nonce_expiration_time.setter
    def nonce_expiration_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41dea7f8495ee80f8799d61d7804b717d25ca68b1e4b248fbd2cab180b069e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonceExpirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="preserveUrlFragmentsForLogins")
    def preserve_url_fragments_for_logins(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preserveUrlFragmentsForLogins"))

    @preserve_url_fragments_for_logins.setter
    def preserve_url_fragments_for_logins(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e93d6d97e3117402570835b85649700103898b2d340f3a94122453ea5340f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveUrlFragmentsForLogins", value)

    @builtins.property
    @jsii.member(jsii_name="tokenRefreshExtensionTime")
    def token_refresh_extension_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenRefreshExtensionTime"))

    @token_refresh_extension_time.setter
    def token_refresh_extension_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798f6295f6936a28db9348babad6509f7b5ba2a4062b8f29eb20e426490cfd77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenRefreshExtensionTime", value)

    @builtins.property
    @jsii.member(jsii_name="tokenStoreEnabled")
    def token_store_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tokenStoreEnabled"))

    @token_store_enabled.setter
    def token_store_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6387f0a8119ff13c61f8762fe71e0b478c4d73a8be504502c2b833de007bb1bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tokenStorePath")
    def token_store_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenStorePath"))

    @token_store_path.setter
    def token_store_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5550012f41d85cf2cf82a1e9cec9d5e6bfdbc39dd4e1fb13f5d49e9bb058de90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStorePath", value)

    @builtins.property
    @jsii.member(jsii_name="tokenStoreSasSettingName")
    def token_store_sas_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenStoreSasSettingName"))

    @token_store_sas_setting_name.setter
    def token_store_sas_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3792801f29804c559647a7f34ad43f98493925aecf8b995d34f62423f27f8218)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenStoreSasSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="validateNonce")
    def validate_nonce(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "validateNonce"))

    @validate_nonce.setter
    def validate_nonce(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbda8461b86a72e5eeed1ee5293b74b2bcc54e673472c5fbf26d7f67d44ce822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validateNonce", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2Login]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2Login], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2Login],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c3cd0f99218a1048aa86cf8ecff6c0b45a6c0ad8b30666ff20ba63e34ac0467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2MicrosoftV2",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_setting_name": "clientSecretSettingName",
        "allowed_audiences": "allowedAudiences",
        "login_scopes": "loginScopes",
    },
)
class WindowsWebAppSlotAuthSettingsV2MicrosoftV2:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param allowed_audiences: Specifies a list of Allowed Audiences that will be requested as part of Microsoft Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param login_scopes: The list of Login scopes that will be requested as part of Microsoft Account authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c179e2c7556f4f4da602f302da863d88cfc03be106d09de52f7846bffac2cbc6)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_setting_name", value=client_secret_setting_name, expected_type=type_hints["client_secret_setting_name"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument login_scopes", value=login_scopes, expected_type=type_hints["login_scopes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_setting_name": client_secret_setting_name,
        }
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if login_scopes is not None:
            self._values["login_scopes"] = login_scopes

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The OAuth 2.0 client ID that was created for the app used for authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_setting_name(self) -> builtins.str:
        '''The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        result = self._values.get("client_secret_setting_name")
        assert result is not None, "Required property 'client_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of Allowed Audiences that will be requested as part of Microsoft Sign-In authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of Login scopes that will be requested as part of Microsoft Account authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        result = self._values.get("login_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2MicrosoftV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2MicrosoftV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2MicrosoftV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fbd1410ce18da70808126e4fce9cc08519906c2a7d9c0c116ab1e100047676)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetLoginScopes")
    def reset_login_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginScopes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingNameInput")
    def client_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loginScopesInput")
    def login_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loginScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0470457fec5a51ed43ab42684e78b84ef05d62c6b02eb4ec039a4d48f085c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d575bc5708facb77b3e21b5a1345f6f76de549ee7ca6d862e7a2b09ff3a3b214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretSettingName")
    def client_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretSettingName"))

    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10d97e3185e0d3a4d6ebf2e62d31f2a267a82fcc2ea7e4aada9a99fc90ceb098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="loginScopes")
    def login_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loginScopes"))

    @login_scopes.setter
    def login_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577bf794417bc7565df1c8e1b5821fbafea82c69cd13c8d970e2f8e71cfe9891)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ff7a8816d525ea5020d064c66e380bbf03490982f5ee132eb5be14a7eca850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotAuthSettingsV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__108df4830944e5a59d1c700cea5488c987b329842062f7bd35ea589d8593b23d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveDirectoryV2")
    def put_active_directory_v2(
        self,
        *,
        client_id: builtins.str,
        tenant_auth_endpoint: builtins.str,
        allowed_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_secret_certificate_thumbprint: typing.Optional[builtins.str] = None,
        client_secret_setting_name: typing.Optional[builtins.str] = None,
        jwt_allowed_client_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
        jwt_allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        www_authentication_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param tenant_auth_endpoint: The Azure Tenant Endpoint for the Authenticating Tenant. e.g. ``https://login.microsoftonline.com/v2.0/{tenant-guid}/``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tenant_auth_endpoint WindowsWebAppSlot#tenant_auth_endpoint}
        :param allowed_applications: The list of allowed Applications for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_applications WindowsWebAppSlot#allowed_applications}
        :param allowed_audiences: Specifies a list of Allowed audience values to consider when validating JWTs issued by Azure Active Directory. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param allowed_groups: The list of allowed Group Names for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_groups WindowsWebAppSlot#allowed_groups}
        :param allowed_identities: The list of allowed Identities for the Default Authorisation Policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_identities WindowsWebAppSlot#allowed_identities}
        :param client_secret_certificate_thumbprint: The thumbprint of the certificate used for signing purposes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_certificate_thumbprint WindowsWebAppSlot#client_secret_certificate_thumbprint}
        :param client_secret_setting_name: The App Setting name that contains the client secret of the Client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param jwt_allowed_client_applications: A list of Allowed Client Applications in the JWT Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_client_applications WindowsWebAppSlot#jwt_allowed_client_applications}
        :param jwt_allowed_groups: A list of Allowed Groups in the JWT Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#jwt_allowed_groups WindowsWebAppSlot#jwt_allowed_groups}
        :param login_parameters: A map of key-value pairs to send to the Authorisation Endpoint when a user logs in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_parameters WindowsWebAppSlot#login_parameters}
        :param www_authentication_disabled: Should the www-authenticate provider should be omitted from the request? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#www_authentication_disabled WindowsWebAppSlot#www_authentication_disabled}
        '''
        value = WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2(
            client_id=client_id,
            tenant_auth_endpoint=tenant_auth_endpoint,
            allowed_applications=allowed_applications,
            allowed_audiences=allowed_audiences,
            allowed_groups=allowed_groups,
            allowed_identities=allowed_identities,
            client_secret_certificate_thumbprint=client_secret_certificate_thumbprint,
            client_secret_setting_name=client_secret_setting_name,
            jwt_allowed_client_applications=jwt_allowed_client_applications,
            jwt_allowed_groups=jwt_allowed_groups,
            login_parameters=login_parameters,
            www_authentication_disabled=www_authentication_disabled,
        )

        return typing.cast(None, jsii.invoke(self, "putActiveDirectoryV2", [value]))

    @jsii.member(jsii_name="putAppleV2")
    def put_apple_v2(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Apple web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Apple Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsV2AppleV2(
            client_id=client_id, client_secret_setting_name=client_secret_setting_name
        )

        return typing.cast(None, jsii.invoke(self, "putAppleV2", [value]))

    @jsii.member(jsii_name="putAzureStaticWebAppV2")
    def put_azure_static_web_app_v2(self, *, client_id: builtins.str) -> None:
        '''
        :param client_id: The ID of the Client to use to authenticate with Azure Static Web App Authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        '''
        value = WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2(client_id=client_id)

        return typing.cast(None, jsii.invoke(self, "putAzureStaticWebAppV2", [value]))

    @jsii.member(jsii_name="putCustomOidcV2")
    def put_custom_oidc_v2(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16cee008df7359c5e0c31710232f3c1f9da5df646113a1c9c0a05403139d16dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomOidcV2", [value]))

    @jsii.member(jsii_name="putFacebookV2")
    def put_facebook_v2(
        self,
        *,
        app_id: builtins.str,
        app_secret_setting_name: builtins.str,
        graph_api_version: typing.Optional[builtins.str] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_id: The App ID of the Facebook app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_id WindowsWebAppSlot#app_id}
        :param app_secret_setting_name: The app setting name that contains the ``app_secret`` value used for Facebook Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_secret_setting_name WindowsWebAppSlot#app_secret_setting_name}
        :param graph_api_version: The version of the Facebook API to be used while logging in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#graph_api_version WindowsWebAppSlot#graph_api_version}
        :param login_scopes: Specifies a list of scopes to be requested as part of Facebook Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsV2FacebookV2(
            app_id=app_id,
            app_secret_setting_name=app_secret_setting_name,
            graph_api_version=graph_api_version,
            login_scopes=login_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putFacebookV2", [value]))

    @jsii.member(jsii_name="putGithubV2")
    def put_github_v2(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The ID of the GitHub app used for login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for GitHub Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param login_scopes: Specifies a list of OAuth 2.0 scopes that will be requested as part of GitHub Login authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsV2GithubV2(
            client_id=client_id,
            client_secret_setting_name=client_secret_setting_name,
            login_scopes=login_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGithubV2", [value]))

    @jsii.member(jsii_name="putGoogleV2")
    def put_google_v2(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OpenID Connect Client ID for the Google web application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name that contains the ``client_secret`` value used for Google Login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param allowed_audiences: Specifies a list of Allowed Audiences that will be requested as part of Google Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param login_scopes: Specifies a list of Login scopes that will be requested as part of Google Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsV2GoogleV2(
            client_id=client_id,
            client_secret_setting_name=client_secret_setting_name,
            allowed_audiences=allowed_audiences,
            login_scopes=login_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleV2", [value]))

    @jsii.member(jsii_name="putLogin")
    def put_login(
        self,
        *,
        allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        cookie_expiration_convention: typing.Optional[builtins.str] = None,
        cookie_expiration_time: typing.Optional[builtins.str] = None,
        logout_endpoint: typing.Optional[builtins.str] = None,
        nonce_expiration_time: typing.Optional[builtins.str] = None,
        preserve_url_fragments_for_logins: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token_refresh_extension_time: typing.Optional[jsii.Number] = None,
        token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token_store_path: typing.Optional[builtins.str] = None,
        token_store_sas_setting_name: typing.Optional[builtins.str] = None,
        validate_nonce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_external_redirect_urls: External URLs that can be redirected to as part of logging in or logging out of the app. This is an advanced setting typically only needed by Windows Store application backends. **Note:** URLs within the current domain are always implicitly allowed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_external_redirect_urls WindowsWebAppSlot#allowed_external_redirect_urls}
        :param cookie_expiration_convention: The method by which cookies expire. Possible values include: ``FixedTime``, and ``IdentityProviderDerived``. Defaults to ``FixedTime``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_convention WindowsWebAppSlot#cookie_expiration_convention}
        :param cookie_expiration_time: The time after the request is made when the session cookie should expire. Defaults to ``08:00:00``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cookie_expiration_time WindowsWebAppSlot#cookie_expiration_time}
        :param logout_endpoint: The endpoint to which logout requests should be made. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logout_endpoint WindowsWebAppSlot#logout_endpoint}
        :param nonce_expiration_time: The time after the request is made when the nonce should expire. Defaults to ``00:05:00``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#nonce_expiration_time WindowsWebAppSlot#nonce_expiration_time}
        :param preserve_url_fragments_for_logins: Should the fragments from the request be preserved after the login request is made. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#preserve_url_fragments_for_logins WindowsWebAppSlot#preserve_url_fragments_for_logins}
        :param token_refresh_extension_time: The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to ``72`` hours. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_refresh_extension_time WindowsWebAppSlot#token_refresh_extension_time}
        :param token_store_enabled: Should the Token Store configuration Enabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_enabled WindowsWebAppSlot#token_store_enabled}
        :param token_store_path: The directory path in the App Filesystem in which the tokens will be stored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_path WindowsWebAppSlot#token_store_path}
        :param token_store_sas_setting_name: The name of the app setting which contains the SAS URL of the blob storage containing the tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#token_store_sas_setting_name WindowsWebAppSlot#token_store_sas_setting_name}
        :param validate_nonce: Should the nonce be validated while completing the login flow. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#validate_nonce WindowsWebAppSlot#validate_nonce}
        '''
        value = WindowsWebAppSlotAuthSettingsV2Login(
            allowed_external_redirect_urls=allowed_external_redirect_urls,
            cookie_expiration_convention=cookie_expiration_convention,
            cookie_expiration_time=cookie_expiration_time,
            logout_endpoint=logout_endpoint,
            nonce_expiration_time=nonce_expiration_time,
            preserve_url_fragments_for_logins=preserve_url_fragments_for_logins,
            token_refresh_extension_time=token_refresh_extension_time,
            token_store_enabled=token_store_enabled,
            token_store_path=token_store_path,
            token_store_sas_setting_name=token_store_sas_setting_name,
            validate_nonce=validate_nonce,
        )

        return typing.cast(None, jsii.invoke(self, "putLogin", [value]))

    @jsii.member(jsii_name="putMicrosoftV2")
    def put_microsoft_v2(
        self,
        *,
        client_id: builtins.str,
        client_secret_setting_name: builtins.str,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_id: The OAuth 2.0 client ID that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_id WindowsWebAppSlot#client_id}
        :param client_secret_setting_name: The app setting name containing the OAuth 2.0 client secret that was created for the app used for authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_secret_setting_name WindowsWebAppSlot#client_secret_setting_name}
        :param allowed_audiences: Specifies a list of Allowed Audiences that will be requested as part of Microsoft Sign-In authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_audiences WindowsWebAppSlot#allowed_audiences}
        :param login_scopes: The list of Login scopes that will be requested as part of Microsoft Account authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#login_scopes WindowsWebAppSlot#login_scopes}
        '''
        value = WindowsWebAppSlotAuthSettingsV2MicrosoftV2(
            client_id=client_id,
            client_secret_setting_name=client_secret_setting_name,
            allowed_audiences=allowed_audiences,
            login_scopes=login_scopes,
        )

        return typing.cast(None, jsii.invoke(self, "putMicrosoftV2", [value]))

    @jsii.member(jsii_name="putTwitterV2")
    def put_twitter_v2(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret_setting_name: builtins.str,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        value = WindowsWebAppSlotAuthSettingsV2TwitterV2(
            consumer_key=consumer_key,
            consumer_secret_setting_name=consumer_secret_setting_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTwitterV2", [value]))

    @jsii.member(jsii_name="resetActiveDirectoryV2")
    def reset_active_directory_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveDirectoryV2", []))

    @jsii.member(jsii_name="resetAppleV2")
    def reset_apple_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppleV2", []))

    @jsii.member(jsii_name="resetAuthEnabled")
    def reset_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthEnabled", []))

    @jsii.member(jsii_name="resetAzureStaticWebAppV2")
    def reset_azure_static_web_app_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureStaticWebAppV2", []))

    @jsii.member(jsii_name="resetConfigFilePath")
    def reset_config_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigFilePath", []))

    @jsii.member(jsii_name="resetCustomOidcV2")
    def reset_custom_oidc_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomOidcV2", []))

    @jsii.member(jsii_name="resetDefaultProvider")
    def reset_default_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultProvider", []))

    @jsii.member(jsii_name="resetExcludedPaths")
    def reset_excluded_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedPaths", []))

    @jsii.member(jsii_name="resetFacebookV2")
    def reset_facebook_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacebookV2", []))

    @jsii.member(jsii_name="resetForwardProxyConvention")
    def reset_forward_proxy_convention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardProxyConvention", []))

    @jsii.member(jsii_name="resetForwardProxyCustomHostHeaderName")
    def reset_forward_proxy_custom_host_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardProxyCustomHostHeaderName", []))

    @jsii.member(jsii_name="resetForwardProxyCustomSchemeHeaderName")
    def reset_forward_proxy_custom_scheme_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardProxyCustomSchemeHeaderName", []))

    @jsii.member(jsii_name="resetGithubV2")
    def reset_github_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubV2", []))

    @jsii.member(jsii_name="resetGoogleV2")
    def reset_google_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleV2", []))

    @jsii.member(jsii_name="resetHttpRouteApiPrefix")
    def reset_http_route_api_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRouteApiPrefix", []))

    @jsii.member(jsii_name="resetMicrosoftV2")
    def reset_microsoft_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMicrosoftV2", []))

    @jsii.member(jsii_name="resetRequireAuthentication")
    def reset_require_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireAuthentication", []))

    @jsii.member(jsii_name="resetRequireHttps")
    def reset_require_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireHttps", []))

    @jsii.member(jsii_name="resetRuntimeVersion")
    def reset_runtime_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeVersion", []))

    @jsii.member(jsii_name="resetTwitterV2")
    def reset_twitter_v2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTwitterV2", []))

    @jsii.member(jsii_name="resetUnauthenticatedAction")
    def reset_unauthenticated_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnauthenticatedAction", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryV2")
    def active_directory_v2(
        self,
    ) -> WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2OutputReference, jsii.get(self, "activeDirectoryV2"))

    @builtins.property
    @jsii.member(jsii_name="appleV2")
    def apple_v2(self) -> WindowsWebAppSlotAuthSettingsV2AppleV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2AppleV2OutputReference, jsii.get(self, "appleV2"))

    @builtins.property
    @jsii.member(jsii_name="azureStaticWebAppV2")
    def azure_static_web_app_v2(
        self,
    ) -> WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2OutputReference, jsii.get(self, "azureStaticWebAppV2"))

    @builtins.property
    @jsii.member(jsii_name="customOidcV2")
    def custom_oidc_v2(self) -> WindowsWebAppSlotAuthSettingsV2CustomOidcV2List:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2CustomOidcV2List, jsii.get(self, "customOidcV2"))

    @builtins.property
    @jsii.member(jsii_name="facebookV2")
    def facebook_v2(self) -> WindowsWebAppSlotAuthSettingsV2FacebookV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2FacebookV2OutputReference, jsii.get(self, "facebookV2"))

    @builtins.property
    @jsii.member(jsii_name="githubV2")
    def github_v2(self) -> WindowsWebAppSlotAuthSettingsV2GithubV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2GithubV2OutputReference, jsii.get(self, "githubV2"))

    @builtins.property
    @jsii.member(jsii_name="googleV2")
    def google_v2(self) -> WindowsWebAppSlotAuthSettingsV2GoogleV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2GoogleV2OutputReference, jsii.get(self, "googleV2"))

    @builtins.property
    @jsii.member(jsii_name="login")
    def login(self) -> WindowsWebAppSlotAuthSettingsV2LoginOutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2LoginOutputReference, jsii.get(self, "login"))

    @builtins.property
    @jsii.member(jsii_name="microsoftV2")
    def microsoft_v2(self) -> WindowsWebAppSlotAuthSettingsV2MicrosoftV2OutputReference:
        return typing.cast(WindowsWebAppSlotAuthSettingsV2MicrosoftV2OutputReference, jsii.get(self, "microsoftV2"))

    @builtins.property
    @jsii.member(jsii_name="twitterV2")
    def twitter_v2(self) -> "WindowsWebAppSlotAuthSettingsV2TwitterV2OutputReference":
        return typing.cast("WindowsWebAppSlotAuthSettingsV2TwitterV2OutputReference", jsii.get(self, "twitterV2"))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryV2Input")
    def active_directory_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2], jsii.get(self, "activeDirectoryV2Input"))

    @builtins.property
    @jsii.member(jsii_name="appleV2Input")
    def apple_v2_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2], jsii.get(self, "appleV2Input"))

    @builtins.property
    @jsii.member(jsii_name="authEnabledInput")
    def auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "authEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="azureStaticWebAppV2Input")
    def azure_static_web_app_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2], jsii.get(self, "azureStaticWebAppV2Input"))

    @builtins.property
    @jsii.member(jsii_name="configFilePathInput")
    def config_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="customOidcV2Input")
    def custom_oidc_v2_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]], jsii.get(self, "customOidcV2Input"))

    @builtins.property
    @jsii.member(jsii_name="defaultProviderInput")
    def default_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedPathsInput")
    def excluded_paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="facebookV2Input")
    def facebook_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2], jsii.get(self, "facebookV2Input"))

    @builtins.property
    @jsii.member(jsii_name="forwardProxyConventionInput")
    def forward_proxy_convention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardProxyConventionInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardProxyCustomHostHeaderNameInput")
    def forward_proxy_custom_host_header_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardProxyCustomHostHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardProxyCustomSchemeHeaderNameInput")
    def forward_proxy_custom_scheme_header_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardProxyCustomSchemeHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="githubV2Input")
    def github_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2], jsii.get(self, "githubV2Input"))

    @builtins.property
    @jsii.member(jsii_name="googleV2Input")
    def google_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2], jsii.get(self, "googleV2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpRouteApiPrefixInput")
    def http_route_api_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpRouteApiPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="loginInput")
    def login_input(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2Login]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2Login], jsii.get(self, "loginInput"))

    @builtins.property
    @jsii.member(jsii_name="microsoftV2Input")
    def microsoft_v2_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2], jsii.get(self, "microsoftV2Input"))

    @builtins.property
    @jsii.member(jsii_name="requireAuthenticationInput")
    def require_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="requireHttpsInput")
    def require_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeVersionInput")
    def runtime_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="twitterV2Input")
    def twitter_v2_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotAuthSettingsV2TwitterV2"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotAuthSettingsV2TwitterV2"], jsii.get(self, "twitterV2Input"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedActionInput")
    def unauthenticated_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unauthenticatedActionInput"))

    @builtins.property
    @jsii.member(jsii_name="authEnabled")
    def auth_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "authEnabled"))

    @auth_enabled.setter
    def auth_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94bf4e8b695c9665651522d7028e7467606e02b82a10c8e65361c5ca096adfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="configFilePath")
    def config_file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configFilePath"))

    @config_file_path.setter
    def config_file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__919c4d6142e2ae4752781e4e929a0b7e44548db4f1e0bfd86a9ed4d3661c94c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProvider")
    def default_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProvider"))

    @default_provider.setter
    def default_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22b47b7de01d808ec711896c72063b50d476c29806096624f9c24417854aed5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProvider", value)

    @builtins.property
    @jsii.member(jsii_name="excludedPaths")
    def excluded_paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedPaths"))

    @excluded_paths.setter
    def excluded_paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cd7ea40fdab5e47e28db2020aea6e21132f862be37325842d746acb1ccd520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedPaths", value)

    @builtins.property
    @jsii.member(jsii_name="forwardProxyConvention")
    def forward_proxy_convention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardProxyConvention"))

    @forward_proxy_convention.setter
    def forward_proxy_convention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b08014f045ef783297219e85a0689c2a8415c2854c08927f3bbfba377827250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardProxyConvention", value)

    @builtins.property
    @jsii.member(jsii_name="forwardProxyCustomHostHeaderName")
    def forward_proxy_custom_host_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardProxyCustomHostHeaderName"))

    @forward_proxy_custom_host_header_name.setter
    def forward_proxy_custom_host_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f389b518fc5950e3b3f35f51c0b0f6502d3810b387ba67ea659894ed0c5c2cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardProxyCustomHostHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="forwardProxyCustomSchemeHeaderName")
    def forward_proxy_custom_scheme_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardProxyCustomSchemeHeaderName"))

    @forward_proxy_custom_scheme_header_name.setter
    def forward_proxy_custom_scheme_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23983a2135f48ae128f21e5338e46853c938e12df6f9351c1aa072d2ab383d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardProxyCustomSchemeHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="httpRouteApiPrefix")
    def http_route_api_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpRouteApiPrefix"))

    @http_route_api_prefix.setter
    def http_route_api_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566db5470b19c94dd253fae250b230902b5b7b9a7a9791bd566d50d73e84ae7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRouteApiPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="requireAuthentication")
    def require_authentication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireAuthentication"))

    @require_authentication.setter
    def require_authentication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb84980945373e7167e11081f04afe31ddb8542200ab145b091e7be630b878a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="requireHttps")
    def require_https(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireHttps"))

    @require_https.setter
    def require_https(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be55bad382b0f6e999a38a695a63c4a80c6887545f90d12e31b58a5821e75fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireHttps", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba220dc112c26b7db193bdd32c3f2b20aee9b003b0e345c78bc932ae79d891d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedAction")
    def unauthenticated_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthenticatedAction"))

    @unauthenticated_action.setter
    def unauthenticated_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b510f50cca74ec9fe0627289957b8e577fdf233af74c06f5b90903a6c287447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticatedAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb60e6b486fec3d5cbedec2f1f87e16da4792205dd87e2272a104331f14ccc20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2TwitterV2",
    jsii_struct_bases=[],
    name_mapping={
        "consumer_key": "consumerKey",
        "consumer_secret_setting_name": "consumerSecretSettingName",
    },
)
class WindowsWebAppSlotAuthSettingsV2TwitterV2:
    def __init__(
        self,
        *,
        consumer_key: builtins.str,
        consumer_secret_setting_name: builtins.str,
    ) -> None:
        '''
        :param consumer_key: The OAuth 1.0a consumer key of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        :param consumer_secret_setting_name: The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e57466984bde9e623e489d52c57a3e2ebc3a3ba3ca789f42beb70dd36544b03)
            check_type(argname="argument consumer_key", value=consumer_key, expected_type=type_hints["consumer_key"])
            check_type(argname="argument consumer_secret_setting_name", value=consumer_secret_setting_name, expected_type=type_hints["consumer_secret_setting_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_key": consumer_key,
            "consumer_secret_setting_name": consumer_secret_setting_name,
        }

    @builtins.property
    def consumer_key(self) -> builtins.str:
        '''The OAuth 1.0a consumer key of the Twitter application used for sign-in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_key WindowsWebAppSlot#consumer_key}
        '''
        result = self._values.get("consumer_key")
        assert result is not None, "Required property 'consumer_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumer_secret_setting_name(self) -> builtins.str:
        '''The app setting name that contains the OAuth 1.0a consumer secret of the Twitter application used for sign-in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#consumer_secret_setting_name WindowsWebAppSlot#consumer_secret_setting_name}
        '''
        result = self._values.get("consumer_secret_setting_name")
        assert result is not None, "Required property 'consumer_secret_setting_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotAuthSettingsV2TwitterV2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotAuthSettingsV2TwitterV2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotAuthSettingsV2TwitterV2OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a6d538338d4f6e176ecc1d27489d3899a89fb569368e767c957ba782f7f8536)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="consumerKeyInput")
    def consumer_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingNameInput")
    def consumer_secret_setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consumerSecretSettingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consumerKey")
    def consumer_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerKey"))

    @consumer_key.setter
    def consumer_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d788f1f641acca0eaf1afdeadd34c6a3647ecca1680144ac593d20b6d9e903be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerKey", value)

    @builtins.property
    @jsii.member(jsii_name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumerSecretSettingName"))

    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e8f92a5cad66e47a6a5cc4880a9855cf74fd532bd27ea4823cb5e2dd6e32c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumerSecretSettingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2TwitterV2]:
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2TwitterV2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotAuthSettingsV2TwitterV2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1baf9bbe9df74d3d84e11d07dc11816abcebd7e04d85cf5b3c67da07ff04f678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackup",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schedule": "schedule",
        "storage_account_url": "storageAccountUrl",
        "enabled": "enabled",
    },
)
class WindowsWebAppSlotBackup:
    def __init__(
        self,
        *,
        name: builtins.str,
        schedule: typing.Union["WindowsWebAppSlotBackupSchedule", typing.Dict[builtins.str, typing.Any]],
        storage_account_url: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param name: The name which should be used for this Backup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        :param storage_account_url: The SAS URL to the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        :param enabled: Should this backup job be enabled? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        if isinstance(schedule, dict):
            schedule = WindowsWebAppSlotBackupSchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325a76a23950dbd0dc1baabfff7db683f6b40882ea11bb14885e314e90801bcd)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument storage_account_url", value=storage_account_url, expected_type=type_hints["storage_account_url"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "schedule": schedule,
            "storage_account_url": storage_account_url,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def name(self) -> builtins.str:
        '''The name which should be used for this Backup.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> "WindowsWebAppSlotBackupSchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#schedule WindowsWebAppSlot#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("WindowsWebAppSlotBackupSchedule", result)

    @builtins.property
    def storage_account_url(self) -> builtins.str:
        '''The SAS URL to the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account_url WindowsWebAppSlot#storage_account_url}
        '''
        result = self._values.get("storage_account_url")
        assert result is not None, "Required property 'storage_account_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should this backup job be enabled?

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotBackupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ebe259c0bb63b8bf63f04aa124993db9f429c8523536886aa8260508434654)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        frequency_interval: jsii.Number,
        frequency_unit: builtins.str,
        keep_at_least_one_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        value = WindowsWebAppSlotBackupSchedule(
            frequency_interval=frequency_interval,
            frequency_unit=frequency_unit,
            keep_at_least_one_backup=keep_at_least_one_backup,
            retention_period_days=retention_period_days,
            start_time=start_time,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "WindowsWebAppSlotBackupScheduleOutputReference":
        return typing.cast("WindowsWebAppSlotBackupScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["WindowsWebAppSlotBackupSchedule"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotBackupSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrlInput")
    def storage_account_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__319d30e342b04a23ea3421984febb6d13d50d41ac2aa5aef50dd13c5306cf1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322c9555caacd6cdd1a53b46894e1690014f95798ce3b7b2c04ed8a718daae22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountUrl")
    def storage_account_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUrl"))

    @storage_account_url.setter
    def storage_account_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94db0bcced776ee7264d94653598037fa9472349e8ebf34493851ee67763513f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotBackup]:
        return typing.cast(typing.Optional[WindowsWebAppSlotBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotBackup]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7686083c37047d402f5cd42574de7ad73f2d886a5543bba49686eba9d7bad53e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "frequency_interval": "frequencyInterval",
        "frequency_unit": "frequencyUnit",
        "keep_at_least_one_backup": "keepAtLeastOneBackup",
        "retention_period_days": "retentionPeriodDays",
        "start_time": "startTime",
    },
)
class WindowsWebAppSlotBackupSchedule:
    def __init__(
        self,
        *,
        frequency_interval: jsii.Number,
        frequency_unit: builtins.str,
        keep_at_least_one_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        retention_period_days: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param frequency_interval: How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        :param frequency_unit: The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        :param keep_at_least_one_backup: Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        :param retention_period_days: After how many days backups should be deleted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        :param start_time: When the schedule should start working in RFC-3339 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b188522e4f8c4dd100af3011ff6f5b6301336943e80a86cb3ececfed7b37101)
            check_type(argname="argument frequency_interval", value=frequency_interval, expected_type=type_hints["frequency_interval"])
            check_type(argname="argument frequency_unit", value=frequency_unit, expected_type=type_hints["frequency_unit"])
            check_type(argname="argument keep_at_least_one_backup", value=keep_at_least_one_backup, expected_type=type_hints["keep_at_least_one_backup"])
            check_type(argname="argument retention_period_days", value=retention_period_days, expected_type=type_hints["retention_period_days"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "frequency_interval": frequency_interval,
            "frequency_unit": frequency_unit,
        }
        if keep_at_least_one_backup is not None:
            self._values["keep_at_least_one_backup"] = keep_at_least_one_backup
        if retention_period_days is not None:
            self._values["retention_period_days"] = retention_period_days
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def frequency_interval(self) -> jsii.Number:
        '''How often the backup should be executed (e.g. for weekly backup, this should be set to ``7`` and ``frequency_unit`` should be set to ``Day``).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_interval WindowsWebAppSlot#frequency_interval}
        '''
        result = self._values.get("frequency_interval")
        assert result is not None, "Required property 'frequency_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frequency_unit(self) -> builtins.str:
        '''The unit of time for how often the backup should take place. Possible values include: ``Day`` and ``Hour``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#frequency_unit WindowsWebAppSlot#frequency_unit}
        '''
        result = self._values.get("frequency_unit")
        assert result is not None, "Required property 'frequency_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def keep_at_least_one_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the service keep at least one backup, regardless of age of backup. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#keep_at_least_one_backup WindowsWebAppSlot#keep_at_least_one_backup}
        '''
        result = self._values.get("keep_at_least_one_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def retention_period_days(self) -> typing.Optional[jsii.Number]:
        '''After how many days backups should be deleted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_period_days WindowsWebAppSlot#retention_period_days}
        '''
        result = self._values.get("retention_period_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''When the schedule should start working in RFC-3339 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#start_time WindowsWebAppSlot#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotBackupSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotBackupScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotBackupScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffe9f21713c445eec94054e4a73a3477d3ae144c072ef3ad1bbf043e2826b99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeepAtLeastOneBackup")
    def reset_keep_at_least_one_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepAtLeastOneBackup", []))

    @jsii.member(jsii_name="resetRetentionPeriodDays")
    def reset_retention_period_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPeriodDays", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="lastExecutionTime")
    def last_execution_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastExecutionTime"))

    @builtins.property
    @jsii.member(jsii_name="frequencyIntervalInput")
    def frequency_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyUnitInput")
    def frequency_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="keepAtLeastOneBackupInput")
    def keep_at_least_one_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepAtLeastOneBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDaysInput")
    def retention_period_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInterval")
    def frequency_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequencyInterval"))

    @frequency_interval.setter
    def frequency_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a12d761012a8750c9708faff859087b325352031af8d73194d3574457b1fa2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyInterval", value)

    @builtins.property
    @jsii.member(jsii_name="frequencyUnit")
    def frequency_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequencyUnit"))

    @frequency_unit.setter
    def frequency_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabaf67073fb453f4d8888b5102851a341caad19cc189023b3556f487b57811a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyUnit", value)

    @builtins.property
    @jsii.member(jsii_name="keepAtLeastOneBackup")
    def keep_at_least_one_backup(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "keepAtLeastOneBackup"))

    @keep_at_least_one_backup.setter
    def keep_at_least_one_backup(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d947c05d625fff5351be77278b998b0935b150138178323c5d417e072835c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAtLeastOneBackup", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodDays")
    def retention_period_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodDays"))

    @retention_period_days.setter
    def retention_period_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903c26d6e79cd5f303352fa21e0a1c10883066b39f391a844d2eccea2ec7dabd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodDays", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e55bd2ab4594514ce63b23c3490688480126463dd013c8b5508e9cfd192d5f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotBackupSchedule]:
        return typing.cast(typing.Optional[WindowsWebAppSlotBackupSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotBackupSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5cb9df534023f4f3ab9e62763c6e047a0d0f409c8de9779a5cf4d2ff8360dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_service_id": "appServiceId",
        "name": "name",
        "site_config": "siteConfig",
        "app_settings": "appSettings",
        "auth_settings": "authSettings",
        "auth_settings_v2": "authSettingsV2",
        "backup": "backup",
        "client_affinity_enabled": "clientAffinityEnabled",
        "client_certificate_enabled": "clientCertificateEnabled",
        "client_certificate_exclusion_paths": "clientCertificateExclusionPaths",
        "client_certificate_mode": "clientCertificateMode",
        "connection_string": "connectionString",
        "enabled": "enabled",
        "https_only": "httpsOnly",
        "id": "id",
        "identity": "identity",
        "key_vault_reference_identity_id": "keyVaultReferenceIdentityId",
        "logs": "logs",
        "service_plan_id": "servicePlanId",
        "storage_account": "storageAccount",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
        "zip_deploy_file": "zipDeployFile",
    },
)
class WindowsWebAppSlotConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        app_service_id: builtins.str,
        name: builtins.str,
        site_config: typing.Union["WindowsWebAppSlotSiteConfig", typing.Dict[builtins.str, typing.Any]],
        app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        auth_settings: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        auth_settings_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2, typing.Dict[builtins.str, typing.Any]]] = None,
        backup: typing.Optional[typing.Union[WindowsWebAppSlotBackup, typing.Dict[builtins.str, typing.Any]]] = None,
        client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        client_certificate_exclusion_paths: typing.Optional[builtins.str] = None,
        client_certificate_mode: typing.Optional[builtins.str] = None,
        connection_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotConnectionString", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        https_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsWebAppSlotIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
        logs: typing.Optional[typing.Union["WindowsWebAppSlotLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        service_plan_id: typing.Optional[builtins.str] = None,
        storage_account: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotStorageAccount", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsWebAppSlotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
        zip_deploy_file: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param app_service_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param site_config: site_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        :param app_settings: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.
        :param auth_settings: auth_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        :param auth_settings_v2: auth_settings_v2 block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings_v2 WindowsWebAppSlot#auth_settings_v2}
        :param backup: backup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        :param client_affinity_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.
        :param client_certificate_exclusion_paths: Paths to exclude when using client certificates, separated by ; Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_exclusion_paths WindowsWebAppSlot#client_certificate_exclusion_paths}
        :param client_certificate_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.
        :param connection_string: connection_string block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.
        :param https_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#id WindowsWebAppSlot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        :param key_vault_reference_identity_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.
        :param logs: logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        :param service_plan_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_plan_id WindowsWebAppSlot#service_plan_id}.
        :param storage_account: storage_account block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tags WindowsWebAppSlot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        :param virtual_network_subnet_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.
        :param zip_deploy_file: The local path and filename of the Zip packaged application to deploy to this Windows Web App. **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(site_config, dict):
            site_config = WindowsWebAppSlotSiteConfig(**site_config)
        if isinstance(auth_settings, dict):
            auth_settings = WindowsWebAppSlotAuthSettings(**auth_settings)
        if isinstance(auth_settings_v2, dict):
            auth_settings_v2 = WindowsWebAppSlotAuthSettingsV2(**auth_settings_v2)
        if isinstance(backup, dict):
            backup = WindowsWebAppSlotBackup(**backup)
        if isinstance(identity, dict):
            identity = WindowsWebAppSlotIdentity(**identity)
        if isinstance(logs, dict):
            logs = WindowsWebAppSlotLogs(**logs)
        if isinstance(timeouts, dict):
            timeouts = WindowsWebAppSlotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f00c7455d1f916580d990d3c32b78551ea4dd93db7dd917a7ea0c18d245a04f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_service_id", value=app_service_id, expected_type=type_hints["app_service_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument site_config", value=site_config, expected_type=type_hints["site_config"])
            check_type(argname="argument app_settings", value=app_settings, expected_type=type_hints["app_settings"])
            check_type(argname="argument auth_settings", value=auth_settings, expected_type=type_hints["auth_settings"])
            check_type(argname="argument auth_settings_v2", value=auth_settings_v2, expected_type=type_hints["auth_settings_v2"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument client_affinity_enabled", value=client_affinity_enabled, expected_type=type_hints["client_affinity_enabled"])
            check_type(argname="argument client_certificate_enabled", value=client_certificate_enabled, expected_type=type_hints["client_certificate_enabled"])
            check_type(argname="argument client_certificate_exclusion_paths", value=client_certificate_exclusion_paths, expected_type=type_hints["client_certificate_exclusion_paths"])
            check_type(argname="argument client_certificate_mode", value=client_certificate_mode, expected_type=type_hints["client_certificate_mode"])
            check_type(argname="argument connection_string", value=connection_string, expected_type=type_hints["connection_string"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument https_only", value=https_only, expected_type=type_hints["https_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument key_vault_reference_identity_id", value=key_vault_reference_identity_id, expected_type=type_hints["key_vault_reference_identity_id"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument service_plan_id", value=service_plan_id, expected_type=type_hints["service_plan_id"])
            check_type(argname="argument storage_account", value=storage_account, expected_type=type_hints["storage_account"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
            check_type(argname="argument zip_deploy_file", value=zip_deploy_file, expected_type=type_hints["zip_deploy_file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_service_id": app_service_id,
            "name": name,
            "site_config": site_config,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if app_settings is not None:
            self._values["app_settings"] = app_settings
        if auth_settings is not None:
            self._values["auth_settings"] = auth_settings
        if auth_settings_v2 is not None:
            self._values["auth_settings_v2"] = auth_settings_v2
        if backup is not None:
            self._values["backup"] = backup
        if client_affinity_enabled is not None:
            self._values["client_affinity_enabled"] = client_affinity_enabled
        if client_certificate_enabled is not None:
            self._values["client_certificate_enabled"] = client_certificate_enabled
        if client_certificate_exclusion_paths is not None:
            self._values["client_certificate_exclusion_paths"] = client_certificate_exclusion_paths
        if client_certificate_mode is not None:
            self._values["client_certificate_mode"] = client_certificate_mode
        if connection_string is not None:
            self._values["connection_string"] = connection_string
        if enabled is not None:
            self._values["enabled"] = enabled
        if https_only is not None:
            self._values["https_only"] = https_only
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if key_vault_reference_identity_id is not None:
            self._values["key_vault_reference_identity_id"] = key_vault_reference_identity_id
        if logs is not None:
            self._values["logs"] = logs
        if service_plan_id is not None:
            self._values["service_plan_id"] = service_plan_id
        if storage_account is not None:
            self._values["storage_account"] = storage_account
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id
        if zip_deploy_file is not None:
            self._values["zip_deploy_file"] = zip_deploy_file

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def app_service_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_service_id WindowsWebAppSlot#app_service_id}.'''
        result = self._values.get("app_service_id")
        assert result is not None, "Required property 'app_service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_config(self) -> "WindowsWebAppSlotSiteConfig":
        '''site_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#site_config WindowsWebAppSlot#site_config}
        '''
        result = self._values.get("site_config")
        assert result is not None, "Required property 'site_config' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfig", result)

    @builtins.property
    def app_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_settings WindowsWebAppSlot#app_settings}.'''
        result = self._values.get("app_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def auth_settings(self) -> typing.Optional[WindowsWebAppSlotAuthSettings]:
        '''auth_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings WindowsWebAppSlot#auth_settings}
        '''
        result = self._values.get("auth_settings")
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettings], result)

    @builtins.property
    def auth_settings_v2(self) -> typing.Optional[WindowsWebAppSlotAuthSettingsV2]:
        '''auth_settings_v2 block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auth_settings_v2 WindowsWebAppSlot#auth_settings_v2}
        '''
        result = self._values.get("auth_settings_v2")
        return typing.cast(typing.Optional[WindowsWebAppSlotAuthSettingsV2], result)

    @builtins.property
    def backup(self) -> typing.Optional[WindowsWebAppSlotBackup]:
        '''backup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#backup WindowsWebAppSlot#backup}
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[WindowsWebAppSlotBackup], result)

    @builtins.property
    def client_affinity_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_affinity_enabled WindowsWebAppSlot#client_affinity_enabled}.'''
        result = self._values.get("client_affinity_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def client_certificate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_enabled WindowsWebAppSlot#client_certificate_enabled}.'''
        result = self._values.get("client_certificate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def client_certificate_exclusion_paths(self) -> typing.Optional[builtins.str]:
        '''Paths to exclude when using client certificates, separated by ;

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_exclusion_paths WindowsWebAppSlot#client_certificate_exclusion_paths}
        '''
        result = self._values.get("client_certificate_exclusion_paths")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#client_certificate_mode WindowsWebAppSlot#client_certificate_mode}.'''
        result = self._values.get("client_certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_string(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]]:
        '''connection_string block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#connection_string WindowsWebAppSlot#connection_string}
        '''
        result = self._values.get("connection_string")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotConnectionString"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#enabled WindowsWebAppSlot#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def https_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#https_only WindowsWebAppSlot#https_only}.'''
        result = self._values.get("https_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#id WindowsWebAppSlot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["WindowsWebAppSlotIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity WindowsWebAppSlot#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["WindowsWebAppSlotIdentity"], result)

    @builtins.property
    def key_vault_reference_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#key_vault_reference_identity_id WindowsWebAppSlot#key_vault_reference_identity_id}.'''
        result = self._values.get("key_vault_reference_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logs(self) -> typing.Optional["WindowsWebAppSlotLogs"]:
        '''logs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#logs WindowsWebAppSlot#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogs"], result)

    @builtins.property
    def service_plan_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_plan_id WindowsWebAppSlot#service_plan_id}.'''
        result = self._values.get("service_plan_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]]:
        '''storage_account block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#storage_account WindowsWebAppSlot#storage_account}
        '''
        result = self._values.get("storage_account")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotStorageAccount"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tags WindowsWebAppSlot#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WindowsWebAppSlotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#timeouts WindowsWebAppSlot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WindowsWebAppSlotTimeouts"], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}.'''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zip_deploy_file(self) -> typing.Optional[builtins.str]:
        '''The local path and filename of the Zip packaged application to deploy to this Windows Web App.

        **Note:** Using this value requires ``WEBSITE_RUN_FROM_PACKAGE=1`` on the App in ``app_settings``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#zip_deploy_file WindowsWebAppSlot#zip_deploy_file}
        '''
        result = self._values.get("zip_deploy_file")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionString",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "value": "value"},
)
class WindowsWebAppSlotConnectionString:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: The name which should be used for this Connection. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param type: Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}
        :param value: The connection string value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#value WindowsWebAppSlot#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81d070fd168e172b4c5e8e70cfb0d0d518b2ae40ac4e24a5203c78d3aedd84d)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name which should be used for this Connection.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of database. Possible values include: ``MySQL``, ``SQLServer``, ``SQLAzure``, ``Custom``, ``NotificationHub``, ``ServiceBus``, ``EventHub``, ``APIHub``, ``DocDb``, ``RedisCache``, and ``PostgreSQL``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The connection string value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#value WindowsWebAppSlot#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotConnectionString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotConnectionStringList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionStringList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f1c378537402dac7f354bf2f6f72a1bca86cb8985022de6453fa9ead3144cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotConnectionStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f1ba5ed8576d337a19eac8a7279514cfa597289f7ef9ce97d0b7ddf8e8f1fe)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotConnectionStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e3908a44050bc93c41a1c157c2f4629bc01933f74a1cd58d2f7801e82ca89d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9075ec90d5fac55373d40cea64cbf16d2f3327f2465bfcb1e5b77343e56d5fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28820b4091885358bc1f94e371a8c65074356ecaff9f98a6f6ffa52158af883b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2352451bf82e759be0ef7717d7c0ec959384ebdbda5fd2eb9adaf1d5b304e04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotConnectionStringOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotConnectionStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d882142854f1e1f89250c9ddaa0bd2d190772d1e93c073140c8a544c91db2ed7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77b4a5a66c3b4f8627079330330e2a374a8f42a2d6c8311afa2c6fc11571bab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b70e1c89081a3d10d07e032aa9663a742324b603cd9c12d3e1d3e319e1d58c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18761c951867791d2a3653019d77a5887054c0fb71395b5f3961f3bec483abd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72946380f21e05c00a4e7a13cc2299be6429fda2eb2ac884243581a5fc78923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class WindowsWebAppSlotIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acd042ffcf3b7dd2b6d0807e318e903fcbcbd02bd1c1df40a7c10a900e74b184)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#identity_ids WindowsWebAppSlot#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotIdentityOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea0c3cc6cbffcbcb1a38b8cc1eda88158905133c26a52ac55eec227f6d0d7f9b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7606988b609efc5fcad169ccf4a27ab34d6053ab56ea50a8c904ba07bf606d7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d46efe12ef543220fef983c21bd95e38498c6e1dca1d636d5ba42e79ba579c4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotIdentity]:
        return typing.cast(typing.Optional[WindowsWebAppSlotIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6e8d2a885bb90c084be77880325eb4bea0782c07533402bc4858ab210495b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogs",
    jsii_struct_bases=[],
    name_mapping={
        "application_logs": "applicationLogs",
        "detailed_error_messages": "detailedErrorMessages",
        "failed_request_tracing": "failedRequestTracing",
        "http_logs": "httpLogs",
    },
)
class WindowsWebAppSlotLogs:
    def __init__(
        self,
        *,
        application_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_error_messages: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failed_request_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_logs: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogs", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param application_logs: application_logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        :param detailed_error_messages: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.
        :param failed_request_tracing: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.
        :param http_logs: http_logs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        if isinstance(application_logs, dict):
            application_logs = WindowsWebAppSlotLogsApplicationLogs(**application_logs)
        if isinstance(http_logs, dict):
            http_logs = WindowsWebAppSlotLogsHttpLogs(**http_logs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb38c5a849a0aaf33670febe7b15671fbb6c9fd2e503e5b2aa9e92a2f6fb469a)
            check_type(argname="argument application_logs", value=application_logs, expected_type=type_hints["application_logs"])
            check_type(argname="argument detailed_error_messages", value=detailed_error_messages, expected_type=type_hints["detailed_error_messages"])
            check_type(argname="argument failed_request_tracing", value=failed_request_tracing, expected_type=type_hints["failed_request_tracing"])
            check_type(argname="argument http_logs", value=http_logs, expected_type=type_hints["http_logs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_logs is not None:
            self._values["application_logs"] = application_logs
        if detailed_error_messages is not None:
            self._values["detailed_error_messages"] = detailed_error_messages
        if failed_request_tracing is not None:
            self._values["failed_request_tracing"] = failed_request_tracing
        if http_logs is not None:
            self._values["http_logs"] = http_logs

    @builtins.property
    def application_logs(
        self,
    ) -> typing.Optional["WindowsWebAppSlotLogsApplicationLogs"]:
        '''application_logs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_logs WindowsWebAppSlot#application_logs}
        '''
        result = self._values.get("application_logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsApplicationLogs"], result)

    @builtins.property
    def detailed_error_messages(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#detailed_error_messages WindowsWebAppSlot#detailed_error_messages}.'''
        result = self._values.get("detailed_error_messages")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def failed_request_tracing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#failed_request_tracing WindowsWebAppSlot#failed_request_tracing}.'''
        result = self._values.get("failed_request_tracing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def http_logs(self) -> typing.Optional["WindowsWebAppSlotLogsHttpLogs"]:
        '''http_logs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http_logs WindowsWebAppSlot#http_logs}
        '''
        result = self._values.get("http_logs")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogs",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_level": "fileSystemLevel",
        "azure_blob_storage": "azureBlobStorage",
    },
)
class WindowsWebAppSlotLogsApplicationLogs:
    def __init__(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(**azure_blob_storage)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb166d746aed3e596653aaf2dfaacdcf1e7056ec24eea008574fed5055d45d9)
            check_type(argname="argument file_system_level", value=file_system_level, expected_type=type_hints["file_system_level"])
            check_type(argname="argument azure_blob_storage", value=azure_blob_storage, expected_type=type_hints["azure_blob_storage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_level": file_system_level,
        }
        if azure_blob_storage is not None:
            self._values["azure_blob_storage"] = azure_blob_storage

    @builtins.property
    def file_system_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.'''
        result = self._values.get("file_system_level")
        assert result is not None, "Required property 'file_system_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_blob_storage(
        self,
    ) -> typing.Optional["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsApplicationLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={
        "level": "level",
        "retention_in_days": "retentionInDays",
        "sas_url": "sasUrl",
    },
)
class WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        level: builtins.str,
        retention_in_days: jsii.Number,
        sas_url: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#level WindowsWebAppSlot#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c92e548d5dbe7dcce51f828cce7327f1c8250ba7dbc24dfbb3f66b17ecee81)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument sas_url", value=sas_url, expected_type=type_hints["sas_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "level": level,
            "retention_in_days": retention_in_days,
            "sas_url": sas_url,
        }

    @builtins.property
    def level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#level WindowsWebAppSlot#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5f476c4c701378c5fa01f5498e6e7d99963c496496debb1e993155a75fd2bd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="sasUrlInput")
    def sas_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ebfb9fae02da85338e9d40d6964c9e7572e03b7aa4b4001d7df445ce0f14e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffbc7e8723c4042a2012b58a53206570943bfbcb1997c4502a065416d007783)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369cff1c7c20d3edd70c34645f2780dd1963ef9ca0c0f3c712165f793d7059e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a4a1b3a0dc36b99ed6ccae2116f7ebae978457155dc5d58b079506206bfafd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsApplicationLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsApplicationLogsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6498b9985e3e1d001a0c8bef946fafc906c72218d5f42cab8e90689bcba9ed1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureBlobStorage")
    def put_azure_blob_storage(
        self,
        *,
        level: builtins.str,
        retention_in_days: jsii.Number,
        sas_url: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#level WindowsWebAppSlot#level}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param sas_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        '''
        value = WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage(
            level=level, retention_in_days=retention_in_days, sas_url=sas_url
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorage", [value]))

    @jsii.member(jsii_name="resetAzureBlobStorage")
    def reset_azure_blob_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorage", []))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference:
        return typing.cast(WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLevelInput")
    def file_system_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemLevel")
    def file_system_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemLevel"))

    @file_system_level.setter
    def file_system_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb60dfc52768ba00f259a2f3ab45abbe658c987ac4a6b946f881fd788a95af98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemLevel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsApplicationLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e50c4a8825ca89149f119c3962b9d302c3a4d9d0782305a92387cb84fbc0846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogs",
    jsii_struct_bases=[],
    name_mapping={
        "azure_blob_storage": "azureBlobStorage",
        "file_system": "fileSystem",
    },
)
class WindowsWebAppSlotLogsHttpLogs:
    def __init__(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union["WindowsWebAppSlotLogsHttpLogsFileSystem", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        if isinstance(azure_blob_storage, dict):
            azure_blob_storage = WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(**azure_blob_storage)
        if isinstance(file_system, dict):
            file_system = WindowsWebAppSlotLogsHttpLogsFileSystem(**file_system)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ad82175360c2bb1633ac60b8975b96f42b18b78421a984b7e693af1842673f)
            check_type(argname="argument azure_blob_storage", value=azure_blob_storage, expected_type=type_hints["azure_blob_storage"])
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if azure_blob_storage is not None:
            self._values["azure_blob_storage"] = azure_blob_storage
        if file_system is not None:
            self._values["file_system"] = file_system

    @builtins.property
    def azure_blob_storage(
        self,
    ) -> typing.Optional["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage"]:
        '''azure_blob_storage block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        result = self._values.get("azure_blob_storage")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogsAzureBlobStorage"], result)

    @builtins.property
    def file_system(self) -> typing.Optional["WindowsWebAppSlotLogsHttpLogsFileSystem"]:
        '''file_system block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        result = self._values.get("file_system")
        return typing.cast(typing.Optional["WindowsWebAppSlotLogsHttpLogsFileSystem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsAzureBlobStorage",
    jsii_struct_bases=[],
    name_mapping={"sas_url": "sasUrl", "retention_in_days": "retentionInDays"},
)
class WindowsWebAppSlotLogsHttpLogsAzureBlobStorage:
    def __init__(
        self,
        *,
        sas_url: builtins.str,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param sas_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60553a01ae9ffb15032ca862ecbd9d515d16239f1fc029db1d96b10fb208da41)
            check_type(argname="argument sas_url", value=sas_url, expected_type=type_hints["sas_url"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sas_url": sas_url,
        }
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days

    @builtins.property
    def sas_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.'''
        result = self._values.get("sas_url")
        assert result is not None, "Required property 'sas_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9fe385817586befb393afdbfd1c37cdaccb075c3b2bdf9dc0b013d01fb479e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRetentionInDays")
    def reset_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInDays", []))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="sasUrlInput")
    def sas_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124881726eeb404123f7c33232a091a284253fbafcf48519199cd10e9e542774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sasUrl")
    def sas_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasUrl"))

    @sas_url.setter
    def sas_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b13fbc4c2352b53e2288ea6e258cd8bef6c4f81b67e1182755fbe568c8bf517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748ac0e8c265ef40b41e6df0ec121b14bf9bf44bbb943d71c6122678ad2ccec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsFileSystem",
    jsii_struct_bases=[],
    name_mapping={
        "retention_in_days": "retentionInDays",
        "retention_in_mb": "retentionInMb",
    },
)
class WindowsWebAppSlotLogsHttpLogsFileSystem:
    def __init__(
        self,
        *,
        retention_in_days: jsii.Number,
        retention_in_mb: jsii.Number,
    ) -> None:
        '''
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7416ce2b5e04b634ccaa5a96102d0f1d68ff38e8c73fe64002e2b9ad26266e0)
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument retention_in_mb", value=retention_in_mb, expected_type=type_hints["retention_in_mb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "retention_in_days": retention_in_days,
            "retention_in_mb": retention_in_mb,
        }

    @builtins.property
    def retention_in_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        assert result is not None, "Required property 'retention_in_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def retention_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.'''
        result = self._values.get("retention_in_mb")
        assert result is not None, "Required property 'retention_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotLogsHttpLogsFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50cb51d778aff2c213054d58db3cd1260af678c7d3b339d8d2ad84b01d104006)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInMbInput")
    def retention_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2198abda390c8e69bb00cc3ca3d3f341d887ae57ce52809ee0479ac9d1ca97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInMb")
    def retention_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInMb"))

    @retention_in_mb.setter
    def retention_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0b2bc1e28ec100f90ccb99b8ffe049f69136468041af77e79ff2f321bf58bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7426e36d42a2f67397e158bb5f93f229c305f5b0e5d430b4236a1facc71610b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsHttpLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsHttpLogsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0641ddaa2163cee2e57f46d09f20e13ff10d0f36ba9e5343019da7de58012296)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAzureBlobStorage")
    def put_azure_blob_storage(
        self,
        *,
        sas_url: builtins.str,
        retention_in_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param sas_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sas_url WindowsWebAppSlot#sas_url}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        '''
        value = WindowsWebAppSlotLogsHttpLogsAzureBlobStorage(
            sas_url=sas_url, retention_in_days=retention_in_days
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobStorage", [value]))

    @jsii.member(jsii_name="putFileSystem")
    def put_file_system(
        self,
        *,
        retention_in_days: jsii.Number,
        retention_in_mb: jsii.Number,
    ) -> None:
        '''
        :param retention_in_days: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_days WindowsWebAppSlot#retention_in_days}.
        :param retention_in_mb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#retention_in_mb WindowsWebAppSlot#retention_in_mb}.
        '''
        value = WindowsWebAppSlotLogsHttpLogsFileSystem(
            retention_in_days=retention_in_days, retention_in_mb=retention_in_mb
        )

        return typing.cast(None, jsii.invoke(self, "putFileSystem", [value]))

    @jsii.member(jsii_name="resetAzureBlobStorage")
    def reset_azure_blob_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobStorage", []))

    @jsii.member(jsii_name="resetFileSystem")
    def reset_file_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystem", []))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference, jsii.get(self, "azureBlobStorage"))

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference, jsii.get(self, "fileSystem"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobStorageInput")
    def azure_blob_storage_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage], jsii.get(self, "azureBlobStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemInput")
    def file_system_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem], jsii.get(self, "fileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogsHttpLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotLogsHttpLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e8327a6ebd6a9e00e616d0d0a450b25d17a434715e9225b7b393dc5173db7a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotLogsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768ae7d079759a43664acc204b754598890185a459e0c333c904c821f07bc41c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationLogs")
    def put_application_logs(
        self,
        *,
        file_system_level: builtins.str,
        azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file_system_level: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system_level WindowsWebAppSlot#file_system_level}.
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        '''
        value = WindowsWebAppSlotLogsApplicationLogs(
            file_system_level=file_system_level, azure_blob_storage=azure_blob_storage
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationLogs", [value]))

    @jsii.member(jsii_name="putHttpLogs")
    def put_http_logs(
        self,
        *,
        azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage, typing.Dict[builtins.str, typing.Any]]] = None,
        file_system: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsFileSystem, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param azure_blob_storage: azure_blob_storage block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#azure_blob_storage WindowsWebAppSlot#azure_blob_storage}
        :param file_system: file_system block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#file_system WindowsWebAppSlot#file_system}
        '''
        value = WindowsWebAppSlotLogsHttpLogs(
            azure_blob_storage=azure_blob_storage, file_system=file_system
        )

        return typing.cast(None, jsii.invoke(self, "putHttpLogs", [value]))

    @jsii.member(jsii_name="resetApplicationLogs")
    def reset_application_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationLogs", []))

    @jsii.member(jsii_name="resetDetailedErrorMessages")
    def reset_detailed_error_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetailedErrorMessages", []))

    @jsii.member(jsii_name="resetFailedRequestTracing")
    def reset_failed_request_tracing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailedRequestTracing", []))

    @jsii.member(jsii_name="resetHttpLogs")
    def reset_http_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpLogs", []))

    @builtins.property
    @jsii.member(jsii_name="applicationLogs")
    def application_logs(self) -> WindowsWebAppSlotLogsApplicationLogsOutputReference:
        return typing.cast(WindowsWebAppSlotLogsApplicationLogsOutputReference, jsii.get(self, "applicationLogs"))

    @builtins.property
    @jsii.member(jsii_name="httpLogs")
    def http_logs(self) -> WindowsWebAppSlotLogsHttpLogsOutputReference:
        return typing.cast(WindowsWebAppSlotLogsHttpLogsOutputReference, jsii.get(self, "httpLogs"))

    @builtins.property
    @jsii.member(jsii_name="applicationLogsInput")
    def application_logs_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotLogsApplicationLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsApplicationLogs], jsii.get(self, "applicationLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorMessagesInput")
    def detailed_error_messages_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "detailedErrorMessagesInput"))

    @builtins.property
    @jsii.member(jsii_name="failedRequestTracingInput")
    def failed_request_tracing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failedRequestTracingInput"))

    @builtins.property
    @jsii.member(jsii_name="httpLogsInput")
    def http_logs_input(self) -> typing.Optional[WindowsWebAppSlotLogsHttpLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogsHttpLogs], jsii.get(self, "httpLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorMessages")
    def detailed_error_messages(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "detailedErrorMessages"))

    @detailed_error_messages.setter
    def detailed_error_messages(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b6a96e5d0bb5a72f5922d541e76801d479e22da444d6722a4e68b3eeb0b7f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detailedErrorMessages", value)

    @builtins.property
    @jsii.member(jsii_name="failedRequestTracing")
    def failed_request_tracing(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failedRequestTracing"))

    @failed_request_tracing.setter
    def failed_request_tracing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45144d45d95c3670e9abfac2ae6a9e567db0d2ff23c27dee7a00c9c3b4b349ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failedRequestTracing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotLogs]:
        return typing.cast(typing.Optional[WindowsWebAppSlotLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsWebAppSlotLogs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d901e876f63fc569df892545eb89674cc3c5363db3dca268f9634b8093112425)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfig",
    jsii_struct_bases=[],
    name_mapping={
        "always_on": "alwaysOn",
        "api_definition_url": "apiDefinitionUrl",
        "api_management_api_id": "apiManagementApiId",
        "app_command_line": "appCommandLine",
        "application_stack": "applicationStack",
        "auto_heal_enabled": "autoHealEnabled",
        "auto_heal_setting": "autoHealSetting",
        "auto_swap_slot_name": "autoSwapSlotName",
        "container_registry_managed_identity_client_id": "containerRegistryManagedIdentityClientId",
        "container_registry_use_managed_identity": "containerRegistryUseManagedIdentity",
        "cors": "cors",
        "default_documents": "defaultDocuments",
        "ftps_state": "ftpsState",
        "health_check_eviction_time_in_min": "healthCheckEvictionTimeInMin",
        "health_check_path": "healthCheckPath",
        "http2_enabled": "http2Enabled",
        "ip_restriction": "ipRestriction",
        "load_balancing_mode": "loadBalancingMode",
        "local_mysql_enabled": "localMysqlEnabled",
        "managed_pipeline_mode": "managedPipelineMode",
        "minimum_tls_version": "minimumTlsVersion",
        "remote_debugging_enabled": "remoteDebuggingEnabled",
        "remote_debugging_version": "remoteDebuggingVersion",
        "scm_ip_restriction": "scmIpRestriction",
        "scm_minimum_tls_version": "scmMinimumTlsVersion",
        "scm_use_main_ip_restriction": "scmUseMainIpRestriction",
        "use32_bit_worker": "use32BitWorker",
        "virtual_application": "virtualApplication",
        "vnet_route_all_enabled": "vnetRouteAllEnabled",
        "websockets_enabled": "websocketsEnabled",
        "worker_count": "workerCount",
    },
)
class WindowsWebAppSlotSiteConfig:
    def __init__(
        self,
        *,
        always_on: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        api_definition_url: typing.Optional[builtins.str] = None,
        api_management_api_id: typing.Optional[builtins.str] = None,
        app_command_line: typing.Optional[builtins.str] = None,
        application_stack: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigApplicationStack", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_heal_setting: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSetting", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_swap_slot_name: typing.Optional[builtins.str] = None,
        container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
        container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cors: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigCors", typing.Dict[builtins.str, typing.Any]]] = None,
        default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
        ftps_state: typing.Optional[builtins.str] = None,
        health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        http2_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestriction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        load_balancing_mode: typing.Optional[builtins.str] = None,
        local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        managed_pipeline_mode: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
        remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remote_debugging_version: typing.Optional[builtins.str] = None,
        scm_ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[builtins.str, typing.Any]]]]] = None,
        scm_minimum_tls_version: typing.Optional[builtins.str] = None,
        scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        use32_bit_worker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        virtual_application: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        websockets_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        worker_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param always_on: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.
        :param api_definition_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.
        :param api_management_api_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.
        :param app_command_line: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.
        :param application_stack: application_stack block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        :param auto_heal_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.
        :param auto_heal_setting: auto_heal_setting block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        :param auto_swap_slot_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.
        :param container_registry_managed_identity_client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.
        :param container_registry_use_managed_identity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.
        :param cors: cors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        :param default_documents: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.
        :param ftps_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.
        :param health_check_eviction_time_in_min: The amount of time in minutes that a node is unhealthy before being removed from the load balancer. Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        :param health_check_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.
        :param http2_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.
        :param ip_restriction: ip_restriction block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}
        :param load_balancing_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.
        :param local_mysql_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.
        :param managed_pipeline_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.
        :param remote_debugging_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.
        :param remote_debugging_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.
        :param scm_ip_restriction: scm_ip_restriction block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}
        :param scm_minimum_tls_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.
        :param scm_use_main_ip_restriction: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.
        :param use32_bit_worker: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.
        :param virtual_application: virtual_application block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        :param vnet_route_all_enabled: Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        :param websockets_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.
        :param worker_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.
        '''
        if isinstance(application_stack, dict):
            application_stack = WindowsWebAppSlotSiteConfigApplicationStack(**application_stack)
        if isinstance(auto_heal_setting, dict):
            auto_heal_setting = WindowsWebAppSlotSiteConfigAutoHealSetting(**auto_heal_setting)
        if isinstance(cors, dict):
            cors = WindowsWebAppSlotSiteConfigCors(**cors)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b2cdd7804c528b844b4ebb2ba42ecd15551b389cd3ea8f6a4d69012ad8c244f)
            check_type(argname="argument always_on", value=always_on, expected_type=type_hints["always_on"])
            check_type(argname="argument api_definition_url", value=api_definition_url, expected_type=type_hints["api_definition_url"])
            check_type(argname="argument api_management_api_id", value=api_management_api_id, expected_type=type_hints["api_management_api_id"])
            check_type(argname="argument app_command_line", value=app_command_line, expected_type=type_hints["app_command_line"])
            check_type(argname="argument application_stack", value=application_stack, expected_type=type_hints["application_stack"])
            check_type(argname="argument auto_heal_enabled", value=auto_heal_enabled, expected_type=type_hints["auto_heal_enabled"])
            check_type(argname="argument auto_heal_setting", value=auto_heal_setting, expected_type=type_hints["auto_heal_setting"])
            check_type(argname="argument auto_swap_slot_name", value=auto_swap_slot_name, expected_type=type_hints["auto_swap_slot_name"])
            check_type(argname="argument container_registry_managed_identity_client_id", value=container_registry_managed_identity_client_id, expected_type=type_hints["container_registry_managed_identity_client_id"])
            check_type(argname="argument container_registry_use_managed_identity", value=container_registry_use_managed_identity, expected_type=type_hints["container_registry_use_managed_identity"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument default_documents", value=default_documents, expected_type=type_hints["default_documents"])
            check_type(argname="argument ftps_state", value=ftps_state, expected_type=type_hints["ftps_state"])
            check_type(argname="argument health_check_eviction_time_in_min", value=health_check_eviction_time_in_min, expected_type=type_hints["health_check_eviction_time_in_min"])
            check_type(argname="argument health_check_path", value=health_check_path, expected_type=type_hints["health_check_path"])
            check_type(argname="argument http2_enabled", value=http2_enabled, expected_type=type_hints["http2_enabled"])
            check_type(argname="argument ip_restriction", value=ip_restriction, expected_type=type_hints["ip_restriction"])
            check_type(argname="argument load_balancing_mode", value=load_balancing_mode, expected_type=type_hints["load_balancing_mode"])
            check_type(argname="argument local_mysql_enabled", value=local_mysql_enabled, expected_type=type_hints["local_mysql_enabled"])
            check_type(argname="argument managed_pipeline_mode", value=managed_pipeline_mode, expected_type=type_hints["managed_pipeline_mode"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
            check_type(argname="argument remote_debugging_enabled", value=remote_debugging_enabled, expected_type=type_hints["remote_debugging_enabled"])
            check_type(argname="argument remote_debugging_version", value=remote_debugging_version, expected_type=type_hints["remote_debugging_version"])
            check_type(argname="argument scm_ip_restriction", value=scm_ip_restriction, expected_type=type_hints["scm_ip_restriction"])
            check_type(argname="argument scm_minimum_tls_version", value=scm_minimum_tls_version, expected_type=type_hints["scm_minimum_tls_version"])
            check_type(argname="argument scm_use_main_ip_restriction", value=scm_use_main_ip_restriction, expected_type=type_hints["scm_use_main_ip_restriction"])
            check_type(argname="argument use32_bit_worker", value=use32_bit_worker, expected_type=type_hints["use32_bit_worker"])
            check_type(argname="argument virtual_application", value=virtual_application, expected_type=type_hints["virtual_application"])
            check_type(argname="argument vnet_route_all_enabled", value=vnet_route_all_enabled, expected_type=type_hints["vnet_route_all_enabled"])
            check_type(argname="argument websockets_enabled", value=websockets_enabled, expected_type=type_hints["websockets_enabled"])
            check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if always_on is not None:
            self._values["always_on"] = always_on
        if api_definition_url is not None:
            self._values["api_definition_url"] = api_definition_url
        if api_management_api_id is not None:
            self._values["api_management_api_id"] = api_management_api_id
        if app_command_line is not None:
            self._values["app_command_line"] = app_command_line
        if application_stack is not None:
            self._values["application_stack"] = application_stack
        if auto_heal_enabled is not None:
            self._values["auto_heal_enabled"] = auto_heal_enabled
        if auto_heal_setting is not None:
            self._values["auto_heal_setting"] = auto_heal_setting
        if auto_swap_slot_name is not None:
            self._values["auto_swap_slot_name"] = auto_swap_slot_name
        if container_registry_managed_identity_client_id is not None:
            self._values["container_registry_managed_identity_client_id"] = container_registry_managed_identity_client_id
        if container_registry_use_managed_identity is not None:
            self._values["container_registry_use_managed_identity"] = container_registry_use_managed_identity
        if cors is not None:
            self._values["cors"] = cors
        if default_documents is not None:
            self._values["default_documents"] = default_documents
        if ftps_state is not None:
            self._values["ftps_state"] = ftps_state
        if health_check_eviction_time_in_min is not None:
            self._values["health_check_eviction_time_in_min"] = health_check_eviction_time_in_min
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if http2_enabled is not None:
            self._values["http2_enabled"] = http2_enabled
        if ip_restriction is not None:
            self._values["ip_restriction"] = ip_restriction
        if load_balancing_mode is not None:
            self._values["load_balancing_mode"] = load_balancing_mode
        if local_mysql_enabled is not None:
            self._values["local_mysql_enabled"] = local_mysql_enabled
        if managed_pipeline_mode is not None:
            self._values["managed_pipeline_mode"] = managed_pipeline_mode
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version
        if remote_debugging_enabled is not None:
            self._values["remote_debugging_enabled"] = remote_debugging_enabled
        if remote_debugging_version is not None:
            self._values["remote_debugging_version"] = remote_debugging_version
        if scm_ip_restriction is not None:
            self._values["scm_ip_restriction"] = scm_ip_restriction
        if scm_minimum_tls_version is not None:
            self._values["scm_minimum_tls_version"] = scm_minimum_tls_version
        if scm_use_main_ip_restriction is not None:
            self._values["scm_use_main_ip_restriction"] = scm_use_main_ip_restriction
        if use32_bit_worker is not None:
            self._values["use32_bit_worker"] = use32_bit_worker
        if virtual_application is not None:
            self._values["virtual_application"] = virtual_application
        if vnet_route_all_enabled is not None:
            self._values["vnet_route_all_enabled"] = vnet_route_all_enabled
        if websockets_enabled is not None:
            self._values["websockets_enabled"] = websockets_enabled
        if worker_count is not None:
            self._values["worker_count"] = worker_count

    @builtins.property
    def always_on(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#always_on WindowsWebAppSlot#always_on}.'''
        result = self._values.get("always_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def api_definition_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_definition_url WindowsWebAppSlot#api_definition_url}.'''
        result = self._values.get("api_definition_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_management_api_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#api_management_api_id WindowsWebAppSlot#api_management_api_id}.'''
        result = self._values.get("api_management_api_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_command_line(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#app_command_line WindowsWebAppSlot#app_command_line}.'''
        result = self._values.get("app_command_line")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_stack(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigApplicationStack"]:
        '''application_stack block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#application_stack WindowsWebAppSlot#application_stack}
        '''
        result = self._values.get("application_stack")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigApplicationStack"], result)

    @builtins.property
    def auto_heal_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_enabled WindowsWebAppSlot#auto_heal_enabled}.'''
        result = self._values.get("auto_heal_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_heal_setting(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSetting"]:
        '''auto_heal_setting block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_heal_setting WindowsWebAppSlot#auto_heal_setting}
        '''
        result = self._values.get("auto_heal_setting")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSetting"], result)

    @builtins.property
    def auto_swap_slot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#auto_swap_slot_name WindowsWebAppSlot#auto_swap_slot_name}.'''
        result = self._values.get("auto_swap_slot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_managed_identity_client_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_managed_identity_client_id WindowsWebAppSlot#container_registry_managed_identity_client_id}.'''
        result = self._values.get("container_registry_managed_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#container_registry_use_managed_identity WindowsWebAppSlot#container_registry_use_managed_identity}.'''
        result = self._values.get("container_registry_use_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cors(self) -> typing.Optional["WindowsWebAppSlotSiteConfigCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#cors WindowsWebAppSlot#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigCors"], result)

    @builtins.property
    def default_documents(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#default_documents WindowsWebAppSlot#default_documents}.'''
        result = self._values.get("default_documents")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ftps_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ftps_state WindowsWebAppSlot#ftps_state}.'''
        result = self._values.get("ftps_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_eviction_time_in_min(self) -> typing.Optional[jsii.Number]:
        '''The amount of time in minutes that a node is unhealthy before being removed from the load balancer.

        Possible values are between ``2`` and ``10``. Defaults to ``10``. Only valid in conjunction with ``health_check_path``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_eviction_time_in_min WindowsWebAppSlot#health_check_eviction_time_in_min}
        '''
        result = self._values.get("health_check_eviction_time_in_min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#health_check_path WindowsWebAppSlot#health_check_path}.'''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#http2_enabled WindowsWebAppSlot#http2_enabled}.'''
        result = self._values.get("http2_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestriction"]]]:
        '''ip_restriction block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_restriction WindowsWebAppSlot#ip_restriction}
        '''
        result = self._values.get("ip_restriction")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestriction"]]], result)

    @builtins.property
    def load_balancing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#load_balancing_mode WindowsWebAppSlot#load_balancing_mode}.'''
        result = self._values.get("load_balancing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_mysql_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#local_mysql_enabled WindowsWebAppSlot#local_mysql_enabled}.'''
        result = self._values.get("local_mysql_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def managed_pipeline_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#managed_pipeline_mode WindowsWebAppSlot#managed_pipeline_mode}.'''
        result = self._values.get("managed_pipeline_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_tls_version WindowsWebAppSlot#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_debugging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_enabled WindowsWebAppSlot#remote_debugging_enabled}.'''
        result = self._values.get("remote_debugging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def remote_debugging_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#remote_debugging_version WindowsWebAppSlot#remote_debugging_version}.'''
        result = self._values.get("remote_debugging_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]]:
        '''scm_ip_restriction block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_ip_restriction WindowsWebAppSlot#scm_ip_restriction}
        '''
        result = self._values.get("scm_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]], result)

    @builtins.property
    def scm_minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_minimum_tls_version WindowsWebAppSlot#scm_minimum_tls_version}.'''
        result = self._values.get("scm_minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#scm_use_main_ip_restriction WindowsWebAppSlot#scm_use_main_ip_restriction}.'''
        result = self._values.get("scm_use_main_ip_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def use32_bit_worker(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#use_32_bit_worker WindowsWebAppSlot#use_32_bit_worker}.'''
        result = self._values.get("use32_bit_worker")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def virtual_application(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]]:
        '''virtual_application block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_application WindowsWebAppSlot#virtual_application}
        '''
        result = self._values.get("virtual_application")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]], result)

    @builtins.property
    def vnet_route_all_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#vnet_route_all_enabled WindowsWebAppSlot#vnet_route_all_enabled}
        '''
        result = self._values.get("vnet_route_all_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def websockets_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#websockets_enabled WindowsWebAppSlot#websockets_enabled}.'''
        result = self._values.get("websockets_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def worker_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#worker_count WindowsWebAppSlot#worker_count}.'''
        result = self._values.get("worker_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigApplicationStack",
    jsii_struct_bases=[],
    name_mapping={
        "current_stack": "currentStack",
        "docker_container_name": "dockerContainerName",
        "docker_container_registry": "dockerContainerRegistry",
        "docker_container_tag": "dockerContainerTag",
        "dotnet_core_version": "dotnetCoreVersion",
        "dotnet_version": "dotnetVersion",
        "java_container": "javaContainer",
        "java_container_version": "javaContainerVersion",
        "java_embedded_server_enabled": "javaEmbeddedServerEnabled",
        "java_version": "javaVersion",
        "node_version": "nodeVersion",
        "php_version": "phpVersion",
        "python": "python",
        "python_version": "pythonVersion",
        "tomcat_version": "tomcatVersion",
    },
)
class WindowsWebAppSlotSiteConfigApplicationStack:
    def __init__(
        self,
        *,
        current_stack: typing.Optional[builtins.str] = None,
        docker_container_name: typing.Optional[builtins.str] = None,
        docker_container_registry: typing.Optional[builtins.str] = None,
        docker_container_tag: typing.Optional[builtins.str] = None,
        dotnet_core_version: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_container: typing.Optional[builtins.str] = None,
        java_container_version: typing.Optional[builtins.str] = None,
        java_embedded_server_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        python_version: typing.Optional[builtins.str] = None,
        tomcat_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param current_stack: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.
        :param docker_container_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.
        :param docker_container_registry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.
        :param docker_container_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.
        :param dotnet_core_version: The version of DotNetCore to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_core_version WindowsWebAppSlot#dotnet_core_version}
        :param dotnet_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.
        :param java_container: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.
        :param java_container_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.
        :param java_embedded_server_enabled: Should the application use the embedded web server for the version of Java in use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_embedded_server_enabled WindowsWebAppSlot#java_embedded_server_enabled}
        :param java_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.
        :param python: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python WindowsWebAppSlot#python}.
        :param python_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.
        :param tomcat_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tomcat_version WindowsWebAppSlot#tomcat_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c1b0db59ad18c5da48d45af84137e7af6195ac053e5f09b77e2807499f7d65)
            check_type(argname="argument current_stack", value=current_stack, expected_type=type_hints["current_stack"])
            check_type(argname="argument docker_container_name", value=docker_container_name, expected_type=type_hints["docker_container_name"])
            check_type(argname="argument docker_container_registry", value=docker_container_registry, expected_type=type_hints["docker_container_registry"])
            check_type(argname="argument docker_container_tag", value=docker_container_tag, expected_type=type_hints["docker_container_tag"])
            check_type(argname="argument dotnet_core_version", value=dotnet_core_version, expected_type=type_hints["dotnet_core_version"])
            check_type(argname="argument dotnet_version", value=dotnet_version, expected_type=type_hints["dotnet_version"])
            check_type(argname="argument java_container", value=java_container, expected_type=type_hints["java_container"])
            check_type(argname="argument java_container_version", value=java_container_version, expected_type=type_hints["java_container_version"])
            check_type(argname="argument java_embedded_server_enabled", value=java_embedded_server_enabled, expected_type=type_hints["java_embedded_server_enabled"])
            check_type(argname="argument java_version", value=java_version, expected_type=type_hints["java_version"])
            check_type(argname="argument node_version", value=node_version, expected_type=type_hints["node_version"])
            check_type(argname="argument php_version", value=php_version, expected_type=type_hints["php_version"])
            check_type(argname="argument python", value=python, expected_type=type_hints["python"])
            check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
            check_type(argname="argument tomcat_version", value=tomcat_version, expected_type=type_hints["tomcat_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if current_stack is not None:
            self._values["current_stack"] = current_stack
        if docker_container_name is not None:
            self._values["docker_container_name"] = docker_container_name
        if docker_container_registry is not None:
            self._values["docker_container_registry"] = docker_container_registry
        if docker_container_tag is not None:
            self._values["docker_container_tag"] = docker_container_tag
        if dotnet_core_version is not None:
            self._values["dotnet_core_version"] = dotnet_core_version
        if dotnet_version is not None:
            self._values["dotnet_version"] = dotnet_version
        if java_container is not None:
            self._values["java_container"] = java_container
        if java_container_version is not None:
            self._values["java_container_version"] = java_container_version
        if java_embedded_server_enabled is not None:
            self._values["java_embedded_server_enabled"] = java_embedded_server_enabled
        if java_version is not None:
            self._values["java_version"] = java_version
        if node_version is not None:
            self._values["node_version"] = node_version
        if php_version is not None:
            self._values["php_version"] = php_version
        if python is not None:
            self._values["python"] = python
        if python_version is not None:
            self._values["python_version"] = python_version
        if tomcat_version is not None:
            self._values["tomcat_version"] = tomcat_version

    @builtins.property
    def current_stack(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.'''
        result = self._values.get("current_stack")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.'''
        result = self._values.get("docker_container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_registry(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.'''
        result = self._values.get("docker_container_registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_container_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.'''
        result = self._values.get("docker_container_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dotnet_core_version(self) -> typing.Optional[builtins.str]:
        '''The version of DotNetCore to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_core_version WindowsWebAppSlot#dotnet_core_version}
        '''
        result = self._values.get("dotnet_core_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dotnet_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.'''
        result = self._values.get("dotnet_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_container(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.'''
        result = self._values.get("java_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_container_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.'''
        result = self._values.get("java_container_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def java_embedded_server_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the application use the embedded web server for the version of Java in use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_embedded_server_enabled WindowsWebAppSlot#java_embedded_server_enabled}
        '''
        result = self._values.get("java_embedded_server_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def java_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.'''
        result = self._values.get("java_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.'''
        result = self._values.get("node_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def php_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.'''
        result = self._values.get("php_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def python(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python WindowsWebAppSlot#python}.'''
        result = self._values.get("python")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def python_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.'''
        result = self._values.get("python_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tomcat_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tomcat_version WindowsWebAppSlot#tomcat_version}.'''
        result = self._values.get("tomcat_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigApplicationStack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigApplicationStackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigApplicationStackOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce7f77af22299eb4330935f93341e33bf05fb159d1e7e7b4af61adf3b5af938)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCurrentStack")
    def reset_current_stack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurrentStack", []))

    @jsii.member(jsii_name="resetDockerContainerName")
    def reset_docker_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerName", []))

    @jsii.member(jsii_name="resetDockerContainerRegistry")
    def reset_docker_container_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerRegistry", []))

    @jsii.member(jsii_name="resetDockerContainerTag")
    def reset_docker_container_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerContainerTag", []))

    @jsii.member(jsii_name="resetDotnetCoreVersion")
    def reset_dotnet_core_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDotnetCoreVersion", []))

    @jsii.member(jsii_name="resetDotnetVersion")
    def reset_dotnet_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDotnetVersion", []))

    @jsii.member(jsii_name="resetJavaContainer")
    def reset_java_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaContainer", []))

    @jsii.member(jsii_name="resetJavaContainerVersion")
    def reset_java_container_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaContainerVersion", []))

    @jsii.member(jsii_name="resetJavaEmbeddedServerEnabled")
    def reset_java_embedded_server_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaEmbeddedServerEnabled", []))

    @jsii.member(jsii_name="resetJavaVersion")
    def reset_java_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaVersion", []))

    @jsii.member(jsii_name="resetNodeVersion")
    def reset_node_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeVersion", []))

    @jsii.member(jsii_name="resetPhpVersion")
    def reset_php_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhpVersion", []))

    @jsii.member(jsii_name="resetPython")
    def reset_python(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPython", []))

    @jsii.member(jsii_name="resetPythonVersion")
    def reset_python_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonVersion", []))

    @jsii.member(jsii_name="resetTomcatVersion")
    def reset_tomcat_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTomcatVersion", []))

    @builtins.property
    @jsii.member(jsii_name="currentStackInput")
    def current_stack_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentStackInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerNameInput")
    def docker_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerRegistryInput")
    def docker_container_registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerRegistryInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerContainerTagInput")
    def docker_container_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerContainerTagInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetCoreVersionInput")
    def dotnet_core_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dotnetCoreVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="dotnetVersionInput")
    def dotnet_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dotnetVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaContainerInput")
    def java_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="javaContainerVersionInput")
    def java_container_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaContainerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="javaEmbeddedServerEnabledInput")
    def java_embedded_server_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "javaEmbeddedServerEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="javaVersionInput")
    def java_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeVersionInput")
    def node_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="phpVersionInput")
    def php_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonInput")
    def python_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pythonInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonVersionInput")
    def python_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pythonVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="tomcatVersionInput")
    def tomcat_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tomcatVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="currentStack")
    def current_stack(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentStack"))

    @current_stack.setter
    def current_stack(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ddbe8e69682b6024307a36a7998197da9c689768c5430b98f3949b6c40c4e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentStack", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerName")
    def docker_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerName"))

    @docker_container_name.setter
    def docker_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8122218b3e8eab28883e46b92d8beeb552fbdae9ed367233a74c624480af40bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerRegistry")
    def docker_container_registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerRegistry"))

    @docker_container_registry.setter
    def docker_container_registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722187b854f312a1aa1e2dd9409099148bbeda6a0a0d462e862af2451cdbc3d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerRegistry", value)

    @builtins.property
    @jsii.member(jsii_name="dockerContainerTag")
    def docker_container_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerContainerTag"))

    @docker_container_tag.setter
    def docker_container_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23df1ee704b61647e06aa22336843cc0e8efc187c73507395c5e986ac2f3fac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerContainerTag", value)

    @builtins.property
    @jsii.member(jsii_name="dotnetCoreVersion")
    def dotnet_core_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dotnetCoreVersion"))

    @dotnet_core_version.setter
    def dotnet_core_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a56325347c18b420ebc3c0181a2b93f29c784e2339993039867f0ce95565a93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dotnetCoreVersion", value)

    @builtins.property
    @jsii.member(jsii_name="dotnetVersion")
    def dotnet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dotnetVersion"))

    @dotnet_version.setter
    def dotnet_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b14d9fb44941d0c50b7fb095149edcdf1a853e6eca816aeb1370bbb2b3222dde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dotnetVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaContainer")
    def java_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaContainer"))

    @java_container.setter
    def java_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a707ab1b57c818fe22dba000af567867cc24b87c1f5c8fb8b2462d9d16085cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaContainer", value)

    @builtins.property
    @jsii.member(jsii_name="javaContainerVersion")
    def java_container_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaContainerVersion"))

    @java_container_version.setter
    def java_container_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c784edf64d4a387b2126aba803fd497a8afa8a3e87b3533f98adb4b51f1345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaContainerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="javaEmbeddedServerEnabled")
    def java_embedded_server_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "javaEmbeddedServerEnabled"))

    @java_embedded_server_enabled.setter
    def java_embedded_server_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fb32c13b1fec2e552f700eb5746e01162355374463d5151d633c4f60b8eabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaEmbeddedServerEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="javaVersion")
    def java_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "javaVersion"))

    @java_version.setter
    def java_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c6d8dcced822e214a1f715660fe25a0034989a49fe78845bc2e2130622113fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="nodeVersion")
    def node_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeVersion"))

    @node_version.setter
    def node_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cd4af7336080a7178db361f16abf5c2fa4d22a15844034789336de55126963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="phpVersion")
    def php_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phpVersion"))

    @php_version.setter
    def php_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def77d56ce07f45e52c9d0239988001f828f6e6ecd9dc425c28a8c9f0661c3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phpVersion", value)

    @builtins.property
    @jsii.member(jsii_name="python")
    def python(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "python"))

    @python.setter
    def python(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0bbc01f384d793e210342c67757883d272e796c71f515f4190484454784a32e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "python", value)

    @builtins.property
    @jsii.member(jsii_name="pythonVersion")
    def python_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pythonVersion"))

    @python_version.setter
    def python_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2440c0becb6c7636dc26433eb1f9b696b747f22b7c780dd8fd9848a1a007d84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tomcatVersion")
    def tomcat_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tomcatVersion"))

    @tomcat_version.setter
    def tomcat_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56f6b2ccb5611dd25c2eff4b73bcba3065a53fb082c236ccc96d7d7c99b69a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tomcatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2db3a61bbb19ca9aa7f6bf1d66dfe1d0e293b404802371aa5b501460614585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSetting",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "trigger": "trigger"},
)
class WindowsWebAppSlotSiteConfigAutoHealSetting:
    def __init__(
        self,
        *,
        action: typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingAction", typing.Dict[builtins.str, typing.Any]],
        trigger: typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        if isinstance(action, dict):
            action = WindowsWebAppSlotSiteConfigAutoHealSettingAction(**action)
        if isinstance(trigger, dict):
            trigger = WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(**trigger)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6111285450c9db0042c7ef52ea2cf96a5949064ea1c5de8bca0d7e2ac360ac)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "trigger": trigger,
        }

    @builtins.property
    def action(self) -> "WindowsWebAppSlotSiteConfigAutoHealSettingAction":
        '''action block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingAction", result)

    @builtins.property
    def trigger(self) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger":
        '''trigger block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        result = self._values.get("trigger")
        assert result is not None, "Required property 'trigger' is missing"
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTrigger", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingAction",
    jsii_struct_bases=[],
    name_mapping={
        "action_type": "actionType",
        "custom_action": "customAction",
        "minimum_process_execution_time": "minimumProcessExecutionTime",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingAction:
    def __init__(
        self,
        *,
        action_type: builtins.str,
        custom_action: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction", typing.Dict[builtins.str, typing.Any]]] = None,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.
        :param custom_action: custom_action block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.
        '''
        if isinstance(custom_action, dict):
            custom_action = WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(**custom_action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05573e34b2865598d12f17efbd803ad79c6c6b0c9c5b2091807bcd47cf47f995)
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument custom_action", value=custom_action, expected_type=type_hints["custom_action"])
            check_type(argname="argument minimum_process_execution_time", value=minimum_process_execution_time, expected_type=type_hints["minimum_process_execution_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_type": action_type,
        }
        if custom_action is not None:
            self._values["custom_action"] = custom_action
        if minimum_process_execution_time is not None:
            self._values["minimum_process_execution_time"] = minimum_process_execution_time

    @builtins.property
    def action_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.'''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_action(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction"]:
        '''custom_action block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        '''
        result = self._values.get("custom_action")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction"], result)

    @builtins.property
    def minimum_process_execution_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.'''
        result = self._values.get("minimum_process_execution_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction",
    jsii_struct_bases=[],
    name_mapping={"executable": "executable", "parameters": "parameters"},
)
class WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction:
    def __init__(
        self,
        *,
        executable: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param executable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#executable WindowsWebAppSlot#executable}.
        :param parameters: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d65156c937a6f9c2c2eb4d7b7f6ac388140a2823e365cc5d23fa11b82d999b15)
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "executable": executable,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def executable(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#executable WindowsWebAppSlot#executable}.'''
        result = self._values.get("executable")
        assert result is not None, "Required property 'executable' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af23a22f92e1355b8ece4c08ee3e890bae921b0de336316a4b2a2b76708e2e41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="executableInput")
    def executable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executableInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="executable")
    def executable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executable"))

    @executable.setter
    def executable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092bd95209c641d8648d9b0e7d7533dc30f13429a6cd4da19e6aa591b41fa899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executable", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ad9b2f462786343a87c2dbb949edfc3dee6fd95cd476f5d6488194f11b0f77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146844df752364c4327a78096d8d8b5d62d00c27b5ccdc833b3a88d809bbd522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5f4c402985196e50eaa7b76beae7457a362d3993356448041dc7206777b47b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomAction")
    def put_custom_action(
        self,
        *,
        executable: builtins.str,
        parameters: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param executable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#executable WindowsWebAppSlot#executable}.
        :param parameters: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#parameters WindowsWebAppSlot#parameters}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction(
            executable=executable, parameters=parameters
        )

        return typing.cast(None, jsii.invoke(self, "putCustomAction", [value]))

    @jsii.member(jsii_name="resetCustomAction")
    def reset_custom_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAction", []))

    @jsii.member(jsii_name="resetMinimumProcessExecutionTime")
    def reset_minimum_process_execution_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumProcessExecutionTime", []))

    @builtins.property
    @jsii.member(jsii_name="customAction")
    def custom_action(
        self,
    ) -> WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference, jsii.get(self, "customAction"))

    @builtins.property
    @jsii.member(jsii_name="actionTypeInput")
    def action_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customActionInput")
    def custom_action_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction], jsii.get(self, "customActionInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumProcessExecutionTimeInput")
    def minimum_process_execution_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumProcessExecutionTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a814650370718c57d6d2852fdbb8538c071b4716d9b11f12aa0cfca88bff00e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="minimumProcessExecutionTime")
    def minimum_process_execution_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumProcessExecutionTime"))

    @minimum_process_execution_time.setter
    def minimum_process_execution_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a05c1bb4b032ddfa4d06f02f7e2a25c4d6fead1023cc0dcd1e8a2c6b5609807d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumProcessExecutionTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f8bf9bdc80438ae1ce6b9406a2ab56eab4bd6ac7ad26f5a5809db7b8d731aa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a7a76f5ecb33aa179c5405c987a7e38e71cc47b7b6d884299448c9b43febc73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        action_type: builtins.str,
        custom_action: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction, typing.Dict[builtins.str, typing.Any]]] = None,
        minimum_process_execution_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action_type WindowsWebAppSlot#action_type}.
        :param custom_action: custom_action block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#custom_action WindowsWebAppSlot#custom_action}
        :param minimum_process_execution_time: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#minimum_process_execution_time WindowsWebAppSlot#minimum_process_execution_time}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingAction(
            action_type=action_type,
            custom_action=custom_action,
            minimum_process_execution_time=minimum_process_execution_time,
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        private_memory_kb: typing.Optional[jsii.Number] = None,
        requests: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests", typing.Dict[builtins.str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param private_memory_kb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.
        :param requests: requests block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(
            private_memory_kb=private_memory_kb,
            requests=requests,
            slow_request=slow_request,
            status_code=status_code,
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97e9cc42c78bbbef71717566cf8d8ac305a7bd1a60eb951f0fffa615dcacb26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "private_memory_kb": "privateMemoryKb",
        "requests": "requests",
        "slow_request": "slowRequest",
        "status_code": "statusCode",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTrigger:
    def __init__(
        self,
        *,
        private_memory_kb: typing.Optional[jsii.Number] = None,
        requests: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests", typing.Dict[builtins.str, typing.Any]]] = None,
        slow_request: typing.Optional[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest", typing.Dict[builtins.str, typing.Any]]] = None,
        status_code: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param private_memory_kb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.
        :param requests: requests block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        :param slow_request: slow_request block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        :param status_code: status_code block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        if isinstance(requests, dict):
            requests = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(**requests)
        if isinstance(slow_request, dict):
            slow_request = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(**slow_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__595d2a7fad1fd2440a60b0a500dd856bbcfd8ab201035166f792ec4a5a1ec1f0)
            check_type(argname="argument private_memory_kb", value=private_memory_kb, expected_type=type_hints["private_memory_kb"])
            check_type(argname="argument requests", value=requests, expected_type=type_hints["requests"])
            check_type(argname="argument slow_request", value=slow_request, expected_type=type_hints["slow_request"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private_memory_kb is not None:
            self._values["private_memory_kb"] = private_memory_kb
        if requests is not None:
            self._values["requests"] = requests
        if slow_request is not None:
            self._values["slow_request"] = slow_request
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def private_memory_kb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#private_memory_kb WindowsWebAppSlot#private_memory_kb}.'''
        result = self._values.get("private_memory_kb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"]:
        '''requests block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#requests WindowsWebAppSlot#requests}
        '''
        result = self._values.get("requests")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"], result)

    @builtins.property
    def slow_request(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"]:
        '''slow_request block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#slow_request WindowsWebAppSlot#slow_request}
        '''
        result = self._values.get("slow_request")
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"], result)

    @builtins.property
    def status_code(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        '''status_code block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#status_code WindowsWebAppSlot#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224baec3c322038d7760411ac3e0d1cc8ee9b6cabc1eb48184c343fd004e8027)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequests")
    def put_requests(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(
            count=count, interval=interval
        )

        return typing.cast(None, jsii.invoke(self, "putRequests", [value]))

    @jsii.member(jsii_name="putSlowRequest")
    def put_slow_request(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        time_taken: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#path WindowsWebAppSlot#path}.
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(
            count=count, interval=interval, time_taken=time_taken, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putSlowRequest", [value]))

    @jsii.member(jsii_name="putStatusCode")
    def put_status_code(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47149a0674dfc76cc05f5de0cd9b4d907578b0a16ff55b3b9fa6a5c34d26b67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCode", [value]))

    @jsii.member(jsii_name="resetPrivateMemoryKb")
    def reset_private_memory_kb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateMemoryKb", []))

    @jsii.member(jsii_name="resetRequests")
    def reset_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequests", []))

    @jsii.member(jsii_name="resetSlowRequest")
    def reset_slow_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlowRequest", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="requests")
    def requests(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference", jsii.get(self, "requests"))

    @builtins.property
    @jsii.member(jsii_name="slowRequest")
    def slow_request(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference", jsii.get(self, "slowRequest"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(
        self,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList":
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList", jsii.get(self, "statusCode"))

    @builtins.property
    @jsii.member(jsii_name="privateMemoryKbInput")
    def private_memory_kb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privateMemoryKbInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsInput")
    def requests_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests"], jsii.get(self, "requestsInput"))

    @builtins.property
    @jsii.member(jsii_name="slowRequestInput")
    def slow_request_input(
        self,
    ) -> typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"]:
        return typing.cast(typing.Optional["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest"], jsii.get(self, "slowRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode"]]], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="privateMemoryKb")
    def private_memory_kb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privateMemoryKb"))

    @private_memory_kb.setter
    def private_memory_kb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1007cf936ebb99c1d2a615358348e161eaf7d479413a5c79793e7a1011f73b4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateMemoryKb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470233d27f9efa797ea9a4e0c373efcbb7e7b3333345d46406f205edff610642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "interval": "interval"},
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests:
    def __init__(self, *, count: jsii.Number, interval: builtins.str) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f50d99a00520c10dd35153deb8cf49a8cd229984dd4dbd2a8589854cc52d0d4)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "count": count,
            "interval": interval,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e43a01c7efad811e9da1762e5a2feb2be93a54fc3c8e2879b2d6aca51fefb8de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5833f1998607109299e8914098761627bd5ca3ef0dd45fa865ab0e90a422349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3799d6ad2f906c314d5ca1aa3795d5e0c1e6cf1784e31c7852d640c1acecc859)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e316f955293db8e97906250060f56409f654544ae4cfaa1f56ec79cf4b8a0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "time_taken": "timeTaken",
        "path": "path",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest:
    def __init__(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        time_taken: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param time_taken: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#path WindowsWebAppSlot#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__015e6e6fc9ddb5a667ef5ba416439dd8ee956e5859c1b69b979ec6cf8dec92bc)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument time_taken", value=time_taken, expected_type=type_hints["time_taken"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "count": count,
            "interval": interval,
            "time_taken": time_taken,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_taken(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#time_taken WindowsWebAppSlot#time_taken}.'''
        result = self._values.get("time_taken")
        assert result is not None, "Required property 'time_taken' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#path WindowsWebAppSlot#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ce7237f7257744b69b034d84b9678e1fcf9fd6065a888bb62e695fb55ea129)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="timeTakenInput")
    def time_taken_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeTakenInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed274e9db5f85da2895f10514474e72a59de8d852cfe24a86132e00f8dda876d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f256a16be3f322226c74a3c47129d4e2f34f8df23c231b98743f8f26cebecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b9c6109fd2c9fbd15ce666e1df6e4c14030ed3b66612f4080d1b8aea9a8b7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="timeTaken")
    def time_taken(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeTaken"))

    @time_taken.setter
    def time_taken(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6dfb6f8ff21dc6a6015a1906bb030e6552e735dcb19eb5e4ca25384d2c243a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeTaken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd0c04549518126ece5b6103bcf380a819623525e34bd04c96a43a8e24b0d5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "interval": "interval",
        "status_code_range": "statusCodeRange",
        "path": "path",
        "sub_status": "subStatus",
        "win32_status": "win32Status",
    },
)
class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode:
    def __init__(
        self,
        *,
        count: jsii.Number,
        interval: builtins.str,
        status_code_range: builtins.str,
        path: typing.Optional[builtins.str] = None,
        sub_status: typing.Optional[jsii.Number] = None,
        win32_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.
        :param interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.
        :param status_code_range: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#status_code_range WindowsWebAppSlot#status_code_range}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#path WindowsWebAppSlot#path}.
        :param sub_status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sub_status WindowsWebAppSlot#sub_status}.
        :param win32_status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#win32_status WindowsWebAppSlot#win32_status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2a64c26ba4a9342372c180eb9ecb0d50b2b1bcaafd005142c0e1f31569090a)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument status_code_range", value=status_code_range, expected_type=type_hints["status_code_range"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument sub_status", value=sub_status, expected_type=type_hints["sub_status"])
            check_type(argname="argument win32_status", value=win32_status, expected_type=type_hints["win32_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "count": count,
            "interval": interval,
            "status_code_range": status_code_range,
        }
        if path is not None:
            self._values["path"] = path
        if sub_status is not None:
            self._values["sub_status"] = sub_status
        if win32_status is not None:
            self._values["win32_status"] = win32_status

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#count WindowsWebAppSlot#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#interval WindowsWebAppSlot#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#status_code_range WindowsWebAppSlot#status_code_range}.'''
        result = self._values.get("status_code_range")
        assert result is not None, "Required property 'status_code_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#path WindowsWebAppSlot#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_status(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#sub_status WindowsWebAppSlot#sub_status}.'''
        result = self._values.get("sub_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def win32_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#win32_status WindowsWebAppSlot#win32_status}.'''
        result = self._values.get("win32_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797af0a22049d80e886003601f5c4852f4115c66f9f0ea87727b1fea95cc6eeb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f2bd220ef0bd393c29dded799390f25167adb3d1bcda98dd8500b4d843e357)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088c7dc79f6c35a8e030d5ff2fede12681087176caf471827d9558aa690a6d2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a835642669347df5190ff2c31ac1c3002103776464a2133e21497550adb754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e3c76efe295104396b085a9218f83147260c643f3d0340a70394e472bf32af1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18e1beb33de4eb1f8a335b4115fab23913a8c2aa190999742710c4f76706682)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be3dd95f12ade73169f860361dde5adf454fb407b4bcec382b4914938a225ba3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSubStatus")
    def reset_sub_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubStatus", []))

    @jsii.member(jsii_name="resetWin32Status")
    def reset_win32_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWin32Status", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRangeInput")
    def status_code_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subStatusInput")
    def sub_status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "subStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="win32StatusInput")
    def win32_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "win32StatusInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e49da4aaa5e67ed9a1de8b19e3b630f34b6e3b3afe2e057efba23947f901f81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e584f697292af13947e2796ec4b6734b0d499b458c99e9b194d40cbafb79f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d40dcd56e12d1ab496ae46f0da985d6755e9fee658bff51da2c532a19b0c167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="statusCodeRange")
    def status_code_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCodeRange"))

    @status_code_range.setter
    def status_code_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773f63a03e1c6678260868fe70c1173c6dc2970881f88c1e08f744c867cd633a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCodeRange", value)

    @builtins.property
    @jsii.member(jsii_name="subStatus")
    def sub_status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "subStatus"))

    @sub_status.setter
    def sub_status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15cf05293d06d8c8d214b0464387c8e92aa0e86622d1bd0110b9d4363bfe77f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subStatus", value)

    @builtins.property
    @jsii.member(jsii_name="win32Status")
    def win32_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "win32Status"))

    @win32_status.setter
    def win32_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e30077bb53e128394ceda7ef1c8cbd21aed9515edfe3335124a2b2c317d81a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "win32Status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a95019cd63c8057d772060cdf9a973f884ff23bf483afb5ba34774a4d96be95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigCors",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_origins": "allowedOrigins",
        "support_credentials": "supportCredentials",
    },
)
class WindowsWebAppSlotSiteConfigCors:
    def __init__(
        self,
        *,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        support_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470f63c4a9f0ea7250afae6ab0d8c5bc50f0608c9397c7b48910a74d9e2600c9)
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument support_credentials", value=support_credentials, expected_type=type_hints["support_credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_origins is not None:
            self._values["allowed_origins"] = allowed_origins
        if support_credentials is not None:
            self._values["support_credentials"] = support_credentials

    @builtins.property
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of origins that should be allowed to make cross-origin calls.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        '''
        result = self._values.get("allowed_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def support_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Are credentials allowed in CORS requests? Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        result = self._values.get("support_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigCorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigCorsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__783bcb44e463475d57108011523f9742a9df2a89479997d31425b735573bcdbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedOrigins")
    def reset_allowed_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOrigins", []))

    @jsii.member(jsii_name="resetSupportCredentials")
    def reset_support_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="supportCredentialsInput")
    def support_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "supportCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9bdc5029dd6a98e3f5e45b167778193ee0f576795ba9461a879d6150b7e971e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="supportCredentials")
    def support_credentials(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "supportCredentials"))

    @support_credentials.setter
    def support_credentials(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521617e82bc33f68c3ea66563c3f8403cc2c8fadbd134e256cd380a4f7621037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteConfigCors]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfigCors],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a929c6b3f2c324a4493910c66528805a15eeb5ca519bb3f0362578c61e6cbcff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "headers": "headers",
        "ip_address": "ipAddress",
        "name": "name",
        "priority": "priority",
        "service_tag": "serviceTag",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
    },
)
class WindowsWebAppSlotSiteConfigIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigIpRestrictionHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: The action to take. Possible values are ``Allow`` or ``Deny``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param headers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#headers WindowsWebAppSlot#headers}.
        :param ip_address: The CIDR notation of the IP or IP Range to match. For example: ``10.0.0.0/24`` or ``192.168.10.1/32`` or ``fe80::/64`` or ``13.107.6.152/31,13.107.128.0/22`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}
        :param name: The name which should be used for this ``ip_restriction``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param priority: The priority value of this ``ip_restriction``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#priority WindowsWebAppSlot#priority}
        :param service_tag: The Service Tag used for this IP Restriction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}
        :param virtual_network_subnet_id: The Virtual Network Subnet ID used for this IP Restriction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49912332d49341cfebf2049d27bded47355f9ff7970d599cc3dc9df770344585)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_tag", value=service_tag, expected_type=type_hints["service_tag"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if headers is not None:
            self._values["headers"] = headers
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_tag is not None:
            self._values["service_tag"] = service_tag
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to take. Possible values are ``Allow`` or ``Deny``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#headers WindowsWebAppSlot#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The CIDR notation of the IP or IP Range to match.

        For example: ``10.0.0.0/24`` or ``192.168.10.1/32`` or ``fe80::/64`` or ``13.107.6.152/31,13.107.128.0/22``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name which should be used for this ``ip_restriction``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority value of this ``ip_restriction``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#priority WindowsWebAppSlot#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''The Service Tag used for this IP Restriction.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}
        '''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''The Virtual Network Subnet ID used for this IP Restriction.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}
        '''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class WindowsWebAppSlotSiteConfigIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a77b92cd344064b9699e81b5bc034fc9c5d1849b0e0910223095f88d77bd52ec)
            check_type(argname="argument x_azure_fdid", value=x_azure_fdid, expected_type=type_hints["x_azure_fdid"])
            check_type(argname="argument x_fd_health_probe", value=x_fd_health_probe, expected_type=type_hints["x_fd_health_probe"])
            check_type(argname="argument x_forwarded_for", value=x_forwarded_for, expected_type=type_hints["x_forwarded_for"])
            check_type(argname="argument x_forwarded_host", value=x_forwarded_host, expected_type=type_hints["x_forwarded_host"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if x_azure_fdid is not None:
            self._values["x_azure_fdid"] = x_azure_fdid
        if x_fd_health_probe is not None:
            self._values["x_fd_health_probe"] = x_fd_health_probe
        if x_forwarded_for is not None:
            self._values["x_forwarded_for"] = x_forwarded_for
        if x_forwarded_host is not None:
            self._values["x_forwarded_host"] = x_forwarded_host

    @builtins.property
    def x_azure_fdid(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigIpRestrictionHeadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeadersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e523b6f3b945d710e24534fbb14eaa8e1f85836c8f01dc93d753444057ded8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab356762259d51f6af2922e656253287a62489b6561c37144b4623643f2ffa2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aea0a1c3ee5e8c6216c26e4054c744b56b57029c35ba17245c56b86df47745b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c69d593b8c872489d6c6825aa1268848943e65e64a6a85d0cf019455ed3bb6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__434e4bac9284d4e0963bf42d0ec6ab5ee0bc72a51c4551aaabf536a1666e2f0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b57c81242e2bc268ba5801e5537b3857729c021a60eb65d6bdaa1601eb4a0a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__848ee55047bc87051ab74096f3d3f2916459e52554eb25054575d978bfa0f52a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetXAzureFdid")
    def reset_x_azure_fdid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXAzureFdid", []))

    @jsii.member(jsii_name="resetXFdHealthProbe")
    def reset_x_fd_health_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXFdHealthProbe", []))

    @jsii.member(jsii_name="resetXForwardedFor")
    def reset_x_forwarded_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedFor", []))

    @jsii.member(jsii_name="resetXForwardedHost")
    def reset_x_forwarded_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedHost", []))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdidInput")
    def x_azure_fdid_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xAzureFdidInput"))

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbeInput")
    def x_fd_health_probe_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xFdHealthProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedForInput")
    def x_forwarded_for_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedForInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedHostInput")
    def x_forwarded_host_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedHostInput"))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdid")
    def x_azure_fdid(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xAzureFdid"))

    @x_azure_fdid.setter
    def x_azure_fdid(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d311ffa436a22b01e32c426183aa71f40c4bad55fc1564b873828bdc748bc24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed76b2b8489e14079895382d74f71249dc1fa2c9d8372aef3fa723b8f73595d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43121fb2b9d6f1b49db2cb92fbba37a5ea2b8f846bcc1466b7c0ed75a4096015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50df49933dc4d30451986df50b1d0b6315b79181c6a57d2481a10704c3e8c580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c953891fe66070050afc88805f52874afabf648b2992c77e77c40e8b1161f1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e996b951806e16b14604c3c2e9d04d26f2f89610a96328f2cb7d7a3d1348465b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b5b56f53ebb96ff79f9c6c0777254a31b0010f75df56c978eb2cb93d330e6f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c370e6138effc2eb831940244daf34e16499aa1a38e70fec93c1a519ebafdfa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c98898ba2e7782a6dd42428712bda76a0a8ec063f2da650e7fe3a3bded77b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfc7e763da90a0f6e4b7f26c24cb087cd2336e74de1852face87de72bf20637)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034fcedbb534bce1df618da7f6b6d746e69821f1105d83d8da963e0baa7f09cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigIpRestrictionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigIpRestrictionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82af4a2e106817700f9020b7ebd4f7a2fa4e863507c661486b816502dbb3ec2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6ef27e16919a957b442da22cb71201cd8f7b72a17948ef284efe6ff6e0c280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceTag")
    def reset_service_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceTag", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> WindowsWebAppSlotSiteConfigIpRestrictionHeadersList:
        return typing.cast(WindowsWebAppSlotSiteConfigIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTagInput")
    def service_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceTagInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__615a847921b8c42463d11dc573980d68e76560d9ed15533061005fce2e2c90ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10482b175e74e5b945dc5e3220a6365716cd052f1d85e4d84d0caed47026be82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1029c89617f74acbf6f304ff62f88b59bd65654adaa921342e97a6e2aa28df19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0fde8bdb8e2ddaffb2636a2dc6c87bd97570ed5d6f5398bd5e455a201fabd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4910cb8731118f445af9ba39e37856446693c09612e6b955a7595ad1b16c979)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5800b0371c0711f80204a63fff5b9f6a975e4fb2d9de0e2d9783bb49a1dc5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3efe8ccbe72b80d9912890add9c116d12971f4f62ccd24368c8bed4c41706663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b5b3bc46797cd6aa8d1b57b9e138895c76939171be62238ac400a5c2e6200b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putApplicationStack")
    def put_application_stack(
        self,
        *,
        current_stack: typing.Optional[builtins.str] = None,
        docker_container_name: typing.Optional[builtins.str] = None,
        docker_container_registry: typing.Optional[builtins.str] = None,
        docker_container_tag: typing.Optional[builtins.str] = None,
        dotnet_core_version: typing.Optional[builtins.str] = None,
        dotnet_version: typing.Optional[builtins.str] = None,
        java_container: typing.Optional[builtins.str] = None,
        java_container_version: typing.Optional[builtins.str] = None,
        java_embedded_server_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        java_version: typing.Optional[builtins.str] = None,
        node_version: typing.Optional[builtins.str] = None,
        php_version: typing.Optional[builtins.str] = None,
        python: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        python_version: typing.Optional[builtins.str] = None,
        tomcat_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param current_stack: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#current_stack WindowsWebAppSlot#current_stack}.
        :param docker_container_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_name WindowsWebAppSlot#docker_container_name}.
        :param docker_container_registry: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_registry WindowsWebAppSlot#docker_container_registry}.
        :param docker_container_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#docker_container_tag WindowsWebAppSlot#docker_container_tag}.
        :param dotnet_core_version: The version of DotNetCore to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_core_version WindowsWebAppSlot#dotnet_core_version}
        :param dotnet_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#dotnet_version WindowsWebAppSlot#dotnet_version}.
        :param java_container: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container WindowsWebAppSlot#java_container}.
        :param java_container_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_container_version WindowsWebAppSlot#java_container_version}.
        :param java_embedded_server_enabled: Should the application use the embedded web server for the version of Java in use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_embedded_server_enabled WindowsWebAppSlot#java_embedded_server_enabled}
        :param java_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#java_version WindowsWebAppSlot#java_version}.
        :param node_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#node_version WindowsWebAppSlot#node_version}.
        :param php_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#php_version WindowsWebAppSlot#php_version}.
        :param python: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python WindowsWebAppSlot#python}.
        :param python_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#python_version WindowsWebAppSlot#python_version}.
        :param tomcat_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#tomcat_version WindowsWebAppSlot#tomcat_version}.
        '''
        value = WindowsWebAppSlotSiteConfigApplicationStack(
            current_stack=current_stack,
            docker_container_name=docker_container_name,
            docker_container_registry=docker_container_registry,
            docker_container_tag=docker_container_tag,
            dotnet_core_version=dotnet_core_version,
            dotnet_version=dotnet_version,
            java_container=java_container,
            java_container_version=java_container_version,
            java_embedded_server_enabled=java_embedded_server_enabled,
            java_version=java_version,
            node_version=node_version,
            php_version=php_version,
            python=python,
            python_version=python_version,
            tomcat_version=tomcat_version,
        )

        return typing.cast(None, jsii.invoke(self, "putApplicationStack", [value]))

    @jsii.member(jsii_name="putAutoHealSetting")
    def put_auto_heal_setting(
        self,
        *,
        action: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingAction, typing.Dict[builtins.str, typing.Any]],
        trigger: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#trigger WindowsWebAppSlot#trigger}
        '''
        value = WindowsWebAppSlotSiteConfigAutoHealSetting(
            action=action, trigger=trigger
        )

        return typing.cast(None, jsii.invoke(self, "putAutoHealSetting", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        support_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_origins: Specifies a list of origins that should be allowed to make cross-origin calls. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#allowed_origins WindowsWebAppSlot#allowed_origins}
        :param support_credentials: Are credentials allowed in CORS requests? Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#support_credentials WindowsWebAppSlot#support_credentials}
        '''
        value = WindowsWebAppSlotSiteConfigCors(
            allowed_origins=allowed_origins, support_credentials=support_credentials
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putIpRestriction")
    def put_ip_restriction(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea378504f83ab448eed4bd74c5ecfc79d4df9bd8db7c021cb31d8c99a585127c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpRestriction", [value]))

    @jsii.member(jsii_name="putScmIpRestriction")
    def put_scm_ip_restriction(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestriction", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53c0cc9c3f543fcacf6c6b15390376c9afbf50276ed3c75b5ca2a7ed5dac9df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScmIpRestriction", [value]))

    @jsii.member(jsii_name="putVirtualApplication")
    def put_virtual_application(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplication", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d43b69b39efd870b867a33de5cb04e8d0ade3264e980b41abebf323f4ad303a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualApplication", [value]))

    @jsii.member(jsii_name="resetAlwaysOn")
    def reset_always_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysOn", []))

    @jsii.member(jsii_name="resetApiDefinitionUrl")
    def reset_api_definition_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiDefinitionUrl", []))

    @jsii.member(jsii_name="resetApiManagementApiId")
    def reset_api_management_api_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiManagementApiId", []))

    @jsii.member(jsii_name="resetAppCommandLine")
    def reset_app_command_line(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppCommandLine", []))

    @jsii.member(jsii_name="resetApplicationStack")
    def reset_application_stack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationStack", []))

    @jsii.member(jsii_name="resetAutoHealEnabled")
    def reset_auto_heal_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealEnabled", []))

    @jsii.member(jsii_name="resetAutoHealSetting")
    def reset_auto_heal_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHealSetting", []))

    @jsii.member(jsii_name="resetAutoSwapSlotName")
    def reset_auto_swap_slot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSwapSlotName", []))

    @jsii.member(jsii_name="resetContainerRegistryManagedIdentityClientId")
    def reset_container_registry_managed_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryManagedIdentityClientId", []))

    @jsii.member(jsii_name="resetContainerRegistryUseManagedIdentity")
    def reset_container_registry_use_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryUseManagedIdentity", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetDefaultDocuments")
    def reset_default_documents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultDocuments", []))

    @jsii.member(jsii_name="resetFtpsState")
    def reset_ftps_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFtpsState", []))

    @jsii.member(jsii_name="resetHealthCheckEvictionTimeInMin")
    def reset_health_check_eviction_time_in_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckEvictionTimeInMin", []))

    @jsii.member(jsii_name="resetHealthCheckPath")
    def reset_health_check_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckPath", []))

    @jsii.member(jsii_name="resetHttp2Enabled")
    def reset_http2_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Enabled", []))

    @jsii.member(jsii_name="resetIpRestriction")
    def reset_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRestriction", []))

    @jsii.member(jsii_name="resetLoadBalancingMode")
    def reset_load_balancing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingMode", []))

    @jsii.member(jsii_name="resetLocalMysqlEnabled")
    def reset_local_mysql_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalMysqlEnabled", []))

    @jsii.member(jsii_name="resetManagedPipelineMode")
    def reset_managed_pipeline_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedPipelineMode", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetRemoteDebuggingEnabled")
    def reset_remote_debugging_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingEnabled", []))

    @jsii.member(jsii_name="resetRemoteDebuggingVersion")
    def reset_remote_debugging_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteDebuggingVersion", []))

    @jsii.member(jsii_name="resetScmIpRestriction")
    def reset_scm_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmIpRestriction", []))

    @jsii.member(jsii_name="resetScmMinimumTlsVersion")
    def reset_scm_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmMinimumTlsVersion", []))

    @jsii.member(jsii_name="resetScmUseMainIpRestriction")
    def reset_scm_use_main_ip_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScmUseMainIpRestriction", []))

    @jsii.member(jsii_name="resetUse32BitWorker")
    def reset_use32_bit_worker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUse32BitWorker", []))

    @jsii.member(jsii_name="resetVirtualApplication")
    def reset_virtual_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualApplication", []))

    @jsii.member(jsii_name="resetVnetRouteAllEnabled")
    def reset_vnet_route_all_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnetRouteAllEnabled", []))

    @jsii.member(jsii_name="resetWebsocketsEnabled")
    def reset_websockets_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsocketsEnabled", []))

    @jsii.member(jsii_name="resetWorkerCount")
    def reset_worker_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerCount", []))

    @builtins.property
    @jsii.member(jsii_name="applicationStack")
    def application_stack(
        self,
    ) -> WindowsWebAppSlotSiteConfigApplicationStackOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigApplicationStackOutputReference, jsii.get(self, "applicationStack"))

    @builtins.property
    @jsii.member(jsii_name="autoHealSetting")
    def auto_heal_setting(
        self,
    ) -> WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference, jsii.get(self, "autoHealSetting"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> WindowsWebAppSlotSiteConfigCorsOutputReference:
        return typing.cast(WindowsWebAppSlotSiteConfigCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="detailedErrorLoggingEnabled")
    def detailed_error_logging_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "detailedErrorLoggingEnabled"))

    @builtins.property
    @jsii.member(jsii_name="ipRestriction")
    def ip_restriction(self) -> WindowsWebAppSlotSiteConfigIpRestrictionList:
        return typing.cast(WindowsWebAppSlotSiteConfigIpRestrictionList, jsii.get(self, "ipRestriction"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestriction")
    def scm_ip_restriction(self) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionList":
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionList", jsii.get(self, "scmIpRestriction"))

    @builtins.property
    @jsii.member(jsii_name="scmType")
    def scm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmType"))

    @builtins.property
    @jsii.member(jsii_name="virtualApplication")
    def virtual_application(
        self,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationList":
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationList", jsii.get(self, "virtualApplication"))

    @builtins.property
    @jsii.member(jsii_name="windowsFxVersion")
    def windows_fx_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowsFxVersion"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOnInput")
    def always_on_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "alwaysOnInput"))

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrlInput")
    def api_definition_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiDefinitionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiIdInput")
    def api_management_api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementApiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appCommandLineInput")
    def app_command_line_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appCommandLineInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationStackInput")
    def application_stack_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack], jsii.get(self, "applicationStackInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealEnabledInput")
    def auto_heal_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoHealEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHealSettingInput")
    def auto_heal_setting_input(
        self,
    ) -> typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting], jsii.get(self, "autoHealSettingInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSwapSlotNameInput")
    def auto_swap_slot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoSwapSlotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryManagedIdentityClientIdInput")
    def container_registry_managed_identity_client_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryManagedIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryUseManagedIdentityInput")
    def container_registry_use_managed_identity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "containerRegistryUseManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional[WindowsWebAppSlotSiteConfigCors]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfigCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDocumentsInput")
    def default_documents_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultDocumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="ftpsStateInput")
    def ftps_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ftpsStateInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMinInput")
    def health_check_eviction_time_in_min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckEvictionTimeInMinInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckPathInput")
    def health_check_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckPathInput"))

    @builtins.property
    @jsii.member(jsii_name="http2EnabledInput")
    def http2_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "http2EnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRestrictionInput")
    def ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]], jsii.get(self, "ipRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingModeInput")
    def load_balancing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="localMysqlEnabledInput")
    def local_mysql_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "localMysqlEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPipelineModeInput")
    def managed_pipeline_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPipelineModeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingEnabledInput")
    def remote_debugging_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "remoteDebuggingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersionInput")
    def remote_debugging_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteDebuggingVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmIpRestrictionInput")
    def scm_ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestriction"]]], jsii.get(self, "scmIpRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersionInput")
    def scm_minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scmMinimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="scmUseMainIpRestrictionInput")
    def scm_use_main_ip_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "scmUseMainIpRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="use32BitWorkerInput")
    def use32_bit_worker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "use32BitWorkerInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualApplicationInput")
    def virtual_application_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplication"]]], jsii.get(self, "virtualApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="vnetRouteAllEnabledInput")
    def vnet_route_all_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "vnetRouteAllEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="websocketsEnabledInput")
    def websockets_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "websocketsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCountInput")
    def worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysOn")
    def always_on(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "alwaysOn"))

    @always_on.setter
    def always_on(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75b13b7bcccf7f5dff6386fa2c134ca114e3be8ac25bd5fc475b9a8923fde5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysOn", value)

    @builtins.property
    @jsii.member(jsii_name="apiDefinitionUrl")
    def api_definition_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiDefinitionUrl"))

    @api_definition_url.setter
    def api_definition_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf6c9e347d43696d3856d9e36fb4c97bb55e707dd7b3141211eaa6b28f696b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiDefinitionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementApiId")
    def api_management_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementApiId"))

    @api_management_api_id.setter
    def api_management_api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5985c3c4ace45ee9189c1d838985dd30937dd18a58720490cb412359ecd9f73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementApiId", value)

    @builtins.property
    @jsii.member(jsii_name="appCommandLine")
    def app_command_line(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appCommandLine"))

    @app_command_line.setter
    def app_command_line(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2062484f321eee105079ad9fcc82a8e34d0956145dc50885b4128829a584b127)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appCommandLine", value)

    @builtins.property
    @jsii.member(jsii_name="autoHealEnabled")
    def auto_heal_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoHealEnabled"))

    @auto_heal_enabled.setter
    def auto_heal_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__294d2f5e413a851901899c023f2b1207cd9d0a3138efea1673bcdf6cf2039a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHealEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="autoSwapSlotName")
    def auto_swap_slot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoSwapSlotName"))

    @auto_swap_slot_name.setter
    def auto_swap_slot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77e4e1c1bed99157c85612fafdb5876580aee353bc0c34e5e24752a8482441b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSwapSlotName", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryManagedIdentityClientId")
    def container_registry_managed_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryManagedIdentityClientId"))

    @container_registry_managed_identity_client_id.setter
    def container_registry_managed_identity_client_id(
        self,
        value: builtins.str,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fadc886a9f26a60afb6eba03a73087de46e5e8007395cf10b80599a357a2ce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryManagedIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryUseManagedIdentity")
    def container_registry_use_managed_identity(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "containerRegistryUseManagedIdentity"))

    @container_registry_use_managed_identity.setter
    def container_registry_use_managed_identity(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5beb51af2ed4b5a0eb7e4e4d17a7748926c2cded58510587b105b4a63065c1f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryUseManagedIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDocuments")
    def default_documents(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultDocuments"))

    @default_documents.setter
    def default_documents(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402be6f3eb01a33df48f1471817e00dc848c1813638fc872c746e5cd52f66657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="ftpsState")
    def ftps_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ftpsState"))

    @ftps_state.setter
    def ftps_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3102c613215858eebfc831770b8d79bc9282bc824416a9385380415c77fc920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ftpsState", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckEvictionTimeInMin")
    def health_check_eviction_time_in_min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckEvictionTimeInMin"))

    @health_check_eviction_time_in_min.setter
    def health_check_eviction_time_in_min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1afe95caf3835ef7c6a8c9daae75e6fbdb7f53e45a1011265d513a62bb54f6c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEvictionTimeInMin", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d267a2a3f04bb99a87177684c19676f49c9f5e72b4eceef40211219b5ce341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckPath", value)

    @builtins.property
    @jsii.member(jsii_name="http2Enabled")
    def http2_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "http2Enabled"))

    @http2_enabled.setter
    def http2_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3acec33d9c15d6d47ea51d6f266fc13da94b45c52c7e64b8bd64dd20a7aa729a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2Enabled", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingMode")
    def load_balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingMode"))

    @load_balancing_mode.setter
    def load_balancing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2008233cfdc6bc5f45ad45f5a7f230e2e8f64f3d1f509e07fd37b08013a6d66d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingMode", value)

    @builtins.property
    @jsii.member(jsii_name="localMysqlEnabled")
    def local_mysql_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "localMysqlEnabled"))

    @local_mysql_enabled.setter
    def local_mysql_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c84618945ccf2f3652d07e0169ece13fced66628351253a4283c07b0f07e91aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMysqlEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="managedPipelineMode")
    def managed_pipeline_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPipelineMode"))

    @managed_pipeline_mode.setter
    def managed_pipeline_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36da70bf2013f91d22d3210f7a371498ade72cb0c50f96d198a9d9815e3ecfab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPipelineMode", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae259c12fa3475943a34140df25416fd4b8588d7b1c3a86e7334d7f3639a84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingEnabled")
    def remote_debugging_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "remoteDebuggingEnabled"))

    @remote_debugging_enabled.setter
    def remote_debugging_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d8f2ce5b118bb338df7e5e08420bbdf50e7349f0fbe9e6e0e0becd24db517d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="remoteDebuggingVersion")
    def remote_debugging_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteDebuggingVersion"))

    @remote_debugging_version.setter
    def remote_debugging_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd1cedb5dc7999dd23dfb98ee81c00ba86031e730c2c4d987bc66c4474774a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteDebuggingVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scmMinimumTlsVersion")
    def scm_minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmMinimumTlsVersion"))

    @scm_minimum_tls_version.setter
    def scm_minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146866444087ddd0aa0c0f5ed9b6e7f94aa53318841399d32d4df27fb5bb20ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scmMinimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="scmUseMainIpRestriction")
    def scm_use_main_ip_restriction(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "scmUseMainIpRestriction"))

    @scm_use_main_ip_restriction.setter
    def scm_use_main_ip_restriction(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9db5b91f3420a6b61826e66badfc7ca0e779c88a0d04179fa90afc85e64d63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scmUseMainIpRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="use32BitWorker")
    def use32_bit_worker(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "use32BitWorker"))

    @use32_bit_worker.setter
    def use32_bit_worker(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c98e38da3e420d2135e28f290c6733d51899a19c8cf29f3224bdf33da175259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "use32BitWorker", value)

    @builtins.property
    @jsii.member(jsii_name="vnetRouteAllEnabled")
    def vnet_route_all_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "vnetRouteAllEnabled"))

    @vnet_route_all_enabled.setter
    def vnet_route_all_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd901827a9ec0546ad8fc7c4eef7e92d56370655242d53956a4d3381c79f4cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnetRouteAllEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="websocketsEnabled")
    def websockets_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "websocketsEnabled"))

    @websockets_enabled.setter
    def websockets_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30264053e476cec68c84f92e40d32ed46b790b696ef0cbedf23af6b6e549400b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websocketsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d431ce97ae5d1f821e83cf47f0f953792debbcb61b4eb93df2f7cc1907dfa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteConfig]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844fb1223b17c7c7ddf7cbd0b641327a3137d17ae50e3561530ecc081906b80a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "headers": "headers",
        "ip_address": "ipAddress",
        "name": "name",
        "priority": "priority",
        "service_tag": "serviceTag",
        "virtual_network_subnet_id": "virtualNetworkSubnetId",
    },
)
class WindowsWebAppSlotSiteConfigScmIpRestriction:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        service_tag: typing.Optional[builtins.str] = None,
        virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: The action to take. Possible values are ``Allow`` or ``Deny``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        :param headers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#headers WindowsWebAppSlot#headers}.
        :param ip_address: The CIDR notation of the IP or IP Range to match. For example: ``10.0.0.0/24`` or ``192.168.10.1/32`` or ``fe80::/64`` or ``13.107.6.152/31,13.107.128.0/22`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}
        :param name: The name which should be used for this ``ip_restriction``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        :param priority: The priority value of this ``ip_restriction``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#priority WindowsWebAppSlot#priority}
        :param service_tag: The Service Tag used for this IP Restriction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}
        :param virtual_network_subnet_id: The Virtual Network Subnet ID used for this IP Restriction. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6879987b34070b1b1aa9a6bbb39a0af826feb2c9172f80030c3a41d0faeaa03)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument service_tag", value=service_tag, expected_type=type_hints["service_tag"])
            check_type(argname="argument virtual_network_subnet_id", value=virtual_network_subnet_id, expected_type=type_hints["virtual_network_subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if headers is not None:
            self._values["headers"] = headers
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if service_tag is not None:
            self._values["service_tag"] = service_tag
        if virtual_network_subnet_id is not None:
            self._values["virtual_network_subnet_id"] = virtual_network_subnet_id

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to take. Possible values are ``Allow`` or ``Deny``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#action WindowsWebAppSlot#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders"]]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#headers WindowsWebAppSlot#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders"]]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''The CIDR notation of the IP or IP Range to match.

        For example: ``10.0.0.0/24`` or ``192.168.10.1/32`` or ``fe80::/64`` or ``13.107.6.152/31,13.107.128.0/22``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#ip_address WindowsWebAppSlot#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name which should be used for this ``ip_restriction``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority value of this ``ip_restriction``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#priority WindowsWebAppSlot#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_tag(self) -> typing.Optional[builtins.str]:
        '''The Service Tag used for this IP Restriction.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#service_tag WindowsWebAppSlot#service_tag}
        '''
        result = self._values.get("service_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_subnet_id(self) -> typing.Optional[builtins.str]:
        '''The Virtual Network Subnet ID used for this IP Restriction.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_network_subnet_id WindowsWebAppSlot#virtual_network_subnet_id}
        '''
        result = self._values.get("virtual_network_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigScmIpRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "x_azure_fdid": "xAzureFdid",
        "x_fd_health_probe": "xFdHealthProbe",
        "x_forwarded_for": "xForwardedFor",
        "x_forwarded_host": "xForwardedHost",
    },
)
class WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders:
    def __init__(
        self,
        *,
        x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
        x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param x_azure_fdid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.
        :param x_fd_health_probe: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.
        :param x_forwarded_for: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.
        :param x_forwarded_host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d183f20c21be45549b2b49c32adcef256f3d7f9c7c1a44d6ed48548c471d6dd)
            check_type(argname="argument x_azure_fdid", value=x_azure_fdid, expected_type=type_hints["x_azure_fdid"])
            check_type(argname="argument x_fd_health_probe", value=x_fd_health_probe, expected_type=type_hints["x_fd_health_probe"])
            check_type(argname="argument x_forwarded_for", value=x_forwarded_for, expected_type=type_hints["x_forwarded_for"])
            check_type(argname="argument x_forwarded_host", value=x_forwarded_host, expected_type=type_hints["x_forwarded_host"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if x_azure_fdid is not None:
            self._values["x_azure_fdid"] = x_azure_fdid
        if x_fd_health_probe is not None:
            self._values["x_fd_health_probe"] = x_fd_health_probe
        if x_forwarded_for is not None:
            self._values["x_forwarded_for"] = x_forwarded_for
        if x_forwarded_host is not None:
            self._values["x_forwarded_host"] = x_forwarded_host

    @builtins.property
    def x_azure_fdid(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_azure_fdid WindowsWebAppSlot#x_azure_fdid}.'''
        result = self._values.get("x_azure_fdid")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_fd_health_probe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_fd_health_probe WindowsWebAppSlot#x_fd_health_probe}.'''
        result = self._values.get("x_fd_health_probe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_for WindowsWebAppSlot#x_forwarded_for}.'''
        result = self._values.get("x_forwarded_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def x_forwarded_host(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#x_forwarded_host WindowsWebAppSlot#x_forwarded_host}.'''
        result = self._values.get("x_forwarded_host")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42ac085ce916e259136454ec78b817d79ea3070c730168a0e0a645c3ecae304)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a60a8609b27d4e94870b689492b6521e86e9a43a05b94ad792ffea331b8a416)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481654eebce2bfaaf9ba178f321b9ca9ece565c134c18c861fa6f64c320ff555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3f531e7ea33b2c4694804468c63876da5d42ce8f4b7ca7f3ff372921ab47b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df3d852b6be161cfbe1609cfb84d065a5b7e20adfeb3782b8916d9bff03df6c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f679f3bf51fb7c97ce9806a07f63b941aa6342174c9e7cb135675fd0ca934b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9898b336577cdf92394934c6cdfb1395b180ed7433d1f40664528ac18cd36104)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetXAzureFdid")
    def reset_x_azure_fdid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXAzureFdid", []))

    @jsii.member(jsii_name="resetXFdHealthProbe")
    def reset_x_fd_health_probe(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXFdHealthProbe", []))

    @jsii.member(jsii_name="resetXForwardedFor")
    def reset_x_forwarded_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedFor", []))

    @jsii.member(jsii_name="resetXForwardedHost")
    def reset_x_forwarded_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXForwardedHost", []))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdidInput")
    def x_azure_fdid_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xAzureFdidInput"))

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbeInput")
    def x_fd_health_probe_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xFdHealthProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedForInput")
    def x_forwarded_for_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedForInput"))

    @builtins.property
    @jsii.member(jsii_name="xForwardedHostInput")
    def x_forwarded_host_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "xForwardedHostInput"))

    @builtins.property
    @jsii.member(jsii_name="xAzureFdid")
    def x_azure_fdid(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xAzureFdid"))

    @x_azure_fdid.setter
    def x_azure_fdid(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d104e2d726bcccc6f73eee22d13b105b3fd94a167bad912fec5996d308fb14ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xAzureFdid", value)

    @builtins.property
    @jsii.member(jsii_name="xFdHealthProbe")
    def x_fd_health_probe(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xFdHealthProbe"))

    @x_fd_health_probe.setter
    def x_fd_health_probe(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006cb1b48eb3c248cf04066c7f04140a7345ed6e26f0af28ac3d5b542cef9439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xFdHealthProbe", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedFor")
    def x_forwarded_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedFor"))

    @x_forwarded_for.setter
    def x_forwarded_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0d2945551ced0b6d731e965c63778cc5a71c1c5763678b4185eb810ef11897)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedFor", value)

    @builtins.property
    @jsii.member(jsii_name="xForwardedHost")
    def x_forwarded_host(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "xForwardedHost"))

    @x_forwarded_host.setter
    def x_forwarded_host(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5843792506122b0faed02e2f5cb8491d2d966555e76e86211fe7eec3ab0e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xForwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9beb4b8f85395ce9dda3d4e37e730adbc730dfbceb7c0afe9db5701a600b3287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa4274b0b8e39c532c17d3ec880eff5f3fa268c7db0eec554305dec2346425ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47dbde19d5a077cd33ff6023e3b5135417fc446f566f1d359696dbf618c33376)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc5b3ce11d122d10f18e52b09c7e60aa11bc59ef9f28e18f95996576cba00f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f280ac19de42d8065f3864d38b7d911c7ac5e291a4251782598a589160bca3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c029b5c75c40ba018aaabba0ddc37e4e3605daeea2a85d22f656c0792e683a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8615ce096174c0a0c46ffa6fecd3a613d7b96ff99c4f0e4c40cf65040b7f552c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b100f398f9197fa41727489adc6934bfd49b1ddefdae07c78733c338032081)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5508b4b52432124c003a73c49ed82f214f47fc9865dd7fc8803f5da52df1c477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetServiceTag")
    def reset_service_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceTag", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetId")
    def reset_virtual_network_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList:
        return typing.cast(WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceTagInput")
    def service_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceTagInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdInput")
    def virtual_network_subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkSubnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e32039f9fc434c64ea7865c70c14b803a7c2e1ffc4b9c860a3495eec0f05a20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7878c9f9f978a3a30414797b5b6c8aa2c722ae6e30722ba4758de2d154aeb5f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51ad027fcec1a0af280a1d0a30153c779a34722986d46482874a0f30c12c9f0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02004ddbc7e7d69db9483c0a1499a65f3af363aa12891cbad15861373547c6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="serviceTag")
    def service_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceTag"))

    @service_tag.setter
    def service_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__557a4d941526d4f97e9e2696ae199ed30afbe0730b4d5ef47af5e30697f73348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceTag", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkSubnetId"))

    @virtual_network_subnet_id.setter
    def virtual_network_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d41df6b78aff77378c9a9ea7dfc59a9b1da36387c2ef078ce1217750092ebb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d2ee222f317e7844d2b9126c5d1c97e22979ce879299bf209cb94a1cc6271e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplication",
    jsii_struct_bases=[],
    name_mapping={
        "physical_path": "physicalPath",
        "preload": "preload",
        "virtual_path": "virtualPath",
        "virtual_directory": "virtualDirectory",
    },
)
class WindowsWebAppSlotSiteConfigVirtualApplication:
    def __init__(
        self,
        *,
        physical_path: builtins.str,
        preload: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        virtual_path: builtins.str,
        virtual_directory: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param physical_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.
        :param preload: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#preload WindowsWebAppSlot#preload}.
        :param virtual_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.
        :param virtual_directory: virtual_directory block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_directory WindowsWebAppSlot#virtual_directory}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f3d97c9d11ecc502144d921506e7a6935597b49e8f7019dcddc890e209e4d6)
            check_type(argname="argument physical_path", value=physical_path, expected_type=type_hints["physical_path"])
            check_type(argname="argument preload", value=preload, expected_type=type_hints["preload"])
            check_type(argname="argument virtual_path", value=virtual_path, expected_type=type_hints["virtual_path"])
            check_type(argname="argument virtual_directory", value=virtual_directory, expected_type=type_hints["virtual_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "physical_path": physical_path,
            "preload": preload,
            "virtual_path": virtual_path,
        }
        if virtual_directory is not None:
            self._values["virtual_directory"] = virtual_directory

    @builtins.property
    def physical_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.'''
        result = self._values.get("physical_path")
        assert result is not None, "Required property 'physical_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preload(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#preload WindowsWebAppSlot#preload}.'''
        result = self._values.get("preload")
        assert result is not None, "Required property 'preload' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def virtual_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.'''
        result = self._values.get("virtual_path")
        assert result is not None, "Required property 'virtual_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_directory(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]]:
        '''virtual_directory block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_directory WindowsWebAppSlot#virtual_directory}
        '''
        result = self._values.get("virtual_directory")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigVirtualApplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigVirtualApplicationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa609b5c3988ba41dad677686a266bee83b8096ec32b12a3caef9a8c2096c2d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f838a625b2d15864c0056a3efa9230a7abda27fd7e02b22bd6cda15e45216bfd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e60234787d6ef5455804d0a0a68271c5b61d2fd9042a6f515829ac285f262e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52bda3feb58fdccbdb0d88b70011dcff94c64f014756a9c7a5e8e0dcd7c12d12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c51e771011be0399eeb93b8272ad9e5298990771f2680333224dea0e0a6b63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0245ac9e608422b49a703264cdebb6b136cc2d74f013f1fd10c60629f5289f08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa51d5c657fe0b401a79b336551b6d22107eaedf4e7992445b66f21503b710ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVirtualDirectory")
    def put_virtual_directory(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d50fbaef69a63e5984904dfbe3eacbfec184ed4af8fe78df3eda6b421c3c408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVirtualDirectory", [value]))

    @jsii.member(jsii_name="resetVirtualDirectory")
    def reset_virtual_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="virtualDirectory")
    def virtual_directory(
        self,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList":
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList", jsii.get(self, "virtualDirectory"))

    @builtins.property
    @jsii.member(jsii_name="physicalPathInput")
    def physical_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "physicalPathInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadInput")
    def preload_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preloadInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualDirectoryInput")
    def virtual_directory_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory"]]], jsii.get(self, "virtualDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualPathInput")
    def virtual_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualPathInput"))

    @builtins.property
    @jsii.member(jsii_name="physicalPath")
    def physical_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "physicalPath"))

    @physical_path.setter
    def physical_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f0687af086eb8eb6881e5754fa9efefaceac68ddccbef838f10d01ee59494f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "physicalPath", value)

    @builtins.property
    @jsii.member(jsii_name="preload")
    def preload(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preload"))

    @preload.setter
    def preload(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980d6578fe3ec229d3bc21708f9db67398175e98dd2e9c90456a0f923b866634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preload", value)

    @builtins.property
    @jsii.member(jsii_name="virtualPath")
    def virtual_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualPath"))

    @virtual_path.setter
    def virtual_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aed765128ddd7a63143a15dc23c6c8283ebd0987ec9961bc884fbf5ceeaa5b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e70e3916b318810002eba8b3457745da0ba931193f30c9666c1be775a5b9a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory",
    jsii_struct_bases=[],
    name_mapping={"physical_path": "physicalPath", "virtual_path": "virtualPath"},
)
class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory:
    def __init__(
        self,
        *,
        physical_path: typing.Optional[builtins.str] = None,
        virtual_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param physical_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.
        :param virtual_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b8f18e4dd59f4db815ccbb81209efd8c76e3a1d15ec58fcc5a52883f3419f9)
            check_type(argname="argument physical_path", value=physical_path, expected_type=type_hints["physical_path"])
            check_type(argname="argument virtual_path", value=virtual_path, expected_type=type_hints["virtual_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if physical_path is not None:
            self._values["physical_path"] = physical_path
        if virtual_path is not None:
            self._values["virtual_path"] = virtual_path

    @builtins.property
    def physical_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#physical_path WindowsWebAppSlot#physical_path}.'''
        result = self._values.get("physical_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#virtual_path WindowsWebAppSlot#virtual_path}.'''
        result = self._values.get("virtual_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c20be605ad3eca6fdca492b5ba4fbd19a67feccb5bfdf8a527e665013f7f179)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0231c31b67dbfaa731a1ee0013f855a7706b4abe80e86e8067779b97d6a90b1b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9578ba0492bef1512ffa68d46a685925a073937b7574395d5c88f32fc10618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e753790fbff204ddfead3b603884c1eac4efff48bde7b58da65f7c089fb0826a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384eb4d51f94cd20cdf113a4f33f373c4ed0b7f06e70917ce58ce270eff5f7e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdebff5a36260ca56e0d629c7922575844757502b899a63114291c77a5c56691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__996d94188c6d65d09290d2e3c624f756fadbaac599469072ca15502ed2509f3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPhysicalPath")
    def reset_physical_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhysicalPath", []))

    @jsii.member(jsii_name="resetVirtualPath")
    def reset_virtual_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualPath", []))

    @builtins.property
    @jsii.member(jsii_name="physicalPathInput")
    def physical_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "physicalPathInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualPathInput")
    def virtual_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualPathInput"))

    @builtins.property
    @jsii.member(jsii_name="physicalPath")
    def physical_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "physicalPath"))

    @physical_path.setter
    def physical_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9c99b82f0b246160e20a9920a0efe809a1d5061c60c88640d295bd691e0e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "physicalPath", value)

    @builtins.property
    @jsii.member(jsii_name="virtualPath")
    def virtual_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualPath"))

    @virtual_path.setter
    def virtual_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83bb957b23fd8464b76b120d728d92e9754102421d3fd2a4da39f8921144a5df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395e4ef7f7e878d4e4d6ede1eaf0489061e613e37ca68240901a553d27485161)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredential",
    jsii_struct_bases=[],
    name_mapping={},
)
class WindowsWebAppSlotSiteCredential:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotSiteCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotSiteCredentialList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredentialList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7229b8d36e9863d792cd89a1927fa01be7b42aff37f410cc985f66df2f236220)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotSiteCredentialOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa80a262c7b8d4d536d63b608768c59f4e71b6f5b18882af099b0c9be3a5cae8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotSiteCredentialOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a13fae3140f88c3af2765e96c317916a799300900c37bb4a429ff10dce959440)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a42ef683f6073979d2e942eb8dc16657ff1430c2f1388b4926dcb2284871315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1fd003c6787f8d63d9822d128a2dc61c8742685724a6579c080828bd175ff78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class WindowsWebAppSlotSiteCredentialOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotSiteCredentialOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a21d087f9d29f35653162380c982a03b71163fb4fc684f262ff42ffb9646989c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsWebAppSlotSiteCredential]:
        return typing.cast(typing.Optional[WindowsWebAppSlotSiteCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsWebAppSlotSiteCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1454a7ba6a0452158550eda53e321193ae17b6fbf34a10aa6831d2b791f7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccount",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "account_name": "accountName",
        "name": "name",
        "share_name": "shareName",
        "type": "type",
        "mount_path": "mountPath",
    },
)
class WindowsWebAppSlotStorageAccount:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        account_name: builtins.str,
        name: builtins.str,
        share_name: builtins.str,
        type: builtins.str,
        mount_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#access_key WindowsWebAppSlot#access_key}.
        :param account_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#account_name WindowsWebAppSlot#account_name}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}.
        :param share_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#share_name WindowsWebAppSlot#share_name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}.
        :param mount_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#mount_path WindowsWebAppSlot#mount_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4fe8093ab79cc0a6806610971fca41204aed5195faf5db5e94bf3fa21d6ea3)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key": access_key,
            "account_name": account_name,
            "name": name,
            "share_name": share_name,
            "type": type,
        }
        if mount_path is not None:
            self._values["mount_path"] = mount_path

    @builtins.property
    def access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#access_key WindowsWebAppSlot#access_key}.'''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#account_name WindowsWebAppSlot#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#name WindowsWebAppSlot#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#share_name WindowsWebAppSlot#share_name}.'''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#type WindowsWebAppSlot#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#mount_path WindowsWebAppSlot#mount_path}.'''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotStorageAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotStorageAccountList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccountList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0826a1015f7d46bd3e9de31eca9fbb04a6e80a9a3b88058e8363211893f3d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsWebAppSlotStorageAccountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0964fefbe1d90dbf5bf03fd065abdc020460e741c491ed005a9e8ff73a82ab3b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsWebAppSlotStorageAccountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f6ce8b959076d4b23bd275ae3adc320a25302b578afc583ca551c6ca0a0c89f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3504f16163c7555fa632c6583c947498c25b02311809ca8f890d0e61f87a2aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13f230ccf6305e304f257394e50ba0497e783ded7ca01e5d8bfb26a2748dbc18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078c65f80ebef67de767e0ded308f9de7e24955061cd6a03db276dee1112e601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsWebAppSlotStorageAccountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotStorageAccountOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08afdaa06449fcc61c3c58d38ef4c5af76bfcc1c5998c5ac6f395e4bbe37c2b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountPath")
    def reset_mount_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountPath", []))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mountPathInput")
    def mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ff0f10ab1aeb05c73e34cef2c99cb3540814d665e527873a90d130acd031153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d8bae4c84a3def269b618519b907f7dd5b3a9e04f80cac97be35414fe1c67a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="mountPath")
    def mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountPath"))

    @mount_path.setter
    def mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e3ab4e41f3aea87d911230a074ecc1f393d72c3fc9ad81da7c01b853956fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bc9244ac2af24c8603db2ec43cae7d588b5f302575188cf73cd15e27d6175f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76124b38d17b8d4c8dcee91e779b783b67efbdc8f7a2f4c73db695a06e302ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9daddc613d16fc98c245016238d1d43cd7262ec7b96a2e158bec25a0c8912a17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e59731f62561c2fb1daeffc81f74b42822029f4bf83c39be7c2eec1b889866d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WindowsWebAppSlotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#create WindowsWebAppSlot#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#delete WindowsWebAppSlot#delete}.
        :param read: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#read WindowsWebAppSlot#read}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#update WindowsWebAppSlot#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec33f891d151e10bbbf0eaf3f91677cc4fb6f4dc458f26f9b24dcccbda253be9)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#create WindowsWebAppSlot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#delete WindowsWebAppSlot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#read WindowsWebAppSlot#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/azurerm/3.55.0/docs/resources/windows_web_app_slot#update WindowsWebAppSlot#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsWebAppSlotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsWebAppSlotTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsWebAppSlot.WindowsWebAppSlotTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4424579ec7e134b1cdae7260e4393dfce306e338185676fc9de5282cbe86a67)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc8fba0ced29ac1a0d119223c288ce04ea5cbe0784b1b2a65bec4315e2d79b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3488f961e78a47ce4a0f22a72b9c7094e87a696cf0f06e776b868f3614e26471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0abe49a516e7ac1c7729aee00ed4e99e9a29f18ff1c57020109af4698023b8f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473f5d8dd74f16cd81cc762b243a2a0a6b5d5f3491a129b5562346ba961d6d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7113e3274955b6315cff53d7a5d82e742fb9da5c00696ed0842071f1976739af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WindowsWebAppSlot",
    "WindowsWebAppSlotAuthSettings",
    "WindowsWebAppSlotAuthSettingsActiveDirectory",
    "WindowsWebAppSlotAuthSettingsActiveDirectoryOutputReference",
    "WindowsWebAppSlotAuthSettingsFacebook",
    "WindowsWebAppSlotAuthSettingsFacebookOutputReference",
    "WindowsWebAppSlotAuthSettingsGithub",
    "WindowsWebAppSlotAuthSettingsGithubOutputReference",
    "WindowsWebAppSlotAuthSettingsGoogle",
    "WindowsWebAppSlotAuthSettingsGoogleOutputReference",
    "WindowsWebAppSlotAuthSettingsMicrosoft",
    "WindowsWebAppSlotAuthSettingsMicrosoftOutputReference",
    "WindowsWebAppSlotAuthSettingsOutputReference",
    "WindowsWebAppSlotAuthSettingsTwitter",
    "WindowsWebAppSlotAuthSettingsTwitterOutputReference",
    "WindowsWebAppSlotAuthSettingsV2",
    "WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2",
    "WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2AppleV2",
    "WindowsWebAppSlotAuthSettingsV2AppleV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2",
    "WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2CustomOidcV2",
    "WindowsWebAppSlotAuthSettingsV2CustomOidcV2List",
    "WindowsWebAppSlotAuthSettingsV2CustomOidcV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2FacebookV2",
    "WindowsWebAppSlotAuthSettingsV2FacebookV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2GithubV2",
    "WindowsWebAppSlotAuthSettingsV2GithubV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2GoogleV2",
    "WindowsWebAppSlotAuthSettingsV2GoogleV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2Login",
    "WindowsWebAppSlotAuthSettingsV2LoginOutputReference",
    "WindowsWebAppSlotAuthSettingsV2MicrosoftV2",
    "WindowsWebAppSlotAuthSettingsV2MicrosoftV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2OutputReference",
    "WindowsWebAppSlotAuthSettingsV2TwitterV2",
    "WindowsWebAppSlotAuthSettingsV2TwitterV2OutputReference",
    "WindowsWebAppSlotBackup",
    "WindowsWebAppSlotBackupOutputReference",
    "WindowsWebAppSlotBackupSchedule",
    "WindowsWebAppSlotBackupScheduleOutputReference",
    "WindowsWebAppSlotConfig",
    "WindowsWebAppSlotConnectionString",
    "WindowsWebAppSlotConnectionStringList",
    "WindowsWebAppSlotConnectionStringOutputReference",
    "WindowsWebAppSlotIdentity",
    "WindowsWebAppSlotIdentityOutputReference",
    "WindowsWebAppSlotLogs",
    "WindowsWebAppSlotLogsApplicationLogs",
    "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage",
    "WindowsWebAppSlotLogsApplicationLogsAzureBlobStorageOutputReference",
    "WindowsWebAppSlotLogsApplicationLogsOutputReference",
    "WindowsWebAppSlotLogsHttpLogs",
    "WindowsWebAppSlotLogsHttpLogsAzureBlobStorage",
    "WindowsWebAppSlotLogsHttpLogsAzureBlobStorageOutputReference",
    "WindowsWebAppSlotLogsHttpLogsFileSystem",
    "WindowsWebAppSlotLogsHttpLogsFileSystemOutputReference",
    "WindowsWebAppSlotLogsHttpLogsOutputReference",
    "WindowsWebAppSlotLogsOutputReference",
    "WindowsWebAppSlotSiteConfig",
    "WindowsWebAppSlotSiteConfigApplicationStack",
    "WindowsWebAppSlotSiteConfigApplicationStackOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSetting",
    "WindowsWebAppSlotSiteConfigAutoHealSettingAction",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomActionOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingActionOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTrigger",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequestsOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequestOutputReference",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeList",
    "WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCodeOutputReference",
    "WindowsWebAppSlotSiteConfigCors",
    "WindowsWebAppSlotSiteConfigCorsOutputReference",
    "WindowsWebAppSlotSiteConfigIpRestriction",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeaders",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeadersList",
    "WindowsWebAppSlotSiteConfigIpRestrictionHeadersOutputReference",
    "WindowsWebAppSlotSiteConfigIpRestrictionList",
    "WindowsWebAppSlotSiteConfigIpRestrictionOutputReference",
    "WindowsWebAppSlotSiteConfigOutputReference",
    "WindowsWebAppSlotSiteConfigScmIpRestriction",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersList",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionHeadersOutputReference",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionList",
    "WindowsWebAppSlotSiteConfigScmIpRestrictionOutputReference",
    "WindowsWebAppSlotSiteConfigVirtualApplication",
    "WindowsWebAppSlotSiteConfigVirtualApplicationList",
    "WindowsWebAppSlotSiteConfigVirtualApplicationOutputReference",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryList",
    "WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectoryOutputReference",
    "WindowsWebAppSlotSiteCredential",
    "WindowsWebAppSlotSiteCredentialList",
    "WindowsWebAppSlotSiteCredentialOutputReference",
    "WindowsWebAppSlotStorageAccount",
    "WindowsWebAppSlotStorageAccountList",
    "WindowsWebAppSlotStorageAccountOutputReference",
    "WindowsWebAppSlotTimeouts",
    "WindowsWebAppSlotTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__f6ddd99522bfde6c5bc60be25b59ee4010853a70b7bb83e5d9bbb79a54001d42(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    app_service_id: builtins.str,
    name: builtins.str,
    site_config: typing.Union[WindowsWebAppSlotSiteConfig, typing.Dict[builtins.str, typing.Any]],
    app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    auth_settings: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_settings_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2, typing.Dict[builtins.str, typing.Any]]] = None,
    backup: typing.Optional[typing.Union[WindowsWebAppSlotBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_certificate_exclusion_paths: typing.Optional[builtins.str] = None,
    client_certificate_mode: typing.Optional[builtins.str] = None,
    connection_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotConnectionString, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    https_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[WindowsWebAppSlotIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
    logs: typing.Optional[typing.Union[WindowsWebAppSlotLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    service_plan_id: typing.Optional[builtins.str] = None,
    storage_account: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotStorageAccount, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    zip_deploy_file: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4eed8de5e1f235bbe89a43eaf4c70ba4cc7a8e366c1718580459a49078a2a25(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotConnectionString, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08bdec799d80ac734028040beb76e6a2bed953d161f5945628cca2e0dd75a5c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotStorageAccount, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a029239dc53304a99ba881342b6dfc3fbca9ca02af1e57469ae33d96fd5023(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94ad378f16bac67ab6bf9605ded3dda132aeb4f2f33762e23428a778317778c4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0ec27cfc15cfc90031ce83eda8c427714b35c7abb51f84a08f9948b780ff1c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e24ec14a5703c54e3a7e4425e258d1245fd3fed982ab84944d217b366683e8a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf28c0023e4468181f0a42e5e56fbae3f2bfc34dd64f88ea4cad7d5713c4206(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf2cf019814029ad51efe32299138233b9bd59e0df2548216ecac6aef02115ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79aad3add9fb3d9d4e213ea7abe359455bda185b23005937e7cc3c3a8350ff2c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa499da99b7c6df7e783ec1eac60314ad45be717f44423f0a748c30326468932(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11826114989e5ff2c8e1caefab935d70243bfccfcc6ac0d37b86bc5cf2f7df70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2ef5fada5887ed6b4306c81d2ace3ee5d01c6961333f1edf220d9c9d902ac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b443a4f2710131e2ef520657a4d853230612b40cbb9a7c85a942d0463311d467(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359f08939091be0ba2c15eac57a97f979cdb4c0bf1e176f29ca1ad95a61b5f8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e6b5c63b8c681792bb85075853c8e3bacf98659a58c9a8f041923eb3acb09f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b793dea2ea9f15d2199130fdea7188a76ebd330e3693673aa473b61b5ad26c0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a3cee88ef2c0f7903d6124de73c7132ff600b5c0fefb28352007a15bcf4d25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3707bd7e3fca64e5e38479177f06ea1beead785566d51b0106177ac84c1946(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    active_directory: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsActiveDirectory, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_provider: typing.Optional[builtins.str] = None,
    facebook: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsFacebook, typing.Dict[builtins.str, typing.Any]]] = None,
    github: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsGithub, typing.Dict[builtins.str, typing.Any]]] = None,
    google: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsGoogle, typing.Dict[builtins.str, typing.Any]]] = None,
    issuer: typing.Optional[builtins.str] = None,
    microsoft: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsMicrosoft, typing.Dict[builtins.str, typing.Any]]] = None,
    runtime_version: typing.Optional[builtins.str] = None,
    token_refresh_extension_hours: typing.Optional[jsii.Number] = None,
    token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    twitter: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsTwitter, typing.Dict[builtins.str, typing.Any]]] = None,
    unauthenticated_client_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868bcbff896a41ff3890f6b0d0601b2f1a303fb12bc3e577e43d2d849d9daf86(
    *,
    client_id: builtins.str,
    allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_secret: typing.Optional[builtins.str] = None,
    client_secret_setting_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed289310ecff6c955de81db5153b619f7caa14d4f75fb4098eba7fc547b3e451(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2ce9c0bbccece442b7a83e96eeef0d61d5a23182f21bd748b2878bd4135229(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43b29d40be4746b425c09e0d4bf0dfc26f4b95b119632005ff873581a85d490(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e62a1ac05668fa288a2c1b72a1be047eb4175210533602acf5af53b58f1653(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189f910e3b91b348ac33b19d7a80645a20ccfd7ee33f34d645960d370c876e20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9898f499a466a1c3b0c31ec6d099f3595e2727fb6f583ee9bbcd5b9ff6ea996c(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsActiveDirectory],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca9f25873d1e129b0ae705e1dce0ff35833907fb6fe72fe5567e5daea47b0ee(
    *,
    app_id: builtins.str,
    app_secret: typing.Optional[builtins.str] = None,
    app_secret_setting_name: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e9add771a8a85989b1aeed94b740a3f6342ed4eb48a5b19255bc293b54fc95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f955dc7abfd911398f0ba03d070fabdb282ae521987bd57ad94585019aeb999f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__342c2ce6f2e2f28abdf8fff1781671e757400f423851a112cabd5924444dbb10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f5689e7a343f2bf6bcb2c1a579308869ed54345f72d962ce89bc95a2a38106(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53358f627d3237750f6c6543c7309d497060bc0498e21351987b4efc4478effa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd16bb15c55c7d93a42e8337589a8c62239d35949574ea9dafb711453f96e6c0(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsFacebook],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08b71235b42267cc6710c8859abb40328e4aefd175d880b63548b0a35402eb1(
    *,
    client_id: builtins.str,
    client_secret: typing.Optional[builtins.str] = None,
    client_secret_setting_name: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958385d0779e84ef976cc8f93ef614e046da13040cd3213a4d801489a62e9ebb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fbe5ff91489ac2f9a5ea9a9d012f8a963bd1a730c3dac489ab60a86377b1ce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95da73fc61f3e60daa462919be59d2d1e1aca04d1a961d90b89d14b009217cda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eace5adb99fb1e404287ba5710925293c8c234ce25581515028133812fa58f95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3c2c9b1eb55b3b37731dfe29fcb8e94d1383024318489fa5294e7a651cade1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7c46688222b0d5eddf4f3f4429f5d6c28d92ca87b2177aa9adc725ec6bfcd6(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsGithub],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fc9456e5a2b99d9c9d5fa404d92dc48d3a36b1907f11626586d013d237fe11(
    *,
    client_id: builtins.str,
    client_secret: typing.Optional[builtins.str] = None,
    client_secret_setting_name: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed29c3a27bddbc446426ecb6d7dca0df18515e01370f96d03feba8b4c8cf7b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda8a5ccef6453e903afbc63eee6965db1805bf60874a470a9313063b22f0531(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8dabeae006496ca4deb7d5dbc56a381201a14488e980d5d73016559b77992f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f77e0f15bebc554d3feda2ae8cd56b81d556d9b51c70af883a8d8bff63d1dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7de0137cdeeeb6751f9acd8454c3d47824abf70102402ae2f2df339bdaa6d033(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca92677b504b665e9d813011fba7af2fb92d671f5e6a7164f090a01f001604f(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsGoogle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7642d3c6eb8db232d8f86a85763b579dd7bc58cb0f5c5c7065696673e9c569(
    *,
    client_id: builtins.str,
    client_secret: typing.Optional[builtins.str] = None,
    client_secret_setting_name: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c356a1dd04e2858ce3c979247edadd6b8002277976fad1313767d7350718bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8898984aaa845b60b7c4728d9cc1e29e1f02674bdeb277a34e4edd5fe1b75f6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822673928abaf834d2bd34c53e947a4ede76f9bb62107aafa9f6e8af30e2ca2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__039ac8b50caad86d2c52b9338304deb24f7a91eec29aa0a282d8451f19cf08d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007ca8cb3ccde7773ba5cc3799e8a5101e06ced17d262e3c012a17f5bc90f257(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83fc4c8c5e645b9dcd9d60680dd8d41ea6e68b3ecceb6520acabe9d51c249eb7(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsMicrosoft],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b15be9e2db1b6e4c7275431eb30d674c0b3ad1ad2c4df36bfa0bbfd84f95ba3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17e6c60d7cd7bd61917f2f9a03292633e71c71a21e2707e10798ff239173a73e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a3b3bc2742c2114b7846df8935b2867674c2ee56dece631917934aa77cd7c26(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d2faf3b4ce6c3a3631ad0a3fbe6a121b8a3d2c4444bf0e422b263f8578564f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c632f4491f14332a3ec9f7656f325054396f3dd0ed85813acd5aff43ab7f05b3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164a5b65e87a8ea7aebe06d5ec2611aa41cb6a89815a62be0c84d03f7c21bb75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6986d8782f275cf905124ef5943def4166c5134fce85069fef61e31332f2274e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e442b2395a1e63d79c38d2ef81398cfeec43c26b47483551767d9108fe5a4618(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5e1ee24229cf65dfd2a19f5aee313dd64ef8d02aebd9c456653ce5f59dbacc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9728715065674c928b89ba81ab3faf282edfa242f3c5964dcdf8b53fb46e3c3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d868d9f7f0d39984400f12321681721d7ca7e72e5c6f843488650a657360f16(
    value: typing.Optional[WindowsWebAppSlotAuthSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4ef8866204511f52f39cf00216c2ace2b0650f706d141e2645eb12c732a44e(
    *,
    consumer_key: builtins.str,
    consumer_secret: typing.Optional[builtins.str] = None,
    consumer_secret_setting_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0954efc04d8af6ef74d8b6836c5ad6440d09fd5b78aaffce0c06f9f6b6236c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fce152f2a983733ec38726861f15e82715e96c614fc2464e1ae43b46cf5f948(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff0b199e9c7dffb97b9c3fc6c38ec83d6ce072caa04a89a8df8e9cfca6242835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa7d701758c8c079963482f6d359860283486bce84788f4976fec6b38d7f36f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a049663d59c01556f8cffb1f2a84ccc2bb3ae5e2ee253bb509e75213d41da2eb(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsTwitter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e8a09f2123e8647e82ec4f6e0b012ee1e4d024999873b2d62140e78a2fe00d(
    *,
    login: typing.Union[WindowsWebAppSlotAuthSettingsV2Login, typing.Dict[builtins.str, typing.Any]],
    active_directory_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2, typing.Dict[builtins.str, typing.Any]]] = None,
    apple_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2AppleV2, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    azure_static_web_app_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2, typing.Dict[builtins.str, typing.Any]]] = None,
    config_file_path: typing.Optional[builtins.str] = None,
    custom_oidc_v2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_provider: typing.Optional[builtins.str] = None,
    excluded_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    facebook_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2FacebookV2, typing.Dict[builtins.str, typing.Any]]] = None,
    forward_proxy_convention: typing.Optional[builtins.str] = None,
    forward_proxy_custom_host_header_name: typing.Optional[builtins.str] = None,
    forward_proxy_custom_scheme_header_name: typing.Optional[builtins.str] = None,
    github_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2GithubV2, typing.Dict[builtins.str, typing.Any]]] = None,
    google_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2GoogleV2, typing.Dict[builtins.str, typing.Any]]] = None,
    http_route_api_prefix: typing.Optional[builtins.str] = None,
    microsoft_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2MicrosoftV2, typing.Dict[builtins.str, typing.Any]]] = None,
    require_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    runtime_version: typing.Optional[builtins.str] = None,
    twitter_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2TwitterV2, typing.Dict[builtins.str, typing.Any]]] = None,
    unauthenticated_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f9f7a6815cb1b45d489e3bb8ca0dc6c07276bf2fc742c168233d2fccaad84d3(
    *,
    client_id: builtins.str,
    tenant_auth_endpoint: builtins.str,
    allowed_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_secret_certificate_thumbprint: typing.Optional[builtins.str] = None,
    client_secret_setting_name: typing.Optional[builtins.str] = None,
    jwt_allowed_client_applications: typing.Optional[typing.Sequence[builtins.str]] = None,
    jwt_allowed_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    login_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    www_authentication_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1556cba47f961b57421b7e526f6d60662821cd5bf44505a61fd44fe41e8d3c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74d3bd055d37baceb955b29dc65f9258235d685c2214bd92707449eda7ea7e5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f23254bb6c9986ecd343adadb1c5558d47e01ebc9c3c928df25be4a151be02(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb49e3c2f62e4f02a4fa3dea9b1ec93106fcd5ae1fc6223cad418a7284c35d33(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__609f73dae80aabb7caab2f7c83ede01cdd2d26a34e77ab59906b9ec608cadaf0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96400477d50776117db2057e7ed727da79519d145f8f7fdbb5c893e094ddfdce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f27a7ce68c5a257d9f6b8df97435ef34a97700a466f10ec560965c9552c502(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16cf01d1192bb12f5b486306bd68b771514e0ff3e0df0f401adbc97e49b7ccad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648d650fce3295bc1a6b84a5b5052c4bbcd0f0ee885c673c0360ba1203d3d4c6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd7ed5f106fffa50d29b3951d3995d7fd7388ea4376d63904777911327064342(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27822f172a4bb33d8d802400d9b8782b2646573d9b1873ce5069fcb962373ccc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3315d791dee383f93c68f0ff3d94c6c6e25a32edbee6370a65c6c412cb69cbff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c1ee7c035919f16217b723cffd7607d6826836821e603f13fdaa0731b60cbb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc8416685b4bab62699ea8d02c27968b8156b56a736d35b9c8a09701c813eca(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2ActiveDirectoryV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1554237578e1cf1d1379e5ca212b816dce611ada09983328f819c2b0a540c74(
    *,
    client_id: builtins.str,
    client_secret_setting_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3557a05cb0419c0fa89408e0c1ae17b046794a93936b84f5f13e9c6e70e0bc79(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f767acb1039b5d5ffa950650261b4fb778bd1fe2c9d8fbe8d74f34fc37712fd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e540aecd7032280628d5082bba112bb6e1baa82fdff281c343317b84de4cecd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b01dd51be2ddd751e2d5bd39cc94a81808f17f4f4535e581a9c81e390e037ef(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2AppleV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d85945d65fac243ea635cee683c472398569537618fdd2c1ab133daabe20da(
    *,
    client_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072c0cfed72d0ea8d5cb3a71f699a5a0643da7baee1b0846460c365c21ece9ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd9cb3493147605ccc9f30005a5b8c02e1f2dc77160ac229b82941973428a31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d538708f033774c14b558f450a219623e6c44bdfbd3d5e6a4cf62dbea2d90ed(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2AzureStaticWebAppV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bbe18c12566a75723bfd946074bb46e7a18afe8e7b8a64d7d857f3c8b9d8832(
    *,
    client_id: builtins.str,
    name: builtins.str,
    openid_configuration_endpoint: builtins.str,
    name_claim_type: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff206d7cd860b94ecbbc2141e4cd47c7d042e0aad841dfdcea598d29a596c891(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b11dca0380b39bbea0dc46c98fdcd4fec1931f8e5272574df89f8e59656454(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55f23be1373ab362fd71b3bc75e6abea99d09bed52578811aabe2f6e8dcd0c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899bed833414dfa767e7d3e1d9ed1e9b68553810a1a7b7d6828ee54bcfc4fbc7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c5dce477f1c78cd1ffdc583f03917f722cb131472e3baf7d2d7d8d1d213841(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc3a34919c53f53af3c879f7e97c78d76f861c47654c994898282d991750a62(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotAuthSettingsV2CustomOidcV2]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb68115b8d04972acca01b743b56ba82db5e86219862038f8532586f2944a73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91aa3f316da337a14d411235c6ca85d7659957c787d427d52051f10e9c3586a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c237a8bd4760390a9563cda5de9400ab121902e5ec908c53539460bed64e5be9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832cee9a4c9bb5ec5a0a6dd8554236d22a2858910897739bfd8ed5077447abf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e3e9cecfb5b6a579b0659006cbb05e28afd0d116d1d9d69458d01224dc024f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c0ae64130264e7433da8ff21fa01181bfab2495fff062a84a44f99f593c382(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c30d8db8d789fc767d4d7ad62a83092c8b162e78091973e0649140066df6095(
    value: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225e39c41b6f3cf019296c60524ccdfb8701001b27c00b916fc96a8812d14cc2(
    *,
    app_id: builtins.str,
    app_secret_setting_name: builtins.str,
    graph_api_version: typing.Optional[builtins.str] = None,
    login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26a63613bc24845698f7ed2734f617a96f45b09d859170759cbc4e216a7bf806(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6826eb97e195eb1084225f23167363de78e123e529f87e12459eeddf64120d57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904a6e84cc1dc09fe5d1d42ed4d84b2da6bd415298ebfb2d3a599530b039ec63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db47302076551b931193454e06c210d8af98048004594fc4bff9d545a811498(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ab645da0a3d2cad080f85959e59971667bcaedf124a87019da17725edfc114(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a3c42ebbfeda4169fdbee33f90b4ab8b044f28246ca56c5ffa879ca04b04d1(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2FacebookV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b734b01ed37534954fe022a65732f9e7d054ca6a159d91f383e646a5869758(
    *,
    client_id: builtins.str,
    client_secret_setting_name: builtins.str,
    login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ca89e23f5742b2e38126cb11f0dd848ea2628a82bd3f91d11e71dfd868f240(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538f2effcc0138034b9930812f48ef6727f489bd9df393c7023278e2bffa8f67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e9f7bc95fbf2d1818a75a24cd889195e715b5d993f85ca5903e5483fc2be15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdde59b2b18866164fee00a157a8e3d8f9dd513c6c4112bafa31df5ccb154662(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8001d9030cc987a7e44a3e8242af649fe61a0a45ac278d93eebe5339d83f458(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2GithubV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c76f816facfb937c9bb85a9795333d2d4551814ee6acc94df7f5246f7d0c591(
    *,
    client_id: builtins.str,
    client_secret_setting_name: builtins.str,
    allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61115394e33d80e6acb7cfe5cc134958422229878df51a022e1fbfbe3b40f8ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798eba42177ce830e6cbc402fde2393d9e62518615add3535dbe73afce679d4b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17fc6ebcf2736d53fb374dfef150512b0c1b5a75092a605f87ef0ddaa3885d92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1f8c60530177081ecb0bf18fa1d8ee0fb244e5ecf7436161aa0cb99dea65375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__829e4b401385be1c0af4b14998d70d2c3c53427c14a14b49de4dca8da96e4b62(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a9d47927c87c3a5a5ca692c789581cc214692c199e66d264972b4a40a7d1c1(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2GoogleV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1819e90a271fb232c22bdf76d4255c6bd0def46d79aa83c37774d6ad2a85732(
    *,
    allowed_external_redirect_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    cookie_expiration_convention: typing.Optional[builtins.str] = None,
    cookie_expiration_time: typing.Optional[builtins.str] = None,
    logout_endpoint: typing.Optional[builtins.str] = None,
    nonce_expiration_time: typing.Optional[builtins.str] = None,
    preserve_url_fragments_for_logins: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token_refresh_extension_time: typing.Optional[jsii.Number] = None,
    token_store_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token_store_path: typing.Optional[builtins.str] = None,
    token_store_sas_setting_name: typing.Optional[builtins.str] = None,
    validate_nonce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac56f5a2de09b1232fb36885229f7870f78a420471fc102a6abf5371378ef83(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4417ca3890410aa61b36c04c22fa6208003cd0cd3830a9a4d77c277a2a0a9a2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7132540967c78955b1bdb69a2c0f1fb829eb4f14e557eba4de828687ade5daf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3242000455594468b865842becff74609684d42513968328814a9491f60cdd5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597195d049837207b77b086078071ea0902c000da472c1454b0dd22b1c68a6c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41dea7f8495ee80f8799d61d7804b717d25ca68b1e4b248fbd2cab180b069e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e93d6d97e3117402570835b85649700103898b2d340f3a94122453ea5340f22(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798f6295f6936a28db9348babad6509f7b5ba2a4062b8f29eb20e426490cfd77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6387f0a8119ff13c61f8762fe71e0b478c4d73a8be504502c2b833de007bb1bf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5550012f41d85cf2cf82a1e9cec9d5e6bfdbc39dd4e1fb13f5d49e9bb058de90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3792801f29804c559647a7f34ad43f98493925aecf8b995d34f62423f27f8218(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbda8461b86a72e5eeed1ee5293b74b2bcc54e673472c5fbf26d7f67d44ce822(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3cd0f99218a1048aa86cf8ecff6c0b45a6c0ad8b30666ff20ba63e34ac0467(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2Login],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c179e2c7556f4f4da602f302da863d88cfc03be106d09de52f7846bffac2cbc6(
    *,
    client_id: builtins.str,
    client_secret_setting_name: builtins.str,
    allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    login_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fbd1410ce18da70808126e4fce9cc08519906c2a7d9c0c116ab1e100047676(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0470457fec5a51ed43ab42684e78b84ef05d62c6b02eb4ec039a4d48f085c2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d575bc5708facb77b3e21b5a1345f6f76de549ee7ca6d862e7a2b09ff3a3b214(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d97e3185e0d3a4d6ebf2e62d31f2a267a82fcc2ea7e4aada9a99fc90ceb098(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577bf794417bc7565df1c8e1b5821fbafea82c69cd13c8d970e2f8e71cfe9891(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ff7a8816d525ea5020d064c66e380bbf03490982f5ee132eb5be14a7eca850(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2MicrosoftV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__108df4830944e5a59d1c700cea5488c987b329842062f7bd35ea589d8593b23d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16cee008df7359c5e0c31710232f3c1f9da5df646113a1c9c0a05403139d16dc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotAuthSettingsV2CustomOidcV2, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94bf4e8b695c9665651522d7028e7467606e02b82a10c8e65361c5ca096adfa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__919c4d6142e2ae4752781e4e929a0b7e44548db4f1e0bfd86a9ed4d3661c94c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22b47b7de01d808ec711896c72063b50d476c29806096624f9c24417854aed5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cd7ea40fdab5e47e28db2020aea6e21132f862be37325842d746acb1ccd520(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b08014f045ef783297219e85a0689c2a8415c2854c08927f3bbfba377827250(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f389b518fc5950e3b3f35f51c0b0f6502d3810b387ba67ea659894ed0c5c2cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23983a2135f48ae128f21e5338e46853c938e12df6f9351c1aa072d2ab383d41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566db5470b19c94dd253fae250b230902b5b7b9a7a9791bd566d50d73e84ae7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb84980945373e7167e11081f04afe31ddb8542200ab145b091e7be630b878a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be55bad382b0f6e999a38a695a63c4a80c6887545f90d12e31b58a5821e75fe8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba220dc112c26b7db193bdd32c3f2b20aee9b003b0e345c78bc932ae79d891d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b510f50cca74ec9fe0627289957b8e577fdf233af74c06f5b90903a6c287447(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb60e6b486fec3d5cbedec2f1f87e16da4792205dd87e2272a104331f14ccc20(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e57466984bde9e623e489d52c57a3e2ebc3a3ba3ca789f42beb70dd36544b03(
    *,
    consumer_key: builtins.str,
    consumer_secret_setting_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6d538338d4f6e176ecc1d27489d3899a89fb569368e767c957ba782f7f8536(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d788f1f641acca0eaf1afdeadd34c6a3647ecca1680144ac593d20b6d9e903be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e8f92a5cad66e47a6a5cc4880a9855cf74fd532bd27ea4823cb5e2dd6e32c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1baf9bbe9df74d3d84e11d07dc11816abcebd7e04d85cf5b3c67da07ff04f678(
    value: typing.Optional[WindowsWebAppSlotAuthSettingsV2TwitterV2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325a76a23950dbd0dc1baabfff7db683f6b40882ea11bb14885e314e90801bcd(
    *,
    name: builtins.str,
    schedule: typing.Union[WindowsWebAppSlotBackupSchedule, typing.Dict[builtins.str, typing.Any]],
    storage_account_url: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ebe259c0bb63b8bf63f04aa124993db9f429c8523536886aa8260508434654(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__319d30e342b04a23ea3421984febb6d13d50d41ac2aa5aef50dd13c5306cf1d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322c9555caacd6cdd1a53b46894e1690014f95798ce3b7b2c04ed8a718daae22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94db0bcced776ee7264d94653598037fa9472349e8ebf34493851ee67763513f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7686083c37047d402f5cd42574de7ad73f2d886a5543bba49686eba9d7bad53e(
    value: typing.Optional[WindowsWebAppSlotBackup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b188522e4f8c4dd100af3011ff6f5b6301336943e80a86cb3ececfed7b37101(
    *,
    frequency_interval: jsii.Number,
    frequency_unit: builtins.str,
    keep_at_least_one_backup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    retention_period_days: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffe9f21713c445eec94054e4a73a3477d3ae144c072ef3ad1bbf043e2826b99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a12d761012a8750c9708faff859087b325352031af8d73194d3574457b1fa2f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabaf67073fb453f4d8888b5102851a341caad19cc189023b3556f487b57811a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d947c05d625fff5351be77278b998b0935b150138178323c5d417e072835c21(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903c26d6e79cd5f303352fa21e0a1c10883066b39f391a844d2eccea2ec7dabd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55bd2ab4594514ce63b23c3490688480126463dd013c8b5508e9cfd192d5f59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5cb9df534023f4f3ab9e62763c6e047a0d0f409c8de9779a5cf4d2ff8360dc(
    value: typing.Optional[WindowsWebAppSlotBackupSchedule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f00c7455d1f916580d990d3c32b78551ea4dd93db7dd917a7ea0c18d245a04f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    app_service_id: builtins.str,
    name: builtins.str,
    site_config: typing.Union[WindowsWebAppSlotSiteConfig, typing.Dict[builtins.str, typing.Any]],
    app_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    auth_settings: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_settings_v2: typing.Optional[typing.Union[WindowsWebAppSlotAuthSettingsV2, typing.Dict[builtins.str, typing.Any]]] = None,
    backup: typing.Optional[typing.Union[WindowsWebAppSlotBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    client_affinity_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    client_certificate_exclusion_paths: typing.Optional[builtins.str] = None,
    client_certificate_mode: typing.Optional[builtins.str] = None,
    connection_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotConnectionString, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    https_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[WindowsWebAppSlotIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    key_vault_reference_identity_id: typing.Optional[builtins.str] = None,
    logs: typing.Optional[typing.Union[WindowsWebAppSlotLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    service_plan_id: typing.Optional[builtins.str] = None,
    storage_account: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotStorageAccount, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_network_subnet_id: typing.Optional[builtins.str] = None,
    zip_deploy_file: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81d070fd168e172b4c5e8e70cfb0d0d518b2ae40ac4e24a5203c78d3aedd84d(
    *,
    name: builtins.str,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f1c378537402dac7f354bf2f6f72a1bca86cb8985022de6453fa9ead3144cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f1ba5ed8576d337a19eac8a7279514cfa597289f7ef9ce97d0b7ddf8e8f1fe(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e3908a44050bc93c41a1c157c2f4629bc01933f74a1cd58d2f7801e82ca89d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9075ec90d5fac55373d40cea64cbf16d2f3327f2465bfcb1e5b77343e56d5fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28820b4091885358bc1f94e371a8c65074356ecaff9f98a6f6ffa52158af883b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2352451bf82e759be0ef7717d7c0ec959384ebdbda5fd2eb9adaf1d5b304e04(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotConnectionString]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d882142854f1e1f89250c9ddaa0bd2d190772d1e93c073140c8a544c91db2ed7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77b4a5a66c3b4f8627079330330e2a374a8f42a2d6c8311afa2c6fc11571bab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b70e1c89081a3d10d07e032aa9663a742324b603cd9c12d3e1d3e319e1d58c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18761c951867791d2a3653019d77a5887054c0fb71395b5f3961f3bec483abd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72946380f21e05c00a4e7a13cc2299be6429fda2eb2ac884243581a5fc78923(
    value: typing.Optional[typing.Union[WindowsWebAppSlotConnectionString, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd042ffcf3b7dd2b6d0807e318e903fcbcbd02bd1c1df40a7c10a900e74b184(
    *,
    type: builtins.str,
    identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0c3cc6cbffcbcb1a38b8cc1eda88158905133c26a52ac55eec227f6d0d7f9b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7606988b609efc5fcad169ccf4a27ab34d6053ab56ea50a8c904ba07bf606d7d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46efe12ef543220fef983c21bd95e38498c6e1dca1d636d5ba42e79ba579c4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6e8d2a885bb90c084be77880325eb4bea0782c07533402bc4858ab210495b5(
    value: typing.Optional[WindowsWebAppSlotIdentity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb38c5a849a0aaf33670febe7b15671fbb6c9fd2e503e5b2aa9e92a2f6fb469a(
    *,
    application_logs: typing.Optional[typing.Union[WindowsWebAppSlotLogsApplicationLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    detailed_error_messages: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    failed_request_tracing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    http_logs: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogs, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb166d746aed3e596653aaf2dfaacdcf1e7056ec24eea008574fed5055d45d9(
    *,
    file_system_level: builtins.str,
    azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c92e548d5dbe7dcce51f828cce7327f1c8250ba7dbc24dfbb3f66b17ecee81(
    *,
    level: builtins.str,
    retention_in_days: jsii.Number,
    sas_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5f476c4c701378c5fa01f5498e6e7d99963c496496debb1e993155a75fd2bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ebfb9fae02da85338e9d40d6964c9e7572e03b7aa4b4001d7df445ce0f14e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffbc7e8723c4042a2012b58a53206570943bfbcb1997c4502a065416d007783(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369cff1c7c20d3edd70c34645f2780dd1963ef9ca0c0f3c712165f793d7059e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a4a1b3a0dc36b99ed6ccae2116f7ebae978457155dc5d58b079506206bfafd(
    value: typing.Optional[WindowsWebAppSlotLogsApplicationLogsAzureBlobStorage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6498b9985e3e1d001a0c8bef946fafc906c72218d5f42cab8e90689bcba9ed1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb60dfc52768ba00f259a2f3ab45abbe658c987ac4a6b946f881fd788a95af98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e50c4a8825ca89149f119c3962b9d302c3a4d9d0782305a92387cb84fbc0846(
    value: typing.Optional[WindowsWebAppSlotLogsApplicationLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ad82175360c2bb1633ac60b8975b96f42b18b78421a984b7e693af1842673f(
    *,
    azure_blob_storage: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    file_system: typing.Optional[typing.Union[WindowsWebAppSlotLogsHttpLogsFileSystem, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60553a01ae9ffb15032ca862ecbd9d515d16239f1fc029db1d96b10fb208da41(
    *,
    sas_url: builtins.str,
    retention_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9fe385817586befb393afdbfd1c37cdaccb075c3b2bdf9dc0b013d01fb479e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124881726eeb404123f7c33232a091a284253fbafcf48519199cd10e9e542774(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b13fbc4c2352b53e2288ea6e258cd8bef6c4f81b67e1182755fbe568c8bf517(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748ac0e8c265ef40b41e6df0ec121b14bf9bf44bbb943d71c6122678ad2ccec1(
    value: typing.Optional[WindowsWebAppSlotLogsHttpLogsAzureBlobStorage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7416ce2b5e04b634ccaa5a96102d0f1d68ff38e8c73fe64002e2b9ad26266e0(
    *,
    retention_in_days: jsii.Number,
    retention_in_mb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cb51d778aff2c213054d58db3cd1260af678c7d3b339d8d2ad84b01d104006(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2198abda390c8e69bb00cc3ca3d3f341d887ae57ce52809ee0479ac9d1ca97(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0b2bc1e28ec100f90ccb99b8ffe049f69136468041af77e79ff2f321bf58bbb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7426e36d42a2f67397e158bb5f93f229c305f5b0e5d430b4236a1facc71610b6(
    value: typing.Optional[WindowsWebAppSlotLogsHttpLogsFileSystem],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0641ddaa2163cee2e57f46d09f20e13ff10d0f36ba9e5343019da7de58012296(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8327a6ebd6a9e00e616d0d0a450b25d17a434715e9225b7b393dc5173db7a0(
    value: typing.Optional[WindowsWebAppSlotLogsHttpLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768ae7d079759a43664acc204b754598890185a459e0c333c904c821f07bc41c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b6a96e5d0bb5a72f5922d541e76801d479e22da444d6722a4e68b3eeb0b7f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45144d45d95c3670e9abfac2ae6a9e567db0d2ff23c27dee7a00c9c3b4b349ec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d901e876f63fc569df892545eb89674cc3c5363db3dca268f9634b8093112425(
    value: typing.Optional[WindowsWebAppSlotLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2cdd7804c528b844b4ebb2ba42ecd15551b389cd3ea8f6a4d69012ad8c244f(
    *,
    always_on: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    api_definition_url: typing.Optional[builtins.str] = None,
    api_management_api_id: typing.Optional[builtins.str] = None,
    app_command_line: typing.Optional[builtins.str] = None,
    application_stack: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigApplicationStack, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_heal_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_heal_setting: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSetting, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_swap_slot_name: typing.Optional[builtins.str] = None,
    container_registry_managed_identity_client_id: typing.Optional[builtins.str] = None,
    container_registry_use_managed_identity: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cors: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigCors, typing.Dict[builtins.str, typing.Any]]] = None,
    default_documents: typing.Optional[typing.Sequence[builtins.str]] = None,
    ftps_state: typing.Optional[builtins.str] = None,
    health_check_eviction_time_in_min: typing.Optional[jsii.Number] = None,
    health_check_path: typing.Optional[builtins.str] = None,
    http2_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, typing.Dict[builtins.str, typing.Any]]]]] = None,
    load_balancing_mode: typing.Optional[builtins.str] = None,
    local_mysql_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    managed_pipeline_mode: typing.Optional[builtins.str] = None,
    minimum_tls_version: typing.Optional[builtins.str] = None,
    remote_debugging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    remote_debugging_version: typing.Optional[builtins.str] = None,
    scm_ip_restriction: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, typing.Dict[builtins.str, typing.Any]]]]] = None,
    scm_minimum_tls_version: typing.Optional[builtins.str] = None,
    scm_use_main_ip_restriction: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    use32_bit_worker: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    virtual_application: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vnet_route_all_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    websockets_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    worker_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c1b0db59ad18c5da48d45af84137e7af6195ac053e5f09b77e2807499f7d65(
    *,
    current_stack: typing.Optional[builtins.str] = None,
    docker_container_name: typing.Optional[builtins.str] = None,
    docker_container_registry: typing.Optional[builtins.str] = None,
    docker_container_tag: typing.Optional[builtins.str] = None,
    dotnet_core_version: typing.Optional[builtins.str] = None,
    dotnet_version: typing.Optional[builtins.str] = None,
    java_container: typing.Optional[builtins.str] = None,
    java_container_version: typing.Optional[builtins.str] = None,
    java_embedded_server_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    java_version: typing.Optional[builtins.str] = None,
    node_version: typing.Optional[builtins.str] = None,
    php_version: typing.Optional[builtins.str] = None,
    python: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    python_version: typing.Optional[builtins.str] = None,
    tomcat_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce7f77af22299eb4330935f93341e33bf05fb159d1e7e7b4af61adf3b5af938(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ddbe8e69682b6024307a36a7998197da9c689768c5430b98f3949b6c40c4e5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8122218b3e8eab28883e46b92d8beeb552fbdae9ed367233a74c624480af40bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722187b854f312a1aa1e2dd9409099148bbeda6a0a0d462e862af2451cdbc3d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23df1ee704b61647e06aa22336843cc0e8efc187c73507395c5e986ac2f3fac2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a56325347c18b420ebc3c0181a2b93f29c784e2339993039867f0ce95565a93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b14d9fb44941d0c50b7fb095149edcdf1a853e6eca816aeb1370bbb2b3222dde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a707ab1b57c818fe22dba000af567867cc24b87c1f5c8fb8b2462d9d16085cf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c784edf64d4a387b2126aba803fd497a8afa8a3e87b3533f98adb4b51f1345(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fb32c13b1fec2e552f700eb5746e01162355374463d5151d633c4f60b8eabf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6d8dcced822e214a1f715660fe25a0034989a49fe78845bc2e2130622113fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cd4af7336080a7178db361f16abf5c2fa4d22a15844034789336de55126963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def77d56ce07f45e52c9d0239988001f828f6e6ecd9dc425c28a8c9f0661c3e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0bbc01f384d793e210342c67757883d272e796c71f515f4190484454784a32e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2440c0becb6c7636dc26433eb1f9b696b747f22b7c780dd8fd9848a1a007d84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56f6b2ccb5611dd25c2eff4b73bcba3065a53fb082c236ccc96d7d7c99b69a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2db3a61bbb19ca9aa7f6bf1d66dfe1d0e293b404802371aa5b501460614585(
    value: typing.Optional[WindowsWebAppSlotSiteConfigApplicationStack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6111285450c9db0042c7ef52ea2cf96a5949064ea1c5de8bca0d7e2ac360ac(
    *,
    action: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingAction, typing.Dict[builtins.str, typing.Any]],
    trigger: typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05573e34b2865598d12f17efbd803ad79c6c6b0c9c5b2091807bcd47cf47f995(
    *,
    action_type: builtins.str,
    custom_action: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction, typing.Dict[builtins.str, typing.Any]]] = None,
    minimum_process_execution_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d65156c937a6f9c2c2eb4d7b7f6ac388140a2823e365cc5d23fa11b82d999b15(
    *,
    executable: builtins.str,
    parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af23a22f92e1355b8ece4c08ee3e890bae921b0de336316a4b2a2b76708e2e41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092bd95209c641d8648d9b0e7d7533dc30f13429a6cd4da19e6aa591b41fa899(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ad9b2f462786343a87c2dbb949edfc3dee6fd95cd476f5d6488194f11b0f77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146844df752364c4327a78096d8d8b5d62d00c27b5ccdc833b3a88d809bbd522(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingActionCustomAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5f4c402985196e50eaa7b76beae7457a362d3993356448041dc7206777b47b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a814650370718c57d6d2852fdbb8538c071b4716d9b11f12aa0cfca88bff00e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a05c1bb4b032ddfa4d06f02f7e2a25c4d6fead1023cc0dcd1e8a2c6b5609807d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f8bf9bdc80438ae1ce6b9406a2ab56eab4bd6ac7ad26f5a5809db7b8d731aa7(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7a76f5ecb33aa179c5405c987a7e38e71cc47b7b6d884299448c9b43febc73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e9cc42c78bbbef71717566cf8d8ac305a7bd1a60eb951f0fffa615dcacb26d(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSetting],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595d2a7fad1fd2440a60b0a500dd856bbcfd8ab201035166f792ec4a5a1ec1f0(
    *,
    private_memory_kb: typing.Optional[jsii.Number] = None,
    requests: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests, typing.Dict[builtins.str, typing.Any]]] = None,
    slow_request: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    status_code: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224baec3c322038d7760411ac3e0d1cc8ee9b6cabc1eb48184c343fd004e8027(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47149a0674dfc76cc05f5de0cd9b4d907578b0a16ff55b3b9fa6a5c34d26b67(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1007cf936ebb99c1d2a615358348e161eaf7d479413a5c79793e7a1011f73b4e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470233d27f9efa797ea9a4e0c373efcbb7e7b3333345d46406f205edff610642(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTrigger],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f50d99a00520c10dd35153deb8cf49a8cd229984dd4dbd2a8589854cc52d0d4(
    *,
    count: jsii.Number,
    interval: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43a01c7efad811e9da1762e5a2feb2be93a54fc3c8e2879b2d6aca51fefb8de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5833f1998607109299e8914098761627bd5ca3ef0dd45fa865ab0e90a422349(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3799d6ad2f906c314d5ca1aa3795d5e0c1e6cf1784e31c7852d640c1acecc859(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e316f955293db8e97906250060f56409f654544ae4cfaa1f56ec79cf4b8a0b(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerRequests],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015e6e6fc9ddb5a667ef5ba416439dd8ee956e5859c1b69b979ec6cf8dec92bc(
    *,
    count: jsii.Number,
    interval: builtins.str,
    time_taken: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ce7237f7257744b69b034d84b9678e1fcf9fd6065a888bb62e695fb55ea129(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed274e9db5f85da2895f10514474e72a59de8d852cfe24a86132e00f8dda876d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f256a16be3f322226c74a3c47129d4e2f34f8df23c231b98743f8f26cebecc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b9c6109fd2c9fbd15ce666e1df6e4c14030ed3b66612f4080d1b8aea9a8b7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6dfb6f8ff21dc6a6015a1906bb030e6552e735dcb19eb5e4ca25384d2c243a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd0c04549518126ece5b6103bcf380a819623525e34bd04c96a43a8e24b0d5f(
    value: typing.Optional[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerSlowRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2a64c26ba4a9342372c180eb9ecb0d50b2b1bcaafd005142c0e1f31569090a(
    *,
    count: jsii.Number,
    interval: builtins.str,
    status_code_range: builtins.str,
    path: typing.Optional[builtins.str] = None,
    sub_status: typing.Optional[jsii.Number] = None,
    win32_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797af0a22049d80e886003601f5c4852f4115c66f9f0ea87727b1fea95cc6eeb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f2bd220ef0bd393c29dded799390f25167adb3d1bcda98dd8500b4d843e357(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088c7dc79f6c35a8e030d5ff2fede12681087176caf471827d9558aa690a6d2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a835642669347df5190ff2c31ac1c3002103776464a2133e21497550adb754(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e3c76efe295104396b085a9218f83147260c643f3d0340a70394e472bf32af1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18e1beb33de4eb1f8a335b4115fab23913a8c2aa190999742710c4f76706682(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be3dd95f12ade73169f860361dde5adf454fb407b4bcec382b4914938a225ba3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e49da4aaa5e67ed9a1de8b19e3b630f34b6e3b3afe2e057efba23947f901f81(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e584f697292af13947e2796ec4b6734b0d499b458c99e9b194d40cbafb79f87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d40dcd56e12d1ab496ae46f0da985d6755e9fee658bff51da2c532a19b0c167(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773f63a03e1c6678260868fe70c1173c6dc2970881f88c1e08f744c867cd633a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15cf05293d06d8c8d214b0464387c8e92aa0e86622d1bd0110b9d4363bfe77f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e30077bb53e128394ceda7ef1c8cbd21aed9515edfe3335124a2b2c317d81a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a95019cd63c8057d772060cdf9a973f884ff23bf483afb5ba34774a4d96be95(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigAutoHealSettingTriggerStatusCode, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470f63c4a9f0ea7250afae6ab0d8c5bc50f0608c9397c7b48910a74d9e2600c9(
    *,
    allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    support_credentials: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783bcb44e463475d57108011523f9742a9df2a89479997d31425b735573bcdbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9bdc5029dd6a98e3f5e45b167778193ee0f576795ba9461a879d6150b7e971e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521617e82bc33f68c3ea66563c3f8403cc2c8fadbd134e256cd380a4f7621037(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a929c6b3f2c324a4493910c66528805a15eeb5ca519bb3f0362578c61e6cbcff(
    value: typing.Optional[WindowsWebAppSlotSiteConfigCors],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49912332d49341cfebf2049d27bded47355f9ff7970d599cc3dc9df770344585(
    *,
    action: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    service_tag: typing.Optional[builtins.str] = None,
    virtual_network_subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77b92cd344064b9699e81b5bc034fc9c5d1849b0e0910223095f88d77bd52ec(
    *,
    x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e523b6f3b945d710e24534fbb14eaa8e1f85836c8f01dc93d753444057ded8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab356762259d51f6af2922e656253287a62489b6561c37144b4623643f2ffa2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aea0a1c3ee5e8c6216c26e4054c744b56b57029c35ba17245c56b86df47745b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c69d593b8c872489d6c6825aa1268848943e65e64a6a85d0cf019455ed3bb6e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434e4bac9284d4e0963bf42d0ec6ab5ee0bc72a51c4551aaabf536a1666e2f0d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b57c81242e2bc268ba5801e5537b3857729c021a60eb65d6bdaa1601eb4a0a2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestrictionHeaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__848ee55047bc87051ab74096f3d3f2916459e52554eb25054575d978bfa0f52a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d311ffa436a22b01e32c426183aa71f40c4bad55fc1564b873828bdc748bc24(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed76b2b8489e14079895382d74f71249dc1fa2c9d8372aef3fa723b8f73595d4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43121fb2b9d6f1b49db2cb92fbba37a5ea2b8f846bcc1466b7c0ed75a4096015(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50df49933dc4d30451986df50b1d0b6315b79181c6a57d2481a10704c3e8c580(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c953891fe66070050afc88805f52874afabf648b2992c77e77c40e8b1161f1e(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e996b951806e16b14604c3c2e9d04d26f2f89610a96328f2cb7d7a3d1348465b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b5b56f53ebb96ff79f9c6c0777254a31b0010f75df56c978eb2cb93d330e6f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c370e6138effc2eb831940244daf34e16499aa1a38e70fec93c1a519ebafdfa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c98898ba2e7782a6dd42428712bda76a0a8ec063f2da650e7fe3a3bded77b5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfc7e763da90a0f6e4b7f26c24cb087cd2336e74de1852face87de72bf20637(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034fcedbb534bce1df618da7f6b6d746e69821f1105d83d8da963e0baa7f09cd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigIpRestriction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82af4a2e106817700f9020b7ebd4f7a2fa4e863507c661486b816502dbb3ec2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6ef27e16919a957b442da22cb71201cd8f7b72a17948ef284efe6ff6e0c280(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__615a847921b8c42463d11dc573980d68e76560d9ed15533061005fce2e2c90ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10482b175e74e5b945dc5e3220a6365716cd052f1d85e4d84d0caed47026be82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1029c89617f74acbf6f304ff62f88b59bd65654adaa921342e97a6e2aa28df19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0fde8bdb8e2ddaffb2636a2dc6c87bd97570ed5d6f5398bd5e455a201fabd0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4910cb8731118f445af9ba39e37856446693c09612e6b955a7595ad1b16c979(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5800b0371c0711f80204a63fff5b9f6a975e4fb2d9de0e2d9783bb49a1dc5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3efe8ccbe72b80d9912890add9c116d12971f4f62ccd24368c8bed4c41706663(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b5b3bc46797cd6aa8d1b57b9e138895c76939171be62238ac400a5c2e6200b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea378504f83ab448eed4bd74c5ecfc79d4df9bd8db7c021cb31d8c99a585127c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigIpRestriction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53c0cc9c3f543fcacf6c6b15390376c9afbf50276ed3c75b5ca2a7ed5dac9df(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d43b69b39efd870b867a33de5cb04e8d0ade3264e980b41abebf323f4ad303a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75b13b7bcccf7f5dff6386fa2c134ca114e3be8ac25bd5fc475b9a8923fde5c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf6c9e347d43696d3856d9e36fb4c97bb55e707dd7b3141211eaa6b28f696b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5985c3c4ace45ee9189c1d838985dd30937dd18a58720490cb412359ecd9f73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2062484f321eee105079ad9fcc82a8e34d0956145dc50885b4128829a584b127(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294d2f5e413a851901899c023f2b1207cd9d0a3138efea1673bcdf6cf2039a13(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77e4e1c1bed99157c85612fafdb5876580aee353bc0c34e5e24752a8482441b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fadc886a9f26a60afb6eba03a73087de46e5e8007395cf10b80599a357a2ce3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5beb51af2ed4b5a0eb7e4e4d17a7748926c2cded58510587b105b4a63065c1f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402be6f3eb01a33df48f1471817e00dc848c1813638fc872c746e5cd52f66657(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3102c613215858eebfc831770b8d79bc9282bc824416a9385380415c77fc920(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1afe95caf3835ef7c6a8c9daae75e6fbdb7f53e45a1011265d513a62bb54f6c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d267a2a3f04bb99a87177684c19676f49c9f5e72b4eceef40211219b5ce341(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3acec33d9c15d6d47ea51d6f266fc13da94b45c52c7e64b8bd64dd20a7aa729a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2008233cfdc6bc5f45ad45f5a7f230e2e8f64f3d1f509e07fd37b08013a6d66d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84618945ccf2f3652d07e0169ece13fced66628351253a4283c07b0f07e91aa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36da70bf2013f91d22d3210f7a371498ade72cb0c50f96d198a9d9815e3ecfab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae259c12fa3475943a34140df25416fd4b8588d7b1c3a86e7334d7f3639a84e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d8f2ce5b118bb338df7e5e08420bbdf50e7349f0fbe9e6e0e0becd24db517d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd1cedb5dc7999dd23dfb98ee81c00ba86031e730c2c4d987bc66c4474774a60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146866444087ddd0aa0c0f5ed9b6e7f94aa53318841399d32d4df27fb5bb20ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9db5b91f3420a6b61826e66badfc7ca0e779c88a0d04179fa90afc85e64d63(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c98e38da3e420d2135e28f290c6733d51899a19c8cf29f3224bdf33da175259(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd901827a9ec0546ad8fc7c4eef7e92d56370655242d53956a4d3381c79f4cd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30264053e476cec68c84f92e40d32ed46b790b696ef0cbedf23af6b6e549400b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d431ce97ae5d1f821e83cf47f0f953792debbcb61b4eb93df2f7cc1907dfa0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844fb1223b17c7c7ddf7cbd0b641327a3137d17ae50e3561530ecc081906b80a(
    value: typing.Optional[WindowsWebAppSlotSiteConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6879987b34070b1b1aa9a6bbb39a0af826feb2c9172f80030c3a41d0faeaa03(
    *,
    action: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    service_tag: typing.Optional[builtins.str] = None,
    virtual_network_subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d183f20c21be45549b2b49c32adcef256f3d7f9c7c1a44d6ed48548c471d6dd(
    *,
    x_azure_fdid: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_fd_health_probe: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_forwarded_for: typing.Optional[typing.Sequence[builtins.str]] = None,
    x_forwarded_host: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42ac085ce916e259136454ec78b817d79ea3070c730168a0e0a645c3ecae304(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a60a8609b27d4e94870b689492b6521e86e9a43a05b94ad792ffea331b8a416(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481654eebce2bfaaf9ba178f321b9ca9ece565c134c18c861fa6f64c320ff555(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3f531e7ea33b2c4694804468c63876da5d42ce8f4b7ca7f3ff372921ab47b4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3d852b6be161cfbe1609cfb84d065a5b7e20adfeb3782b8916d9bff03df6c8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f679f3bf51fb7c97ce9806a07f63b941aa6342174c9e7cb135675fd0ca934b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9898b336577cdf92394934c6cdfb1395b180ed7433d1f40664528ac18cd36104(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d104e2d726bcccc6f73eee22d13b105b3fd94a167bad912fec5996d308fb14ad(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006cb1b48eb3c248cf04066c7f04140a7345ed6e26f0af28ac3d5b542cef9439(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0d2945551ced0b6d731e965c63778cc5a71c1c5763678b4185eb810ef11897(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5843792506122b0faed02e2f5cb8491d2d966555e76e86211fe7eec3ab0e5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9beb4b8f85395ce9dda3d4e37e730adbc730dfbceb7c0afe9db5701a600b3287(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa4274b0b8e39c532c17d3ec880eff5f3fa268c7db0eec554305dec2346425ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47dbde19d5a077cd33ff6023e3b5135417fc446f566f1d359696dbf618c33376(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc5b3ce11d122d10f18e52b09c7e60aa11bc59ef9f28e18f95996576cba00f2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f280ac19de42d8065f3864d38b7d911c7ac5e291a4251782598a589160bca3c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c029b5c75c40ba018aaabba0ddc37e4e3605daeea2a85d22f656c0792e683a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8615ce096174c0a0c46ffa6fecd3a613d7b96ff99c4f0e4c40cf65040b7f552c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigScmIpRestriction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b100f398f9197fa41727489adc6934bfd49b1ddefdae07c78733c338032081(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5508b4b52432124c003a73c49ed82f214f47fc9865dd7fc8803f5da52df1c477(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestrictionHeaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e32039f9fc434c64ea7865c70c14b803a7c2e1ffc4b9c860a3495eec0f05a20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7878c9f9f978a3a30414797b5b6c8aa2c722ae6e30722ba4758de2d154aeb5f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ad027fcec1a0af280a1d0a30153c779a34722986d46482874a0f30c12c9f0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02004ddbc7e7d69db9483c0a1499a65f3af363aa12891cbad15861373547c6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557a4d941526d4f97e9e2696ae199ed30afbe0730b4d5ef47af5e30697f73348(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d41df6b78aff77378c9a9ea7dfc59a9b1da36387c2ef078ce1217750092ebb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d2ee222f317e7844d2b9126c5d1c97e22979ce879299bf209cb94a1cc6271e(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigScmIpRestriction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f3d97c9d11ecc502144d921506e7a6935597b49e8f7019dcddc890e209e4d6(
    *,
    physical_path: builtins.str,
    preload: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    virtual_path: builtins.str,
    virtual_directory: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa609b5c3988ba41dad677686a266bee83b8096ec32b12a3caef9a8c2096c2d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f838a625b2d15864c0056a3efa9230a7abda27fd7e02b22bd6cda15e45216bfd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e60234787d6ef5455804d0a0a68271c5b61d2fd9042a6f515829ac285f262e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52bda3feb58fdccbdb0d88b70011dcff94c64f014756a9c7a5e8e0dcd7c12d12(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c51e771011be0399eeb93b8272ad9e5298990771f2680333224dea0e0a6b63(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0245ac9e608422b49a703264cdebb6b136cc2d74f013f1fd10c60629f5289f08(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplication]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa51d5c657fe0b401a79b336551b6d22107eaedf4e7992445b66f21503b710ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d50fbaef69a63e5984904dfbe3eacbfec184ed4af8fe78df3eda6b421c3c408(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0687af086eb8eb6881e5754fa9efefaceac68ddccbef838f10d01ee59494f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980d6578fe3ec229d3bc21708f9db67398175e98dd2e9c90456a0f923b866634(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed765128ddd7a63143a15dc23c6c8283ebd0987ec9961bc884fbf5ceeaa5b37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e70e3916b318810002eba8b3457745da0ba931193f30c9666c1be775a5b9a5(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplication, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b8f18e4dd59f4db815ccbb81209efd8c76e3a1d15ec58fcc5a52883f3419f9(
    *,
    physical_path: typing.Optional[builtins.str] = None,
    virtual_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c20be605ad3eca6fdca492b5ba4fbd19a67feccb5bfdf8a527e665013f7f179(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0231c31b67dbfaa731a1ee0013f855a7706b4abe80e86e8067779b97d6a90b1b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9578ba0492bef1512ffa68d46a685925a073937b7574395d5c88f32fc10618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e753790fbff204ddfead3b603884c1eac4efff48bde7b58da65f7c089fb0826a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384eb4d51f94cd20cdf113a4f33f373c4ed0b7f06e70917ce58ce270eff5f7e2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdebff5a36260ca56e0d629c7922575844757502b899a63114291c77a5c56691(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996d94188c6d65d09290d2e3c624f756fadbaac599469072ca15502ed2509f3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9c99b82f0b246160e20a9920a0efe809a1d5061c60c88640d295bd691e0e67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83bb957b23fd8464b76b120d728d92e9754102421d3fd2a4da39f8921144a5df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395e4ef7f7e878d4e4d6ede1eaf0489061e613e37ca68240901a553d27485161(
    value: typing.Optional[typing.Union[WindowsWebAppSlotSiteConfigVirtualApplicationVirtualDirectory, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7229b8d36e9863d792cd89a1927fa01be7b42aff37f410cc985f66df2f236220(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa80a262c7b8d4d536d63b608768c59f4e71b6f5b18882af099b0c9be3a5cae8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a13fae3140f88c3af2765e96c317916a799300900c37bb4a429ff10dce959440(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a42ef683f6073979d2e942eb8dc16657ff1430c2f1388b4926dcb2284871315(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1fd003c6787f8d63d9822d128a2dc61c8742685724a6579c080828bd175ff78(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a21d087f9d29f35653162380c982a03b71163fb4fc684f262ff42ffb9646989c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1454a7ba6a0452158550eda53e321193ae17b6fbf34a10aa6831d2b791f7fe(
    value: typing.Optional[WindowsWebAppSlotSiteCredential],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4fe8093ab79cc0a6806610971fca41204aed5195faf5db5e94bf3fa21d6ea3(
    *,
    access_key: builtins.str,
    account_name: builtins.str,
    name: builtins.str,
    share_name: builtins.str,
    type: builtins.str,
    mount_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0826a1015f7d46bd3e9de31eca9fbb04a6e80a9a3b88058e8363211893f3d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0964fefbe1d90dbf5bf03fd065abdc020460e741c491ed005a9e8ff73a82ab3b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6ce8b959076d4b23bd275ae3adc320a25302b578afc583ca551c6ca0a0c89f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3504f16163c7555fa632c6583c947498c25b02311809ca8f890d0e61f87a2aa0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f230ccf6305e304f257394e50ba0497e783ded7ca01e5d8bfb26a2748dbc18(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078c65f80ebef67de767e0ded308f9de7e24955061cd6a03db276dee1112e601(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsWebAppSlotStorageAccount]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08afdaa06449fcc61c3c58d38ef4c5af76bfcc1c5998c5ac6f395e4bbe37c2b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff0f10ab1aeb05c73e34cef2c99cb3540814d665e527873a90d130acd031153(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d8bae4c84a3def269b618519b907f7dd5b3a9e04f80cac97be35414fe1c67a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e3ab4e41f3aea87d911230a074ecc1f393d72c3fc9ad81da7c01b853956fb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc9244ac2af24c8603db2ec43cae7d588b5f302575188cf73cd15e27d6175f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76124b38d17b8d4c8dcee91e779b783b67efbdc8f7a2f4c73db695a06e302ed2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9daddc613d16fc98c245016238d1d43cd7262ec7b96a2e158bec25a0c8912a17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e59731f62561c2fb1daeffc81f74b42822029f4bf83c39be7c2eec1b889866d(
    value: typing.Optional[typing.Union[WindowsWebAppSlotStorageAccount, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec33f891d151e10bbbf0eaf3f91677cc4fb6f4dc458f26f9b24dcccbda253be9(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4424579ec7e134b1cdae7260e4393dfce306e338185676fc9de5282cbe86a67(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8fba0ced29ac1a0d119223c288ce04ea5cbe0784b1b2a65bec4315e2d79b7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3488f961e78a47ce4a0f22a72b9c7094e87a696cf0f06e776b868f3614e26471(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0abe49a516e7ac1c7729aee00ed4e99e9a29f18ff1c57020109af4698023b8f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473f5d8dd74f16cd81cc762b243a2a0a6b5d5f3491a129b5562346ba961d6d77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7113e3274955b6315cff53d7a5d82e742fb9da5c00696ed0842071f1976739af(
    value: typing.Optional[typing.Union[WindowsWebAppSlotTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
