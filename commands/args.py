def add_target_argument(parser):
    """
    Asset ID or CSV file path.
    Used by commands that operate on one or many assets.
    """
    parser.add_argument(
        "-target",
        metavar="ASSET_ID",
        help="Asset ID or path to CSV file"
    )


# def add_asset_id_argument(parser):
#     """
#     Single asset ID.
#     """
#     parser.add_argument(
#         "-asset_id",
#         help="Single asset ID"
#     )
