import logging

import pytest

logger = logging.getLogger('streamsets.stf_tests')

@pytest.fixture
def simple_pipeline(sch, sch_authoring_sdc):
    """A trivial pipeline for use in job tests:
    dev_data_generator >> trash
    """
    logger.info('*************** sch_authoring_sdc')
    logger.info(sch_authoring_sdc is None)
    logger.info(type(sch_authoring_sdc))
    pipeline_builder = sch.get_pipeline_builder(sch_authoring_sdc)

    dev_data_generator = pipeline_builder.add_stage('Dev Data Generator')
    trash = pipeline_builder.add_stage('Trash')
    pipeline_builder.add_error_stage('Discard')
    dev_data_generator >> trash
    pipeline = pipeline_builder.build('test_simple_pipeline')
    sch.publish_pipeline(pipeline)
    yield pipeline


def test_simple_job_lifecycle_with_fixture(sch, simple_pipeline):
    """Create a job using simple_pipeline fixture
    dev_data_generator >> trash
    """
    # Build and add a job
    job_builder = sch.get_job_builder()
    job = job_builder.build(f'test_simple_job_lifecycle',
                            pipeline=simple_pipeline)
    job.data_collector_labels = ['stf-3']
    sch.add_job(job)

    # Start, stop and delete the job
    sch.start_job(job)
    assert job.status == 'ACTIVE'

    sch.stop_job(job)
    assert job.status == 'INACTIVE'

    sch.delete_job(job)


def test_simple_job_lifecycle(sch, sch_authoring_sdc):
    """Create a job with a pipeline like following
    dev_data_generator >> trash
    """
    # Build and publish a pipeline
    pipeline_builder = sch.get_pipeline_builder(sch_authoring_sdc)

    dev_data_generator = pipeline_builder.add_stage('Dev Data Generator')
    trash = pipeline_builder.add_stage('Trash')
    pipeline_builder.add_error_stage('Discard')
    dev_data_generator >> trash
    pipeline = pipeline_builder.build('test_simple_pipeline')
    sch.publish_pipeline(pipeline)

    # Build and add a job
    job_builder = sch.get_job_builder()
    job = job_builder.build('test_simple_job_lifecycle',
                            pipeline=pipeline)
    job.data_collector_labels = ['stf-3']
    sch.add_job(job)

    # Start, stop and delete the job
    sch.start_job(job)
    assert job.status == 'ACTIVE'

    sch.stop_job(job)
    assert job.status == 'INACTIVE'

    sch.delete_job(job)
