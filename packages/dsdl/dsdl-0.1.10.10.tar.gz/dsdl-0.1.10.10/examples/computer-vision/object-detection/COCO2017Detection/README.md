# COCO2017 Object Detection Demo

> - demo1: 最简demo: 所有内容均放入一个yaml文件
> - demo2: 过渡demo: 定义definition模板，支持import操作
> - demo3: 最佳demo: Definition模板 + 类别形参，完全将def模板和data实例解耦

## 执行步骤

1. 安装DSDL sdk
```bash
pip install dsdl
```

2. 使用DSDL的parser生成demo中的`coco_val_demo.py`文件
```bash
dsdl parse --yaml examples/computer-vision/object-detection/COCO2017Detection/demo1/coco_val_demo.yaml
dsdl parse --yaml examples/computer-vision/object-detection/COCO2017Detection/demo2/coco_val_demo.yaml -p examples/computer-vision/object-detection/COCO2017Detection/demo2
dsdl parse --yaml examples/computer-vision/object-detection/COCO2017Detection/demo3/coco_val_demo.yaml
or (dsdl parse --yaml examples/computer-vision/object-detection/COCO2017Detection/demo3/coco_val_demo_v2.yaml -p examples/computer-vision/object-detection/COCO2017Detection/demo3)
```

3. 在执行代码之前，需要对文件定位符文件做出一些修改，`examples/computer-vision/object-detection/COCO2017Detection/demo?/config.py`（根据想演示的demo将?替换为1-3具体数字）中，需要修改其中的  

   1. 本地读取：`local`中的参数`working_dir`  

   2. 阿里云OSS读取：`ali_oss`中的参数（阿里云OSS的配置`access_key_secret`, `endpoint`, `access_key_id`；桶名称`bucket_name`，数据在桶中的目录`working_dir`）  

4. 执行命令：

   ```bash
   dsdl view -y <yaml path> -c <config path> -l ali-oss -n 10 -r -v -f Label BBox
   ```

   或：

   ```bash
   dsdl view -y <yaml path> -c <config path> -l ali-oss -n 10 -r -v -t detection
   ```


  每个参数的意义为：

| 参数简写 | 参数全写      | 参数解释                                                     |
| -------- | ------------- | :----------------------------------------------------------- |
| -y       | `--yaml`      | dsdl_yaml文件的路径                                          |
| -c       | `--config`    | 配置文件的路径                                               |
| -l       | `--location`  | 只可以指定为`local`或是`ali-oss`，分别表示读取本地的数据与读取阿里云的数据 |
| -n       | `--num`       | 加载数据集的样本数量                                         |
| -r       | `--random`    | 在加载数据集中的样本时是否随机选取样本，如果不指定的话就按顺序从开始选取样本 |
| -v       | `--visualize` | 是否将加载的数据进行可视化展示                               |
| -f       | `--fields`    | 选择需要进行可视化的字段，如`-f BBox`表示可视化bbox，`-f Label`表示对label进行可视化等等，可以同时选择多个，如`-f Label BBox` |
| -t       | `--task`      | 可以选择当前需要可视化的任务类型，如果选择`-t detection`，则等价于`-f Label BBox Polygon` |
