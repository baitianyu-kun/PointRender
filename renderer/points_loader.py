import numpy as np


def load_points(filename):
    if filename.suffix == '.npy':
        return np.load(filename)
    elif filename.suffix == '.txt':
        return np.loadtxt(filename,delimiter=',')
    else:
        raise NotImplementedError('implement your own points loader')


def get_output_path(POINT_cfgs, suffix='jpg'):
    from pathlib import Path
    POINT_cfgs.output=Path(POINT_cfgs.output)
    if POINT_cfgs.output.is_dir():
        POINT_cfgs.output.mkdir(exist_ok=True, parents=True)
        POINT_cfgs.output /= Path(POINT_cfgs.file).stem
    output = POINT_cfgs.output
    output = output.with_suffix('.' + suffix)
    if output.exists():
        import os
        output = output.with_name(output.stem + '_' + str(int(100 * os.times().elapsed)) + output.suffix)
    return output.__str__()
