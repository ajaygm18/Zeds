#!/usr/bin/env python3
"""
Quick test script to verify BERT model setup and basic functionality
"""
import sys
import os

print("="*60)
print("BERT Sentiment Analysis - Quick Test")
print("="*60)
print()

# Test 1: Check if BERT model files exist
print("Test 1: Checking BERT model files...")
bert_path = "chinese_L-12_H-768_A-12"
required_files = [
    "bert_config.json",
    "vocab.txt",
    "bert_model.ckpt.data-00000-of-00001",
    "bert_model.ckpt.index",
    "bert_model.ckpt.meta"
]

all_exist = True
for file in required_files:
    filepath = os.path.join(bert_path, file)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"  ✓ {file} ({size:,} bytes)")
    else:
        print(f"  ✗ {file} NOT FOUND")
        all_exist = False

if not all_exist:
    print("\n❌ BERT model files are incomplete!")
    sys.exit(1)

print("\n✓ All BERT model files present")
print()

# Test 2: Check TensorFlow import
print("Test 2: Checking TensorFlow...")
try:
    import tensorflow as tf
    print(f"  ✓ TensorFlow version: {tf.__version__}")
except ImportError as e:
    print(f"  ✗ TensorFlow import failed: {e}")
    sys.exit(1)
print()

# Test 3: Check data files
print("Test 3: Checking data files...")
data_files = ["train.tsv", "dev.tsv", "test.tsv"]
for file in data_files:
    filepath = os.path.join("data", file)
    if os.path.exists(filepath):
        lines = sum(1 for _ in open(filepath, encoding='utf-8'))
        print(f"  ✓ {file} ({lines:,} samples)")
    else:
        print(f"  ✗ {file} NOT FOUND")

print()

# Test 4: Load BERT config
print("Test 4: Loading BERT configuration...")
try:
    import json
    with open(os.path.join(bert_path, "bert_config.json"), 'r') as f:
        config = json.load(f)
    print(f"  ✓ Hidden size: {config['hidden_size']}")
    print(f"  ✓ Num layers: {config['num_hidden_layers']}")
    print(f"  ✓ Num attention heads: {config['num_attention_heads']}")
    print(f"  ✓ Vocab size: {config['vocab_size']}")
except Exception as e:
    print(f"  ✗ Failed to load config: {e}")
    sys.exit(1)

print()
print("="*60)
print("✅ All checks passed! BERT model is ready.")
print("="*60)
print()
print("Note: Full training takes several hours. The model is configured with:")
print("  - Max sequence length: 300 tokens")
print("  - Training epochs: 3")
print("  - Batch size: 16")
print("  - Learning rate: 5e-5")
print()
print("To train: bash train.sh")
print("To predict: bash predict.sh (after training)")
print()
