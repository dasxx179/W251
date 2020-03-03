# Homework 9: Distributed Training and Neural Machine Translation

We train Nvidia OpenSeq2Seq which is a framework for sequence to sequence tasks such as Automatic Speech Recognition (ASR) and Natural Language Processing (NLP).

## Initialization

2 V100 GPUs were used with 2 TB of storage.  The settings that were used for training are in the `transformer-base.py` file.  

## Important Commands

To train the actual network, the command used was: `nohup mpirun --allow-run-as-root -n 4 -H <vm1 private ip address>:2,<vm2 private ip address>:2 -bind-to none -map-by slot --mca btl_tcp_if_include eth0 -x NCCL_SOCKET_IFNAME=eth0 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH python run.py --config_file=/data/transformer-base.py --use_horovod=True --mode=train_eval &` 

## Questions

1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)

   It took about 22 hours.  

2. Do you think your model is fully trained? How can you tell?

   In the loss images, there is a saturation point where it flattens out.    

3. Were you overfitting?

   There is not an increase on the evaluation loss, which means that there is no overfitting.  

4. Were your GPUs fully utilized?

   All 4 GPUs were used during the process.  

5. Did you monitor network traffic (hint: `apt install nmon `) ? Was network the bottleneck?

   The network traffic was not a bottleneck for upon looking at the network traffic, the network transfer rates were pretty constant around 175 Mbps.  

6. Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?

   The learning rate has a steep slope in the beginning and ramps up and reaches a peak before ultimately settling down in a smooth descending curve afterwards.  I believe this is because initially, the model is extremely untrained and does not understand the training data.  So, it needs to rapidly learn and understand all the unfamiliar data.  However, afterwards, we would want it to slow down so it has time to make correct predictions after its rapid learning.  

7. How big was your training set (mb)? How many training lines did it contain?

   The training dataset was about 695 MB.  

8. What are the files that a TF checkpoint is comprised of?

   There is a data, index, and metadata file.  There are various losses at different checkpoints as well.  

9. How big is your resulting model checkpoint (mb)?

   The checkpoint was about 804 mb.  

10. Remember the definition of a "step". How long did an average step take?

    We did a total of 50000 steps in about 22 hours which is .631 steps/second.  1/.631 is 1.58 is one step takes 1.58 seconds.  

11. How does that correlate with the observed network utilization between nodes?

    The network utilization was constant for our case, but an improvement in network utilization and overall network speed would decrease the training time taken which would ultimately result in a higher steps/second time.  