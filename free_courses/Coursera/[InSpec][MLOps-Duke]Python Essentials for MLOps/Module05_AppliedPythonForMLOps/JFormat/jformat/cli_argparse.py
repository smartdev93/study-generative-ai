import argparse
import sys
from pathlib import Path

from jformat.core import *

def main():
    parser = argparse.ArgumentParser(
        prog="JFormat",   # This will be shown in usage
        description=(
            "JFormat: Read a JSON file, sort its keys by value, "  # Short explanation displayed under --help
            "and output a well-sorted JSON string."
        )
    )
    
    # Positional: path to the input JSON file
    parser.add_argument(
        "json_file", 
        metavar="JSON_FILE", 
        help="Path to the input JSON file to be sorted."
    )

    """
        ***** OPTIONAL ARGUMENTS *****
        By definition, any argument whose name starts with '-' or '--' is considered optional. We do not have to supply them.
        In case we want to enforce an optional flag, we can pass require=True to add_argument() but argparse still treats it as an "optional-style".
    """
    
    # Optional boolean flag (-r/--reverse) 
    # Cases:
    #   - No fla-r/--reverse: False
    #   - Flag "-r/--reverse": True
    parser.add_argument(
        "-r", "--reverse", 
        action="store_true", # If the flag is present, args.reverse = True. Else: args.reverse = False
        # action="store_false" -> Reverse
        help="Sort by value in descending order (default: ascending)."
        # required=True  Uncomment to enforce this flag.
    )

    # Optional output file (-o/--output)
    # Cases:
    #   - Default: None -> print out
    #   - If given: write to the path
    parser.add_argument(
        "-o", "--output",   # argparse picks the longest option-string to form the dest. In this case: args.reverse
                            # In case we only specify: "-o" then the dest is args.r
        metavar="OUTPUT_FILE", 
        type=str, 
        default=None, 
        help=(  
                "If given, write the sorted JSON to OUTPUT_FILE; "
                "ortherwise print to standard output."
            )
        )

    args = parser.parse_args()
    #print(args)

    try:
        data = load_json_file(args.json_file)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] Invalid JSON format: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Could not read '{args.json_file}': {e}", file=sys.stderr)
        sys.exit(1)
    
    sorted_data = sort_dict_by_value(data=data, reverse=args.reverse)
    sorted_json = rewrite_to_json_file(sorted_data, indent=4)

    if args.output:
        output_path = Path(args.output)
        try:
            with output_path.open("w", encoding="utf-8") as f_out:
                f_out.write(sorted_json)
        except Exception as e:
            print(f"[ERROR] Cannot write to '{output_path}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(sorted_data)



if __name__ == "__main__":
    #main()
    print(sys.path)

"""
To run the JFormat:

python -m jformat.cli [-h] [-r] [-o OUTPUT_FILE] JSON_FILE

Here, the flag '-m' is not a flag of the parser.
In this case, '-m' flags tell Python, "look for a module named jformat.cli, load it as if it were a script,
and run it if __name__ == "__main__"
"""