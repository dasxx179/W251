# Homework 6

## BERT Toxicity Classification

In this project, I trained a toxicity classification using BERT on two GPUS: V100 and the P100.

Clearly, as is seen by the training times in the jupyter notebook, the V100 is much faster than the P100. The V100 was approximately 4x faster than the P100. In fact, the V100 trained 2 epochs in half the time it took the P100 to train 1 epoch. Moreover, the V100 also predicted 4x faster than the P100.

Ultimately, when running 2 epochs on the V100 (I did not do both for 12 hours would kill all my IBM credit), it was interesting that the AUC was pretty much the exact same compared to the 1 epoch V100. However, the toxicity statements outputted from the V100 indeed appeared to be much more accurate. This is especially prevalent in the "most toxic" for the 2 epoch V100, for those statements are extremely attacking and verbose.
