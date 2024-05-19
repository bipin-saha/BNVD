# Bangladeshi Native Vehicle Dataset - BNVD

## Overview
The success of autonomous navigation relies on robust and precise vehicle recognition, hindered by the scarcity of region-specific vehicle detection datasets, impeding the development of context-aware systems. To advance terrestrial object detection research, this paper proposes a native vehicle detection dataset for the most commonly appeared vehicle classes in Bangladesh. 17 distinct vehicle classes have been taken into account, with fully annotated 81542 instances of 17326 images. Each image width is set to at least 1280px. The dataset’s average vehicle bounding box-to-image ratio is 4.7036. This Bangladesh Native Vehicle Dataset (BNVD) has accounted for several geographical, illumination, variety of vehicle sizes, and orientations to be more robust on surprised scenarios. In the context of examining the BNVD dataset, this work provides a thorough assessment with four successive You Only Look Once (YOLO) models, namely YOLO v5, v6, v7, and v8. These dataset’s effectiveness is methodically evaluated and contrasted with other vehicle datasets already in use. The BNVD dataset exhibits mean average precision(mAP) at 50% intersection over union(IoU) is 0.848 corresponding precision and recall values of 0.841 and 0.774. The research findings indicate a mAP of 0.643 at an IoU range of 0.5 to 0.95. The experiments show that the BNVD dataset serves as a reliable representation of vehicle distribution and presents considerable complexities.

## Dataset Details
- Total Images: 17,326
- Instances: 81,542
- BBox Per Image - 4.7036
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

| Model        | Dataset          | mAP0.5     | mAP 0.5:0.95   | Precision  | Recall     | Weight                                                                                                                                                                   |
| --------     | ---------------- | ---------- | -------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **YOLOv5**   | CARL-D           | 0.437      | 0.328          | 0.633      | 0.423      | |   
|              | DhakaAI          | 0.416      | 0.255          | 0.640      | 0.393      | |
|              | P2 Dhaka         | 0.655      | 0.400          | 0.804      | 0.581      | |
|              | PoribohonBD      | 0.981      | 0.743          | 0.939      | 0.948      | |
|              | **BNVD**         | **0.826**  | **0.609**      | **0.836**  | **0.762**  | [Weight](https://github.com/bipin-saha/BNVD-Bangladeshi-Native-Vehicle-Dataset/blob/52da6457d5a2f9f7dbc9fb6f1754f9c7d7875571/Cheakpoints/YOLO%20V5/weights/best.pt)      |
| **YOLOv6**   | CARL-D           | 0.479      | 0.372          | 0.58       | 0.453      | |
|              | DhakaAI          | 0.420      | 0.262          | 0.311      | 0.548      | |
|              | P2 Dhaka         | 0.775      | 0.494          | 0.762      | 0.71       | |
|              | PoribohonBD      | 0.899      | 0.648          | 0.899      | 0.81       | |
|              | **BNVD**         | **0.837**  | **0.624**      | **0.805**  | **0.76**   | [Weight](https://github.com/bipin-saha/BNVD-Bangladeshi-Native-Vehicle-Dataset/blob/52da6457d5a2f9f7dbc9fb6f1754f9c7d7875571/Cheakpoints/YOLO%20V6/weights/best_ckpt.pt) |
| **YOLOv7**   | CARL-D           | 0.478      | 0.369          | 0.619      | 0.459      | |
|              | DhakaAI          | 0.464      | 0.284          | 0.692      | 0.438      | |
|              | P2 Dhaka         | 0.743      | 0.462          | 0.816      | 0.688      | |
|              | PoribohonBD      | 0.907      | 0.656          | 0.914      | 0.841      | |
|              | **BNVD**         | **0.841**  | **0.623**      | **0.83**  | **0.779**  | [Weight](https://github.com/bipin-saha/BNVD-Bangladeshi-Native-Vehicle-Dataset/blob/52da6457d5a2f9f7dbc9fb6f1754f9c7d7875571/Cheakpoints/YOLO%20V7/weights/best.pt)      |
| **YOLOv8**   | CARL-D           | 0.478      | 0.359          | 0.602      | 0.446      | |
|              | DhakaAI          | 0.435      | 0.276          | 0.694      | 0.446      | |
|              | P2 Dhaka         | 0.69       | 0.449          | 0.798      | 0.604      | | 
|              | PoribohonBD      | 0.889      | 0.658          | 0.898      | 0.823      | |
|              | **BNVD**         | **0.848**  | **0.643**      | **0.841**  | **0.774**  | [Weight](https://github.com/bipin-saha/BNVD-Bangladeshi-Native-Vehicle-Dataset/blob/52da6457d5a2f9f7dbc9fb6f1754f9c7d7875571/Cheakpoints/YOLO%20V8/weights/best.pt)      |

## Download
The dataset and related resources can be downloaded from [here](https://www.kaggle.com/datasets/df94f7d6faf5374ca372cdb7456067ffa7786867578fa6b524d0fe7b5ee43ab6).

## Checkpoints
Pre-trained model weight files can be found in the "Checkpoints" folder of this repository.

## License
This dataset is released under the [insert license type] license.

## Citation
If you use this dataset in your work, please consider citing:

[Insert citation information here]

## Contributors
We would like to thank the following contributors for their valuable contributions to the development of this dataset.

- Bipin Saha (bipinsaha.bd@gmail.com)
- Md. Johirul Islam (johirul@phy.ruet.ac.bd)
- Shaikh Khaled Mostaque* (misha@ru.ac.bd)
- Aditya Bhowmik (bhowmik.aditya0@gmail.com)
- Tapodhir Karmakar Taton (tapodhirtaton@gmail.com)
- Md Nakib Hayat Chowdhury (nakib2025@gmail.com)
- Mamun Ibne Bin Reaz* (mamun.reaz@iub.edu.bd)
  

For any queries or concerns, please contact [bipinsaha.bd@gmail.com, mamun.reaz@iub.edu.bd].
