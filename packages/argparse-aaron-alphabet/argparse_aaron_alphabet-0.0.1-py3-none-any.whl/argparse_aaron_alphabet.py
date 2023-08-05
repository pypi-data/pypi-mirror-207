import argparse

def parser(*args, **kwargs):
    return ArgumentParser(
        *args,
        **kwargs,
        fromfile_prefix_chars="@",
        allow_abbrev=False,
    )
