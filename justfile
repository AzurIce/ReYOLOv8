set windows-shell := ["powershell.exe", "-Command"]

convert-data-gen1 SRC DST CAT TBIN='5':
    python singleShot_eventDataHandler_GEN1.py --timeWindow 50 --dataset GEN1 --category {{CAT}} --source {{SRC}} --destination {{DST}} --method vtei --bins {{TBIN}}

test WEIGHT:
    python val.py --data vtei_gen1.yaml --model {{WEIGHT}} --channels 5 --split test --show_sequences 3 --workers 0

train MODEL NAME:
    python train.py --batch 48 --nbs 24 --epochs 100 --data vtei_gen1.yaml  --model {{MODEL}} --channels 5 --hyp default_gen1.yaml --suppress 0.125 --positive 0.25 --zoom_out 0.2 --flip 0.5 --val_epoch 10 --clip_length 5 --clip_stride 5 --name {{NAME}}
