# optimizer
optimizer = dict(type='SGD', lr=0.0125, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# lr_config = dict(policy='step', step=[30, 60, 90])
# runner = dict(type='EpochBasedRunner', max_epochs=100)
lr_config = dict(
    policy='step',
    step=[4, 8, 12],
    warmup='linear',
    warmup_iters=40000,
    warmup_ratio=0.01)
runner = dict(type='EpochBasedRunner', max_epochs=13)
