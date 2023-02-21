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
>-<
]
>

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

    # This IS an Amiga EXE (ptr now at 6th cell)
    [
      [-]<[-]<[-]<[-]  # clear cells and move back to 3rd cell
      <+++..---...+++.-<.++>.<.-->
      .......
      ......
      +.---
      <.++>.<.-->>  # 000003F3 magic cookie
      # Generate rest of the Amiga exe and halt on 0xF2 0x00
      <<.>.>  # Check constants

      # All we need to do from here is end on a 0 cell with a 0 to the right
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
