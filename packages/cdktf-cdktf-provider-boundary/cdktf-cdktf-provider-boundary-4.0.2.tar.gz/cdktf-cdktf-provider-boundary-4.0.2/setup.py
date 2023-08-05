import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-boundary",
    "version": "4.0.2",
    "description": "Prebuilt boundary Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-boundary.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-boundary.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_boundary",
        "cdktf_cdktf_provider_boundary._jsii",
        "cdktf_cdktf_provider_boundary.account",
        "cdktf_cdktf_provider_boundary.account_oidc",
        "cdktf_cdktf_provider_boundary.account_password",
        "cdktf_cdktf_provider_boundary.auth_method",
        "cdktf_cdktf_provider_boundary.auth_method_oidc",
        "cdktf_cdktf_provider_boundary.auth_method_password",
        "cdktf_cdktf_provider_boundary.credential_json",
        "cdktf_cdktf_provider_boundary.credential_library_vault",
        "cdktf_cdktf_provider_boundary.credential_library_vault_ssh_certificate",
        "cdktf_cdktf_provider_boundary.credential_ssh_private_key",
        "cdktf_cdktf_provider_boundary.credential_store_static",
        "cdktf_cdktf_provider_boundary.credential_store_vault",
        "cdktf_cdktf_provider_boundary.credential_username_password",
        "cdktf_cdktf_provider_boundary.group",
        "cdktf_cdktf_provider_boundary.host",
        "cdktf_cdktf_provider_boundary.host_catalog",
        "cdktf_cdktf_provider_boundary.host_catalog_plugin",
        "cdktf_cdktf_provider_boundary.host_catalog_static",
        "cdktf_cdktf_provider_boundary.host_set",
        "cdktf_cdktf_provider_boundary.host_set_plugin",
        "cdktf_cdktf_provider_boundary.host_set_static",
        "cdktf_cdktf_provider_boundary.host_static",
        "cdktf_cdktf_provider_boundary.managed_group",
        "cdktf_cdktf_provider_boundary.provider",
        "cdktf_cdktf_provider_boundary.role",
        "cdktf_cdktf_provider_boundary.scope",
        "cdktf_cdktf_provider_boundary.target",
        "cdktf_cdktf_provider_boundary.user",
        "cdktf_cdktf_provider_boundary.worker"
    ],
    "package_data": {
        "cdktf_cdktf_provider_boundary._jsii": [
            "provider-boundary@4.0.2.jsii.tgz"
        ],
        "cdktf_cdktf_provider_boundary": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.16.0, <0.17.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.80.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
