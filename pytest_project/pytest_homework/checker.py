import pytest


@pytest.mark.jobs
@pytest.mark.completeness
# test checks that a number of job titles equal 19
def test_number_of_job_titles(connect_to_database):
    connect_to_database.execute('select count(*) from hr.jobs')
    result = connect_to_database.fetchone()
    connect_to_database.close()
    reg_number = result[0]
    assert reg_number == 19


@pytest.mark.jobs
@pytest.mark.validity
# test checks that max salary corresponds to the highest job title
def test_salary_min_max(connect_to_database):
    connect_to_database.execute('select job_title from hr.jobs order by max_salary desc')
    result = connect_to_database.fetchone()
    connect_to_database.close()
    job_with_max_salary = result[0]
    assert job_with_max_salary == 'President'


@pytest.mark.employees
@pytest.mark.consistency
# test checks that salary in hr.employees correspond to salary in hr.jobs
def test_salary_correctness(connect_to_database):
    connect_to_database.execute('with salary_avg (avg_salary, job_id) as (select floor(avg(salary)) as avg_salary, job_id from  hr.employees group by job_id) select avg_salary, j.max_salary, j.min_salary, j.job_id from hr.jobs j join salary_avg on j.job_id = salary_avg.job_id where avg_salary < j.min_salary or avg_salary > j.max_salary')
    result = connect_to_database.fetchone()
    assert result is None


@pytest.mark.employees
@pytest.mark.completeness
# test checks that there is no records without salary data in hr.employees
def test_salary_completeness(connect_to_database):
    connect_to_database.execute('select * from hr.employees where salary is null')
    result = connect_to_database.fetchone()
    connect_to_database.close()
    assert result is None


@pytest.mark.locations
@pytest.mark.completeness
# test checks that there are no locations with empty location_id
def test_location_id(connect_to_database):
    connect_to_database.execute('select * from hr.locations where location_id is null')
    result = connect_to_database.fetchone()
    connect_to_database.close()
    assert result is None


@pytest.mark.locations
@pytest.mark.validity
# test checks that there are no duplicates in location, and all locations correspond to correct city and country_id
def test_location_validity(connect_to_database):
    connect_to_database.execute('select location_id, city, country_id, count(*) from hr.locations group by location_id, city, country_id having count(*) > 1')
    result = connect_to_database.fetchone()
    connect_to_database.close()
    assert result is None
