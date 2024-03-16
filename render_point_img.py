import yaml
import argparse
from easydict import EasyDict
from renderer import init_mitsuba
from pathlib import Path
import mitsuba
from renderer.points_loader import get_output_path

def load_config(config_path):
    cfgs = EasyDict(yaml.safe_load(open(config_path)))
    if cfgs.POINT.preview:
        cfgs.RENDERER.sample = 1
        cfgs.RENDERER.max_depth = 2
        cfgs.RENDERER.width=640
        cfgs.RENDERER.height=480
    return cfgs

def main():

    if cfgs.POINT.xml is not None:
        from mitsuba import load_file
        cfgs.POINT.xml=Path(cfgs.POINT.xml)
        print(f"load the scene from: {cfgs.POINT.xml}")
        assert cfgs.POINT.xml.exists()
        scene = load_file(cfgs.POINT.xml.__str__())
    else:
        from renderer.points_loader import load_points
        from renderer.wrapper import build_scene
        cfgs.POINT.file=Path(cfgs.POINT.file)
        print(f"load the scene from: {cfgs.POINT.file}")
        assert cfgs.POINT.file.exists()
        points = load_points(cfgs.POINT.file)

        print(f"point cloud shape: {points.shape}")
        scene = build_scene(points, cfgs)

    img = mitsuba.render(scene)
    file = get_output_path(cfgs.POINT, 'jpg')
    print(f"save to {file}")
    mitsuba.util.write_bitmap(file, img)


if __name__ == '__main__':
    cfgs=load_config('./config.yaml')

    # init Path
    # 
    # 
    # 

    init_mitsuba(cfgs.RENDERER)
    main()
