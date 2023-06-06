import argparse
import json
import os
import shutil
from datetime import datetime
from pathlib import Path
import sys
from tqdm import tqdm

def sort_files(source_dir, target_dir, write):
    # Získání souborů
    files = list(Path(source_dir).rglob("*.json"))
    total_files = len(files)
    processed_files = 0

    print(f"Processing {total_files} files.")
    for file_path in tqdm(files, f"Processing files..."):
        try:
            # Načtení obsahu souboru
            with open(file_path, "r") as file:
                data = file.read()

            # Parsování JSON dat
            json_data = json.loads(data)

            # Extrahování atributů
            count = json_data.get("count")
            date = json_data.get("date")
            text = json_data.get("text")

            # Získání roku a týdne z data
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            year = date_obj.year
            week = date_obj.strftime("%U")

            # Vytvoření cílového adresáře
            target_year_dir = os.path.join(target_dir, str(year))
            target_week_dir = os.path.join(target_year_dir, f"W{week}")

            os.makedirs(target_week_dir, exist_ok=True)

            # Přejmenování souboru
            new_filename = f"{date[5:]}_{count}.json"
            new_file_path = os.path.join(target_week_dir, new_filename)

            # Přemístění souboru
            if write:
                shutil.move(file_path, new_file_path)

            # Výpis informací
            path_json = json.dumps({"source": str(file_path), "target": new_file_path}, ensure_ascii=False)
            print(path_json)
            processed_files += 1

        except Exception as e:
            # Výpis chyby
            print(f"Error: {str(e)}", file=sys.stderr)

    print(f"Success: processed {processed_files}/{total_files} files.")

def get_input_directory(args):
    input_directory = None

    # Zkontrolování, zda byl argument --input zadán
    if args.input:
        input_directory = args.input
    else:
        # Kontrola, zda je nastavena proměnná prostředí SOURCE_DIRECTORY
        if "SOURCE_DIRECTORY" in os.environ:
            input_directory = os.environ["SOURCE_DIRECTORY"]
        else:
            # Použití aktuálního adresáře
            input_directory = os.getcwd()

    return input_directory

def get_output_directory(args):
    output_directory = None

    # Zkontrolování, zda byl argument --output zadán
    if args.output:
        output_directory = args.output
    else:
        # Kontrola, zda je nastavena proměnná prostředí TARGET_DIRECTORY
        if "TARGET_DIRECTORY" in os.environ:
            output_directory = os.environ["TARGET_DIRECTORY"]
        else:
            # Použití aktuálního adresáře
            output_directory = os.getcwd()

    return output_directory

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", "-i", help="Input directory path")
    parser.add_argument("--output", "-o", help="Output directory path")
    parser.add_argument("--write", "-w", action="store_true", help="Write files (disable dry run)")
    parser.add_argument("--version", "-v", action="version", version="1.0.0")

    args = parser.parse_args()

    # Kontrola módu "dry run" nebo "write"
    if args.write:
        print("Program běží v módu WRITE - provede skutečné změny.")
    else:
        print("Program běží v módu DRY RUN - jen vypisuje změny, ale neprovádí je.")

    input_directory = get_input_directory(args)
    output_directory = get_output_directory(args)

    print(f"Processing files in directory: {input_directory}...")
    sort_files(input_directory, output_directory, args.write)

    print(f"Success: processed all files.")


if __name__ == "__main__":
    main()
