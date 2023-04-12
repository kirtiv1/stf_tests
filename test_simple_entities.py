import logging

import pytest

logger = logging.getLogger('streamsets.stf_tests')

@pytest.fixture
def simple_job(sch, simple_pipeline, sch_executor_sdc_label):
    """Generates a job using simple_pipeline fixture and cleans up after"""
    job_builder = sch.get_job_builder()
    job = job_builder.build('Simple Job',
                            pipeline=simple_pipeline)
    job.data_collector_labels = sch_executor_sdc_label
    sch.add_job(job)

    try:
        yield job
    finally:
        sch.delete_job(job)


@pytest.fixture
def simple_pipeline(sch, sch_authoring_sdc):
    """A trivial pipeline for use in job tests:
    dev_data_generator >> trash
    """
    pipeline_builder = sch.get_pipeline_builder(engine_type='data_collector', engine_id=sch_authoring_sdc)

    dev_data_generator = pipeline_builder.add_stage('Dev Data Generator')
    trash = pipeline_builder.add_stage('Trash')
    pipeline_builder.add_error_stage('Discard')
    dev_data_generator >> trash
    pipeline = pipeline_builder.build(title='Simple Pipeline')
    sch.publish_pipeline(pipeline)

    try:
        yield pipeline
    finally:
        sch.delete_pipeline(pipeline)

def test_simple_job_lifecycle(sch, simple_job):
    """Create a job with a pipeline like following
    dev_data_generator >> trash
    """
    # Start, stop and delete the job
    sch.start_job(simple_job)
    assert simple_job.status == 'ACTIVE'

    sch.stop_job(simple_job)
    assert simple_job.status == 'INACTIVE'


