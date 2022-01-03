# python tools/train.py \
#     configs/fdy/exps/resnet/resnet50_1xb32_fp16_in1k.py \
#     --work-dir work_dirs/resnet50_1xb32_fp16_in1k \
#     --seed 0 \
#     --deterministic

python tools/train.py \
    configs/fdy/exps/swin_transformer/20220103_swin-tiny_1xb32_in1k.py \
    --work-dir work_dirs/20220103_swin-tiny_1xb32_in1k \
    --seed 0 \
    --deterministic