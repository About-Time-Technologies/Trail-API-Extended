import logging
from .args import add_target_argument
from utils import get_asset_ids
from trail import Trail

logger = logging.getLogger(__name__)

DELETE_REASONS = [
    "redundant",
]

def handle(args):
    logger.debug("Delete command invoked")

    logger.debug(
        "Options: force=%s permanent=%s reason=%s description=%s",
        args.force,
        args.permanent,
        args.reason,
        args.description,
    )

    # Validation
    if args.reason is None:
            logger.error(
                "Deletion requires --reason. "
                "Valid options are: %s",
                ", ".join(DELETE_REASONS)
            )
            return

    target = args.target
    asset_ids = get_asset_ids(target)

    logger.debug(f"Deleting {asset_ids}")

    trail = Trail()
    trail.loadKey("./.env")

    for asset in asset_ids:
        trail.deleteItem(asset, args.reason, args.description, args.force, args.permanent)
        

def register(subparsers):
    parser = subparsers.add_parser(
        "delete",
        help="Delete one or more assets"
    )

    add_target_argument(parser)

    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Force deletion without confirmation"
    )

    parser.add_argument(
        "--permanent",
        action="store_true",
        default=False,
        help="Permanently delete the asset (cannot be undone)"
    )

    parser.add_argument(
        "--reason",
        choices=DELETE_REASONS,
        help="Reason for deletion"
    )

    parser.add_argument(
        "--description",
        metavar="TEXT",
        help="Additional description (free-form text)"
    )

    parser.set_defaults(handler=handle)
