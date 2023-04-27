# The new config inherits a base config to highlight the necessary modification
_base_ = '../resnet_strikes_back/mask-rcnn_r50-rsb-pre_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2), mask_head=dict(num_classes=2)))

# Modify dataset related settings
data_root = 'data/ic_bin/'
metainfo = {
    'classes': ('1','2'),
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train_pbr/000000/scene_gt_coco.json',
        data_prefix=dict(img='train_pbr/000000/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='val/000000/scene_gt_coco.json',
        data_prefix=dict(img='val/000000/')))
test_dataloader = val_dataloader

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'val/000000/scene_gt_coco.json')
test_evaluator = val_evaluator

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/resnet_strikes_back/mask_rcnn_r50_fpn_rsb-pretrain_1x_coco/mask_rcnn_r50_fpn_rsb-pretrain_1x_coco_20220113_174054-06ce8ba0.pth'
