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
In this project, we created two predictive models for image classification. For Model I, we designed a Convolutional Neural Network (CNN) model based on VGG-Net, with 60% accuracy which improved significantly compared with the baseline logistic regression model. For Model II, we designed a semi-supervised learning model. We used a pre-trained CNN (VGG16) as the base model for transfer learning, mapping the noisy labels to clean labels. Then we used trained network to get predicted labels from the noisy labels and utilized the predicted labels to train our CNN model in Model I, which yielded 70% accuracy. Besides, we trained an Improved Model II using Model I trained on clean and augmented data to correct noise labels, then used combined data to trained the model which yielded 77% accuracy.
	
**Contribution statement**: 
+ Du, Christie: data augmentation, processed data, finetuned model1 and model2, trained and saved model1 and model2, tested baseline, model1 and model2, model merging
+ Liu, Fucheng: research on ways of dealing with noise, trained model 1 on CPU
+ Naik, Vaishak: transfer learning and label cleaning for model 2
+ Xia, Yiming:
+ Zeng, Shanyue: research on classification and noise methods, designed and trained model1 and an improved model, feature engineering, README summary

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
