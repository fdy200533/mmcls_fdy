_base_ = [
    '../../models/resnet50.py',
    '../../datasets/imagenet_bs64.py',
    # '../../schedules/imagenet_bs32.py',
    '../../default_runtime.py'
]

# optimizer
optimizer = dict(type='SGD', lr=0.025, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# lr_config = dict(policy='step', step=[30, 60, 90])
# runner = dict(type='EpochBasedRunner', max_epochs=100)
lr_config = dict(
    policy='step',
    step=[6, 12, 18],
    warmup='linear',
    warmup_iters=1000,
    warmup_ratio=0.1)
runner = dict(type='EpochBasedRunner', max_epochs=20)

# fp16 settings
fp16 = dict(loss_scale=512.)
