import logging
from .args import add_target_argument
from utils import get_asset_ids
from trail import Trail

logger = logging.getLogger(__name__)


def handle(args):
    logger.debug("Change department command invoked")

    logger.debug(
        "Options: department=%s",
        args.department,
    )

    # Validation
    if args.department is None:
        logger.error("Department change requires --department")
        return

    target = args.target
    asset_ids = get_asset_ids(target)

    logger.debug(f"Changing department for {len(asset_ids)} asset(s) to '{args.department}'")

    trail = Trail()
    trail.loadKey("./.env")

    for asset in asset_ids:
        trail.updateItemDepartment(asset, args.department)


def register(subparsers):
    parser = subparsers.add_parser(
        "change-department",
        help="Change the department of one or more assets"
    )

    add_target_argument(parser)

    parser.add_argument(
        "--department",
        metavar="DEPARTMENT_NAME",
        required=True,
        help="Target department name"
    )

    parser.set_defaults(handler=handle)
