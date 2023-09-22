import json
import os
import glob

folder_path = "A6_결절_종괴/"
json_files = glob.glob(os.path.join(folder_path, '*.json'))

for json_path in json_files:
    with open(json_path, 'r') as f:
        data = json.load(f)
        raw_data_id = data["metaData"]["Raw data ID"]
        resolution = data["metaData"]["resolution"]
        try:
            box_info = data["labelingInfo"][1]["box"]
            x = box_info["location"][0]["x"]/int(resolution.split("X")[0])
            y = box_info["location"][0]["y"]/int(resolution.split("X")[1])
            width = box_info["location"][0]["width"]/int(resolution.split("X")[0])
            height = box_info["location"][0]["height"]/int(resolution.split("X")[1])
            output_file = os.path.splitext(raw_data_id)[0] + ".txt"
            output_path = os.path.join(folder_path, output_file)
            with open(output_path, "w") as f:
                f.write(f"0 {x} {y} {width} {height}")
            os.remove(json_path)
        except KeyError:
            print(raw_data_id)