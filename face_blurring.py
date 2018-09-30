# ###################################################################################
# python face_blurring.py --source_video ./vido.mp4 --output_video ./video_o.mp4    #
#####################################################################################

from mtcnn.mtcnn import MTCNN
import cv2
import glob
import argparse
import os, sys
from os import listdir, makedirs
import shutil
import numpy as np

img_path = "./img"
bbbox_path = "./bbox"
blur_path = "./blur"
comparison_path = "./comparison"

def reset(reset_path):
    path = reset_path
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("remove existing "+path)
        makedirs(path)
        print("create folder: "+path)
    else:
        makedirs(path)
        print("create foder: "+path)

reset(img_path)
reset(bbbox_path)
reset(blur_path)
reset(comparison_path)

def video_to_images(video, path_output_dir):
	vidcap = cv2.VideoCapture(video)
	count = 0
	while vidcap.isOpened():
	    success, image = vidcap.read()
	    if success:
	        cv2.imwrite(os.path.join(path_output_dir, '%04d.png') % count, image)
	        count += 1
	    else:
	        break
	cv2.destroyAllWindows()
	vidcap.release()


if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--source_video", type=str)
	parser.add_argument("--output_video", type=str)
	args = parser.parse_args()

	video_to_images(args.source_video, img_path)
	print(args.source_video)

	source_path = sorted(glob.glob("./img/*.png"))
	source_path = source_path[1:len(source_path)]
	tmp = cv2.imread(source_path[0])
	height,width,layers = tmp.shape

	name = args.output_video
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	video = cv2.VideoWriter(name, fourcc, 25.0, (width,height))
	video_comparison = cv2.VideoWriter(name[:len(name)-4]+"_comparison.mp4", fourcc, 25.0, (width*2,height))

	for i, fi in enumerate(source_path):

		# if i > 10:
		# 	break

		print(fi)
		img = cv2.imread(fi)
		bbox_img = img.copy()
		blur = img.copy()

		detector = MTCNN()
		if not detector.detect_faces(img) == []:
			for j in range(len(detector.detect_faces(img))):
				pos = detector.detect_faces(img)[j]["box"]
				print(pos)
				bbox_img = cv2.rectangle(bbox_img,(pos[0],pos[1]),(pos[0]+pos[2],pos[1]+pos[3]),(0,255,0),3)
				blur[pos[1]:pos[1]+pos[3], pos[0]:pos[0]+pos[2]] = cv2.blur(blur[pos[1]:pos[1]+pos[3], pos[0]:pos[0]+pos[2]], (40,40))

		comparison_img = np.hstack((bbox_img, blur))

		cv2.imwrite(bbbox_path+"/%05d.jpg"%i,bbox_img)
		cv2.imwrite(blur_path+"/%05d.jpg"%i, blur)
		cv2.imwrite(comparison_path+"/%05d.jpg"%i, comparison_img)

		video.write(blur)
		video_comparison.write(comparison_img)
	video.release()
	video_comparison.release()



