from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    assert read_brazilian_file(path)[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
