---
base_model: G:\llm\model\chatglm3-6b
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: chatglm_sexy_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chatglm_sexy_v1

This model is a fine-tuned version of [G:\llm\model\chatglm3-6b](https://huggingface.co/G:\llm\model\chatglm3-6b) on the sexy_conversations dataset.

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 20.0

### Training results



### Framework versions

- Transformers 4.32.1
- Pytorch 2.1.1+cu121
- Datasets 2.15.0
- Tokenizers 0.13.2
