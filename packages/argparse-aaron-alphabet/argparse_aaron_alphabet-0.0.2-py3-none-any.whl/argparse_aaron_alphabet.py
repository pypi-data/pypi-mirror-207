import argparse

def parser(*args, **kwargs):
    return argparse.ArgumentParser(
        *args,
        **kwargs,
        fromfile_prefix_chars="@",
        allow_abbrev=False,
    )
