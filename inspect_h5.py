import h5py
import os
import sys

# Explicit path to the processed file
target_file = r"F:\_研究生\_研一上\计算感知\data\gen1\reyolo\GEN1_vtei_304_240_50ms_bins_10\images\train\GEN1_train.h5"

print(f"Inspecting file: {target_file}")

if not os.path.exists(target_file):
    print(f"File not found: {target_file}")
    sys.exit(1)

try:
    with h5py.File(target_file, 'r') as f:
        print(f"Root keys: {list(f.keys())}")
        
        for key in f.keys():
            print(f"Key: {key}")
            obj = f[key]
            if isinstance(obj, h5py.Group):
                print(f"  Type: Group")
            elif isinstance(obj, h5py.Dataset):
                print(f"  Type: Dataset | Shape: {obj.shape} | Dtype: {obj.dtype}")
                # Try accessing with integer index
                try:
                    print(f"  Accessing index 0: {obj[0].shape}")
                except Exception as e:
                    print(f"  Failed to access index 0: {e}")

except Exception as e:
    print(f"Error reading file: {e}")