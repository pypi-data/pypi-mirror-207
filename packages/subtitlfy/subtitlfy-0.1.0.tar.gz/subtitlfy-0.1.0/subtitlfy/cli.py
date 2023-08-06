from argparse import ArgumentParser

from subtitlfy.editor import SubtitlesEditor


def _parse_args():
    parser = ArgumentParser(
        prog="subtitlfy", description="Add subtitles to video.")
    parser.add_argument(
        "--text", "-t",
        type=lambda arg: [[int(start), int(end), text] for start, end, text in (iter.split(',') for iter in arg.split(';'))] \
            if len(arg.split(";")) != 1 else arg,
        help="Text for subtitles."
    )
    parser.add_argument(
        "--substitute", "-s",
        action="store_true",
        help="Force a file to be replaced."
    )
    parser.add_argument(
        "--video", "-v",
        type=str,
        required=True,
        help="Text for subtitles."
    )
    return parser.parse_args()

def main():
    args = _parse_args()
    editor = SubtitlesEditor(args.video)
    if isinstance(args.text, list):
        editor.add_text(args.text)
    elif isinstance(args.text, str):
        editor.add_text([[0, editor.get_duration(), args.text]])
    else:
        raise TypeError("'text' should be either 'int,int,str;int,int,str' or 'str'")
    
    editor.release(substitute=args.substitute)

