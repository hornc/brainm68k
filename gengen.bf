# Generates bf code to output INPUT
# Where INPUT is either:
# * Plain text
# * An Amiga OS executable

# It's possible some Amiga executables will not be handled fully
# At least the subset consiting of bfc and all its possible outputs
# are handled correctly
# Amiga EXE mode terminates parsing on (0x03) 0xF2 0x00
# (HUNK_END followed by NULL)

# Setup constants
>-[<+>---]<++++++>  # 91
>--[<+>++++++]   # 43

# Check file format
,

# Probably TEXT
[
  [[<.>-]<+++.---<.>++.--<++.-->>,]
->
]
<

# Possibly Amiga Hunk
+
>>+<<
[
  ,, # get 3rd byte
  ---
  >+<
  [ [-]>-< ]> # Not Amiga EXE Skip next test
  [
    , # Get 4th byte
    -------
    ------
    >+<
    [ [-]>-< ]> # Not an Amiga EXE 0x03 0x??

    # This IS an Amiga EXE
    [ >
      ----[---->+<]>++.++++++++++++.----.--.------.-[-->+<]>.++[->++<]>+.[->+++++<]>-.+[----->+<]>.-[-->+<]>-.
      [-]

    ]

  ]

]

# ERROR: Input != text
>[
+++[++++>---<]>++.+++++++++++++..---.+++.++[--->++<]>++.[-->+<]>+++.++++[->++<]>+.+[--->+<]>.++.+++++.-.[---->+<]>+++.+.--[->++<]>-.+[-->+<]>+.---[->++++<]>.+++[->+++<]>.[--->+<]>+.----.
# |Amiga EXE
++++++++.[-->+<]>+++.[--->+<]>++.----.--.------.-[->+++<]>.++[->++<]>+.[->+++++<]>-.+[----->+<]>.
>++++++++++.
>]
