import pandas, pytest
from DIL import randomization


@pytest.fixture
def noise_fixture(datas_fixture):
    dataSetting = randomization.Noise(datas_fixture)

    return dataSetting


class TestNoise:
    @pytest.fixture(autouse=True)
    def _noiseInit(self, noise_fixture):
        self._noise = noise_fixture

    def test_dataSetting(self):
        assert type(self._noise.datas) is pandas.DataFrame

    @pytest.mark.parametrize(
        "column, randomRange",
        [
            ("나이", [-9, 9]),
            # ("나이", [-8, 9]),
            # ("나이", [-8, 8]),
            # ("나이", [-7, 8]),
        ],
    )
    def test_add(self, column, randomRange):
        original = self._noise.datas[column].copy()

        self._noise.add(column, randomRange)
        noiseAdd_Value = self._noise.datas[column]
        assert not noiseAdd_Value.equals(original)

    @pytest.mark.parametrize(
        "columns, randomRange",
        [
            (["회원번호", "나이"], [-9, 9]),
            (["회원번호", "나이"], [-8, 9]),
            (["회원번호", "나이"], [-8, 8]),
            (["회원번호", "나이"], [-7, 8]),
        ],
    )
    def test_mulipleAdd(self, columns, randomRange):
        original = self._noise.datas[columns].copy()

        self._noise.multipleAdd(columns, randomRange)
        noiseAdd_Value = self._noise.datas[columns]

        assert not noiseAdd_Value.equals(original)
