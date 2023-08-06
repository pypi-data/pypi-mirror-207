import click
from kubeconfig import KubeConfig
import yaml
import requests
import base64
import datetime
import hashlib
import json
import os
from os import path
from pathlib import Path


@click.group()
def cli(**kwargs):
    pass


@cli.command(help="Generate a token to use your cloud workstation", hidden=True)
@click.option(
    "-d",
    "--config-dir",
    default=path.expanduser(os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")),
    help="Path to Metaflow configuration directory",
    show_default=True,
)
@click.option(
    "-p",
    "--profile",
    default="",
    help="The named metaflow profile in which your workstation exists",
)
def generate_workstation_token(config_dir=None, profile=None):
    try:
        metaflow_token = get_metaflow_token_from_config(config_dir, profile)
        auth_url = get_sanitized_url_from_config(config_dir, profile, "OBP_AUTH_SERVER")
        k8s_response = requests.get(
            f"{auth_url}/generate/k8s", headers={"x-api-key": metaflow_token}
        )
        if k8s_response.status_code == 200:
            k8s_response_json = k8s_response.json()
            token = k8s_response_json["token"]
            token_data = base64.b64decode(token.split(".")[1] + "==")
            exec_creds = {
                "kind": "ExecCredential",
                "apiVersion": "client.authentication.k8s.io/v1beta1",
                "spec": {},
                "status": {
                    "token": token,
                    "expirationTimestamp": datetime.datetime.fromtimestamp(
                        json.loads(token_data)["exp"], datetime.timezone.utc
                    ).isoformat(),
                },
            }
            click.echo(json.dumps(exec_creds))
        else:
            click.secho("Failed to generate workstation token.", fg="red")
            click.secho("Error: {}".format(json.dumps(k8s_response.json(), indent=4)))
    except Exception as e:
        click.secho("Failed to generate workstation token.", fg="red")
        click.secho("Error: {}".format(str(e)))


@cli.command(help="Configure a cloud workstation", hidden=True)
@click.option(
    "-d",
    "--config-dir",
    default=path.expanduser(os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")),
    help="Path to Metaflow configuration directory",
    show_default=True,
)
@click.option(
    "-p",
    "--profile",
    default="",
    help="The named metaflow profile in which your workstation exists",
)
@click.option(
    "-b",
    "--binary",
    default="outerbounds",
    help="Path to the location of your outerbounds binary",
)
def configure_cloud_workstation(config_dir=None, profile=None, binary=None):
    try:
        metaflow_token = get_metaflow_token_from_config(config_dir, profile)
        auth_url = get_sanitized_url_from_config(config_dir, profile, "OBP_AUTH_SERVER")
        k8s_response = requests.get(
            f"{auth_url}/generate/k8s", headers={"x-api-key": metaflow_token}
        )
        if k8s_response.status_code != 200:
            click.secho("Failed to generate workstation token.", fg="red")
            click.secho("Error: {}".format(json.dumps(k8s_response.json(), indent=4)))
        else:
            k8s_response_json = k8s_response.json()
            token_data = base64.b64decode(
                k8s_response_json["token"].split(".")[1] + "=="
            )
            ws_namespace = "ws-{}".format(
                hashlib.md5(
                    bytes(json.loads(token_data)["username"], "utf-8")
                ).hexdigest()
            )

            kube_config_path = path.expanduser(
                os.environ.get("KUBECONFIG", "~/.kube/config")
            )
            kube_config = KubeConfig(kube_config_path)
            kube_config.set_context(
                "outerbounds-workstations",
                "outerbounds-cluster",
                ws_namespace,
                "obp-user",
            )

            kube_config.set_cluster(
                "outerbounds-cluster",
                server=k8s_response_json["endpoint"],
                insecure_skip_tls_verify=True,
            )

            with open(kube_config_path, "r") as f:
                kube_yaml = yaml.safe_load(f)

            gen_creds_args = ["generate-workstation-token"]
            if profile != "":
                gen_creds_args.append("--profile")
                gen_creds_args.append(profile)

            gen_creds_args.append("--config-dir")
            gen_creds_args.append(config_dir)

            user_exec_creds = {
                "exec": {
                    "apiVersion": "client.authentication.k8s.io/v1beta1",
                    "command": binary,
                    "args": gen_creds_args,
                    "env": None,
                    "interactiveMode": "Never",
                    "provideClusterInfo": False,
                }
            }

            user_updated = False

            if kube_yaml["users"] is None:
                kube_yaml["users"] = []

            for user in kube_yaml["users"]:
                if user["name"] == "obp-user":
                    user["user"] = user_exec_creds
                    user_updated = True

            if not user_updated:
                kube_yaml["users"].append({"name": "obp-user", "user": user_exec_creds})

            with open(kube_config_path, "w") as f:
                yaml.safe_dump(kube_yaml, f)

            kube_config.use_context("outerbounds-workstations")
    except Exception as e:
        click.secho("Failed to configure cloud workstation", fg="red")
        click.secho("Error: {}".format(str(e)))


@cli.command(help="List all existing workstations", hidden=True)
@click.option(
    "-d",
    "--config-dir",
    default=path.expanduser(os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")),
    help="Path to Metaflow configuration directory",
    show_default=True,
)
@click.option(
    "-p",
    "--profile",
    default="",
    help="The named metaflow profile in which your workstation exists",
)
def list_workstations(config_dir=None, profile=None):
    try:
        metaflow_token = get_metaflow_token_from_config(config_dir, profile)
        api_url = get_sanitized_url_from_config(config_dir, profile, "OBP_API_SERVER")
        workstations_response = requests.get(
            f"{api_url}/v1/workstations", headers={"x-api-key": metaflow_token}
        )
        if workstations_response.status_code != 200:
            click.secho("Failed to generate workstation token.", fg="red")
            click.secho(
                "Error: {}".format(json.dumps(workstations_response.json(), indent=4))
            )
        else:
            click.echo(json.dumps(workstations_response.json(), indent=4))
    except Exception as e:
        click.secho("Failed to list workstations", fg="red")
        click.secho("Error: {}".format(str(e)))


@cli.command(help="Hibernate workstation", hidden=True)
@click.option(
    "-d",
    "--config-dir",
    default=path.expanduser(os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")),
    help="Path to Metaflow configuration directory",
    show_default=True,
)
@click.option(
    "-p",
    "--profile",
    default="",
    help="The named metaflow profile in which your workstation exists",
)
@click.option(
    "-w",
    "--workstation",
    default="",
    help="The ID of the workstation to hibernate",
)
def hibernate_workstation(config_dir=None, profile=None, workstation=None):
    if workstation is None or workstation == "":
        click.secho("Please specify a workstation ID", fg="red")
        return
    try:
        metaflow_token = get_metaflow_token_from_config(config_dir, profile)
        api_url = get_sanitized_url_from_config(config_dir, profile, "OBP_API_SERVER")
        hibernate_response = requests.put(
            f"{api_url}/v1/workstations/hibernate/{workstation}",
            headers={"x-api-key": metaflow_token},
        )
        if hibernate_response.status_code == 200:
            response_json = hibernate_response.json()
            if len(response_json) > 0:
                click.echo(json.dumps(response_json, indent=4))
            else:
                click.secho("Success", fg="green", bold=True)
        else:
            click.secho("Failed to hibernate workstation", fg="red")
            click.secho(
                "Error: {}".format(json.dumps(hibernate_response.json(), indent=4))
            )
    except Exception as e:
        click.secho("Failed to hibernate workstation", fg="red")
        click.secho("Error: {}".format(str(e)))


@cli.command(help="Restart workstation to the int", hidden=True)
@click.option(
    "-d",
    "--config-dir",
    default=path.expanduser(os.environ.get("METAFLOW_HOME", "~/.metaflowconfig")),
    help="Path to Metaflow configuration directory",
    show_default=True,
)
@click.option(
    "-p",
    "--profile",
    default="",
    help="The named metaflow profile in which your workstation exists",
)
@click.option(
    "-w",
    "--workstation",
    default="",
    help="The ID of the workstation to restart",
)
def restart_workstation(config_dir=None, profile=None, workstation=None):
    if workstation is None or workstation == "":
        click.secho("Please specify a workstation ID", fg="red")
        return
    try:
        metaflow_token = get_metaflow_token_from_config(config_dir, profile)
        api_url = get_sanitized_url_from_config(config_dir, profile, "OBP_API_SERVER")
        restart_response = requests.put(
            f"{api_url}/v1/workstations/restart/{workstation}",
            headers={"x-api-key": metaflow_token},
        )
        if restart_response.status_code == 200:
            # Print pretty JSON
            response_json = restart_response.json()
            if len(response_json) > 0:
                click.echo(json.dumps(response_json, indent=4))
            else:
                click.secho("Success", fg="green", bold=True)
        else:
            click.secho("Failed to restart workstation", fg="red")
            click.secho(
                "Error: {}".format(json.dumps(restart_response.json(), indent=4))
            )
    except Exception as e:
        click.secho("Failed to restart workstation", fg="red")
        click.secho("Error: {}".format(str(e)))


def get_metaflow_token_from_config(config_dir, profile):
    config_filename = f"config_{profile}.json" if profile else "config.json"
    config_path = os.path.join(config_dir, config_filename)
    with open(config_path) as json_file:
        config = json.load(json_file)
        if config is None or "METAFLOW_SERVICE_AUTH_KEY" not in config:
            raise Exception("METAFLOW_SERVICE_AUTH_KEY not found in config file")
        return config["METAFLOW_SERVICE_AUTH_KEY"]


def get_sanitized_url_from_config(config_dir, profile, key):
    config_filename = f"config_{profile}.json" if profile else "config.json"
    config_path = os.path.join(config_dir, config_filename)

    with open(config_path) as json_file:
        config = json.load(json_file)
        if key not in config:
            raise Exception(f"Key {key} not found in config file {config_path}")
        url_in_config = config[key]
        if not url_in_config.startswith("https://"):
            url_in_config = f"https://{url_in_config}"

        url_in_config = url_in_config.rstrip("/")
        return url_in_config
