from radicli import Arg
from wasabi import msg

from .. import ty
from ..auth import CLIAuth, get_current_auth
from ..cli import cli
from ..config import SavedSettings, config_dir
from ..errors import CLIError, ProdigyTeamsError
from ..messages import Messages
from ..ui import print_as_json


@cli.command(
    "login",
    no_cluster=Arg("--no-cluster", help=Messages.no_cluster),
)
def login(no_cluster: bool = False) -> None:
    """
    Log in to your Prodigy Teams account. You normally don't need to call this
    manually. It will automatically authenticate when needed.
    """
    auth = get_current_auth()
    auth._ensure_readable_secrets()
    auth.get_id_token(force_refresh=True)
    auth.get_api_token(force_refresh=True)
    if not no_cluster:
        try:
            auth.get_broker_token(force_refresh=True)
        except ProdigyTeamsError as e:
            err = Messages.E116.format(command=f"{cli.prog} login --no-cluster")
            raise CLIError(err, e)
    msg.good(Messages.T012)


@cli.command("info", field=Arg(help=Messages.select_field))
def info(
    field: ty.Optional[ty.Literal["config-dir", "code", "defaults"]] = None
) -> ty.Any:
    """Print information about the CLI"""
    settings = SavedSettings.load()
    info = {
        "config-dir": str(config_dir().absolute()),
        "code": __file__,
        "defaults": settings.to_json(),
    }
    if field:
        print(info[field])
        return info[field]
    else:
        print_as_json(info)
        return info


@cli.command(
    "get-auth-token",
    token_type=Arg(help="The token type"),
)
def get_auth_token(
    token_type: ty.Optional[ty.Literal["api", "cluster", "id"]] = None
) -> CLIAuth:
    """
    Return an auth token. TODO FIXME: this is a temporary hack to allow
    register.py to get a token.
    """
    auth = get_current_auth()
    if token_type == "api":
        print(auth.get_api_token().access_token)
    elif token_type == "cluster":
        print(auth.get_broker_token())
    elif token_type == "id":
        print(auth.get_id_token())
    else:
        raise CLIError(Messages.E117.format(token_type=token_type))
    return auth
