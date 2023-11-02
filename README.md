# Bangladeshi Native Vehicle Dataset - BNVD

![BNVD Banner](link_to_banner_image)

## Overview
Robust and precise vehicle recognition is crucial to the success of Autonomous Navigation. The development of trustworthy and context-aware autonomous navigation systems adapted to the region’s diverse road conditions and vehicular landscape is significantly hampered by the lack of a comprehensive vehicle detection dataset on a particular region. To advance terrestrial object detection research, this paper proposes a native vehicle detection dataset for the most commonly appeared vehicle classes in Bangladesh. 17 distinct vehicle classes have been taken into account, with fully annotated 72722 instances of 14521 images. Each image width is set to at least 1280px. The dataset’s average vehicle bounding box to image ratio is 5.008. This Bangladesh Native Vehicle Dataset (BNVD) has accounted for several geographical, illumination, and variety of vehicle sizes to be more robust on surprised scenarios Four successive You Only Look Once (YOLO) model models—YOLO v5, v6, v7, and v8—were systematically evaluated in order to analyze BNVD dataset. Among these models, YOLO v7 emerged as the most effective, surpassing all others regarding vehicle detection accuracy.

## Dataset Details
- Total Images: 14,521
- Instances : 72722
- BBox Per Image - 5.008
- Vehicle Categories:
  `1. Bicycle`
  `2. Bus`
  `3. Bhotbhoti`
  `4. Car`
  `5. CNG`
  `6. Easybike`
  `7. Leguna`
  `8. Motorbike`
  `9. MPV`
  `10. Pedestrian`
  `11. Pickup`
  `12. PowerTiller`
  `13. Rickshaw`
  `14. ShoppingVan`
  `15. Truck`
  `16. Van`
  `17. Wheelbarrow`

<div align=center>
<img src="https://github.com/bipin-saha/BNVD-Bangladeshi-Native-Vehicle-Dataset/blob/92f4d7e6c194451fd288ba7eecfdd7de8f7e978d/Graphics/Dataset.jpg"/>
</div>

## Model Testing Results
The dataset has been rigorously tested with YOLO v5-v8 models. The mean Average Precision at 50% Intersection over Union (IoU) is an impressive 84.3%.

## Download
The dataset and related resources can be downloaded from [here](link_to_download_page).

## Checkpoints
Pre-trained model weight files can be found in the "Checkpoints" folder of this repository.

## License
This dataset is released under the [insert license type] license.

## Citation
If you use this dataset in your work, please consider citing:

[Insert citation information here]

## Contributors
We would like to thank the following contributors for their valuable contributions to the development of this dataset.

- Bipin Saha
- Aditya Bhowmik
  

For any queries or concerns, please contact [email address].
