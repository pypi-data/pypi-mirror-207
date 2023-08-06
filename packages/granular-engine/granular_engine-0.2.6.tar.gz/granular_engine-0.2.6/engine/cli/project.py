import yaml
import click 
import json
import pprint
from InquirerPy.base.control import Choice
from InquirerPy.utils import color_print

from colorama import Fore, Style

from engine.connections import Callisto, Europa, Neso
from engine.libs.inquirer import select, confirm, filepath

from .auth import login 


@click.command()
def projects():
    """List all the project available in GeoEngine

    Examples:

    \b
    $ engine projects
    """
    callisto = Callisto()
    choose_public_private = select(
        message="Which type of projects do you want to see?",
        choices=["Open-Source", "From my organization"],
        qmark="\U0001F310",
        amark="\U0001F310"
    )
    print ()
    org = None
    if choose_public_private == "From my organization":
        if not callisto.user:
            print ("You are not logged in. Please login using " + Fore.CYAN + "engine login" + Style.RESET_ALL)
            return

        orgs = callisto.get_orgs()
        org_choices = [Choice(org, name=org["name"]) for org in orgs]
        org = select(
            message="Please select an organization",
            choices=org_choices,
            qmark="\U0001F3E2",
            amark="\U0001F3E2"
        )
        print ()

    if org:
        europa = Europa(callisto, org["id"])
    else:
        europa = Europa(callisto)
    
    projects = europa.get_projects()
    project_choices = [Choice(project, name=project["name"]) for project in projects]
    project = select(
        message="Please select a project",
        choices=project_choices,
        qmark="\U0001F4C1",
        amark="\U0001F4C1"
    )
    print ()

    show_detail = confirm(
        message=f"Do you want to see {project['name']} details?",
        qmark="\U0001F4C2",
        amark="\U0001F4C2"
       )

    if show_detail:
        if project["description"]:
            print (Fore.GREEN + "Description : " + Style.RESET_ALL, end="")
            print (Fore.GREEN + project['description'] + Style.RESET_ALL)

        if project["sensorIds"]:
            print (Fore.GREEN + "Sensors : " + Style.RESET_ALL, end="")
            if org:
                neso = Neso(callisto, org["id"])
            else:
                neso = Neso(callisto, None)
            sensor_ids = project['sensorIds']
            sensors = neso.get_sensors()
            print (sensors)
            sensor_names = [sensors[sensor_id]["name"] for sensor_id in sensor_ids]
            print (Fore.GREEN + ', '.join(sensor_names) + Style.RESET_ALL)

        if project["problemType"]:
            print (Fore.GREEN + "Problem Type : " + Style.RESET_ALL, end="")
            print (Fore.GREEN + project['problemType'] + Style.RESET_ALL)

        if project["details"]:
            print (Fore.CYAN + project['details'].split('\n')[0] + Style.RESET_ALL)
        
        if project["bibtex"]:
            print (Fore.MAGENTA + project['bibtex'] + Style.RESET_ALL)
    print ()

    show_exports = confirm(
        message=f"Do you want to see {project['name']} exports?",
        qmark="\U0001F6A7",
        amark="\U0001F6A7"
       )
    print ()

    if show_exports:
        if org:
            europa = Europa(callisto, org['id'])
        else:
            europa = Europa(callisto)
        exports = europa.get_project_exports(project["id"])

        choices = []
        for _, export in exports.items():
            if export['status'] == 'completed':
                choice = f"{export['name']} has "
                formats = export['formats']
                if len(formats) > 2:
                    choice += f"{', '.join(formats[:-1])}, and {str(formats[-1])} formats"
                elif len(formats) == 2:
                    choice += f"{' and '.join(formats)} fromats"
                elif len(formats) == 1:
                    choice += f"{formats[0]} format" 
                if export['designated']:
                    choice += f" and is a deisgnated export of {project['name']}"
                choice += "."
                choices.append(Choice(export, name=choice))

        export = select(
            message="Please select an export",
            choices=choices,
            qmark="\U0001F6A7",
            amark="\U0001F6A7"
            )
        print ()

        text = [("#B5B7B4", "Do you want to generate a experiment tracking configuration for ")]
        if org:
            text += [("#3AB222", org['name']), ("#F7F7F7", "'s ")]
        text += [("#B4195D", project['name']),
                ("#B5B7B4", " with "),
                ("#B29822", export['name']),
                ("#B5B7B4", " export?")]
        color_print(text)
        
        if not callisto.user:
            print ()
            print ("You are not logged in. Engine library requires your organization information to generate experiment tracking configuration.")
            print ("Please login using " + Fore.CYAN + "engine login" + Style.RESET_ALL)
            return

        want_config = confirm(message="", qmark="\U0001F913", amark="\U0001F913")
        print ()

        if want_config:
            project_org = None
            orgs = callisto.get_orgs()
            for org in orgs:
                if project["orgId"] == org["id"]:
                    project_org = org
                    break
            if not project_org:
                click.echo("Please visit https://engine.granular.ai to clone the project.")
            else:       
                which_config = select(
                    message="In which format do you want the configuration file?",
                    choices=["YAML", 
                            "JSON", 
                            "Py config file for geo-libs"],
                    qmark="\U0001F4DD",
                    amark="\U0001F4DD"
                )
                print ()

                config = {
                        "description": project["description"].replace('\n', ' ')[:200],
                        "org": project_org["slug"],
                        "exportName": export["name"],
                        "exportId": export["id"],
                        "projectName": project["name"],
                        "projectId": project["id"],
                        "tags": project["tags"]
                        }
                
                save_path = filepath(
                    message="Please enter a path to save the configuration",
                    qmark="\U0001F4E9",
                    amark="\U0001F4E9"
                    )
                if which_config == 'YAML':
                    if '.yaml' not in save_path:
                        save_path += '.yaml'

                    with open(save_path, 'w') as fout:
                        yaml.dump(config, fout)
                        print ("Saved to " + Fore.GREEN + save_path + Style.RESET_ALL)
                elif which_config == 'JSON':
                    if '.json' not in save_path:
                        save_path += '.json'
                    
                    with open(save_path, 'w') as fout:
                        json.dump(config, fout, indent=4)
                        print ("Saved to " + Fore.GREEN + save_path + Style.RESET_ALL)  
                else:
                    if '.py' not in save_path:
                        save_path += '.py'
                    
                    with open(save_path, 'w') as fout:
                        pp = pprint.PrettyPrinter(indent=4, width=200, compact=True)
                        fout.write(f"engine = {pp.pformat(config)}")
                        print ("Saved to " + Fore.GREEN + save_path + Style.RESET_ALL)

                print ()
    return