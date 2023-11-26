import cv2


cap = cv2.VideoCapture('video/611.mp4')
# cap = cv2.VideoCapture(t)

fps =  int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置VideoWriter以保存新视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('out/6666.mp4' , fourcc, 30, (width, height))

ret_val = cap.isOpened()

while ret_val:
    now_fps = cap.get(1)
    # print(now_fps)
    # if (now_fps % 3 != 0):
    #     ret_val = cap.grab()
    if (now_fps>1200):
        print(now_fps)
        break
    if ret_val:
        ret, frame = cap.read()

        out.write(frame)
        # 显示帧
        # # 显示
        cv2.namedWindow('frame', 0)
        cv2.resizeWindow('frame', 1080, 720)  # 自己设定窗口图片的大小

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break