---
license: other
base_model: THUDM/chatglm3-6b
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: chatglm_amo_v2_0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chatglm_amo_v2_0

This model is a fine-tuned version of [THUDM/chatglm3-6b](https://huggingface.co/THUDM/chatglm3-6b) on the amo_test_data dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.34.1
- Pytorch 2.1.0+cu118
- Datasets 2.14.7
- Tokenizers 0.14.1
