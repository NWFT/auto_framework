from common.handler_log import get_logger
import settings


class BaseCase:
    """basic class for test"""
    name = None
    logger = get_logger(__name__, debug=True)
    settings = settings

    @classmethod
    def setup_class(cls):
        cls.logger.info(f"======{cls.name} start======")

    @classmethod
    def teardown_class(cls):
        cls.logger.info(f"======{cls.name} end======")

