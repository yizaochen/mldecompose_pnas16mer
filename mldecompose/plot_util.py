import matplotlib.gridspec as gridspec
import numpy as np

def get_ylabel_bend_stretch(modeid):
    return r'% in $\lambda_{' + f'{modeid}' +r'}$'

def get_ylabel_twiststretch(modeid1, modeid2):
    return r'% in ($\lambda_{' + f'{modeid1}' +r'}$ - $\lambda_{' + f'{modeid2}' +r'}$)'

def d_data_to_yarray(d_data, key1, key2):
    interaction_list = ['base-stacking', 'backbone', 
                        'ribose', 'base-pairing']
    yarray = np.zeros(4)
    data = d_data[key1][key2]
    for i, key in enumerate(interaction_list):
        yarray[i] = data[key]
    return yarray

def d_data_to_yarray_twiststretch(d_data, key1):
    interaction_list = ['base-stacking', 'backbone', 
                        'ribose', 'base-pairing']
    yarray = np.zeros(4)
    data = d_data[key1]
    for i, key in enumerate(interaction_list):
        yarray[i] = data[key]
    return yarray

def get_d_data_bend_stretch(ml_arr, ml_bdd):
    d_data = {'left': {'top': None, 'middle': None, 'bottom': None}, 
              'right': {'top': None, 'middle': None, 'bottom': None}}
    arr_modeids = [1, 3, 4]
    bdd_modeids = [1, 2, 5]
    key2s = ['top', 'middle', 'bottom']

    # dsRNA
    key1 = 'left'
    for modeid, key2 in zip(arr_modeids, key2s):
        d_data[key1][key2] = ml_arr.get_four_inter_contri_by_mode(modeid)
    # dsDNA
    key1 = 'right'
    for modeid, key2 in zip(bdd_modeids, key2s):
        d_data[key1][key2] = ml_bdd.get_four_inter_contri_by_mode(modeid)
    return d_data


def get_daxes_bend_stretch(fig, hspace, wspace):
    d_axes = {'left': {'top': None, 'middle': None, 'bottom': None}, 
              'right': {'top': None, 'middle': None, 'bottom': None}}
    gs0 = gridspec.GridSpec(3, 2, hspace=hspace, wspace=wspace)

    # dsRNA
    d_axes['left']['top'] = fig.add_subplot(gs0[0,0])
    d_axes['left']['middle'] = fig.add_subplot(gs0[1,0])
    d_axes['left']['bottom'] = fig.add_subplot(gs0[2,0])

    # dsDNA
    d_axes['right']['top'] = fig.add_subplot(gs0[0,1])
    d_axes['right']['middle'] = fig.add_subplot(gs0[1,1])
    d_axes['right']['bottom'] = fig.add_subplot(gs0[2,1])
    return d_axes


def get_d_data_twiststretch_coupling(ml_arr, ml_bdd):
    d_data = {'left': None, 'right': None}
    d_data['left'] = ml_arr.get_diff_two_modes(4, 3)
    d_data['right'] = ml_bdd.get_diff_two_modes(5, 3)
    return d_data

def get_daxes_twiststretch_coupling(fig, hspace, wspace):
    d_axes = {'left': None, 'right': None}
    gs0 = gridspec.GridSpec(1, 2, hspace=hspace, wspace=wspace)
    d_axes['left'] = fig.add_subplot(gs0[0,0])
    d_axes['right'] = fig.add_subplot(gs0[0,1])
    return d_axes