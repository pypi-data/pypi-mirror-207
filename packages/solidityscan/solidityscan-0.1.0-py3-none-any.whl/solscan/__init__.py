import click

from solscan.config import Config
from solscan.scan import Scan

"""
    each command is mapped to @config.command()
    commands can be grouped. a group can be created by mapping the method to @config.group()
"""

# base group. under which all other subcommands go.
@click.group()
def solscan():
    pass

# config command, with subcommands.
@solscan.group()
def config():
    """config file actions"""
    pass

# adds config to the default config path
@config.command()
@click.option("--token", prompt=False, required=False, type=str, help="api token generated from solidityscan")
@click.option("--error-language", prompt=False, required=False, type=str, help="language code for error messages. defaults to 'en'")
def add_update_config(token, error_language):
    """edit config file"""
    if not token and not error_language:
        raise click.UsageError("--token or --error-language is required")

    Config.add_update_config(token, error_language)

# shows the config path
# todo: make config path editable
@config.command()
def show_config_path():
    """show default config path"""
    Config.get_config_path()

# does a scan
@solscan.command()
@click.option("--scan-type", "-s", required=True, type=click.Choice(["project", "block"]), prompt=False, help="type of scan to perform")
@click.option("-project-url", required=False, help="project url to scan")
@click.option("-project-branch", required=False, help="branch of the project")
@click.option("-project-name", required=False, help="name of the project")
@click.option("-skip-file-paths", required=False, help="file paths to skip scanning", multiple=True)
@click.option("-rescan", "-r", is_flag=True, required=False, help="flag to denote if the scan is a rescan")
@click.option("-contract-address", required=False, help="address of the contract")
@click.option("-contract-chain", required=False, help="chain of the contract")
@click.option("-contract-platform", required=False, help="platform of the contract")
@click.option("--token", "-t", required=False, help="api token generated from solidityscan")
def scan(scan_type, project_url, project_branch, project_name, skip_file_paths, rescan, contract_address, contract_chain, contract_platform, token):
    """perform scans on blocks or projects"""
    
    """
        takes input parameters via CLI and does a scan.
        2 allowed scan_types -> project, block

        if there is a --token parameter, the token will not be picked up from config file.
        if there is a -r or -rescan flag, the scan will be considered a rescan
    """

    s = Scan()

    if scan_type == "project":
        if not project_url:
            raise click.UsageError("-project-url flag is required")
        if not project_branch:
            raise click.UsageError("-project-branch flag is required")
        if not project_name:
            raise click.UsageError("-project-name flag is required")

        s.project_scan(project_url, project_branch, project_name, rescan, skip_file_paths, token)
    elif scan_type == "block":
        if not contract_address:
            raise click.UsageError("-contract-address flag is required")
        if not contract_chain:
            raise click.UsageError("-contract-chain flag is required")
        if not contract_platform:
            raise click.UsageError("-contract-platform flag is required")
        
        s.block_scan(contract_address, contract_chain, contract_platform, rescan, token)

if __name__ == "__main__":
    solscan()
