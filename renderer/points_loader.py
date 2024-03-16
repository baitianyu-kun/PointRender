import numpy as np
import os
from pathlib import Path
from datetime import datetime

def load_points(filename):
    if filename.suffix == '.npy':
        return np.load(filename)
    elif filename.suffix == '.txt':
        return np.loadtxt(filename,delimiter=',')
    else:
        raise NotImplementedError('implement your own points loader')


def get_output_path_origin(POINT_cfgs, suffix='jpg'):
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


def get_output_path(output_path, file_name,suffix='jpg'):
    datetime_str = datetime.now().strftime('%y%m%d_%H%M%S')
    os.makedirs(output_path,exist_ok=True)
    save_path=Path(os.path.join(output_path,datetime_str+'_'+file_name+'.' + suffix))
    return save_path.__str__()
