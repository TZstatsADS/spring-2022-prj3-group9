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
In this project, we created two predictive models for image classification for the CIFAR-10 dataset. For Model I, we designed a Convolutional Neural Network (CNN) model based on VGG-Net, with 71% accuracy which is a significant improvement from the baseline logistic regression model (24% accuracy). For Model II, we explored 2 ideas for a weakly supervised learning model. First,  we tried a transfer learning approach using a pre-trained CNN (VGG16) as the base model and mapping the noisy labels to clean labels. Using the cleaned labels we trained model I again, which yielded 72% accuracy. Our final Model II uses Model I trained on clean and augmented data to correct noise labels, then used combined cleaned data to trained the model which yielded 77% accuracy.
	
**Contribution statement**: 
+ Du, Christie: Data augmentation, data processing scripts, image classification research, model1 and model2 development, finetuning, training, and saving, baseline model testing, model idea merging in main.ipynb, model_doc.pdf, presentation
+ Liu, Fucheng: Noisy data research, model 1+2 runtime test on CPU
+ Naik, Vaishak: Noisy data research, transfer learning experimentation (semi-supervised.ipynb), model 2 development and testing, model_doc.pdf 
+ Xia, Yiming: CNN research, baseline model testing, model 1+2 runtime test on free colab GPU, model_doc.pdf, presentation
+ Zeng, Shanyue: CNN, image classification, and noisy data research, model1 development (alternative_model.ipynb), training, testing, and finetuning, model 2 development, model_doc.pdf, presentation

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is organized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
