# CV-Hardware-co-design-for-industries

## Phase1：Porting YOLOv5 model to FPGA and optimizing
The YOLO (You Only Look Once) algorithm serves as a representative of single-stage object detection methods, known for its high speed but relatively lower precision. This approach integrates the process of generating candidate boxes with the actual object detection, making it well-suited for real-time detection tasks. YOLOv5, by employing a lightweight network structure and optimized algorithms, further enhances detection performance and efficiency. While the YOLO series exhibits outstanding performance, its substantial parameter count and computational complexity necessitate more powerful image processors for deployment.

In recent years, with the rapid development of edge computing and intelligent terminals, there is widespread attention towards deploying artificial intelligence models on embedded devices. In the context of this project, which focuses on the application of computer vision in a steelworks environment, our initial investigation delves into the hardware adaptation and optimization of YOLOv5, through deployeing it on FPGA (Field-Programmable Gate Array).



![系统框图_副本](https://github.com/kaamava/CV-Hardware-co-design-for-indusries/assets/106901273/3139a694-ff16-4f42-a879-0e9fd3065ddd)






