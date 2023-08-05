from pathlib import Path
import numpy as np
import rich
import shutil
import argparse
import os
from tqdm import tqdm
import sys
import random
import time
from omegaconf import OmegaConf, DictConfig

# ---------------------------------------------------------------------------------------------
from usls.src.utils import (
    Colors, LOGGER, IMG_FORMAT, VIDEO_FORMAT, CONSOLE
)

from usls.src.info import run_dir_info
from usls.src.labelling import run_inspect
from usls.src.cleanup import run_cleanup
from usls.src.dir_combine import run_dir_combine
from usls.src.spider import run_spider
from usls.src.rename import run_rename
from usls.src.deduplicate import run_deduplicate
from usls.src.video_tools import run_v2is, run_vs2is, run_play 


# TODO
# from usls.src.labelling_det_2 import inspect2
# from usls.src.labelling_cls import classify
from usls.src.label_combine import combine_labels
from usls.src.class_modify import class_modify
# ---------------------------------------------------------------------------------------------





def run(opt: DictConfig):

    task_mapping = {
        'info': run_dir_info,
        'dir_combine': run_dir_combine,
        'dir-combine': run_dir_combine,
        'inspect': run_inspect,
        'clean': run_cleanup,
        'cleanup': run_cleanup,
        'clean-up': run_cleanup,
        'spider': run_spider,
        'rename': run_rename,
        'de-duplicate': run_deduplicate,
        'de_duplicate': run_deduplicate,
        'check': run_deduplicate,
        'v2is': run_v2is,
        'vs2is': run_vs2is,
        'play': run_play,


    }.get(opt.task)(opt)



    exit()

    # # TODO
    # # -------------------------------------
    # #   label combine
    # # -------------------------------------
    # if opt.task == 'label_combine':

    #     assert opt.get('input_dir'), f"No `input_dir=???` args when task is `label_combine`! default: `output_dir=output-label-combine`"
    #     input_dir = opt.input_dir
    #     output_dir = opt.output_dir if opt.get('output_dir') else 'output-label-combine'

    #     combine_labels(input_dir=input_dir, output_dir=output_dir)



    # # -------------------------------------
    # #   class modify
    # # -------------------------------------
    # if opt.task == 'class_modify':
    #     assert opt.get('input_dir'), f"No `input_dir=???` args when task is `class_modify`!"
    #     input_dir = opt.input_dir
        
    #     assert opt.get('to'), f"No `to=???` args when task is `class_modify`!"
    #     to = opt.to

    #     class_modify(
    #         input_dir=input_dir, 
    #         to=to
    #     )

