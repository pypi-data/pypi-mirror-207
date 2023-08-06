import re
import subprocess
from datetime import datetime

import click
from appollo.helpers import login_required_warning_decorator, ssh_tunnel, print_qrcode, get_version_and_build


@click.group('build')
def build():
    """ Subcommands to build an app and track builds.

    \f
    When starting a new project commands are mostly executed in this order :

        1. :code:`appollo build start --build-type="configuration [DIRECTORY]"` to create an Appollo-Remote with the right environment for your application.
        2. :code:`appollo build connect` to get your connection settings and access the Appolo Remote on which you can test and setup your application with XCode.
        3. :code:`appollo build stop` to stop your Appolo Remote when you're done editing your settings.
        4. :code:`appollo build patch` to retrieve the changes made on the Appollo-Remote.
        5. :code:`git apply appollo.patch` to apply the changes locally.
        6. :code:`appollo build start [OPTIONS] [DIRECTORY]` to build your app with Flutter and generate an IPA or to publish your app on the App Store.

    Usage:
    """
    pass


@build.command()
@login_required_warning_decorator
@click.option('-a', '--all', 'show_all', default=False, is_flag=True,
              help="shows your builds and the builds from your teams")
def ls(show_all):
    """ Lists builds on Appollo. """
    from appollo import api
    from appollo.settings import console
    from rich.syntax import Syntax
    from rich.table import Table

    if show_all:
        builds = api.get("/builds/", params={"all": 1})
    else:
        builds = api.get("/builds/")

    if builds:
        table = Table()
        table.add_column("KEY")
        table.add_column("App")
        table.add_column("Name")
        table.add_column("Started at")
        table.add_column("Finished at")
        table.add_column("Status")
        table.add_column("Build Type")
        table.add_column("Started by")
        table.add_column("Certificate")
        table.add_column("Profile")

        for b in builds:
            table.add_row(b['key'], b['application'], b['name'], b['start_time'],
                          b['finish_time'], b['status'], b['build_type'], b['creator'],
                          b['certificate'], b['profile'])

        console.print(table)
    else:
        if show_all:
            code = Syntax(code="$ appollo build start SOURCE_DIRECTORY --app-key APPLICATION_KEY", lexer="shell")
            console.print(f"You did not launch any builds. Create one with")
            console.print(code)
        else:
            code = Syntax(code="$ appollo build ls --all", lexer="shell")
            console.print(f"You do not have any active builds. See all your builds with")
            console.print(code)


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def rm(key):
    """ Deletes a build and its corresponding Appollo-Remote.

    \f

    .. note:: Appollo-Remotes are MacOS build machines on which the flutter build of your application is executed.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", api_params={"all": 1}, name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        build_instance = api.delete(f"/builds/{key}/")

        if build_instance:
            console.print(f"Build with KEY {key} has been deleted")
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def detail(key):
    """ Fetches detailed information of a build.

    Returns the location of the logs and application artifacts.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", api_params={"all": 1}, name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        build_instance = api.get(f"/builds/{key}/")

        if build_instance:
            console.print(Panel(Text.from_markup(
                textwrap.dedent(
                    f"""
                    Appollo Key : [bold]{build_instance["key"]}[/bold]
                    Name : [bold]{build_instance["name"]}[/bold]
                    Application : [bold]{build_instance["application"]}[/bold]
                    Status : [bold]{build_instance["status"] + (" - " + build_instance["substatus"] if build_instance["substatus"] else "")}[/bold]
                    Remote Desktop status : [bold]{build_instance["remote_desktop_status"]}[/bold]
                    Creator : [bold]{build_instance["creator"]}[/bold]
                    """
                )
            ), title="General information"))

            console.print(Panel(Text.from_markup(
                textwrap.dedent(
                    f"""
                    Flutter version: [bold]{build_instance["flutter_version"]}[/bold]
                    Build type : [bold]{build_instance["build_type"]}[/bold]
                    Provisioning profile : [bold]{build_instance["profile"]}[/bold]
                    Certificate : [bold]{build_instance["certificate"]}[/bold]
                    Minimum iOS SDK : [bold]{build_instance["min_sdk"]}[/bold]
                    App version: [bold]{build_instance["app_version"] or "-"}[/bold]
                    Build number: [bold]{build_instance["build_number"] or "-"}[/bold]
                    Mode: [bold]{build_instance["mode"]}[/bold]
                    Target: [bold]{build_instance["target"] or "-"}[/bold]
                    Flavor: [bold]{build_instance["flavor"] or "-"}[/bold]
                    """
                )
            ), title="Build config"))

            if build_instance.get("error_message"):
                console.print(Panel(Text.from_markup(
                    textwrap.dedent(
                        f"""
                        Error message: [bold]{build_instance['error_message']}[/bold]
                        """
                    )
                ), title="Error details"))
                # TODO Add errors codes in doc

            code = Syntax(f"appollo build logs {key}", lexer="shell")
            console.print("To see logs of this build, run")
            console.print(code)
        else:
            console.print("This build was not found or you cannot access it.")
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


def _show_build_progress(ctx, build_instance, tunnel_port=None, tunnel_host=None, tunnel_remote_port=None, no_progress=False):
    from time import sleep
    from rich.syntax import Syntax
    from rich.text import Text
    from appollo.settings import console
    from appollo import api
    from appollo.helpers import handle_error

    build_type = build_instance['build_type']

    console.print(f"{build_instance['name']} has been registered. It has key \"{build_instance['key']}\" "
                  f"and will be started as soon as possible.")
    if build_type == "configuration":
        code = Syntax(code=f"appollo build connect {build_instance['key']}", lexer="shell")
        console.print("To access your Appollo-Remote, you can use the following command when it has been started.")
        console.print(code)
    console.print("Killing the command will not stop the build.")

    if no_progress:
        return False

    # check build progress.
    loop = True
    with console.status("Looking for available instance...", spinner="line") as spinner:
        while loop:
            # update status every 5 seconds.
            sleep(5)
            build_instance = api.get(f"/builds/{build_instance['key']}/")

            status = build_instance["status_code"]
            if status == "created":
                spinner.update("Looking for available instance...")
            elif status == "waiting_instance":
                spinner.update("No instance available at the moment. Waiting for one to be free...")
            elif status == "in_progress":
                substatus = build_instance["substatus_code"]
                if substatus == "starting_instance":
                    spinner.update("Starting instance...")
                elif substatus == "preparing_build":
                    spinner.update("Preparing build...")
                elif substatus == "getting_result":
                    spinner.update("Getting result...")
                elif substatus == "publishing":
                    spinner.update("Publishing...")
                else:
                    spinner.update("Building...")
            elif status == "config":
                spinner.update("Configured for remote access")
                loop = False
            elif status == "succeeded":
                spinner.update("Success!")
                loop = False
            elif status == "failed":
                spinner.update("Failed")
                loop = False
            elif status == "stopped":
                spinner.update("Stopped")
                loop = False

    if status in ["config", "succeeded"]:
        console.print(Text.from_markup(f"\n\nYour build has succeeded, congrats ! Leave us a star on GitHub, we'd greatly appreciate it:"))
        console.print(f"[link]https://github.com/Appollo-CLI/Appollo[/link]\n\n")

        if build_type == "publication":
            console.print("It will appear on your App Store Connect account shortly")
        if build_type == "ad-hoc":
            ipa({build_instance['key']})
        if status == "config":
            ctx.invoke(connect, key=build_instance['key'], tunnel_port=tunnel_port, tunnel_host=tunnel_host, tunnel_remote_port=tunnel_remote_port)
        return True
    elif status in ["failed", "stopped"]:
        if "error_message" in build_instance:
            console.print(Text.from_markup(f"[red]Error: {build_instance['error_message']}[/red]"))
        console.print(Text.from_markup(
            f"Your build has failed, to access logs run : [code]appollo build logs {build_instance['key']}[/code]"))
        handle_error(build_instance['key'])
        return False


@build.command()
@login_required_warning_decorator
@click.argument('app-key', required=False)
@click.argument('directory', type=click.Path(exists=True, resolve_path=True, file_okay=False, dir_okay=True),
                required=False)
@click.option('--build-type', help="Build type",
              type=click.Choice(["configuration", "development", "ad-hoc", "distribution", "validation", "publication"]))
@click.option('--flutter', help="Flutter version for your build (example \"2.8.1\"). Use appollo build flutter-versions to see all available versions",)
@click.option('--minimal-ios-version', help="Minimal iOS version for you application (example \"9.0\")")
@click.option('--app-version', help="App version to set for this build (for example \"1.3.1\"). If not set, the version in pubspec.yaml will be used")
@click.option('--build-number', type=int, help="Build number to set for this build (the number after '+' in the version in pubspec.yaml). If not set, the build number in pubspec.yaml will be used")
@click.option('--mode', type=click.Choice(["release", "profile", "debug"]), help="Mode to build the app in. Defaults to release")
@click.option('--target', help="The main entry-point file of the application. Defaults to lib/main.dart")
@click.option('--flavor', help="Custom app flavor")
@click.option('--tunnel-port', type=int, help="Start a reverse SSH tunnel when the build is started, forwarding to this port. Note: this only applies to configuration builds")
@click.option('--tunnel-host', help="If --tunnel-port is specified, this is the host to forward to (defaults to localhost)")
@click.option('--tunnel-remote-port', type=int, help="If --tunnel-port is specified, this is the port on the VM (defaults to the same port, except for 22 and 5900)")
@click.option('--no-progress', is_flag=True, help="Do not display the progress and exit the command immediately.")
@click.option('--no-flutter-warning', is_flag=True, help="Do not display a warning if no flutter version is specified and the local flutter version does not match the build version.")
@click.pass_context
def start(ctx, build_type, flutter, minimal_ios_version, app_version, build_number, mode, target, flavor, tunnel_port, tunnel_host, tunnel_remote_port, no_progress, no_flutter_warning, app_key=None, directory=None):
    """ Start a new build from scratch

    DIRECTORY : Home directory of the flutter project. If not provided, gets the current directory.

    \f
    The Appollo tool is composed of:

        - *Appollo-Remote* : The pre-configured build machines which handle the setup, build and release of your app
        - *Appollo-cli* : The CLI command line that works as an interface to start Appollo-Remote build machines

    :code:`appollo build start [DIRECTORY] --build-type <build-type>` creates an Appollo-Remote and builds the app
    either for development, ad-hoc, distribution, validation or publication

        * **Configuration**: launch an Appollo-Remote to allow you to configure your project on XCode
        * **Development** : builds the app for testing on an iOS simulator.
        * **Ad-hoc** : Build an .ipa file for testing on the devices listed in your developer account. For the list of
          devices check :code:`appollo apple detail <apple-dev-account-key>`.
        * **Distribution** : Build an .ipa file that can be distributed on any device.
        * **Validation** : Build an .ipa file and validates that it can be released on the App Store.
        * **Publication** : Build an .ipa file and publish it on the App Store. Once this build succeeds you have
          to go on the App Store to complete information and screenshots related to your new application version.

    Killing this command will not stop the build. You can check the progress of all your Appollo-Remotes by running
    :code:`appollo build ls` or get detailed information by running :code:`appollo build detail` and selecting your build.

    To avoid having to specify all the parameters each time, you can create a .appollo file in the directory where the
    command is run. Each parameter is specified on a line in the form PARAM=VALUE. For example:

    .. code-block::

       app-key=123
       flutter=3.0.0
       minimal-ios-version=11.0

    All files and directories in the provided directory will be uploaded, except:

        * build/
        * windows/
        * linux/
        * .dart_tool/
        * .pub-cache/
        * .pub/
        * .git/
        * .gradle/
        * source.zip
        * .app.zip
        * appollo.patch

    You can also specify additional files and directories in a .appolloignore file, with each files and directories
    you want to ignore on separate lines, with directories ending with '/'

    """
    import os
    import textwrap
    import questionary
    from appollo import api
    from appollo.helpers import terminal_menu, zip_directory
    from appollo.settings import console
    from rich.text import Text
    from questionary import Choice

    if directory is None:
        directory = os.getcwd()

    # Check that the command was run for a flutter directory
    if not os.path.exists(os.path.join(directory, "lib")) or not os.path.exists(os.path.join(directory, "pubspec.yaml")):
        res = console.input("This directory does not look like it contains a flutter project. Are you sure you want to upload it? (y/N) ")
        if res not in ["y", "Y"]:
            return

    # Get options from .appollo file
    if os.path.isfile(".appollo"):
        with open(".appollo") as config:
            for i, line in enumerate(config.readlines()):
                split = line.split("=")
                if len(split) != 2:
                    print("Error in .appollo file line "+str(i+1)+": should be KEY=VALUE")
                    continue
                key = split[0].strip()
                if key[0] == "#":  # Ignore commented lines
                    continue
                value = split[1].strip()
                if key == "app-key":
                    if not app_key:
                        app_key = value
                elif key == "build-type":
                    if not build_type:
                        build_type = value
                elif key == "flutter":
                    if not flutter:
                        flutter = value
                elif key == "minimal-ios-version":
                    if not minimal_ios_version:
                        minimal_ios_version = value
                elif key == "app-version":
                    if not app_version:
                        app_version = value
                elif key == "build-number":
                    if not build_number:
                        build_number = int(value)
                elif key == "mode":
                    if not mode:
                        mode = value
                elif key == "target":
                    if not target:
                        target = target
                elif key == "flavor":
                    if not flavor:
                        flavor = flavor
                elif key == "tunnel-port":
                    if not tunnel_port:
                        tunnel_port = int(value)
                elif key == "tunnel-host":
                    if not tunnel_host:
                        tunnel_host = value
                elif key == "tunnel-remote-port":
                    if not tunnel_remote_port:
                        tunnel_remote_port = int(value)
                elif key == "no-progress":
                    if no_progress is None:
                        no_progress = value in ["1", "true", "True"]
                elif key == "no-flutter-warning":
                    if no_flutter_warning is None:
                        no_flutter_warning = value in ["1", "true", "True"]
                else:
                    console.print(f"Warning: unknown option '{key}' in .appollo")

    # Select build type if it was not specified
    if build_type is None:
        build_type = questionary.select(
            "Build type",
            choices=["configuration", "development", "ad-hoc", "distribution", "validation", "publication"],
            qmark="",
        ).ask()
        if build_type is None:  # When ctrl-C, exit
            exit()

    # Select app if it was not specified
    if app_key is None:
        extra_options = []
        if build_type == "configuration":
            extra_options = [{'key': "", 'name': "No application (xcode will not be configured)"}]
        app_key = terminal_menu("/applications/", "Application",
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have no app identifiers in your account. Check out [code]$ appollo app mk [/code] to create an app identifier.
                                        """
                                    )), name=lambda a: a['name']+(f" ({a['key']})" if a['key'] != "" else ""), extra_options=extra_options)
        if app_key is None:
            return
        if app_key == "":
            app_key = None

    if build_type in ["validation", "publication"]:
        permission = api.get(f"/builds/publication-permission/{app_key}")
        if permission["free"]:
            if permission.get("next_build_date"):
                permission['next_build_date'] = permission['next_build_date'][:-3] + permission['next_build_date'][-2:]  # Remove timezone ':' otherwise it can't parse
                next_build_date = datetime.strptime(permission["next_build_date"], "%Y-%m-%dT%H:%M:%S.%f%z").astimezone()
                console.print(f"Error: as a free Appollo user, you can only make one publication every {permission['days_delay']} days. You will be able to make a new build on {next_build_date.strftime('%Y-%m-%d at %H:%M')}")
                console.print("To upgrade your account and make as many publication as you want, please go to https://appollo.space/plans")
                return
            else:
                console.print(f"Warning: as a free Appollo user, you can only make one publication every {permission['days_delay']} days. If this build succeeds, you won't be able to make another publication for {permission['days_delay']} days unless you upgrade.")
                console.print("To upgrade your account and make as many publication as you want, please go to https://appollo.space/plans")
                res = console.input("Do you confirm you want to proceed with the build? (Y/n) ")
                if res not in ["", "y", "Y"]:
                    return

    # Get app version and build number
    if build_type != "configuration" and (not app_version or not build_number) and os.path.exists(os.path.join(directory, "pubspec.yaml")):
        try:
            version, build_num = get_version_and_build(os.path.join(directory, "pubspec.yaml"))
            if not app_version:
                app_version = version
            if not build_number:
                build_number = build_num
        except Exception as e:
            console.stderr("Error getting version and build number from pubspec.yaml: "+str(e))

    # Show warning if the build number has already been used
    if build_type == "publication":
        max_build_number = api.get(f"/applications/{app_key}/buildnumber")
        if max_build_number and build_number <= max_build_number:
            res = console.input(f"You have specified {build_number} as build number but you have already made a publication build with number {max_build_number}. To change it, either supply the --build-number parameter or modify it in pubspec.yaml. Do you want to continue anyway? (y/N) ")
            if res not in ["y", "Y"]:
                return

    # If no flutter version is explicitly specified, check that the local version matches the one of the build so the user doesn't get unexpected errors
    try:
        if not no_flutter_warning and not flutter:
            flutter_version_output = subprocess.run("flutter --version", stdout=subprocess.PIPE, text=True, shell=True)
            if flutter_version_output.returncode == 0:
                match = re.match(r"Flutter ([^\s]+) ", flutter_version_output.stdout)
                if match:
                    local_version = match.group(1)
                    build_version = api.get("/flutter-versions/latest")['version']
                    if local_version.split("-")[0].split(".")[:2] != build_version.split("-")[0].split(".")[:2]:  # Only check major and minor
                        console.print(f"Warning: your local flutter version is {local_version} but the build will be run with the latest flutter version ({build_version}). This could lead to unexpected errors if you have not tested your code with version {build_version}. To avoid this, specify the flutter version you want to use with the --flutter parameter or in a .appollo file.")
                        menu_entry_index = questionary.select(
                            "What do you want to do?",
                            choices=[
                                Choice("Continue anyway", 0),
                                Choice(f"Set the build version to {local_version}", 1),
                                Choice("Cancel and specify the version yourself", 2),
                            ],
                            qmark="",
                        ).ask()
                        if menu_entry_index is None:  # When ctrl-C, exit
                            exit()
                        if menu_entry_index == 2:
                            return
                        if menu_entry_index == 1:
                            flutter = local_version
    except Exception:  # If flutter is not installed or the command fails, ignore it
        pass

    console.print(f"Zipping {directory}")
    excluded_dirs = []
    excluded_files = []
    if os.path.isfile(".appolloignore"):
        with open(".appolloignore") as ignore:
            for line in ignore.readlines():
                line = line.strip()
                if line == "":
                    continue
                if line[-1] == "/":
                    excluded_dirs.append(line[:-1])
                else:
                    excluded_files.append(line)

    zip_file = zip_directory(directory, excluded_dirs, excluded_files)

    file_size_mb = round(os.path.getsize(zip_file)/1000000, 2)

    if file_size_mb > 500:
        console.print("Zipped directory size exceeds 500MB, very large applications are not supported by Appollo. Make sure that all files and directories not needed to build are listed in .appolloignore")
        os.remove(".app.zip")
        return

    # Start build
    console.print(f"Uploading {directory} ({file_size_mb} MB)")
    build_instance = api.post(
        "/builds/",
        json_data={
            "application": app_key,
            "build_type": build_type,
            "min_sdk": minimal_ios_version,
            "flutter_version": flutter,
            "app_version": app_version,
            "build_number": build_number,
            "mode": mode,
            "target": target,
            "flavor": flavor,
        },
        files={
            "source": ("source.zip", open(".app.zip", "rb"), "application/zip")
        },
    )

    os.remove(".app.zip")

    if build_instance:
        _show_build_progress(ctx, build_instance, tunnel_port, tunnel_host, tunnel_remote_port, no_progress)


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def ipa(key):
    """ Get the ipa file of a build.

    \b
    This command is used when a build of type ad-hoc, ipa, validation or publication has succeeded.
    It returns an url to get the IPA, either to download it, or to install it if opened from an iOS device.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", api_params={"all": 1}, name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        response = api.get(f"/builds/{key}/ipa/")

        if response:
            console.print(f"[link={response['url']}]{response['url']}[/link]")
            console.print("Open this url to download the IPA, or use an iOS device to open the url or scan this QR code to install it.")
            print_qrcode(response['url'])
    except api.NotFoundException:
            console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
@click.option(
    "-o", "--output", default="source.zip", help="Output filename (default: source.zip)",
    type=click.Path(exists=False, resolve_path=True, file_okay=True, dir_okay=False))
def download(key, output="source.zip"):
    """ Get the modified source code of a build.

    \b
    This command is used when a build is finished or stopped to retrieve its entire directory on the remote machine.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", api_params={"all": 1}, name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        console.print("Downloading modified sources...")
        response = api.get(f"/builds/{key}/result/", json_decode=False)

        if response:
            console.print("The modified sources have been downloaded and are in source.zip")
            with open(output, "wb") as f:
                f.write(response)
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
@click.option('--tunnel-port', type=int, help="Start a reverse SSH tunnel, forwarding to this port. Note: this only applies to configuration builds")
@click.option('--tunnel-host', help="If --tunnel-port is specified, this is the host to forward to (defaults to localhost)")
@click.option('--tunnel-remote-port', type=int, help="If --tunnel-port is specified, this is the port on the VM (defaults to the same port, except for 22 and 5900)")
@click.option("-y", "--yes", is_flag=True, help="Automatically create an Appollo Remote if your build was not setup for remote desktop", )
@click.pass_context
def connect(ctx, key, tunnel_port, tunnel_host, tunnel_remote_port, yes):
    """ Get the connection information for an Appollo-Remote linked to a build.

    \b
    This command is mainly used when it is needed to connect to the Appollo-Remote with a Remote Desktop client :
        - Xcode configuration
        - Debugging and detailed log analysis
        - Correcting code and restarting a build after failure
        - Testing the application on the iPhone or iPad simulator.

    \f
    This command will start an Appollo-Remote and return connection settings and credentials for you to connect with a
    remote desktop client to the Appollo-Remote.

    .. note:: Appollo-Remotes are active for 30 minutes before being closed automatically.
    .. note:: Appollo-Remotes are MacOS build machines on which the flutter build of your application is executed.
    .. note:: The connection uses the VNC protocol, your Remote Desktop client must support it to allow you to use an Appollo-Remote.
    """
    import textwrap
    from datetime import datetime
    from rich.panel import Panel
    from rich.text import Text

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.syntax import Syntax

    if key is None:
        key = terminal_menu("/builds/", "Builds", name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        build_instance = api.get(f"/builds/{key}/connect/")

        if build_instance:
            if build_instance["remote_desktop_status"] == "no_remote_desktop":
                console.print("This build is either stopped or was not setup for remote desktop.")
                if yes or click.confirm("Do you want to create a new build with the same parameters setup for Remote Desktop access ?", default=False):
                    rebuild_instance = api.post(
                        f"/builds/{key}/rebuild/",
                        json_data={
                            "remote_desktop_enabled": True,
                        })

                    if rebuild_instance:
                        _show_build_progress(ctx, rebuild_instance, tunnel_port, tunnel_host, tunnel_remote_port)

            elif build_instance["remote_desktop_status"] == "remote_desktop_preparation":
                console.print("Your Appollo-Remote is currently prepared for being used as Remote Desktop. Please try again in a few moments.")
            else:
                rustdesk_id = build_instance["rustdesk_id"]
                if len(rustdesk_id) == 9:
                    rustdesk_id = rustdesk_id[0:3]+" "+rustdesk_id[3:6]+" "+rustdesk_id[6:9]
                auth_info = Panel(Text.from_markup(
                    textwrap.dedent(
                        f"""
                            RustDesk relay server: appollo.space
                            RustDesk ID: [bold]{rustdesk_id}[/bold]
                            RustDesk password: [bold]{build_instance["rustdesk_password"]}[/bold]
                            
                            VNC: [bold]vnc://{build_instance["host_ip"]}:{build_instance["remote_desktop_port"]}[/bold]
                            
                            user: [bold]appollo[/bold]
                            password: [bold]{build_instance["password"]}[/bold]
                        """
                    )
                ), title="Connection settings and credentials", expand=False)
                console.print(auth_info)
                build_instance['stop_time'] = build_instance['stop_time'][:-3] + build_instance['stop_time'][-2:]  # Remove timezone ':' otherwise it can't parse
                stop_time = datetime.strptime(build_instance["stop_time"], "%Y-%m-%dT%H:%M:%S.%f%z").astimezone()
                console.print("Your machine will automatically stop at "+stop_time.strftime("%H:%M")+", but remember to stop it as soon as you are finished to free up resources by typing")
                console.print(Syntax(code="appollo build stop "+key, lexer="shell"))
                console.print("")
                console.print("Most Remote Desktop applications link the Mac Command key to the Windows key on your keyboard.")
                if tunnel_port:
                    ctx.invoke(tunnel, key=build_instance['key'], port=tunnel_port, remote_port=tunnel_remote_port, host=tunnel_host)
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
@click.option(
    "-o", "--output", default="appollo.patch", help="Output filename (default: appollo.patch)",
    type=click.Path(exists=False, resolve_path=True, file_okay=True, dir_okay=False))
def patch(key, output="appollo.patch"):
    """ Retrieve a patch that gathers all changes made to the source code of a build.

    \b
    This command is used when a build is finished and succeeded or when you have stopped an Appollo Remote on which you configured an app with XCode.

    .. note:: The patch was made on a blank Git repo.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.syntax import Syntax
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", name=build_name, api_params={"all": 1},
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    console.print(f"Downloading patch file as {output}.")
    try:
        response = api.get(f"/builds/{key}/patch/", json_decode=False)

        if response:
            with open(output, "wb") as f:
                f.write(response)
        else:
            return

        code = Syntax("git apply appollo.patch", lexer="shell")
        console.print("To apply a patch, run")
        console.print(code)
        console.print("If the directory you are in is not the top-level git directory (the one where .git is located) you need to add --directory=<this_directory> to the command")
        console.print("For example if this directory is named flutter_app and is contained in the top-level git directory you need to run")
        console.print(Syntax("git apply --directory=flutter_app appollo.patch", lexer="shell"))
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def stop(key):
    """ Stops a running build"""
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", name=build_name,
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You do not have any running builds.
                                        """
                                    )))
        if key is None:
            return

    try:
        build_instance = api.post(f"/builds/{key}/stop/")
        if build_instance:
            console.print(Text.from_markup(f"[bold]{build_instance['name']}[/bold] has been stopped."))
        else:
            console.print(f"Build with KEY \"{key}\" was not found.")
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def logs(key):
    """ Outputs the logs of a build

    \f
    .. note:: Logs are printed only when a command has finished its execution. In particular, Flutter logs are only printed when the flutter command execution has ended.
    """
    import textwrap

    from appollo import api
    from appollo.helpers import terminal_menu
    from appollo.settings import console
    from rich.text import Text

    if key is None:
        key = terminal_menu("/builds/", "Builds", name=build_name, api_params={"all": 1},
                                    does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                        f"""
                                            You have not run any builds yet.
                                        """
                                    )))
        if key is None:
            return

    try:
        logs = api.get(f"/builds/{key}/logs/")
        console.print(logs)
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")


def build_name(build_instance):
    """ Based on a build instance returns a user friendly name for the build. """
    from datetime import datetime

    if "start_time" in build_instance and build_instance["start_time"]:
        build_instance['start_time'] = build_instance['start_time'][:-3]+build_instance['start_time'][-2:]  # Remove timezone ':' otherwise it can't parse
        start_time = datetime.strptime(build_instance['start_time'], "%Y-%m-%dT%H:%M:%S.%f%z").astimezone()
        start_time_str = start_time.strftime('%Y-%m-%d %H:%M')
    else:
        start_time_str = "Not started"

    return f"{build_instance['application'] if build_instance['application'] else 'No application'} - {build_instance['name']} - {build_instance['build_type']} - {start_time_str} ({build_instance['key']}) - {build_instance['status']}"


@build.command()
@login_required_warning_decorator
def flutter_versions():
    """ Lists the Flutter versions available on Appollo. """
    from appollo import api
    from appollo.settings import console
    from rich.columns import Columns

    versions = api.get("/flutter-versions/")

    if versions:
        columns = Columns(versions["stable"], padding=(0, 3), equal=True, title="Stable channel")
        console.print(columns)
        columns = Columns(versions["beta"], padding=(0, 3), equal=True, title="Beta channel")
        console.print(columns)
        console.print("")
        console.print("Note: the builds run on M1 or M2 macs so only versions starting at flutter 3 are available")


@build.command()
@login_required_warning_decorator
@click.argument('key', required=False)
@click.option('--port', required=True, prompt=True, type=int, help="Port to forward to")
@click.option('--remote-port', required=False, type=int, help="Port on the VM (defaults to the same port, except for 22 and 5900)")
@click.option('--host', required=False, help="Host to forward to (defaults to localhost)")
def tunnel(key, port, remote_port, host):
    """ Create a reverse ssh tunnel between this computer and the VM

    This allows you to access a port of this computer or any host accessible frow this computer, from the VM.

    For example if you have a web server running on port 8000, type the command

    appollo build tunnel --port 8000

    and your web server will be accessible on the VM at localhost:8000, which will enable you to run your app in the simulator while connecting to your local web server.
    """
    import textwrap
    import random

    from rich.text import Text

    from appollo.settings import console
    from appollo.helpers import terminal_menu
    from appollo import api

    if remote_port is None:
        if remote_port not in [22, 5900]:
            remote_port = port
        else:
            remote_port = random.Random().randrange(10000, 65000)
    if host is None:
        host = "localhost"
    if key is None:
        key = terminal_menu("/builds/", "Builds", name=build_name,
                            does_not_exist_msg=Text.from_markup(textwrap.dedent(
                                f"""
                                    You have not run any builds yet.
                                """
                            )))
        if key is None:
            return

    try:
        build_instance = api.get(f"/builds/{key}/connect/")
        if build_instance:
            if build_instance["remote_desktop_status"] == "no_remote_desktop":
                console.print("This build was not setup for remote desktop.")
            elif build_instance["remote_desktop_status"] == "remote_desktop_preparation":
                console.print("Your Appollo-Remote is currently prepared for being used as Remote Desktop. Please try again in a few moments.")
            else:
                ssh_tunnel(build_instance['host_ip'], build_instance['ssh_port'], "appollo", build_instance['password'], remote_port, host, port)
    except api.NotFoundException:
        console.print("This build does not exist or you cannot access it.")
