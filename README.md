# CV-Hardware-co-design-for-industries

## Phase1：Porting YOLOv5 model to FPGA and optimizing
The **YOLO** (You Only Look Once) algorithm serves as a representative of **single-stage object detection methods**, known for its high speed but relatively lower precision. This approach integrates the process of generating candidate boxes with the actual object detection, making it well-suited for real-time detection tasks. YOLOv5, by employing a lightweight network structure and optimized algorithms, further enhances detection performance and efficiency. While the YOLO series exhibits outstanding performance, its substantial parameter count and computational complexity necessitate more powerful image processors for deployment.

In recent years, with the rapid development of edge computing and intelligent terminals, there is widespread attention towards deploying **artificial intelligence models on embedded devices**. In the context of this project, which focuses on the **application of computer vision in a steelworks**, our initial investigation delves into the hardware adaptation and optimization of YOLOv5, through deployeing it on **FPGA** (Field-Programmable Gate Array).

FPGAs have many advantages regarding unified **design and optimization capabilities** of arithmetic power, speed, and resources for CNN. The FPGA can call and optimize hardware resources at the trigger level, which can precisely adjust the algorithm structure at the trigger and logic gate level to ensure the precise control of arithmetic power and resources. The rich clock network and routing resources inside the FPGA can be designed for speed and hardware resource consistency to ensure timing convergence and resource coordination.

Translating the network structure of YOLOv5 into **hardware description language (HDL)** code for FPGA is crucial for the porting process, and this can be achieved using High-Level Synthesis (HLS) tools.Simultaneously, **collaborative optimization** on the PC and FPGA sides can be achieved through algorithmic co-design, enhancing both the efficiency and scalability of the algorithm.
![系统框图_副本](https://github.com/kaamava/CV-Hardware-co-design-for-indusries/assets/106901273/3139a694-ff16-4f42-a879-0e9fd3065ddd)






