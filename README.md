# CV-Hardware-co-design-for-industries

## Phase1：Porting YOLOv5 model to FPGA and optimizing
The **YOLO** (You Only Look Once) algorithm serves as a representative of **single-stage object detection methods**, known for its high speed but relatively lower precision. This approach integrates the process of generating candidate boxes with the actual object detection, making it well-suited for real-time detection tasks. YOLOv5, by employing a lightweight network structure and optimized algorithms, further enhances detection performance and efficiency. While the YOLO series exhibits outstanding performance, its substantial parameter count and computational complexity necessitate more powerful image processors for deployment.

In recent years, with the rapid development of edge computing and intelligent terminals, there is widespread attention towards deploying **artificial intelligence models on embedded devices**. In the context of this project, which focuses on the **application of computer vision in a steelworks**, our initial investigation delves into the hardware adaptation and optimization of YOLOv5, through deployeing it on **FPGA** (Field-Programmable Gate Array).

FPGAs have many advantages regarding unified **design and optimization capabilities** of arithmetic power, speed, and resources for CNN. The FPGA can call and optimize hardware resources at the trigger level, which can precisely adjust the algorithm structure at the trigger and logic gate level to ensure the precise control of arithmetic power and resources. The rich clock network and routing resources inside the FPGA can be designed for speed and hardware resource consistency to ensure timing convergence and resource coordination.

Translating the network structure of YOLOv5 into **hardware description language (HDL)** code for FPGA is crucial for the porting process, and this can be achieved using High-Level Synthesis (HLS) tools.Simultaneously, **collaborative optimization** on the PC and FPGA sides can be achieved through algorithmic co-design, enhancing both the efficiency and scalability of the algorithm.
![系统框图_副本](https://github.com/kaamava/CV-Hardware-co-design-for-indusries/assets/106901273/3139a694-ff16-4f42-a879-0e9fd3065ddd)

By judiciously porting the algorithm and conducting hardware optimizations, we can make a more effective attempt to integrate machine vision applications into practical steel production processes.

## Phase2：Employing YOLOv5 to the practical use of clay gun machines
The first approach involves directly labeling moving blocks and stationary blocks, training an object detection model. The objective identification involves computing the pixel difference between the midpoints of the two target boxes.

The second approach is as follows:

Step 1: Label moving blocks, stationary blocks, and the mud gun disk surface, then train an object detection model.

Step 2: Mark feature sub-blocks within the moving blocks' images and the stationary blocks' images. Train a segmentation model for these feature sub-blocks. Alternatively, use the entire mud gun disk surface as the base image, mark moving feature sub-blocks and stationary feature sub-blocks, and train a segmentation model on this image.

Step 3.1: Use the framed images from the original video as input. Based on the object detection model, identify targets for moving blocks, stationary blocks, and the mud gun disk surface.

Step 3.2: Based on the predicted target box's center point, offset left/right and up/down by a certain number of pixels to generate candidate boxes. The purpose is to enlarge the current predicted box, avoiding potential issues if the prediction box is too small. Use the candidate box's image as input, and based on the segmentation model, obtain segmentation results for moving feature sub-blocks and stationary feature sub-blocks.

Step 4: Recognize the pixel difference between the midpoints of the two segmentation results. 
![val_batch0_labels_副本](https://github.com/kaamava/CV-Hardware-co-design-for-industries/assets/106901273/6bedea1f-8f67-4ef4-a395-46a215496b50)
![train_batch0_副本](https://github.com/kaamava/CV-Hardware-co-design-for-industries/assets/106901273/a5ee23f7-e372-40bc-b2b2-703f4d80c10a)
![results_副本](https://github.com/kaamava/CV-Hardware-co-design-for-industries/assets/106901273/af00afbd-df66-41ad-b7a3-16425fecc82f)

## Phase3：Industrial control at the hardware leve

![image](https://github.com/kaamava/CV-Hardware-co-design-for-industries/assets/106901273/0bda7ab9-7b7a-4f1b-9e81-77df0575a112)

