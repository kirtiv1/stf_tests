import logging

import pytest

logger = logging.getLogger('streamsets.stf_tests')

@pytest.fixture(scope='session')
def sch(sch_session):
    yield sch_session
