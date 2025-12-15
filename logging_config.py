import logging


def setup_logging(verbose: bool) -> None:
    """
    Configure global logging.
    Call once at program startup.
    """
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

