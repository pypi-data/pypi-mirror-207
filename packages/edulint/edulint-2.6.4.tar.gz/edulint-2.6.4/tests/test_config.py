import pytest
from edulint.linters import Linter
from edulint.config.arg import UnprocessedArg, ProcessedArg
from edulint.options import Option, TakesVal, Type, Combine, OptionParse, get_option_parses
from edulint.config.config import Config, extract_args, parse_args, combine_and_translate
from edulint.config.config_translations import get_config_translations, Translation
from edulint.linting.tweakers import get_tweakers
from typing import List, Set, Dict


@pytest.fixture
def all_advertised_options() -> List[Option]:
    return list(get_option_parses().keys())


@pytest.fixture
def advertised_options(all_advertised_options: List[Option]) -> Set[Option]:
    return set(all_advertised_options)


@pytest.fixture
def always_managed_options() -> Set[Option]:
    return set((Option.PYLINT, Option.FLAKE8, Option.IB111_WEEK, Option.NO_FLAKE8))


@pytest.fixture
def managed_translations_options() -> List[Option]:
    return list(get_config_translations().keys())


@pytest.fixture
def managed_tweaker_options() -> List[Set[Option]]:
    return list(tweaker.used_options for tweaker in get_tweakers().values())


@pytest.fixture
def managed_options(
        always_managed_options: Set[Option],
        managed_translations_options: List[Option],
        managed_tweaker_options: List[Set[Option]]
) -> Set[Option]:
    return always_managed_options \
        | set(managed_translations_options) \
        | set(opt for options in managed_tweaker_options for opt in options)


def issubset(subset, superset):
    diff = subset - superset
    assert not diff


def test_no_duplicate_advertised_options(all_advertised_options, advertised_options):
    issubset(set(all_advertised_options), advertised_options)


def test_all_advertised_options_managed(advertised_options: List[Option], managed_options: Set[Option]):
    issubset(advertised_options, managed_options)


def test_all_managed_options_are_advertised(advertised_options: List[Option], managed_options: Set[Option]) -> None:
    issubset(managed_options, advertised_options)


def mock_contents(mocker, contents) -> None:
    mocked_file = mocker.mock_open(read_data=contents)
    mocker.patch("builtins.open", mocked_file)


@pytest.mark.parametrize("contents,args", [
    ("", []),
    ("print(\"Hello world\")", []),
    ("# edulint: xxx", ["xxx"]),
    ("# edulint xxx", []),
    ("# edulint: pylint=xxx", ["pylint=xxx"]),
    ("# edulint: flake8=xxx", ["flake8=xxx"]),
    ("# edulint: xxx yyy", ["xxx", "yyy"]),
    ("# edulint: xxx\n# edulint: xxx", ["xxx", "xxx"]),
    ("# edulint: xxx\n# edulint: yyy", ["xxx", "yyy"]),
    ("# edulint: pylint=xxx\n# edulint: pylint=yyy", ["pylint=xxx", "pylint=yyy"]),
    ("# edulint: xxx\n# edulint: pylint=yyy", ["xxx", "pylint=yyy"]),
    ("# edulint: flake8=xxx\n# edulint: pylint=yyy", ["flake8=xxx", "pylint=yyy"]),
    ("\n\n# edulint: xxx", ["xxx"]),
    ("some code\n # edulint: xxx\ncode mentioning edulint a bit\n# edulint: yyy",
     ["xxx", "yyy"]),
    ("           #        edulint:      xxx        ", ["xxx"]),
    ("           #        edulint:      xxx  yyy      ", ["xxx", "yyy"]),
    ("# edulint: pylint=\"xxx       yyy\"", ["pylint=xxx       yyy"]),
    (
        "# edulint: pylint=xxx yyy zzz flake8=aaa bbb pylint= flake8=\"xxx yyy\" ",
        ["pylint=xxx", "yyy", "zzz", "flake8=aaa", "bbb", "pylint=", "flake8=xxx yyy"]
    ),
    ("# edulint: pylint=--enable=missing-module-docstring", ["pylint=--enable=missing-module-docstring"]),
    ("from ib111 import week_12", ["ib111-week=12"]),
    ("from ib111 import week_02  # noqa", ["ib111-week=02"]),
])
def test_extract_args(mocker, contents, args):
    mock_contents(mocker, contents)
    assert extract_args("foo") == args


@pytest.fixture
def options() -> Dict[Option, OptionParse]:
    return {
        Option.PYTHON_SPECIFIC: OptionParse(Option.PYTHON_SPECIFIC, "", TakesVal.NO, False, Type.BOOL, Combine.REPLACE),
        Option.FLAKE8: OptionParse(Option.FLAKE8, "", TakesVal.YES, [], Type.STR, Combine.APPEND),
        Option.IB111_WEEK: OptionParse(Option.IB111_WEEK, "", TakesVal.YES, None, Type.INT, Combine.REPLACE)
    }


@pytest.mark.parametrize("raw,parsed", [
    (["python-specific"], [UnprocessedArg(Option.PYTHON_SPECIFIC, None)]),
    (["python-spec"], [UnprocessedArg(Option.PYTHON_SPECIFIC, None)]),
    (["flake8=foo"], [UnprocessedArg(Option.FLAKE8, "foo")]),
    (["flake8="], [UnprocessedArg(Option.FLAKE8, "")]),
    (["python-specific", "flake8=foo"], [
        UnprocessedArg(Option.PYTHON_SPECIFIC, None), UnprocessedArg(Option.FLAKE8, "foo")
    ]),
    (["flake8=--enable=xxx"], [UnprocessedArg(Option.FLAKE8, "--enable=xxx")]),
    (["ib111-week=02"], [UnprocessedArg(Option.IB111_WEEK, "02")]),
    (["ib111-week=12", "ib111-week=02"], [
        UnprocessedArg(Option.IB111_WEEK, "12"), UnprocessedArg(Option.IB111_WEEK, "02")
    ]),
])
def test_parse_args(raw: List[str], options: Dict[Option, OptionParse], parsed: List[UnprocessedArg]) -> None:
    assert parse_args(raw, options) == parsed


@pytest.fixture
def config_translations() -> Dict[Option, Translation]:
    return {
        Option.ENHANCEMENT: Translation(
            Linter.PYLINT,
            ["aaa"]
        ),
        Option.PYTHON_SPECIFIC: Translation(
            Linter.PYLINT,
            ["bbb"]
        ),
        Option.ALLOWED_ONECHAR_NAMES: Translation(
            Linter.PYLINT,
            ["ccc"]
        )
    }


@pytest.fixture
def ib111_translations() -> List[Translation]:
    return [
        Translation(Linter.PYLINT, ["iii"]),
        Translation(Linter.PYLINT, ["jjj"]),
        Translation(Linter.PYLINT, ["kkk"]),
    ]


@pytest.mark.parametrize("args,config", [
    (
        [UnprocessedArg(Option.ENHANCEMENT, None)],
        Config([ProcessedArg(Option.ENHANCEMENT, True), ProcessedArg(Option.PYLINT, ["aaa"])])
    ),
    (
        [UnprocessedArg(Option.ENHANCEMENT, None), UnprocessedArg(Option.PYLINT, "zzz")],
        Config([ProcessedArg(Option.ENHANCEMENT, True), ProcessedArg(Option.PYLINT, ["aaa", "zzz"])])
    ),
    (
        [UnprocessedArg(Option.PYLINT, "zzz"), UnprocessedArg(Option.ENHANCEMENT, None)],
        Config([ProcessedArg(Option.PYLINT, ["zzz", "aaa"]), ProcessedArg(Option.ENHANCEMENT, True)])
    ),
    (
        [UnprocessedArg(Option.FLAKE8, "zzz"), UnprocessedArg(Option.ENHANCEMENT, None)],
        Config([
            ProcessedArg(Option.FLAKE8, ["zzz"]),
            ProcessedArg(Option.ENHANCEMENT, True),
            ProcessedArg(Option.PYLINT, ["aaa"])
        ])
    ),
    (
        [UnprocessedArg(Option.ALLOWED_ONECHAR_NAMES, "n")],
        Config([ProcessedArg(Option.ALLOWED_ONECHAR_NAMES, "n"), ProcessedArg(Option.PYLINT, ["ccc"])])
    ),
    (
        [UnprocessedArg(Option.IB111_WEEK, "02")],
        Config([ProcessedArg(Option.IB111_WEEK, 2), ProcessedArg(Option.PYLINT, ["kkk"])])
    ),
    (
        [UnprocessedArg(Option.IB111_WEEK, "12"), UnprocessedArg(Option.IB111_WEEK, "02")],
        Config([ProcessedArg(Option.IB111_WEEK, 2), ProcessedArg(Option.PYLINT, ["kkk"])])
    ),
    (
        [UnprocessedArg(Option.IB111_WEEK, "02"), UnprocessedArg(Option.PYLINT, "aaa")],
        Config([ProcessedArg(Option.IB111_WEEK, 2), ProcessedArg(Option.PYLINT, ["aaa", "kkk"])])
    ),
    (
        [UnprocessedArg(Option.IB111_WEEK, "02"), UnprocessedArg(Option.ENHANCEMENT, None)],
        Config([
            ProcessedArg(Option.IB111_WEEK, 2),
            ProcessedArg(Option.ENHANCEMENT, True),
            ProcessedArg(Option.PYLINT, ["aaa", "kkk"])
        ])
    ),
])
def test_combine_and_translate_translates(
        args: List[UnprocessedArg],
        config_translations: Dict[Option, Translation],
        ib111_translations: List[Translation],
        config: Config) -> None:

    result = combine_and_translate(args, get_option_parses(), config_translations, ib111_translations)
    assert result.config == config.config
