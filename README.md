# Body Movement Comparison with Mediapipe

This is an AI that gives real-time feedback to the user of how they're performing a body movement (like, workout, dance, etc) against a benchmark video. 

You can give the benchmark video as a pre-saved file, and the user video as either a pre-saved file or with the webcam feed.

Its built using [mediapipe](https://github.com/google/mediapipe) in the backend, so we get a pretty high FPS (around 15 on MacBook Pro 16) when running on CPU only, as opposed to 2-3 FPS when the same application was built with [tf-pose-estimation](https://github.com/ZheC/tf-pose-estimation).

## Usage on stand alone app on local machine

```
- Install PyCharm Community Edition or some other Python installation
- Once installed, execute the following command from within the pose-comparison directory
  - python MrPose.py
```
