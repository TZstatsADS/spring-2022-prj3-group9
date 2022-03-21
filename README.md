# Project: Weakly supervised learning-- label noise and correction


### [Full Project Description](doc/project3_desc.md)

Term: Spring 2022

+ Team 9
+ Team members
	+ Du, Christie cd3250@columbia.edu 
	+ Liu, Fucheng fl2564@columbia.edu
	+ Naik, Vaishak vvn2107@columbia.edu
	+ Xia, Yiming yx2686@columbia.edu
	+ Zeng, Shanyue sz2896@columbia.edu

+ Project summary: 
In this project, we created two predictive models for image classification. For Model I, we designed a Convolutional Neural Network (CNN) model based on VGG-Net, with accuracy around 60% which improved significantlt compared with the baseline logistic regression model. For model II, we used a pre-trained CNN (VGG16) as the base model for transfer learning, mapping the noisy labels to clean labels. Then we used trained network to get predicted labels from the noisy labels and utilized the predicted labels to train our CNN model in Model I, which yielded 70% accuracy.
	
**Contribution statement**: 
+ Du, Christie:
+ Liu, Fucheng:
+ Naik, Vaishak:
+ Xia, Yiming:
+ Zeng, Shanyue:

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
