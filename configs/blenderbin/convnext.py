# The new config inherits a base config to highlight the necessary modification
_base_ = '../convnext/mask-rcnn_convnext-t-p4-w7_fpn_amp-ms-crop-3x_coco.py'


# MODEL
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2), mask_head=dict(num_classes=2)))

# TRAINER
max_epochs = 8
train_cfg = dict(max_epochs=max_epochs)
default_hooks = dict(checkpoint=dict(max_keep_ckpts=max_epochs))

# Don't use any fancy schedulers
param_scheduler = []

# DATASET
data_root = 'data/'
data_name = "ic_bin_omc_w/"
metainfo = {
    'classes': ('1','2'),
}

train_dataloader = dict(
    batch_size=2,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file= data_name + 'train_pbr/000000/scene_gt_coco.json',
        data_prefix=dict(img=data_name + 'train_pbr/000000/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=  data_name + 'val/000000/scene_gt_coco.json',
        data_prefix=dict(img= data_name + 'val/000000/')))
test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file= 'ic_bin_test/scene_gt_coco.json',
        data_prefix=dict(img= 'ic_bin_test/')))

val_evaluator = dict(ann_file=data_root + data_name + 'val/000000/scene_gt_coco.json')
test_evaluator = dict(
    ann_file=data_root + 'ic_bin_test/scene_gt_coco.json',
    format_only=False,
    outfile_prefix='results/icbin-test')

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/convnext/mask_rcnn_convnext-t_p4_w7_fpn_fp16_ms-crop_3x_coco/mask_rcnn_convnext-t_p4_w7_fpn_fp16_ms-crop_3x_coco_20220426_154953-050731f4.pth'