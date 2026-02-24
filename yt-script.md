# Assignment 4 Demo Transcription

Original Video: https://www.youtube.com/watch?v=FYfkLPk5_8o

## Transcription (Formatted)

Some of the provided examples do not use a class because they are older examples. For Assignment 4, the code should be rewritten into a class structure, while keeping the same functionality shown in the demos.

The demo shows using Pillow to display JPEG images. The instructor notes there is a simpler method for PNG files, but this assignment specifically uses the Pillow approach with JPEG files. The student image files for this assignment are all JPEGs.

The image workflow is: create the main window, create an image variable, open the image, optionally resize it, and cast it to `ImageTk.PhotoImage`. This process is repeated for all four images. The planning table includes the recommended display sizes for each image.

There is one label, placed on an image frame at the top of the GUI. The label is created with the frame as parent, then packed so it becomes visible.

Radio buttons can be created either in a loop or one at a time. The instructor shows both patterns, but emphasizes that creating them individually is also valid. The default radio indicator should be shown (no need to set `indicatoron` explicitly unless changing behavior).

By default, radio buttons stack vertically. For this assignment, they should be packed horizontally using the code in the planning table (for example, `side="left"` and padding between buttons).

For class-based design, all instance variables should use `self`. The assignment should include an `IntVar` to capture the selected radio value, with `set()` and `get()` methods used as needed. The radio buttons should call a method through the `command` parameter.

The demo also suggests starting from a class template file, stripping out unneeded code, then building assignment code incrementally with good indentation and frequent test runs.

## Findings Against Current `asn4.py`

- Class-based design: met.
- Pillow + JPEG image loading: met.
- Four images opened, resized, and cast to `ImageTk.PhotoImage`: met.
- Label on image frame: met.
- Two frames (image + radio button frame): met.
- `IntVar` setup and default value: met (`set(1)`).
- Radio buttons using `variable` + `value` + `command`: met.
- Horizontal radio button layout with padding: met (`side="left", padx=10`).
- Callback uses selected value and swaps image: met.
- Main loop in class app: met.

## Additional Work Needed

- No additional code work is required based on this transcript.
- Possible non-code mark risks to confirm:
  - top-of-file header comment requirement (name/date/course/assignment),
  - exact submission packaging instructions,
  - whether the planning table must be submitted as a separate file.
