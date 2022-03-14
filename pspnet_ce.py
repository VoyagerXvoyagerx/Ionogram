norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    type='EncoderDecoder',
    pretrained='open-mmlab://resnet50_v1c',
    backbone=dict(
        type='ResNetV1c',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        dilations=(1, 1, 2, 4),
        strides=(1, 2, 1, 1),
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=False,
        style='pytorch',
        contract_dilation=True),
    decode_head=dict(
        type='PSPHead',
        in_channels=2048,
        in_index=3,
        channels=512,
        pool_scales=(1, 2, 3, 6),
        dropout_ratio=0.1,
        num_classes=7,
        norm_cfg=dict(type='BN', requires_grad=True),
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss',
            use_sigmoid=False,
            loss_weight=1.0,
            class_weight=[0.008, 1.4, 4, 6, 2, 1, 2])),
    auxiliary_head=dict(
        type='FCNHead',
        in_channels=1024,
        in_index=2,
        channels=256,
        num_convs=1,
        concat_input=False,
        dropout_ratio=0.1,
        num_classes=7,
        norm_cfg=dict(type='BN', requires_grad=True),
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss',
            use_sigmoid=False,
            loss_weight=1.0,
            class_weight=[0.008, 1.4, 4, 6, 2, 1, 2])),
    train_cfg=dict(),
    test_cfg=dict(mode='whole'))
dataset_type = 'StandfordBackgroundDataset'
data_root = 'Iono4311'
img_norm_cfg = dict(
    mean=[5.45, 5.45, 5.45], std=[13.12, 13.12, 13.12], to_rgb=False)
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='RandomFlip', flip_ratio=0),
    dict(type='PhotoMetricDistortion'),
    dict(
        type='Normalize',
        mean=[5.45, 5.45, 5.45],
        std=[13.12, 13.12, 13.12],
        to_rgb=False),
    dict(type='Pad', size=(512, 512), pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(360, 400),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(
                type='Normalize',
                mean=[5.45, 5.45, 5.45],
                std=[13.12, 13.12, 13.12],
                to_rgb=False),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ])
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=8,
    train=dict(
        type='StandfordBackgroundDataset',
        data_root='Iono4311',
        img_dir='cimg',
        ann_dir='cmask',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(type='LoadAnnotations'),
            dict(type='RandomFlip', flip_ratio=0),
            dict(type='PhotoMetricDistortion'),
            dict(
                type='Normalize',
                mean=[5.45, 5.45, 5.45],
                std=[13.12, 13.12, 13.12],
                to_rgb=False),
            dict(type='Pad', size=(512, 512), pad_val=0, seg_pad_val=255),
            dict(type='DefaultFormatBundle'),
            dict(type='Collect', keys=['img', 'gt_semantic_seg'])
        ],
        split='splits/train.txt'),
    val=dict(
        type='StandfordBackgroundDataset',
        data_root='Iono4311',
        img_dir='cimg',
        ann_dir='cmask',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                type='MultiScaleFlipAug',
                img_scale=(360, 400),
                flip=False,
                transforms=[
                    dict(type='Resize', keep_ratio=True),
                    dict(type='RandomFlip'),
                    dict(
                        type='Normalize',
                        mean=[5.45, 5.45, 5.45],
                        std=[13.12, 13.12, 13.12],
                        to_rgb=False),
                    dict(type='ImageToTensor', keys=['img']),
                    dict(type='Collect', keys=['img'])
                ])
        ],
        split='splits/val.txt'),
    test=dict(
        type='StandfordBackgroundDataset',
        data_root='Iono4311',
        img_dir='cimg',
        ann_dir='cmask',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                type='MultiScaleFlipAug',
                img_scale=(360, 400),
                flip=False,
                transforms=[
                    dict(type='Resize', keep_ratio=True),
                    dict(type='RandomFlip'),
                    dict(
                        type='Normalize',
                        mean=[5.45, 5.45, 5.45],
                        std=[13.12, 13.12, 13.12],
                        to_rgb=False),
                    dict(type='ImageToTensor', keys=['img']),
                    dict(type='Collect', keys=['img'])
                ])
        ],
        split='splits/val.txt'))
log_config = dict(
    interval=100, hooks=[dict(type='TextLoggerHook', by_epoch=False)])
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
cudnn_benchmark = True
optimizer = dict(type='SGD', lr=1e-05, momentum=0.9, weight_decay=0.0005)
optimizer_config = dict()
lr_config = dict(policy='poly', power=0.9, min_lr=0.0001, by_epoch=False)
runner = dict(type='IterBasedRunner', max_iters=4310)
checkpoint_config = dict(
    by_epoch=False,
    interval=431,
    meta=dict(
        CLASSES=('Background', 'E', 'Es-l', 'Es-c', 'F1', 'F2', 'Spread F'),
        PALETTE=[[230, 230, 230], [250, 165, 30], [120, 69, 125],
                 [53, 125, 34], [0, 11, 123], [130, 20, 12], [120, 121, 80]]))
evaluation = dict(interval=431, metric='mIoU', pre_eval=True)
work_dir = './work_dirs/pspnet2'
seed = 0
gpu_ids = range(0, 1)
