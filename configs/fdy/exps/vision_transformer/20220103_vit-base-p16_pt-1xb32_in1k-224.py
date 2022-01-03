_base_ = [
    '../../models/vit-base-p16.py',
    '../../datasets/imagenet_bs32_pil_resize_autoaug.py',
    # '../../schedules/imagenet_bs4096_AdamW.py',
    '../../default_runtime.py'
]

# specific to vit pretrain
paramwise_cfg = dict(custom_keys={
    '.cls_token': dict(decay_mult=0.0),
    '.pos_embed': dict(decay_mult=0.0)
})

model = dict(
    head=dict(hidden_dim=3072),
    train_cfg=dict(
        augments=dict(type='BatchMixup', alpha=0.2, num_classes=1000,
                      prob=1.)))

# optimizer
optimizer = dict(
    type='AdamW',
    lr=0.003,
    weight_decay=0.3,
    paramwise_cfg=paramwise_cfg,
)
optimizer_config = dict(grad_clip=dict(max_norm=1.0))

# learning policy
lr_config = dict(
    policy='CosineAnnealing',
    min_lr=0,
    warmup='linear',
    warmup_iters=10000,
    warmup_ratio=1e-4,
)
runner = dict(type='EpochBasedRunner', max_epochs=300)
