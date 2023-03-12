# AIfinity-2023
AIfinity 2023 - Team STEMazon

Submission for the [Aifinity 2023 Hackathon](https://aifinity-2023.devpost.com)

## About the project

In this AI era, people have been discovering more and more potential of AI as an assistant to our daily lives and work. Following this trend, our team (STEMazon) developed [Model.ai](https://devpost.com/software/stemazon-tba), an search-engine-like web application to generate relevant images without background based on user inputs as tags. Utilizing AWS cloud computing services, user input in the search box will be sent to the cloud where requests are sent to the search engine API for images. The iamges are processed at our backend deployed with AWS, and returned and displayed on the user webpages. With this service, our team aim to eliminate the repetitive processes of extracting the subject of the picture from a noisy image. The task that constantly bother designers, artists, marketing employees and all those who have presentation as part of their work. Now with Model.ai, you can choose from 8 options automatically cleaned for you using [U-Squared-Net](https://arxiv.org/pdf/2005.09007.pdf)-based models pretrained on large dataset.

<p align='center'>
<img src='images/ducklogo.png' width=800>
</p>

## Inspiration

Inspired by the impressive, unfathomable features brought about by AWS in running digital systems in many entities, and hence the contribution of promising results, globally, we thought it would be an exciting idea to create an AWS-powered workable application that could realistically enhance the production of physical goods through printing and benefit most individuals in the long run.

## What it does

Check out our demo video which will show you explicitly how our platform works.

## How we built it

We built our platform in the form of a minimum viable product (MVP) using various services provided by AWS, such as API Gateway and Lambda. The frontend is built with VueJS, and the machine learning algorithm is U-2-Net built with PyTorch.

## Challenges we ran into

Given the 48-hour time limit coupled with extreme difficulties faced by our team in compiling our training models using SageMaker under the PyTorch machine learning framework despite our hard-fought efforts, we were unable to implement SageMaker, one of the useful AWS services, in time. We originally planned to utilise SageMaker during the 48 hours allowed to compile and optimise the training models, including for the purpose of optimising our search engine further.

## Accomplishments that we're proud of

We were able to devise and prototype a workable MVP using AWS services during the 48 hours allotted to us.

## What we learned

Teamwork and equitable distribution of workload amongst our four team members based on our strengths helped us brave the tough conditions and fierce competition from over 60 other teams, despite each of our members' commitments in other activities.

## Tech Stack

AWS S3 Cloud Object Storage

AWS Lambda Serverless Computing

AWS SageMaker - the Machine Learning platform

Javascript (Vue.js 3.0 Framework)

Python (Flask Framework)

Python (PyTorch, OpenCV, etc. for ML)

## Screenshots

![Home](images/Home.png)
![Bucket](images/Bucket.png) 

## Get Started

Visit our official [model.ai](http://stemazon-s3.s3-website-ap-southeast-1.amazonaws.com) website, enter the your search text and wait patiently for the images to show up.

## What's next for model.ai

We plan to utilise more AWS services such as SageMaker to devise and implement new and smarter training models and features that enable us to generate more accurate and more optimal image search results based on user inputs. Similarly, we plan to be able to utilise those features that enable and facilitate the generation of 2D and 3D models based on data extracted from single or multiple images selected by users. Furthermore, we intend to partner and collaborate with businesses over the next few years in helping them increase the production of physical goods through our platform. This would in turn enable us to significantly reduce costs of physical goods that consumers need to pay during sales.

## Citation

```
@InProceedings{Qin_2020_PR,
title = {U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection},
author = {Qin, Xuebin and Zhang, Zichen and Huang, Chenyang and Dehghan, Masood and Zaiane, Osmar and Jagersand, Martin},
journal = {Pattern Recognition},
volume = {106},
pages = {107404},
year = {2020}
}
```
