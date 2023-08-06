import socket
from contextlib import closing
import tests.helpers.constants as constants
from geckordp.rdp_client import RDPClient
from geckordp.actors.root import RootActor
from geckordp.actors.descriptors.tab import TabActor
from geckordp.actors.targets.window_global import WindowGlobalActor


def is_port_open(host: str, port: int):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex((host, port)) == 0


def get_client_vars():
    cl = RDPClient(3)
    cl.connect(constants.REMOTE_HOST, constants.REMOTE_PORT)
    root = RootActor(cl)
    current_tab = root.current_tab()
    tab = TabActor(cl, current_tab["actor"])
    descriptors = tab.get_target()
    browser = WindowGlobalActor(cl, descriptors["actor"])
    return cl, root, current_tab, tab, descriptors, browser


def response_valid(actor_id: str, response: dict, allow_null=False) -> bool:
    response_string = str(response).lower()
    return (actor_id in response.get("from", "")
            and "no such actor" not in response_string
            and (allow_null or " is null" not in response_string)
            and "unrecognized" not in response_string)
