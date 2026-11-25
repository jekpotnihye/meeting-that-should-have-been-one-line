# BUILD.md — The Meeting That Should Have Been One Line

Competition: `u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c`
($2 total, no entry fee, deadline 26 Nov 2026 20:30 WIB). Gate:
`/output/entry.txt`, UTF-8, 1–200 characters, not only whitespace.
Program: `python3 main.py` writes the entry verbatim to
`/output/entry.txt` and prints the same text verbatim to stdout.

## Judge brief (criterion order — write FOR the brief)

1. Is a single line, one sentence that could have replaced an entire
   pointless meeting, unmistakably office humor. Loses to any
   one-liner that kills a pointless meeting.
2. Kills the meeting outright: after this line, no one could justify
   holding the meeting at all.
3. Feels relatable to anyone who has sat through a useless meeting,
   drawn from real office life.
4. Lands as a joke, with a turn or a sting that makes it funny rather
   than merely true.
5. Stands alone as a single line, needing no context or explanation.
   Twist in the last word(s). Short: the cap is a ceiling. Fresh,
   specific and true beats polished and generic. Never reuse another
   competition's line; this line is written fresh for this brief,
   and it is not the earlier email-meeting line
   ("Nine of us met to discuss the email nobody had read.").

## Candidates (5 drafted, then polished 3x)

1. "The email already said yes; this meeting is just that yes, with slides."
2. "Everyone replied yes to the email, so this meeting is just us saying yes in a room."
3. "The decision is in the email thread; we're only here because nobody wanted to cancel."
4. "It's approved, it's in the email, and the only thing left undecided is why we're still here."
5. "We already agreed by email; this meeting is the encore nobody requested."

## Polish 1 — pick the entry

Candidate 1 wins. It is the only candidate that IS the replacement
sentence itself: it states the decision ("The email already said
yes") and then dismisses the meeting in the same breath
(criterion 1 and 2). The concrete office artifacts — email, slides —
make it instantly recognizable to anyone who has sat through one
(criterion 3), and the sting lands on the last two words, "with
slides": the same yes, only re-presented (criterion 4). It needs no
context (criterion 5). Candidate 2 ends on the flat "in a room".
Candidate 3 explains why the meeting exists instead of killing it.
Candidate 4 is a comment about the meeting, not the sentence that
replaces it, and it spends 94 characters asking a question.
Candidate 5 calls the meeting an "encore", which flatters it.

## Polish 2 — tighten the wording, harden the program

Wording tried and rejected: "in person" (flatter than "with
slides", no office artifact to picture), "read aloud" (longer, and
it explains the re-presentation instead of picturing it), "with a
deck" (less instantly understood than "slides"), dropping "already"
(loses the kill: without it, the email might have arrived after the
meeting was booked). Kept, unchanged:
"The email already said yes; this meeting is just that yes, with slides."
(71 characters). The program already validates the gate (1–200
characters, single line, not blank) before writing, so an invalid
edit cannot ship silently. Entry text unchanged.

## Polish 3 — read-aloud and standalone test

Read aloud, the line is two beats with a pause at the semicolon:
the decision stated, then the dismissal, sting on "with slides."
No setup, no names, no meeting title is needed — a stranger reads
it cold and pictures the room. Nothing left to trim: 71
characters, well under the 200 cap. Final entry unchanged.

Candidate lengths, for the record: candidate 1, 71 characters;
candidate 2, 84; candidate 3, 84; candidate 4, 94; candidate 5, 72.

## Verification

Two runs of `python3 main.py`, stdout byte-identical to
`/output/entry.txt`: entry is 71 characters / 71 bytes, no trailing
newline in either. No rank, win, or score is claimed here.
