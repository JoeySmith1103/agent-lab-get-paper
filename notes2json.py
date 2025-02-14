import os
import json
import argparse

# python notes2json.py --input-json "research_notes/note_config.json" --output-json "note.json" --note-dir "research_notes"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", "-i", type=str, default="research_notes/note_config.json")
    parser.add_argument("--output-json", "-o", type=str, default="note.json")
    parser.add_argument("--note-dir", type=str, default="research_notes")
    args = parser.parse_args()

    # check validity
    if not os.path.exists(args.input_json):
        raise ValueError("Input json file does not exist.")
    if os.path.exists(args.output_json):
        raise ValueError("Output json file already exists.")
    if not os.path.exists(args.note_dir):
        raise ValueError("Directory does not exist.")

    with open(args.input_json, "r", encoding="utf-8") as f:
        note_config_list = json.load(f)
    
    new_note_config_list = []
    for note_config_dict in note_config_list:
        assert "phases" in note_config_dict and "note_list" in note_config_dict, "Invalid note config dict. (phases and note_list are required.)"
        for idx in range(len(note_config_dict["note_list"])):
            note_path = os.path.join(args.note_dir, note_config_dict["note_list"][idx])
            with open(note_path, "r", encoding="utf-8") as f:
                note_txt = f.read()
            new_note_config_list.append({
                "phases": note_config_dict["phases"],
                "note": note_txt
            })
    
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(new_note_config_list, f, indent=4, ensure_ascii=False)
    print(f"Successfully saved to {args.output_json}")
