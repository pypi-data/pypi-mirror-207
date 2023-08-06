import argparse
from utils.segment import segment_any_rape

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="测试脚本")
    parser.add_argument("--input_path", type=str, help="输入文件夹路径")
    parser.add_argument("--model_path", type=str, help="预训练模型路径")
    parser.add_argument("--batch_size", type=int, help="批次大小")
    parser.add_argument("--num_workers", type=int, default=8, help="CPU核心数")
    parser.add_argument("--stride", type=int, default=64, help="滑动窗口大小")
    parser.add_argument("--numclass", type=int, default=2, help="分割类别")

    args = parser.parse_args()

    segment_any_rape(args)
