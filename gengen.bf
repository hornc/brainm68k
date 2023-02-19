# Generates bf code to output INPUT
# Where INPUT is either:
# * Plain text
# * An Amiga OS executable

# It's possible some Amiga executables will not be handled fully
# At least the subset consiting of bfc and all its possible outputs
# are handled correctly
# Amiga EXE terminates processing on 0xF2 0x00

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
[
  [-]
  >+<  # test ERROR msg
]

# ERROR: Input != text
>[
+++[++++>---<]>++.+++++++++++++..---.+++.++[--->++<]>++.[-->+<]>+++.++++[->++<]>+.+[--->+<]>.++.+++++.-.[---->+<]>+++.+.--[->++<]>-.+[-->+<]>+.---[->++++<]>.+++[->+++<]>.[--->+<]>+.----.
[-][
  # |Amiga EXE
  ++++++++.[-->+<]>+++.[--->+<]>++.----.--.------.-[->+++<]>.++[->++<]>+.[->+++++<]>-.+[----->+<]>.
]
>++++++++++.
>]

