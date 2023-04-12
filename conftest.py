import logging

import pytest

logger = logging.getLogger('streamsets.stf_tests')

@pytest.fixture(scope='session')
def sch_authoring_sdc(args):
    """Create a session-scoped fixture to track the authoring SDC.

    Args:
        args (:obj:`dict`): args to pass

    Returns:
        An instance of :obj:`str` containing the ID of the authoring SDC.
    """
    yield args.sch_authoring_sdc


@pytest.fixture
def sch_executor_sdc_label(args):
    """Create a fixture to keep the executor SDC label.
    If tests use these, jobs in those tests will be run using these label.

    Args:
        args (:obj:`dict`): args to pass

    Returns:
        (:obj:`list`): List of SDC labels
    """
    yield args.sch_executor_sdc_label.split(',') if args.sch_executor_sdc_label else []