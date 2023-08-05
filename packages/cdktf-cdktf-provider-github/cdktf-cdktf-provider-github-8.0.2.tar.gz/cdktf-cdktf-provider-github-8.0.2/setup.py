import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-github",
    "version": "8.0.2",
    "description": "Prebuilt github Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-github.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-github.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_github",
        "cdktf_cdktf_provider_github._jsii",
        "cdktf_cdktf_provider_github.actions_environment_secret",
        "cdktf_cdktf_provider_github.actions_environment_variable",
        "cdktf_cdktf_provider_github.actions_organization_oidc_subject_claim_customization_template",
        "cdktf_cdktf_provider_github.actions_organization_permissions",
        "cdktf_cdktf_provider_github.actions_organization_secret",
        "cdktf_cdktf_provider_github.actions_organization_secret_repositories",
        "cdktf_cdktf_provider_github.actions_organization_variable",
        "cdktf_cdktf_provider_github.actions_repository_access_level",
        "cdktf_cdktf_provider_github.actions_repository_oidc_subject_claim_customization_template",
        "cdktf_cdktf_provider_github.actions_repository_permissions",
        "cdktf_cdktf_provider_github.actions_runner_group",
        "cdktf_cdktf_provider_github.actions_secret",
        "cdktf_cdktf_provider_github.actions_variable",
        "cdktf_cdktf_provider_github.app_installation_repositories",
        "cdktf_cdktf_provider_github.app_installation_repository",
        "cdktf_cdktf_provider_github.branch",
        "cdktf_cdktf_provider_github.branch_default",
        "cdktf_cdktf_provider_github.branch_protection",
        "cdktf_cdktf_provider_github.branch_protection_v3",
        "cdktf_cdktf_provider_github.data_github_actions_environment_secrets",
        "cdktf_cdktf_provider_github.data_github_actions_environment_variables",
        "cdktf_cdktf_provider_github.data_github_actions_organization_oidc_subject_claim_customization_template",
        "cdktf_cdktf_provider_github.data_github_actions_organization_public_key",
        "cdktf_cdktf_provider_github.data_github_actions_organization_registration_token",
        "cdktf_cdktf_provider_github.data_github_actions_organization_secrets",
        "cdktf_cdktf_provider_github.data_github_actions_organization_variables",
        "cdktf_cdktf_provider_github.data_github_actions_public_key",
        "cdktf_cdktf_provider_github.data_github_actions_registration_token",
        "cdktf_cdktf_provider_github.data_github_actions_repository_oidc_subject_claim_customization_template",
        "cdktf_cdktf_provider_github.data_github_actions_secrets",
        "cdktf_cdktf_provider_github.data_github_actions_variables",
        "cdktf_cdktf_provider_github.data_github_app",
        "cdktf_cdktf_provider_github.data_github_branch",
        "cdktf_cdktf_provider_github.data_github_branch_protection_rules",
        "cdktf_cdktf_provider_github.data_github_collaborators",
        "cdktf_cdktf_provider_github.data_github_dependabot_organization_public_key",
        "cdktf_cdktf_provider_github.data_github_dependabot_organization_secrets",
        "cdktf_cdktf_provider_github.data_github_dependabot_public_key",
        "cdktf_cdktf_provider_github.data_github_dependabot_secrets",
        "cdktf_cdktf_provider_github.data_github_enterprise",
        "cdktf_cdktf_provider_github.data_github_external_groups",
        "cdktf_cdktf_provider_github.data_github_ip_ranges",
        "cdktf_cdktf_provider_github.data_github_issue_labels",
        "cdktf_cdktf_provider_github.data_github_membership",
        "cdktf_cdktf_provider_github.data_github_organization",
        "cdktf_cdktf_provider_github.data_github_organization_ip_allow_list",
        "cdktf_cdktf_provider_github.data_github_organization_team_sync_groups",
        "cdktf_cdktf_provider_github.data_github_organization_teams",
        "cdktf_cdktf_provider_github.data_github_organization_webhooks",
        "cdktf_cdktf_provider_github.data_github_ref",
        "cdktf_cdktf_provider_github.data_github_release",
        "cdktf_cdktf_provider_github.data_github_repositories",
        "cdktf_cdktf_provider_github.data_github_repository",
        "cdktf_cdktf_provider_github.data_github_repository_branches",
        "cdktf_cdktf_provider_github.data_github_repository_deploy_keys",
        "cdktf_cdktf_provider_github.data_github_repository_file",
        "cdktf_cdktf_provider_github.data_github_repository_milestone",
        "cdktf_cdktf_provider_github.data_github_repository_pull_request",
        "cdktf_cdktf_provider_github.data_github_repository_pull_requests",
        "cdktf_cdktf_provider_github.data_github_repository_teams",
        "cdktf_cdktf_provider_github.data_github_repository_webhooks",
        "cdktf_cdktf_provider_github.data_github_ssh_keys",
        "cdktf_cdktf_provider_github.data_github_team",
        "cdktf_cdktf_provider_github.data_github_tree",
        "cdktf_cdktf_provider_github.data_github_user",
        "cdktf_cdktf_provider_github.data_github_users",
        "cdktf_cdktf_provider_github.dependabot_organization_secret",
        "cdktf_cdktf_provider_github.dependabot_organization_secret_repositories",
        "cdktf_cdktf_provider_github.dependabot_secret",
        "cdktf_cdktf_provider_github.emu_group_mapping",
        "cdktf_cdktf_provider_github.enterprise_organization",
        "cdktf_cdktf_provider_github.issue",
        "cdktf_cdktf_provider_github.issue_label",
        "cdktf_cdktf_provider_github.membership",
        "cdktf_cdktf_provider_github.organization_block",
        "cdktf_cdktf_provider_github.organization_project",
        "cdktf_cdktf_provider_github.organization_security_manager",
        "cdktf_cdktf_provider_github.organization_settings",
        "cdktf_cdktf_provider_github.organization_webhook",
        "cdktf_cdktf_provider_github.project_card",
        "cdktf_cdktf_provider_github.project_column",
        "cdktf_cdktf_provider_github.provider",
        "cdktf_cdktf_provider_github.release",
        "cdktf_cdktf_provider_github.repository",
        "cdktf_cdktf_provider_github.repository_autolink_reference",
        "cdktf_cdktf_provider_github.repository_collaborator",
        "cdktf_cdktf_provider_github.repository_collaborators",
        "cdktf_cdktf_provider_github.repository_deploy_key",
        "cdktf_cdktf_provider_github.repository_environment",
        "cdktf_cdktf_provider_github.repository_file",
        "cdktf_cdktf_provider_github.repository_milestone",
        "cdktf_cdktf_provider_github.repository_project",
        "cdktf_cdktf_provider_github.repository_pull_request",
        "cdktf_cdktf_provider_github.repository_tag_protection",
        "cdktf_cdktf_provider_github.repository_webhook",
        "cdktf_cdktf_provider_github.team",
        "cdktf_cdktf_provider_github.team_members",
        "cdktf_cdktf_provider_github.team_membership",
        "cdktf_cdktf_provider_github.team_repository",
        "cdktf_cdktf_provider_github.team_settings",
        "cdktf_cdktf_provider_github.team_sync_group_mapping",
        "cdktf_cdktf_provider_github.user_gpg_key",
        "cdktf_cdktf_provider_github.user_invitation_accepter",
        "cdktf_cdktf_provider_github.user_ssh_key"
    ],
    "package_data": {
        "cdktf_cdktf_provider_github._jsii": [
            "provider-github@8.0.2.jsii.tgz"
        ],
        "cdktf_cdktf_provider_github": [
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
