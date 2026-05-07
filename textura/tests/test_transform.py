"""Tests for the transform module."""

from textura.transform import (
    upper,
    lower,
    title,
    sentence,
    alternating,
    sort_lines,
    reverse_lines,
    random_lines,
    sort_by_length,
    dedup_lines,
    dedup_words,
    grep_lines,
    grep_v_lines,
    wrap_text,
    unwrap_text,
    extract_column,
    join_lines,
    split_lines,
)


def test_upper():
    assert upper("hello") == "HELLO"
    assert upper("Hello") == "HELLO"


def test_lower():
    assert lower("HELLO") == "hello"
    assert lower("Hello") == "hello"


def test_title():
    assert title("hello world") == "Hello World"
    assert title("hello   world") == "Hello   World"


def test_sentence():
    assert sentence("hello") == "Hello"
    assert sentence("HELLO") == "Hello"
    assert sentence("") == ""
    assert sentence("hello world") == "Hello world"


def test_alternating():
    assert alternating("hello") == "HeLlO"
    assert alternating("hello world") == "HeLlO WoRlD"


def test_sort_lines():
    text = "banana\napple\ncherry"
    assert sort_lines(text) == "apple\nbanana\ncherry"
    assert sort_lines(text, reverse=True) == "cherry\nbanana\napple"


def test_reverse_lines():
    text = "first\nsecond\nthird"
    assert reverse_lines(text) == "third\nsecond\nfirst"


def test_random_lines():
    # We can't test the exact output, but we can test that the lines are the same set.
    text = "a\nb\nc"
    result = random_lines(text)
    lines = set(result.splitlines())
    assert lines == {"a", "b", "c"}


def test_sort_by_length():
    text = "aa\nbbb\nc"
    assert sort_by_length(text) == "c\naa\nbbb"
    assert sort_by_length(text, reverse=True) == "bbb\naa\nc"


def test_dedup_lines():
    text = "apple\nbanana\napple\ncherry"
    assert dedup_lines(text) == "apple\nbanana\ncherry"


def test_dedup_words():
    text = "apple banana apple cherry"
    # Note: our dedup_words splits by whitespace and joins by single space.
    assert dedup_words(text) == "apple banana cherry"


def test_grep_lines():
    text = "apple\nbanana\ncherry"
    assert grep_lines(text, "a") == "apple\nbanana"
    assert grep_lines(text, "^b") == "banana"


def test_grep_v_lines():
    text = "apple\nbanana\ncherry"
    assert grep_v_lines(text, "a") == "banana\ncherry"
    assert grep_v_lines(text, "^b") == "apple\ncherry"


def test_wrap_text():
    text = "This is a long sentence that should be wrapped."
    assert wrap_text(text, width=10) == "This is a\nlong sentence\nthat should\nbe wrapped."


def test_unwrap_text():
    text = "This is a\nlong sentence\nthat should\nbe wrapped."
    # Note: our unwrap joins with space and collapses whitespace.
    assert unwrap_text(text) == "This is a long sentence that should be wrapped."


def test_extract_column():
    text = "a b c\nd e f\ng h i"
    assert extract_column(text, 0) == "a\nd\ng"
    assert extract_column(text, 1) == "b\ne\nh"
    assert extract_column(text, 2) == "c\nf\ni"
    # With delimiter
    text2 = "a,b,c\nd,e,f\ng,h,i"
    assert extract_column(text2, 0, delimiter=",") == "a\nd\ng"


def test_join_lines():
    text = "a\nb\nc"
    assert join_lines(text, "-") == "a-b-c"


def test_split_lines():
    text = "a\nb\nc"
    assert split_lines(text) == ["a", "b", "c"]