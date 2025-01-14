# marys-lamb
Building a cute little bot that wins Noisebridgers hearts. And money.

# How to run code


## Dependencies
Install the following (Python) dependencies (will make install file):
- asyncio
- numpy
- cv2
- PCA9685 library 
- redis

## Running on pi

```
python main.py
```

## Running viewer on laptop

```
python ui.py
```

## Glossary of terminology

I made up a few terms, mostly because I'm weird and not very well-read.

- FishBrain : It partitions the input mask into three sections; if the way ahead is clear "enough", it will continue straight. Otherwise, if there's an opening to the side, it will turn there. Otherwise, it'll stop. Coined because, for obstacle avoidance, it is designed to wriggle around like a fish.
- Intermittent accel : Fine-tuning acceleration is hard. Too little acceleration means it can't overcome static friction, but too much means it will go careening into a wall. So I have it so every other call to move will cause the vehicle to just coast. So it accelerates in spurts. I swear I'll calibrate the motors better later.


# TODO

## Metacoding

- have centralized dependency management
- stricter test functionss
- Add everything to global config file

## Vision

- Load model as TFLite
- Get a public storage of a trained model
- Clean up the Jupyter notebook

## Controls

- Adapt FishBrain (planner) to only take bottom half of screen into account
- More thoroughly test the intermittent control system
- Actually have a good acceleration tuning for the motor system so the car moves at constant speed
