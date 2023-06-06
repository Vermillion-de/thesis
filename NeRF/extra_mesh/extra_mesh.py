import torch
import numpy as np
import trimesh
import mcubes
import configargparse

import polyscope as ps
import plotly.graph_objects as go

from model.nerf import NeRF
from model.embedder import get_embedder
from model.utils import batchify


if torch.cuda.is_available(): 
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
else :
    torch.set_default_tensor_type("torch.float32")

## code borrowed from NeuS
def extract_geometry(bound_min, bound_max, resolution, threshold, query_func):
    print('threshold: {}'.format(threshold))

    ## extract value field
    N = 64
    X = torch.linspace(bound_min[0], bound_max[0], resolution).split(N)
    Y = torch.linspace(bound_min[1], bound_max[1], resolution).split(N)
    Z = torch.linspace(bound_min[2], bound_max[2], resolution).split(N)

    u = np.zeros([resolution, resolution, resolution], dtype=np.float32)
    with torch.no_grad():
        for xi, xs in enumerate(X):
            for yi, ys in enumerate(Y):
                for zi, zs in enumerate(Z):
                    xx, yy, zz = torch.meshgrid(xs, ys, zs)
                    pts = torch.cat([xx.reshape(-1, 1), yy.reshape(-1, 1), zz.reshape(-1, 1)], dim=-1)
                    val = query_func(pts).reshape(len(xs), len(ys), len(zs)).detach().cpu().numpy()
                    u[xi * N: xi * N + len(xs), yi * N: yi * N + len(ys), zi * N: zi * N + len(zs)] = val
    ## came out with marching cubes
    vertices, triangles = mcubes.marching_cubes(u, threshold)
    b_max_np = bound_max.detach().cpu().numpy()
    b_min_np = bound_min.detach().cpu().numpy()
    vertices = vertices / (resolution - 1.0) * (b_max_np - b_min_np)[None, :] + b_min_np[None, :]
    return vertices, triangles

## given points([n_pts, 3]) and NeRF
def network_alpha(input_pts, nerf, embed_fn, embeddirs_fn, netchunk=1024*32):
    embedded_pts  = embed_fn(input_pts)
    embedded_dirs = embeddirs_fn(input_pts) ## yes, view_dir = pts
    embedded = torch.cat([embedded_pts, embedded_dirs], -1)
    outputs_flat = batchify(nerf, netchunk)(embedded)
    return outputs_flat[:,-1]

## visualize data with plotly
def visualize_plotly(vertices, triangles):
    fig = go.Figure(data=[
        go.Mesh3d(
            # 8 vertices of a cube
            x=vertices[:,0],
            y=vertices[:,1],
            z=vertices[:,2],
            colorbar_title='z',
            colorscale=[[0, 'gold'],
                        [0.5, 'mediumturquoise'],
                        [1, 'magenta']],
            # Intensity of each vertex, which will be interpolated and color-coded
            intensity = np.linspace(0, 1, 12, endpoint=True),
            intensitymode='cell',
            # i, j and k give the vertices of triangles
            i = triangles[:,0],
            j = triangles[:,1],
            k = triangles[:,2],
            name='y',
            showscale=True
        )
    ])
    fig.show()

## visualize data with polyscope
def visualize_polyscope(vertices, triangles):
    ps.init()
    ps.register_surface_mesh("Mesh", vertices, triangles)
    ps.show()

def extra_mesh(args):
    ## preparing for loading data
    embed_fn, input_ch = get_embedder(10)
    embeddirs_fn, input_ch_views = get_embedder(4)
    model = NeRF(D=8, W=256,input_ch=input_ch, output_ch=4, skips=[4], input_ch_views=input_ch_views, use_viewdirs=True)
    ckpt = torch.load(args.model)
    model.load_state_dict(ckpt['network_fn_state_dict'])

    ## preparing for marching cubes
    bound_min = torch.tensor(args.bound_min, dtype=torch.float32)
    bound_max = torch.tensor(args.bound_max, dtype=torch.float32)
    print("Marching_cubing")
    vertices, triangles = extract_geometry(bound_min, bound_max, resolution=args.resolution, threshold=0.5, 
                                            query_func=lambda x: network_alpha(x, model, embed_fn, embeddirs_fn))
    print("Marching_cubing Done!")
    mesh = trimesh.Trimesh(vertices, triangles)
    
    if args.save_path != "":
        print("Saving into ", args.save_path)
        mesh.export(args.save_path)
    
    if args.visualize=="plotly":
        visualize_plotly(vertices, triangles)
    elif args.visualize=="polyscope":
        visualize_polyscope(vertices, triangles)
    else:
        pass


def config_parser():
    parser = configargparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="../pretrained/lego_018000.tar", 
                        help="The path to pretrained model" )
    parser.add_argument("--visualize", type=str, default="plotly", 
                        help="The api used for visualization [polyscope, plotly]")
    parser.add_argument("--save_path", type=str, default="", 
                        help="The path of saved mesh.")
    parser.add_argument("---bound_min", default=[-2,-2,-2], type=list,
                        help="The bounding box of min to extract (e.g. --bound_min [-2,-2,-2,])")
    parser.add_argument("---bound_max", default=[+2,+2,+2], type=list,
                        help="The bounding box of max to extract (e.g. --bound_min [+2,+2,+2,])")
    parser.add_argument("--resolution", default=200, type=int,
                        help="The resolution of extrated mesh.")
    return parser

if __name__ == "__main__":
    parser = config_parser()
    args = parser.parse_args()
    extra_mesh(args)