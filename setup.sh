#!/bin/bash
# Setup script to download BERT pre-trained model and install dependencies

echo "==========================================="
echo "Zeds Project Setup Script"
echo "==========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --quiet --upgrade pip
pip3 install --quiet tensorflow pandas scikit-learn matplotlib numpy keras

if [ $? -eq 0 ]; then
    echo "✓ Python dependencies installed successfully"
else
    echo "✗ Failed to install Python dependencies"
    exit 1
fi
echo ""

# Download BERT model if not exists
BERT_DIR="Codes/sentiment/chinese_L-12_H-768_A-12"
if [ -d "$BERT_DIR" ]; then
    echo "✓ BERT model already exists at $BERT_DIR"
else
    echo "Downloading BERT Chinese pre-trained model (this may take a few minutes)..."
    cd Codes/sentiment
    
    wget --quiet --show-progress https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip -O chinese_model.zip
    
    if [ $? -eq 0 ]; then
        echo "✓ BERT model downloaded successfully"
        echo "Extracting model files..."
        unzip -q chinese_model.zip
        rm chinese_model.zip
        echo "✓ BERT model extracted to $BERT_DIR"
    else
        echo "✗ Failed to download BERT model"
        cd ../..
        exit 1
    fi
    cd ../..
fi
echo ""

# Verify BERT model files
if [ -f "$BERT_DIR/bert_config.json" ] && [ -f "$BERT_DIR/vocab.txt" ] && [ -f "$BERT_DIR/bert_model.ckpt.data-00000-of-00001" ]; then
    echo "✓ BERT model files verified"
else
    echo "✗ BERT model files are incomplete"
    exit 1
fi
echo ""

echo "==========================================="
echo "Setup completed successfully!"
echo "==========================================="
echo ""
echo "You can now:"
echo "  1. Run stock price prediction: cd Codes/stockPrice && python3 prediction.py"
echo "  2. Train sentiment model: cd Codes/sentiment && bash train.sh"
echo "  3. Test sentiment model: cd Codes/sentiment && bash predict.sh"
echo ""
