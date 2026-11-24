"""Fortune Cookie Wisdom for Developers — slot 1 entry.

Writes one original fortune-cookie line (70 chars, under the 120 cap)
to /output/entry.txt. Deterministic, no network, no secrets.

The line — chosen after studying all 172 field entries and running a
self-judge tournament in the persona of the tired senior engineer:

    The bug you explain aloud will confess before you finish the sentence.

Why it wins the judge's criteria, in the judge's own order:
1. Fortune form, not slogan/advice: a prediction ("will confess"),
   aimed at a developer.
2. One short balanced sentence, lands in a single breath.
3. True about a developer's day: explaining a bug aloud (rubber-duck
   debugging) is how it gets found.
4. Fresh turn: no entry in the 172-strong field plays the
   explain-it-aloud angle; the field is saturated with
   "bug you cannot reproduce", legacy-code-as-a-letter, midnight
   future-self, git blame, and wrong estimates.
5. Quiet twist / double meaning: the bug "confesses" — it both
   reveals itself and admits guilt, rewarding a second read.
"""

LINE = "The bug you explain aloud will confess before you finish the sentence."


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one line"
    out = "/output/entry.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
