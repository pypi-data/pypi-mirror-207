from xmltodict import unparse
import argparse
import json
import os
import shutil
from tqdm import tqdm


def base_dict(filename, width, height, depth=3):
    return {
        "annotation": {
            "filename": os.path.split(filename)[-1],
            "folder": "VOCCOCO", "segmented": "0", "owner": {"name": "unknown"},
            "source": {'database': "The COCO 2017 database", 'annotation': "COCO 2017", "image": "unknown"},
            "size": {'width': width, 'height': height, "depth": depth},
            "object": []
        }
    }


BBOX_OFFSET = 0


def base_object(size_info, name, bbox):
    x1, y1, w, h = bbox
    x2, y2 = x1 + w, y1 + h

    width = size_info['width']
    height = size_info['height']

    x1 = max(x1, 0) + BBOX_OFFSET
    y1 = max(y1, 0) + BBOX_OFFSET
    x2 = min(x2, width - 1) + BBOX_OFFSET
    y2 = min(y2, height - 1) + BBOX_OFFSET

    return {
        'name': name, 'pose': 'Unspecified', 'truncated': '0', 'difficult': '0',
        'bndbox': {'xmin': x1, 'ymin': y1, 'xmax': x2, 'ymax': y2}
    }


def json_to_voc(json_file,
                output_folder,
                folder_input_images=None):

    filename = json_file
    print("Parse", filename)
    data = json.load(open(filename))


    cate = {x['id']: x['name']
            for x in data['categories']}

    images = {}
    for im in tqdm(data["images"], "Parse Images"):
        img = base_dict(im['file_name'], im['width'], im['height'], 3)
        images[im["id"]] = img

    for an in tqdm(data["annotations"], "Parse Annotations"):
        ann = base_object(images[an['image_id']]['annotation']
                        ["size"], cate[an['category_id']], an['bbox'])
        images[an['image_id']]['annotation']['object'].append(ann)

    dst_base = output_folder
    dst_dirs = {x: os.path.join(dst_base, x)
                for x in ["Annotations", "ImageSets", "JPEGImages"]}
    dst_dirs['ImageSets'] = os.path.join(dst_dirs['ImageSets'], "Main")
    # for k, d in dst_dirs.items():
    #     os.makedirs(d, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)


    for k, im in tqdm(images.items(), "Write Annotations"):
        im['annotation']['object'] = im['annotation']['object'] or [None]
        # print(im['annotation']['filename'])
        unparse(im,
                open(os.path.join(output_folder,
                                f"{os.path.splitext(im['annotation']['filename'])[0]}.xml"), "w"),
                # open(os.path.join(dst_dirs["Annotations"],
                #         "{}.xml".format(str(k).zfill(12))), "w"),
                full_document=False, pretty=True)

        image_name = im['annotation']['filename']
        if folder_input_images is None:
            src = os.path.join(os.path.dirname(json_file),
                            image_name)
        else:
            src = os.path.join(folder_input_images,
                               image_name)

        dst = os.path.join(output_folder,
                        image_name)
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)
