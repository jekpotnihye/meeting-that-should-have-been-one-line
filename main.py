"""The single sentence that could have replaced a pointless meeting.

The email already carried the decision, so the meeting adds nothing
but a re-presentation of it. The sting lands on the final words:
the same yes, only now with slides.

Polish 2: wording tried and rejected — "in person" (flatter than
"with slides", no office artifact), "read aloud" (longer, and it
explains the re-presentation instead of picturing it), "with a deck"
(less instantly understood than "slides"). Kept, unchanged.

Polish 3: read aloud, the line is two beats — decision stated,
then dismissal — with the pause at the semicolon and the sting on
"with slides." No setup, no names, no meeting title is needed; a
stranger reads it cold and pictures the room. Nothing left to trim:
71 characters, well under the 200 cap. Final entry unchanged.
"""

import sys
from pathlib import Path

ENTRY = "The email already said yes; this meeting is just that yes, with slides."


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if len(ENTRY) < 1 or len(ENTRY) > 200:
        raise ValueError(f"entry is {len(ENTRY)} characters; gate allows 1 to 200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(ENTRY.encode("utf-8"))
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
