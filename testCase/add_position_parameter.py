import os
import json
import shutil
import argparse
import cv2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Json add position parameter")
    parser.add_argument(
        "--json-path",
        type=str,
        default="/home/adt/data/data2/jinyan/jingyan/test/test_data/0007-0488-01.json",
        help="path for json file",
    )

    args = parser.parse_args()
    filepath = args.json_path
    if filepath.endswith(".json"):
        print("===>", filepath)
        json_obj = dict()
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            new_shapes = []
            for idx, obj in enumerate(data["shapes"]):
                points = None
                if obj["shape_type"] == "polygon" or obj["shape_type"] == "rectangle":
                    points = obj["points"]
                    points_x_min = min(row[0] for row in points)
                    points_x_max = max(row[0] for row in points)
                    points_y_min = min(row[1] for row in points)
                    points_y_max = max(row[1] for row in points)
                    center_x = (points_x_min + points_x_max) / 2
                    center_y = (points_y_min + points_y_max) / 2
                    obj['position'] = [center_x, center_y]
                    new_shapes.append(obj)
                else:
                    print('only support shape_type polygon and rectangle')
            data["shapes"] = new_shapes
        with open(os.path.join(filepath), 'w') as f:
            json.dump(data, f, indent=2)

            # with open(filepath, "r", encoding="utf-8") as f:
        #     data["shapes"]=new_shapes
        #     im_path=filepath.replace('json','jpg')
        #     image=cv2.imread(im_path)
        #     for idx, obj in enumerate(data["shapes"]):
        #         points = obj["points"]
        #         x = min(row[0] for row in points)
        #         y = min(row[1] for row in points)
        #         x2 = max(row[0] for row in points)
        #         y2 = max(row[1] for row in points)
        #         w = (obj['position'][0]-x)*2
        #         h = (obj['position'][1]-y)*2
        #         cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), (0, 255, 0), 2)
        # cv2.imwrite('test.jpg', image)
