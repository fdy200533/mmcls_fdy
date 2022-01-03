_base_ = [
    '../../models/resnet50.py', '../../datasets/imagenet_bs64.py',
    '../../schedules/imagenet_bs32.py', '../../default_runtime.py'
]

# fp16 settings
fp16 = dict(loss_scale=512.)