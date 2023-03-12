# AIfinity-2023
AIfinity 2023 - Team STEMazon

Submission for the [Aifinity 2023 Hackathon](https://aifinity-2023.devpost.com)

## About the project

In this AI era, people have been discovering more and more potential of AI as an assistant to our daily lives and work. Following this trend, our team (STEMazon) developed [model.ai](https://devpost.com/software/stemazon-tba), an search-engine-like web application to generate relevant images without backgrounds based on user inputs as tags. Utilising AWS cloud computing services, user input in the search box will be sent to the cloud where requests are sent to the search engine API for images. The iamges are processed at our backend deployed with AWS, and returned and displayed on the user webpages. With this service, our team aims to eliminate the repetitive processes of extracting the subject of the picture from a noisy image. The task that constantly bother designers, artists, marketing employees and all those who have presentations as part of their work routines. Now with model.ai, you can choose from 8 options automatically cleaned for you using U-Squared-Net-based models pretrained on large datasets.

<p align='center'>
<img src='images/ducklogo.png' width=800>
</p>

## Tech Stack

AWS S3 Cloud Object Storage

AWS Lambda Serverless Computing

AWS SageMaker - the Machine Learning platform

Javascript (Vue.js 3.0 Framework)

Python (Flask Framework)

Python (Pytorch, Opencv, etc. for ML)

## Screenshots

![Home](images/Home.png)
![Bucket](images/Bucket.png) 

## Get Started

Visit our official [model.ai](http://stemazon-s3.s3-website-ap-southeast-1.amazonaws.com) website, enter the your search text and wait patiently for the images to show up.

## Future Prospect

* 2D image to label map generator + label map to 3D model generator = search-engine-like 3D model generator
