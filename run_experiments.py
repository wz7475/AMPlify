import argparse
import os



def process_file(filepath: str, output_filename: str):
    command = f"python src/AMPlify.py -s {filepath} -on {output_filename}"
    print(command)
    os.system(command)

def main(input_dir: str, output_dir: str, suffix_to_process: str) -> None:
    # make output dir
    os.makedirs(output_dir, exist_ok=True)

    # walk input dir
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(suffix_to_process):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_dir, root, file)
                process_file(input_file, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', type=str, required=True)
    parser.add_argument('-o','--output_dir', type=str, required=True)
    parser.add_argument('-s','--suffix_to_process', type=str, required=True)
    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.suffix_to_process)
    print('Done')