import numpy as np

from LarpixParser import get_vdrift as GetV
from LarpixParser import event_parser as EvtParser
from LarpixParser import util

def get_pixel_plane_position(packets_arr, geom_dict, run_config):
    # The io_group (pacman) configuration per module is assumed to be the same. Otherwise the larpix layout dictionary should capture the full larpix layout of the multi-module detector. 

    tpc_centers = run_config['tpc_offsets']
    nr_iogroup_module = run_config['nr_iogroup_module']
    
    x, y, z, direction = [], [], [], []
    for packet in packets_arr:
        io_group = packet['io_group']

        module_id = (io_group - 1) // nr_iogroup_module # counting from 0
        io_group = io_group - module_id * nr_iogroup_module
        
        xyz = geom_dict[io_group, packet['io_channel'], packet['chip_id'], packet['channel_id']]
        
        # Note tpc_centers is ordered by z, y, x, as in larnd-sim config files
        x_offset = tpc_centers[module_id][2]*10
        y_offset = tpc_centers[module_id][1]*10
        z_offset = tpc_centers[module_id][0]*10
        
        x.append(xyz[0] + x_offset)
        y.append(xyz[1] + y_offset)
        z.append(xyz[2] + z_offset)
        direction.append(xyz[3])
 
    return x, y, z, direction

def get_t_drift(t0, packets_arr, run_config):

    t = packets_arr['timestamp'].astype(float) * run_config['CLOCK_CYCLE']
    t_drift = t - t0 # us

    return t_drift


def get_hit3D_position_tdrift(t0,  packets, packets_arr, geom_dict, run_config, **kwargs):

    x, y, z_anode, direction = get_pixel_plane_position(packets_arr, geom_dict, run_config)

    if "drift_model" not in kwargs:
        drift_model = run_config['drift_model']
        v_drift = GetV.v_drift(run_config, drift_model)
    else:
        v_drift = GetV.v_drift(run_config, **kwargs)

    t_drift = get_t_drift(t0, packets_arr, run_config)

    z = z_anode + direction * t_drift * v_drift

    return x, y, z, t_drift
