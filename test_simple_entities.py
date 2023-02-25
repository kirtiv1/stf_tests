import logging

import pytest

logger = logging.getLogger('streamsets.stf_tests')

@pytest.fixture
def simple_pipeline(sch, sch_authoring_sdc):
    """A trivial pipeline for use in job tests:

    dev_data_generator >> trash
    """
    pipeline_builder = sch.get_pipeline_builder(sch_authoring_sdc)

    dev_data_generator = pipeline_builder.add_stage('Dev Data Generator')
    trash = pipeline_builder.add_stage('Trash')
    pipeline_builder.add_error_stage('Discard')
    dev_data_generator >> trash
    pipeline = pipeline_builder.build('test_simple_pipeline')
    sch.publish_pipeline(pipeline)
    yield pipeline


def test_simple_job_lifecycle(sch, simple_pipeline):
    tag_name = f'tag_test_job'
    jobs_with_tag = sch.jobs.get_all(job_tag=tag_name)
    job_count = len(jobs_with_tag)
    logger.debug(f'There are {job_count} jobs for [{sch.username}].')
    job_builder = sch.get_job_builder()
    job = job_builder.build(f'test_simple_job_lifecycle',
                            pipeline=simple_pipeline,
                            tags=[tag_name])
    job.data_collector_labels = ['stf-3']
    sch.add_job(job)
    jobs_with_tag = sch.jobs.get_all(job_tag=tag_name)
    assert any(job_with_tag.job_id == job.job_id for job_with_tag in jobs_with_tag)
    assert len(jobs_with_tag) == job_count + 1

    sch.start_job(job)
    assert job.status == 'ACTIVE'

    sch.stop_job(job)
    assert job.status == 'INACTIVE'

    sch.delete_job(job)
    jobs_with_tag = sch.jobs.get_all(job_tag=tag_name)
    assert not any(job_with_tag.job_id == job.job_id for job_with_tag in jobs_with_tag)
    assert len(jobs_with_tag) == job_count
